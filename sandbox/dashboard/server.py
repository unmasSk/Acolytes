#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dashboard MVP Server
====================

Flask API server for Acolytes dashboard MVP.
Provides 7 main endpoints for system monitoring, management, and agent chat.

Endpoints:
- GET /api/stats: System statistics
- GET /api/agents: Active agents information  
- GET /api/quests: Quest status and progress
- GET /api/flags: Pending flags (placeholder for future implementation)
- POST /api/chat/broadcast: Broadcast agent messages to chat
- GET /api/chat/messages: Retrieve chat messages with pagination
- GET /api/chat/quests: Enhanced quest information for chat context

Database: SQLite connection to ./sandbox/project.db
Port: 5000 (development)
CORS: Enabled for local development
"""

from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import sqlite3
import json
import os
from datetime import datetime
import traceback

app = Flask(__name__)
CORS(app)  # Enable CORS for development

# Database configuration
DB_PATH = 'project.db'

def get_db_connection():
    """Get SQLite database connection with error handling."""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row  # Enable column access by name
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

def safe_json_loads(json_str):
    """Safely parse JSON string, return empty dict if invalid."""
    if not json_str:
        return {}
    try:
        return json.loads(json_str)
    except (json.JSONDecodeError, TypeError):
        return {}

@app.route('/')
def serve_frontend():
    """Serve index.html when it exists, otherwise show API info."""
    try:
        return send_from_directory('.', 'index.html')
    except:
        return jsonify({
            'service': 'Acolytes Dashboard API',
            'version': '1.0.0-mvp',
            'endpoints': {
                'stats': '/api/stats',
                'agents': '/api/agents', 
                'quests': '/api/quests',
                'flags': '/api/flags',
                'chat_broadcast': '/api/chat/broadcast',
                'chat_messages': '/api/chat/messages',
                'chat_quests': '/api/chat/quests'
            },
            'status': 'running'
        })

@app.route('/api/stats')
def get_stats():
    """
    GET /api/stats
    
    Returns system statistics including agent count, active quests, 
    session information, and overall system health.
    
    Response format:
    {
        "total_agents": int,
        "active_quests": int,
        "completed_quests": int,
        "total_sessions": int,
        "active_jobs": int,
        "system_health": "healthy|warning|error",
        "last_activity": "timestamp",
        "uptime": "human readable"
    }
    """
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Database connection failed'}), 500
            
        cursor = conn.cursor()
        
        # Get total agents count
        cursor.execute("SELECT COUNT(*) as count FROM agents_catalog")
        total_agents = cursor.fetchone()['count']
        
        # Get quest statistics
        cursor.execute("SELECT status, COUNT(*) as count FROM acolyte_quests GROUP BY status")
        quest_stats = {row['status']: row['count'] for row in cursor.fetchall()}
        
        # Get session count
        cursor.execute("SELECT COUNT(*) as count FROM sessions")
        total_sessions = cursor.fetchone()['count']
        
        # Get active jobs count  
        cursor.execute("SELECT COUNT(*) as count FROM jobs WHERE status = 'active'")
        active_jobs = cursor.fetchone()['count']
        
        # Get last activity (most recent session)
        cursor.execute("SELECT MAX(created_at) as last_activity FROM sessions")
        last_activity = cursor.fetchone()['last_activity']
        
        conn.close()
        
        # Determine system health based on active components
        system_health = "healthy"
        if active_jobs == 0:
            system_health = "warning"
        if total_agents < 50:
            system_health = "warning"
            
        response = {
            'total_agents': total_agents,
            'active_quests': quest_stats.get('working', 0),
            'completed_quests': quest_stats.get('completed', 0),
            'waiting_quests': quest_stats.get('waiting', 0),
            'total_sessions': total_sessions,
            'active_jobs': active_jobs,
            'system_health': system_health,
            'last_activity': last_activity,
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(response)
        
    except Exception as e:
        print(f"Error in /api/stats: {e}")
        print(traceback.format_exc())
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

@app.route('/api/agents')
def get_agents():
    """
    GET /api/agents
    
    Returns information about all agents in the system including
    their type, module, role, and current status.
    
    Response format:
    {
        "agents": [
            {
                "id": int,
                "name": string,
                "type": string,
                "module": string,
                "sub_module": string,
                "role": object,
                "tech_stack": array,
                "tags": array,
                "status": "active|idle"
            }
        ],
        "summary": {
            "total": int,
            "by_type": object,
            "by_module": object
        }
    }
    """
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Database connection failed'}), 500
            
        cursor = conn.cursor()
        
        # Get all agents with their information
        cursor.execute("""
            SELECT id, name, type, module, sub_module, role, tech_stack, tags, scenarios
            FROM agents_catalog 
            ORDER BY type, module, name
        """)
        
        agents = []
        type_counts = {}
        module_counts = {}
        
        for row in cursor.fetchall():
            # Parse JSON fields safely
            role = safe_json_loads(row['role'])
            tech_stack = safe_json_loads(row['tech_stack'])
            tags = safe_json_loads(row['tags'])
            scenarios = safe_json_loads(row['scenarios'])
            
            agent = {
                'id': row['id'],
                'name': row['name'],
                'type': row['type'],
                'module': row['module'],
                'sub_module': row['sub_module'],
                'role': role,
                'tech_stack': tech_stack if isinstance(tech_stack, list) else [],
                'tags': tags if isinstance(tags, list) else [],
                'scenarios_count': len(scenarios) if isinstance(scenarios, list) else 0,
                'status': 'active'  # MVP: assume all agents are active
            }
            
            agents.append(agent)
            
            # Count by type and module
            agent_type = row['type']
            agent_module = row['module'] or 'other'
            
            type_counts[agent_type] = type_counts.get(agent_type, 0) + 1
            module_counts[agent_module] = module_counts.get(agent_module, 0) + 1
        
        conn.close()
        
        response = {
            'agents': agents,
            'summary': {
                'total': len(agents),
                'by_type': type_counts,
                'by_module': module_counts
            },
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(response)
        
    except Exception as e:
        print(f"Error in /api/agents: {e}")
        print(traceback.format_exc())
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

@app.route('/api/quests')
def get_quests():
    """
    GET /api/quests
    
    Returns current quest status and progress information.
    
    Response format:
    {
        "quests": [
            {
                "quest_id": int,
                "quest_name": string,
                "mission": string,
                "status": string,
                "current_agent": string,
                "phase": string,
                "recruited": array,
                "created_at": timestamp,
                "updated_at": timestamp
            }
        ],
        "summary": {
            "total": int,
            "by_status": object,
            "active_agents": array
        }
    }
    """
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Database connection failed'}), 500
            
        cursor = conn.cursor()
        
        # Get all quests
        cursor.execute("""
            SELECT quest_id, quest_name, quest_phase, mission, recruited, 
                   current_agent, status, broadcast, context, result,
                   created_at, updated_at
            FROM acolyte_quests 
            ORDER BY updated_at DESC
        """)
        
        quests = []
        status_counts = {}
        active_agents = set()
        
        for row in cursor.fetchall():
            # Parse recruited agents (comma-separated string to array)
            recruited = []
            if row['recruited']:
                recruited = [agent.strip() for agent in row['recruited'].split(',')]
            
            quest = {
                'quest_id': row['quest_id'],
                'quest_name': row['quest_name'],
                'mission': row['mission'][:200] + '...' if len(row['mission']) > 200 else row['mission'],
                'full_mission': row['mission'],
                'status': row['status'],
                'current_agent': row['current_agent'],
                'phase': row['quest_phase'],
                'recruited': recruited,
                'broadcast': row['broadcast'],
                'context': row['context'],
                'result': row['result'],
                'created_at': datetime.fromtimestamp(row['created_at']).isoformat() if row['created_at'] else None,
                'updated_at': datetime.fromtimestamp(row['updated_at']).isoformat() if row['updated_at'] else None
            }
            
            quests.append(quest)
            
            # Count by status
            quest_status = row['status']
            status_counts[quest_status] = status_counts.get(quest_status, 0) + 1
            
            # Track active agents
            if row['current_agent'] and row['status'] in ['working', 'waiting']:
                active_agents.add(row['current_agent'])
        
        conn.close()
        
        response = {
            'quests': quests,
            'summary': {
                'total': len(quests),
                'by_status': status_counts,
                'active_agents': list(active_agents)
            },
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(response)
        
    except Exception as e:
        print(f"Error in /api/quests: {e}")
        print(traceback.format_exc())
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

@app.route('/api/flags')
def get_flags():
    """
    GET /api/flags
    
    Returns pending flags information (placeholder for future FLAGS system).
    
    Response format:
    {
        "flags": [],
        "summary": {
            "total": 0,
            "pending": 0,
            "resolved": 0
        },
        "note": "FLAGS system not yet implemented in database"
    }
    """
    try:
        # TODO: Implement when FLAGS table is added to database
        # For MVP, return placeholder structure
        
        response = {
            'flags': [],
            'summary': {
                'total': 0,
                'pending': 0,
                'resolved': 0
            },
            'note': 'FLAGS system not yet implemented in database schema',
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(response)
        
    except Exception as e:
        print(f"Error in /api/flags: {e}")
        print(traceback.format_exc())
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

@app.route('/api/chat/broadcast', methods=['POST'])
def post_chat_broadcast():
    """
    POST /api/chat/broadcast
    
    Broadcasts a message from an agent to the chat system.
    
    Request body:
    {
        "agent_name": string (required),
        "message": string (required),
        "quest_id": string (optional)
    }
    
    Response format:
    {
        "success": bool,
        "message_id": int,
        "timestamp": string
    }
    """
    try:
        # Validate content type
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        
        data = request.get_json()
        
        # Validate required fields
        if not data or not isinstance(data, dict):
            return jsonify({'error': 'Invalid JSON data'}), 400
            
        agent_name = data.get('agent_name', '').strip()
        message = data.get('message', '').strip()
        quest_id = data.get('quest_id', '').strip() or None
        
        if not agent_name:
            return jsonify({'error': 'agent_name is required'}), 400
        if not message:
            return jsonify({'error': 'message is required'}), 400
            
        # Sanitize inputs
        if len(agent_name) > 100:
            return jsonify({'error': 'agent_name too long (max 100 characters)'}), 400
        if len(message) > 2000:
            return jsonify({'error': 'message too long (max 2000 characters)'}), 400
            
        # Insert into database
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Database connection failed'}), 500
            
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO agent_chat_messages (agent_name, message, quest_id)
            VALUES (?, ?, ?)
        """, (agent_name, message, quest_id))
        
        message_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        response = {
            'success': True,
            'message_id': message_id,
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(response), 201
        
    except Exception as e:
        print(f"Error in /api/chat/broadcast: {e}")
        print(traceback.format_exc())
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

@app.route('/api/chat/messages')
def get_chat_messages():
    """
    GET /api/chat/messages
    
    Retrieves chat messages with optional pagination.
    
    Query parameters:
    - limit: int (default 50, max 200)
    - offset: int (default 0)
    
    Response format:
    {
        "messages": [
            {
                "id": int,
                "agent_name": string,
                "message": string,
                "timestamp": int,
                "quest_id": string|null,
                "created_at": string
            }
        ],
        "pagination": {
            "limit": int,
            "offset": int,
            "total": int,
            "has_more": bool
        }
    }
    """
    try:
        # Parse query parameters
        limit = request.args.get('limit', 50, type=int)
        offset = request.args.get('offset', 0, type=int)
        
        # Validate parameters
        if limit < 1 or limit > 200:
            return jsonify({'error': 'limit must be between 1 and 200'}), 400
        if offset < 0:
            return jsonify({'error': 'offset must be >= 0'}), 400
            
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Database connection failed'}), 500
            
        cursor = conn.cursor()
        
        # Get total count
        cursor.execute("SELECT COUNT(*) as count FROM agent_chat_messages")
        total_count = cursor.fetchone()['count']
        
        # Get messages with pagination
        cursor.execute("""
            SELECT id, agent_name, message, timestamp, quest_id, created_at
            FROM agent_chat_messages
            ORDER BY timestamp DESC
            LIMIT ? OFFSET ?
        """, (limit, offset))
        
        messages = []
        for row in cursor.fetchall():
            message = {
                'id': row['id'],
                'agent_name': row['agent_name'],
                'message': row['message'],
                'timestamp': row['timestamp'],
                'quest_id': row['quest_id'],
                'created_at': row['created_at']
            }
            messages.append(message)
        
        conn.close()
        
        response = {
            'messages': messages,
            'pagination': {
                'limit': limit,
                'offset': offset,
                'total': total_count,
                'has_more': (offset + limit) < total_count
            },
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(response)
        
    except Exception as e:
        print(f"Error in /api/chat/messages: {e}")
        print(traceback.format_exc())
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

@app.route('/api/chat/quests')
def get_chat_quests():
    """
    GET /api/chat/quests
    
    Enhanced quest information for chat context.
    Includes active quest details and recent quest history.
    
    Response format:
    {
        "active_quest": {
            "quest_id": int,
            "quest_name": string,
            "mission": string,
            "status": string,
            "current_agent": string,
            "phase": string,
            "recruited": array
        } | null,
        "recent_quests": [
            {
                "quest_id": int,
                "quest_name": string,
                "status": string,
                "current_agent": string,
                "updated_at": string
            }
        ]
    }
    """
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({'error': 'Database connection failed'}), 500
            
        cursor = conn.cursor()
        
        # Get active quest (working status)
        cursor.execute("""
            SELECT quest_id, quest_name, mission, status, current_agent, 
                   quest_phase, recruited
            FROM acolyte_quests 
            WHERE status = 'working'
            ORDER BY updated_at DESC
            LIMIT 1
        """)
        
        active_quest = None
        active_row = cursor.fetchone()
        if active_row:
            recruited = []
            if active_row['recruited']:
                recruited = [agent.strip() for agent in active_row['recruited'].split(',')]
                
            active_quest = {
                'quest_id': active_row['quest_id'],
                'quest_name': active_row['quest_name'],
                'mission': active_row['mission'],
                'status': active_row['status'],
                'current_agent': active_row['current_agent'],
                'phase': active_row['quest_phase'],
                'recruited': recruited
            }
        
        # Get recent quests (last 10)
        cursor.execute("""
            SELECT quest_id, quest_name, status, current_agent, updated_at
            FROM acolyte_quests 
            ORDER BY updated_at DESC
            LIMIT 10
        """)
        
        recent_quests = []
        for row in cursor.fetchall():
            quest = {
                'quest_id': row['quest_id'],
                'quest_name': row['quest_name'],
                'status': row['status'],
                'current_agent': row['current_agent'],
                'updated_at': datetime.fromtimestamp(row['updated_at']).isoformat() if row['updated_at'] else None
            }
            recent_quests.append(quest)
        
        conn.close()
        
        response = {
            'active_quest': active_quest,
            'recent_quests': recent_quests,
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(response)
        
    except Exception as e:
        print(f"Error in /api/chat/quests: {e}")
        print(traceback.format_exc())
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Check if database exists
    if not os.path.exists(DB_PATH):
        print(f"Warning: Database file {DB_PATH} not found!")
        print("Make sure to copy the main project database to this location.")
    
    print("Starting Acolytes Dashboard MVP Server...")
    print("Available endpoints:")
    print("  GET /api/stats - System statistics")
    print("  GET /api/agents - Agent information")
    print("  GET /api/quests - Quest status")
    print("  GET /api/flags - Pending flags")
    print("  POST /api/chat/broadcast - Broadcast agent messages")
    print("  GET /api/chat/messages - Retrieve chat messages")
    print("  GET /api/chat/quests - Enhanced quest info for chat")
    print("\nServer running on http://localhost:5000")
    print("CORS enabled for development")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        threaded=True
    )
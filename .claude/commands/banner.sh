#!/bin/bash

# 🎨 ClaudeSquad Banner Display Script
# Shows a cool ASCII banner for the ClaudeSquad project

clear

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

# Banner
echo -e "${CYAN}"
cat << "EOF"
   _____ _                 _       _____                       _ 
  / ____| |               | |     / ____|                     | |
 | |    | | __ _ _   _  __| | ___| (___   __ _ _   _  __ _  __| |
 | |    | |/ _` | | | |/ _` |/ _ \\___ \ / _` | | | |/ _` |/ _` |
 | |____| | (_| | |_| | (_| |  __/____) | (_| | |_| | (_| | (_| |
  \_____|_|\__,_|\__,_|\__,_|\___|_____/ \__, |\__,_|\__,_|\__,_|
                                            | |                   
                                            |_|                   
EOF
echo -e "${NC}"

# Info
echo -e "${YELLOW}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  🤖 77 Specialized Agents at your service!${NC}"
echo -e "${YELLOW}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Stats
echo -e "${PURPLE}📊 Project Statistics:${NC}"
echo -e "  ${WHITE}├─${NC} Agents: ${GREEN}77${NC} (13 complete, 64 in progress)"
echo -e "  ${WHITE}├─${NC} Dynamic Agents: ${CYAN}7${NC} ClaudeSquad specialists"
echo -e "  ${WHITE}├─${NC} Commands: ${BLUE}10+${NC} automation tools"
echo -e "  ${WHITE}├─${NC} Memory: ${YELLOW}Dual system${NC} (JSON + MCP)"
echo -e "  ${WHITE}└─${NC} Version: ${RED}2.1.0${NC}"
echo ""

# Random motivational quote
QUOTES=(
    "🚀 Building the future of AI orchestration!"
    "💪 Code smarter, not harder!"
    "🎯 Precision through specialization!"
    "⚡ Powered by 77 expert agents!"
    "🔧 Automating excellence, one agent at a time!"
)

# Select random quote
RANDOM_QUOTE=${QUOTES[$RANDOM % ${#QUOTES[@]}]}

echo -e "${YELLOW}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}${RANDOM_QUOTE}${NC}"
echo -e "${YELLOW}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Animation (optional fun spinner)
echo -ne "${GREEN}Loading awesomeness...${NC} "
for i in {1..10}; do
    case $((i % 4)) in
        0) echo -ne "\b⠋";;
        1) echo -ne "\b⠙";;
        2) echo -ne "\b⠹";;
        3) echo -ne "\b⠸";;
    esac
    sleep 0.1
done
echo -e "\b${GREEN}✓${NC}"
echo ""

# Commands reminder
echo -e "${BLUE}Available Commands:${NC}"
echo -e "  /setup     - Initialize project"
echo -e "  /commit    - Smart commit with analysis"
echo -e "  /pr        - Create pull request"
echo -e "  /issue     - Manage issues"
echo -e "  /docs      - Update documentation"
echo ""

echo -e "${WHITE}Ready to rock! 🎸${NC}"
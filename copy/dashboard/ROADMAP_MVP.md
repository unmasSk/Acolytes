# Dashboard MVP - Version 0.1.0 (Super Simple)

## 🎯 Objetivo
Dashboard HTML básico que lea de project.db y muestre datos en tiempo real.

## 📋 Funcionalidades MVP (Solo lo esencial)

### Fase 1: Base (1 archivo HTML)
```
sandbox/dashboard/
├── index.html       # TODO: Dashboard completo en 1 archivo
├── project.db       # Base de datos copiada
└── server.py        # TODO: API simple con Flask/FastAPI
```

### Fase 2: Componentes Básicos

#### 1. **index.html** - Dashboard Todo-en-Uno
- [ ] HTML básico con Tailwind CDN
- [ ] JavaScript vanilla (sin frameworks)
- [ ] Fetch data desde `/api/stats`
- [ ] Auto-refresh cada 5 segundos

#### 2. **server.py** - API Mínima
```python
# Endpoints básicos:
GET /api/stats        # Jobs activos, sesiones, agentes
GET /api/agents       # Lista de agentes
GET /api/quests       # Quests actuales
GET /api/flags        # FLAGS pendientes
```

#### 3. **Datos a Mostrar**
- **Stats Card**: Jobs activos, Sesiones totales, Agentes en catálogo
- **Tabla Agents**: Nombre, tipo, módulo, estado
- **Tabla Quests**: ID, misión, agente actual, status
- **Tabla FLAGS**: Target, status, prioridad

### Fase 3: Mejoras por Agentes

Los agentes mejorarán:
1. **Frontend**: Convertir a Vue.js componentes
2. **Backend**: Añadir WebSockets
3. **Database**: Optimizar queries
4. **Charts**: Añadir visualizaciones
5. **Auth**: Añadir autenticación

## 🚀 Para Empezar

### Paso 1: Crear server.py básico
```python
from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/api/stats')
def stats():
    # Query project.db
    return jsonify({
        "jobs": 5,
        "sessions": 123,
        "agents": 59
    })
```

### Paso 2: Crear index.html básico
```html
<!DOCTYPE html>
<html>
<head>
    <title>Acolytes Dashboard MVP</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-900 text-white">
    <div id="stats"></div>
    <script>
        // Fetch and display data
        setInterval(() => {
            fetch('/api/stats')
                .then(r => r.json())
                .then(data => {
                    // Update DOM
                });
        }, 5000);
    </script>
</body>
</html>
```

## ✅ Criterios de Éxito MVP

1. **Funciona**: Se puede abrir en browser y ver datos
2. **Lee DB**: Consulta project.db real
3. **Auto-refresh**: Actualiza cada 5 segundos
4. **Sin dependencias**: No npm, no node, solo Python + HTML

## 🎯 Objetivo del Test

Probar que múltiples agentes pueden:
1. Leer este roadmap
2. Coordinar via quests
3. Mejorar el MVP progresivamente
4. No interferir entre ellos

---

**NOTA**: Este es un MVP extremadamente básico a propósito. Los agentes lo mejorarán.
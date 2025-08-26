# 🚀 Guía Completa de Instalación - Acolytes for Claude Code

## 📋 Requisitos del Sistema

### Software Necesario
- **Claude Code CLI** (versión más reciente)
- **Git** para control de versiones
- **Python 3.10+** con pip/uv instalado
- **Node.js 18+** y npm (para MCP servers)
- **SQLite3** (incluido en Python)
- **Windows/Mac/Linux** compatible

### Espacio en Disco
- **Mínimo**: 500 MB para instalación base
- **Recomendado**: 2 GB incluyendo MCP servers y dependencias

## 🎯 Instalación Rápida (3 minutos)

### Windows PowerShell
```powershell
# 1. Clonar el repositorio
git clone https://github.com/unmasSk/Acolytes-for-Claude-Code.git
cd Acolytes-for-Claude-Code

# 2. Copiar archivos de agentes a Claude Code
xcopy /e /i .claude %USERPROFILE%\.claude

# 3. Navegar a tu proyecto
cd C:\ruta\a\tu\proyecto

# 4. Inicializar el sistema (6 fases automatizadas)
claude /setup
```

### Mac/Linux Bash
```bash
# 1. Clonar el repositorio
git clone https://github.com/unmasSk/Acolytes-for-Claude-Code.git
cd Acolytes-for-Claude-Code

# 2. Copiar archivos de agentes a Claude Code
cp -r .claude/* ~/.claude/

# 3. Navegar a tu proyecto
cd /ruta/a/tu/proyecto

# 4. Inicializar el sistema
claude /setup
```

## 📦 Instalación Detallada Paso a Paso

### Paso 1: Preparación del Entorno

#### 1.1 Verificar Requisitos
```bash
# Verificar Claude Code
claude --version

# Verificar Python
python --version  # Debe ser 3.10+

# Verificar Node.js
node --version   # Debe ser 18+

# Verificar Git
git --version
```

#### 1.2 Instalar Dependencias Faltantes

**Windows:**
```powershell
# Instalar Python desde Microsoft Store o python.org
winget install Python.Python.3.11

# Instalar Node.js
winget install OpenJS.NodeJS.LTS

# Instalar Git
winget install Git.Git
```

**Mac:**
```bash
# Con Homebrew
brew install python@3.11
brew install node@18
brew install git
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3.11 python3-pip
sudo apt install nodejs npm
sudo apt install git
```

### Paso 2: Clonar e Instalar Acolytes for Claude Code

```bash
# 1. Clonar repositorio
git clone https://github.com/unmasSk/Acolytes-for-Claude-Code.git
cd Acolytes-for-Claude-Code

# 2. Crear estructura de directorios (si no existe)
mkdir -p ~/.claude/agents
mkdir -p ~/.claude/commands
mkdir -p ~/.claude/hooks
mkdir -p ~/.claude/memory
mkdir -p ~/.claude/resources
```

### Paso 3: Copiar Archivos del Sistema

#### Windows (PowerShell como Administrador)
```powershell
# Copiar toda la estructura .claude
xcopy /e /i /y .claude %USERPROFILE%\.claude

# Verificar copia
dir %USERPROFILE%\.claude\agents
# Deberías ver 57+ archivos .md de agentes
```

#### Mac/Linux
```bash
# Copiar con preservación de estructura
cp -r .claude/* ~/.claude/

# Verificar
ls -la ~/.claude/agents/ | head -10
# Deberías ver los archivos de agentes
```

### Paso 4: Configurar MCP Servers

#### 4.1 Instalar SQLite MCP Server (CRÍTICO)
```bash
# Instalar servidor SQLite para memoria persistente
claude mcp add sqlite -s user -- npx -y @modelcontextprotocol/server-sqlite

# Verificar instalación
claude mcp list
# Debe mostrar: sqlite: npx -y @modelcontextprotocol/server-sqlite - ✓ Connected
```

#### 4.2 Instalar Git MCP Server
```bash
# Para control de versiones integrado
claude mcp add server-git -s user -- npx -y @modelcontextprotocol/server-git
```

#### 4.3 Instalar Fetch MCP Server
```bash
# Para obtener información desde URLs
claude mcp add server-fetch -s user -- npx -y @modelcontextprotocol/server-fetch
```

#### 4.4 Instalar Puppeteer MCP (Opcional - Automatización Web)
```bash
# Para automatización visual de navegador
claude mcp add puppeteer -s user -- npx -y @modelcontextprotocol/server-puppeteer
```

#### 4.5 Instalar Magic UI MCP (Opcional - Componentes UI)
```bash
# Para generación instantánea de componentes React/Vue
claude mcp add 21st-dev_magic -s user -- npx -y 21st.dev
```

### Paso 5: Configurar Base de Datos SQLite

```bash
# 1. Navegar a tu proyecto
cd /ruta/a/tu/proyecto

# 2. Crear estructura de base de datos
mkdir -p .claude/memory

# 3. El comando /setup creará automáticamente:
# - project.db con 10 tablas
# - Esquema completo de agents, sessions, flags, etc.
```

### Paso 6: Inicializar en Tu Proyecto

```bash
# En la raíz de tu proyecto
cd /ruta/a/tu/proyecto

# Ejecutar setup de 6 fases
claude /setup
```

#### Qué hace `/setup`:

**Fase 1: Environment & Database Setup**
- Configura SQLite database
- Inicializa 10 tablas del sistema
- Configura MCP connections

**Fase 2: Analysis & Documentation** 
- Para proyectos existentes: Análisis paralelo con 4 agentes
- Para proyectos nuevos: Interview interactivo + especialistas

**Fase 3: CLAUDE.md Creation**
- Genera configuración específica del proyecto
- Define convenciones y estándares

**Fase 4: Jobs & Agent Creation**
- Crea job activo en base de datos
- Configura agentes específicos del proyecto

**Fase 5: Deep Analysis & Initialization**
- Análisis profundo de módulos
- Creación de Acolytes por módulo

**Fase 6: Finalization**
- Verificación de sistema
- Resumen de configuración

## 🔧 Instalación de Hooks (Automatización)

### Hooks Disponibles
```bash
# Ver hooks disponibles
ls ~/.claude/hooks/

# Hooks principales:
# - session_start.py: Carga contexto previo automáticamente
# - todo_sync.py: Sincroniza TODOs con SQLite
# - pre_tool_use.py: Protección Git MCP
# - stop.py: Auto-guardado de sesión
```

### Activar Hooks
Los hooks se activan automáticamente al copiar `.claude/hooks/`. 
No requieren configuración adicional.

## 🚨 Solución de Problemas Comunes

### Error: "MCP Server not connected"
```bash
# 1. Reiniciar Claude Code
claude exit
claude

# 2. Verificar MCP servers
claude mcp list

# 3. Si falta alguno, reinstalar
claude mcp remove [nombre] -s user
claude mcp add [nombre] -s user -- [comando]
```

### Error: "Database not found"
```bash
# Crear manualmente si /setup falla
mkdir -p .claude/memory
touch .claude/memory/project.db

# Reintentar setup
claude /setup
```

### Error: "Agents not found"
```bash
# Verificar instalación de agentes
ls ~/.claude/agents/ | wc -l
# Debe mostrar 57+ archivos

# Si faltan, recopiar
cd /ruta/al/repo/clonado
cp -r .claude/agents/* ~/.claude/agents/
```

### Error en Windows: "Access denied"
```powershell
# Ejecutar PowerShell como Administrador
# Luego repetir comandos xcopy
xcopy /e /i /y .claude %USERPROFILE%\.claude
```

## 📊 Verificación de Instalación

### Test Completo del Sistema
```bash
# 1. Verificar MCP servers
claude mcp list
# Debe mostrar al menos: sqlite, server-git, server-fetch

# 2. Verificar base de datos
claude "Check SQLite database connection"
# Claude ejecutará: mcp__MCP_SQLite_Server__db_info

# 3. Verificar agentes
claude "List available agents"
# Debe mostrar 57 agentes globales

# 4. Probar comando FLAGS
claude /flags
# Debe mostrar sistema FLAGS funcionando

# 5. Probar TODO system
claude /todo add "Test task"
claude /todo
# Debe mostrar la tarea agregada
```

## 🎯 Configuración Post-Instalación

### 1. Personalizar CLAUDE.md
```bash
# Editar configuración del proyecto
claude "Edit CLAUDE.md to add project specific instructions"
```

### 2. Configurar Idioma Preferido
```bash
# En CLAUDE.md agregar:
## Language Configuration
- **User interaction**: Spanish (o tu idioma)
- **Documentation**: English
- **Code comments**: English
```

### 3. Crear Primer Job
```bash
# Crear job activo
claude "/job create 'Initial Setup'"
```

### 4. Generar Acolytes Específicos
```bash
# Si tienes módulos específicos
claude "Create acolyte for authentication module"
claude "Create acolyte for payment module"
```

## 🔐 Seguridad y Mejores Prácticas

### Nunca Hacer
```bash
# ❌ NUNCA usar Git MCP para agregar archivos
mcp__server-git__git_add con ["."] o ["*"]

# ❌ NUNCA commitear .claude/memory/project.db
# Agregar a .gitignore:
echo ".claude/memory/*.db" >> .gitignore
```

### Siempre Hacer
```bash
# ✅ Usar Bash para git operations
git add -A
git commit -m "message"

# ✅ Backup regular de base de datos
cp .claude/memory/project.db .claude/memory/backup_$(date +%Y%m%d).db
```

## 🚀 Comandos Esenciales Post-Instalación

```bash
# Sistema de agentes
claude "Use @backend.python to optimize the API"
claude "Use @coordinator.database for architecture decisions"

# Gestión de tareas
claude /todo           # Ver todas las tareas
claude /todo smart     # Análisis AI de tareas pendientes
claude /save          # Guardar sesión actual

# Coordinación FLAGS
claude /flags         # Procesar FLAGS pendientes

# Verificación sistema
claude /mcp          # Estado de MCP servers
```

## 📚 Recursos Adicionales

### Documentación
- [Repositorio GitHub](https://github.com/unmasSk/Acolytes-for-Claude-Code)
- [Agent Catalog](./.claude/resources/rules/agent-routing-catalog.md)
- [Setup Documentation](./.claude/commands/setup.md)
- [FLAGS System](./.claude/memory/README.md)

### Soporte
- Issues: https://github.com/unmasSk/Acolytes-for-Claude-Code/issues
- Discord: [Comunidad ClaudeSquad]
- Email: soporte@claudesquad.ai

## ✅ Checklist de Instalación Completa

- [ ] Claude Code CLI instalado y funcionando
- [ ] Python 3.10+ y Node.js 18+ instalados
- [ ] Repositorio clonado exitosamente
- [ ] Archivos .claude copiados a directorio home
- [ ] MCP servers instalados (sqlite, git, fetch mínimo)
- [ ] Comando /setup ejecutado en proyecto
- [ ] Base de datos SQLite creada (10 tablas)
- [ ] Hooks activos y funcionando
- [ ] Test de comandos básicos exitoso
- [ ] CLAUDE.md personalizado para tu proyecto

## 🎉 ¡Instalación Completa!

Si todos los checks están completos, tu sistema Acolytes for Claude Code está listo.

**Próximos pasos recomendados:**
1. Ejecuta `claude /todo add "Explorar agentes disponibles"`
2. Prueba un agente: `claude "Use @backend.python to analyze the codebase"`
3. Revisa FLAGS: `claude /flags`
4. Guarda tu primera sesión: `claude /save`

**¡Bienvenido a la era de los equipos de desarrollo AI autónomos!** 🚀✨

---

*Última actualización: Agosto 2025*
*Versión: 2.0.0 - Enterprise FLAGS System*
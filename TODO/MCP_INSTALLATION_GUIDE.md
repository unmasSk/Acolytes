# 🚀 Guía de Instalación MCP - Puppeteer y Chrome DevTools

## 📋 Requisitos Previos
- Node.js y npm instalados
- Python 3.10+ instalado
- Brave Browser instalado en `C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe`
- Claude Code CLI configurado

---

## 1️⃣ PUPPETEER MCP - Automatización Visual

### Instalación Rápida (Una línea)
```bash
claude mcp add puppeteer -s user -- npx -y @modelcontextprotocol/server-puppeteer
```

### Reiniciar Claude Code
Después de instalar, cierra y abre Claude Code para que cargue el servidor.

### Verificar Instalación
```bash
claude mcp list
# Deberías ver: puppeteer: npx -y @modelcontextprotocol/server-puppeteer - ✓ Connected
```

### Uso con Brave Browser
```javascript
// Claude ejecuta esto para abrir Brave con Puppeteer
mcp__puppeteer__puppeteer_navigate({
  url: "https://example.com",
  allowDangerous: true,
  launchOptions: {
    headless: false,
    executablePath: "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe",
    args: [
      "--disable-blink-features=AutomationControlled",
      "--no-first-run",
      "--no-default-browser-check",
      "--disable-popup-blocking"
    ]
  }
})
```

### Herramientas Disponibles
- `mcp__puppeteer__puppeteer_navigate` - Navegar a URLs
- `mcp__puppeteer__puppeteer_screenshot` - Tomar capturas
- `mcp__puppeteer__puppeteer_click` - Hacer clicks
- `mcp__puppeteer__puppeteer_fill` - Llenar formularios
- `mcp__puppeteer__puppeteer_select` - Seleccionar opciones
- `mcp__puppeteer__puppeteer_hover` - Hover sobre elementos
- `mcp__puppeteer__puppeteer_evaluate` - Ejecutar JavaScript

---

## 2️⃣ CHROME DEVTOOLS MCP - Debugging Profundo

### Instalación Paso a Paso

#### 1. Clonar el repositorio
```bash
git clone https://github.com/benjaminr/chrome-devtools-mcp.git
cd chrome-devtools-mcp
```

#### 2. Instalar dependencias con uv
```bash
uv sync
```

#### 3. Agregar a Claude Code
```bash
# Windows - Usar rutas absolutas
claude mcp add chrome-devtools -s user -- "C:/Users/fix.workshop/ClaudeSquad/chrome-devtools-mcp/.venv/Scripts/python.exe" "C:/Users/fix.workshop/ClaudeSquad/chrome-devtools-mcp/server.py"
```

#### 4. Reiniciar Claude Code
Cierra y abre Claude Code después de la instalación.

#### 5. Verificar
```bash
claude mcp list
# Deberías ver ambos servidores conectados
```

---

## 3️⃣ INICIAR BRAVE CON PUERTO DE DEBUGGING (9222)

### 🎯 CREAR ACCESO DIRECTO .BAT (RECOMENDADO)

#### Opción A: Con TU PERFIL NORMAL (Recomendado)
Crea un archivo `Brave-Debug-9222.bat` con este contenido:

```batch
@echo off
echo ========================================
echo    BRAVE BROWSER - DEBUG MODE (9222)
echo ========================================
echo.
echo Iniciando Brave con debugging en puerto 9222...
echo USANDO TU PERFIL NORMAL CON TODOS TUS PLUGINS
echo.

:: Ruta de Brave
set BRAVE_PATH="C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

:: Iniciar Brave con debugging USANDO TU PERFIL NORMAL
start "" %BRAVE_PATH% --remote-debugging-port=9222

echo.
echo ✅ Brave iniciado con debugging en puerto 9222
echo.
echo Para conectar desde Claude Code:
echo   mcp__chrome-devtools__connect_to_browser({port: 9222})
echo.
pause
```

**VENTAJAS del perfil normal**:
- ✅ Todas tus extensiones/plugins
- ✅ Tu sesión de GitHub/Google/etc
- ✅ Tus contraseñas guardadas
- ✅ Tu historial y bookmarks
- ✅ Tu configuración personalizada

#### Opción B: Con perfil temporal (más seguro)
Si prefieres no mezclar debugging con tu perfil personal:

```batch
@echo off
echo ========================================
echo    BRAVE BROWSER - DEBUG MODE (9222)
echo ========================================
echo.
echo Iniciando Brave con perfil temporal...

set BRAVE_PATH="C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
set USER_DATA="C:\temp\brave-debug"

start "" %BRAVE_PATH% --remote-debugging-port=9222 --user-data-dir=%USER_DATA%

echo ✅ Brave iniciado (perfil temporal)
pause
```

**VENTAJAS del perfil temporal**:
- ✅ No afecta tu perfil personal
- ✅ Más seguro para testing
- ❌ Sin extensiones ni sesiones

### 📍 UBICACIÓN DEL ARCHIVO .BAT

1. **Guarda el .bat en**: `C:\Users\tu-usuario\Desktop\Brave-Debug-9222.bat`
2. **Doble click** para ejecutar
3. **IMPORTANTE**: Si usas perfil normal, cierra Brave primero

### 🔌 CONECTAR CHROME DEVTOOLS

Una vez abierto Brave con el .bat:

```javascript
// 1. Conectar al browser existente
await mcp__chrome-devtools__connect_to_browser({port: 9222});

// 2. Ver qué página está abierta
await mcp__chrome-devtools__get_connection_status();

// 3. Navegar o trabajar con la página actual
await mcp__chrome-devtools__execute_javascript({
  code: "document.title"  // Ver título de la página actual
});
```

### ⚠️ IMPORTANTE SOBRE PERFILES

**CON PERFIL NORMAL**:
- Chrome DevTools puede ver tus cookies, localStorage, sesiones
- Útil para debugging de apps donde estás logueado
- Ejemplo: Debuggear tu app en GitHub con tu sesión activa

**CON PERFIL TEMPORAL**:
- Empieza desde cero, sin datos
- Mejor para testing limpio
- No interfiere con tu navegación normal

---

## 4️⃣ FLUJO COMPLETO DE USO

### Opción A: Solo Puppeteer (Más Simple)
```javascript
// 1. Navegar con Brave
mcp__puppeteer__puppeteer_navigate({
  url: "https://google.com",
  allowDangerous: true,
  launchOptions: {
    headless: false,
    executablePath: "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
  }
})

// 2. Interactuar
mcp__puppeteer__puppeteer_fill({selector: "input[name='q']", value: "test"})
mcp__puppeteer__puppeteer_click({selector: "button[type='submit']"})
mcp__puppeteer__puppeteer_screenshot({name: "resultado"})
```

### Opción B: Chrome DevTools (Más Control)
```javascript
// 1. Abrir Brave con debugging (Claude ejecuta)
Bash: '"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" --remote-debugging-port=9222 --user-data-dir=C:/temp/brave-debug &'

// 2. Conectar
mcp__chrome-devtools__connect_to_browser({port: 9222})

// 3. Navegar y debuggear
mcp__chrome-devtools__navigate_to_url({url: "https://example.com"})
mcp__chrome-devtools__execute_javascript({code: "console.log('Hola')"})
mcp__chrome-devtools__get_console_logs()
mcp__chrome-devtools__get_network_requests()
```

---

## 5️⃣ ¿PARA QUÉ USAR CADA UNO?

### 🎭 PUPPETEER MCP - El Actor
**FUERTE EN**: Automatización visual, testing E2E, scraping, capturas de pantalla

**ÚSALO PARA**:
- 🤖 Automatizar tareas repetitivas en web
- 📸 Tomar screenshots de páginas
- 📝 Llenar formularios automáticamente
- 🧪 Testing de interfaces de usuario
- 🕷️ Web scraping con interacción
- 🎮 Simular comportamiento de usuario real
- 📊 Generar PDFs de páginas web
- 🔄 Automatizar flujos de trabajo web

### 🔬 CHROME DEVTOOLS MCP - El Detective
**FUERTE EN**: Debugging profundo, análisis de rendimiento, inspección de red

**ÚSALO PARA**:
- 🐛 Debugging de JavaScript en producción
- 📡 Análisis de requests/responses de red
- 🎯 Inspección del DOM en tiempo real
- ⚡ Análisis de performance y métricas
- 🔍 Monitorear console.log en aplicaciones
- 🏗️ Debugging de aplicaciones React/Vue/Angular
- 📊 Análisis de memoria y CPU
- 🔐 Debugging de problemas de seguridad/CORS

---

## 6️⃣ EJEMPLOS EXTENSIVOS DE USO

### 🎭 PUPPETEER MCP - EJEMPLOS PRÁCTICOS

#### Ejemplo 1: Automatizar Login
```javascript
// Navegar a página de login
await mcp__puppeteer__puppeteer_navigate({
  url: "https://github.com/login",
  allowDangerous: true,
  launchOptions: {
    headless: false,
    executablePath: "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
  }
});

// Llenar credenciales
await mcp__puppeteer__puppeteer_fill({
  selector: "input[name='login']",
  value: "usuario@email.com"
});

await mcp__puppeteer__puppeteer_fill({
  selector: "input[name='password']",
  value: "contraseña"
});

// Hacer click en login
await mcp__puppeteer__puppeteer_click({
  selector: "input[type='submit']"
});

// Tomar screenshot del dashboard
await mcp__puppeteer__puppeteer_screenshot({
  name: "dashboard_logged_in",
  width: 1920,
  height: 1080
});
```

#### Ejemplo 2: Web Scraping de Productos
```javascript
// Ir a Amazon
await mcp__puppeteer__puppeteer_navigate({
  url: "https://www.amazon.com",
  allowDangerous: true,
  launchOptions: {headless: false}
});

// Buscar producto
await mcp__puppeteer__puppeteer_fill({
  selector: "input[id='twotabsearchtextbox']",
  value: "laptop gaming"
});

await mcp__puppeteer__puppeteer_click({
  selector: "input[type='submit']"
});

// Extraer precios y títulos
const productos = await mcp__puppeteer__puppeteer_evaluate({
  script: `
    const items = document.querySelectorAll('[data-component-type="s-search-result"]');
    const productos = [];
    items.forEach(item => {
      const titulo = item.querySelector('h2')?.innerText;
      const precio = item.querySelector('.a-price-whole')?.innerText;
      if (titulo && precio) {
        productos.push({titulo, precio});
      }
    });
    productos.slice(0, 5); // Top 5 productos
  `
});
```

#### Ejemplo 3: Testing de Formulario
```javascript
// Navegar a formulario de contacto
await mcp__puppeteer__puppeteer_navigate({
  url: "https://miapp.com/contacto"
});

// Test: Campo vacío debe mostrar error
await mcp__puppeteer__puppeteer_click({
  selector: "button[type='submit']"
});

const error = await mcp__puppeteer__puppeteer_evaluate({
  script: "document.querySelector('.error-message')?.innerText"
});

// Llenar formulario correctamente
await mcp__puppeteer__puppeteer_fill({
  selector: "input[name='nombre']",
  value: "Juan Pérez"
});

await mcp__puppeteer__puppeteer_fill({
  selector: "input[name='email']",
  value: "juan@email.com"
});

await mcp__puppeteer__puppeteer_select({
  selector: "select[name='asunto']",
  value: "soporte"
});

await mcp__puppeteer__puppeteer_fill({
  selector: "textarea[name='mensaje']",
  value: "Necesito ayuda con mi cuenta"
});

// Enviar y verificar
await mcp__puppeteer__puppeteer_click({
  selector: "button[type='submit']"
});

await mcp__puppeteer__puppeteer_screenshot({
  name: "formulario_enviado"
});
```

#### Ejemplo 4: Automatizar Descarga de Reportes
```javascript
// Login a sistema de reportes
await mcp__puppeteer__puppeteer_navigate({
  url: "https://analytics.miempresa.com"
});

// Navegar a sección de reportes
await mcp__puppeteer__puppeteer_click({
  selector: "a[href='/reports']"
});

// Seleccionar rango de fechas
await mcp__puppeteer__puppeteer_evaluate({
  script: `
    document.querySelector('#fecha-inicio').value = '2025-01-01';
    document.querySelector('#fecha-fin').value = '2025-08-26';
  `
});

// Seleccionar tipo de reporte
await mcp__puppeteer__puppeteer_select({
  selector: "select#tipo-reporte",
  value: "ventas-mensual"
});

// Generar y descargar
await mcp__puppeteer__puppeteer_click({
  selector: "button.generar-reporte"
});

// Esperar y tomar evidencia
await mcp__puppeteer__puppeteer_evaluate({
  script: "new Promise(r => setTimeout(r, 3000))"
});

await mcp__puppeteer__puppeteer_screenshot({
  name: "reporte_generado"
});
```

#### Ejemplo 5: Monitoreo de Competencia
```javascript
// Revisar precio de competidor
await mcp__puppeteer__puppeteer_navigate({
  url: "https://competidor.com/producto/laptop-x1"
});

// Extraer información clave
const datos = await mcp__puppeteer__puppeteer_evaluate({
  script: `
    ({
      precio: document.querySelector('.price')?.innerText,
      stock: document.querySelector('.availability')?.innerText,
      rating: document.querySelector('.rating')?.innerText,
      reviews: document.querySelector('.review-count')?.innerText,
      descripcion: document.querySelector('.product-description')?.innerText
    })
  `
});

// Tomar screenshot para evidencia
await mcp__puppeteer__puppeteer_screenshot({
  name: `competidor_${new Date().toISOString().split('T')[0]}`
});
```

### 🔬 CHROME DEVTOOLS MCP - EJEMPLOS PRÁCTICOS

#### Ejemplo 1: Debugging de Aplicación React
```javascript
// Conectar a app en desarrollo
await mcp__chrome-devtools__connect_to_browser({port: 9222});
await mcp__chrome-devtools__navigate_to_url({url: "http://localhost:3000"});

// Inspeccionar estado de React
const reactState = await mcp__chrome-devtools__execute_javascript({
  code: `
    // Obtener componente React
    const container = document.querySelector('#root');
    const reactFiber = container._reactRootContainer._internalRoot.current;
    
    // Extraer props y state
    const component = reactFiber.child;
    ({
      type: component.type.name,
      props: component.memoizedProps,
      state: component.memoizedState,
      hooks: component.memoizedState
    })
  `
});

// Monitorear renders
await mcp__chrome-devtools__execute_javascript({
  code: `
    // Hook para detectar re-renders
    const originalLog = console.log;
    let renderCount = 0;
    console.log = function(...args) {
      if (args[0]?.includes?.('render')) {
        renderCount++;
        originalLog('🔄 Re-render #' + renderCount, ...args);
      }
      originalLog.apply(console, args);
    };
  `
});
```

#### Ejemplo 2: Análisis de Performance
```javascript
// Conectar y navegar
await mcp__chrome-devtools__connect_to_browser({port: 9222});
await mcp__chrome-devtools__navigate_to_url({url: "https://mi-app-lenta.com"});

// Obtener métricas de performance
const metrics = await mcp__chrome-devtools__get_performance_metrics();

// Analizar tiempo de carga
await mcp__chrome-devtools__execute_javascript({
  code: `
    const perfData = performance.getEntriesByType('navigation')[0];
    ({
      domContentLoaded: perfData.domContentLoadedEventEnd - perfData.domContentLoadedEventStart,
      loadComplete: perfData.loadEventEnd - perfData.loadEventStart,
      domInteractive: perfData.domInteractive,
      firstPaint: performance.getEntriesByType('paint')[0]?.startTime,
      firstContentfulPaint: performance.getEntriesByType('paint')[1]?.startTime,
      recursos: performance.getEntriesByType('resource').length
    })
  `
});

// Identificar recursos lentos
await mcp__chrome-devtools__execute_javascript({
  code: `
    const recursosLentos = performance.getEntriesByType('resource')
      .filter(r => r.duration > 500)
      .map(r => ({
        url: r.name.split('/').pop(),
        duration: Math.round(r.duration),
        type: r.initiatorType
      }))
      .sort((a,b) => b.duration - a.duration);
    console.table(recursosLentos);
    recursosLentos;
  `
});
```

#### Ejemplo 3: Debugging de API Calls
```javascript
// Conectar a aplicación
await mcp__chrome-devtools__connect_to_browser({port: 9222});
await mcp__chrome-devtools__navigate_to_url({url: "https://app.ejemplo.com"});

// Interceptar todas las llamadas fetch
await mcp__chrome-devtools__execute_javascript({
  code: `
    // Override fetch para logging
    const originalFetch = window.fetch;
    window.fetchLog = [];
    
    window.fetch = async function(...args) {
      const [url, options = {}] = args;
      const startTime = performance.now();
      
      console.log('🚀 API Call:', url, options);
      
      try {
        const response = await originalFetch.apply(this, args);
        const duration = performance.now() - startTime;
        
        const logEntry = {
          url: url,
          method: options.method || 'GET',
          status: response.status,
          duration: Math.round(duration),
          timestamp: new Date().toISOString()
        };
        
        window.fetchLog.push(logEntry);
        console.log('✅ Response:', logEntry);
        
        return response;
      } catch (error) {
        console.error('❌ API Error:', url, error);
        throw error;
      }
    };
    'Fetch interceptor installed';
  `
});

// Obtener todas las requests de red
const requests = await mcp__chrome-devtools__get_network_requests({
  filter_status: 400, // Solo errores 4xx
  limit: 10
});

// Ver logs de consola con errores
const logs = await mcp__chrome-devtools__get_console_logs({
  level: "error"
});
```

#### Ejemplo 4: Análisis de Memoria
```javascript
// Conectar
await mcp__chrome-devtools__connect_to_browser({port: 9222});

// Crear snapshot de memoria inicial
await mcp__chrome-devtools__execute_javascript({
  code: `
    window.memoryStart = performance.memory;
    console.log('📊 Memoria inicial:', {
      usedJS: (performance.memory.usedJSHeapSize / 1048576).toFixed(2) + ' MB',
      totalJS: (performance.memory.totalJSHeapSize / 1048576).toFixed(2) + ' MB',
      limit: (performance.memory.jsHeapSizeLimit / 1048576).toFixed(2) + ' MB'
    });
  `
});

// Ejecutar acción que podría causar memory leak
await mcp__chrome-devtools__execute_javascript({
  code: `
    // Simular creación de muchos objetos
    window.leakyArray = [];
    for(let i = 0; i < 100000; i++) {
      window.leakyArray.push({
        id: i,
        data: new Array(100).fill('x'.repeat(100))
      });
    }
  `
});

// Comparar memoria
await mcp__chrome-devtools__execute_javascript({
  code: `
    const memoryEnd = performance.memory;
    const delta = {
      usedJS: ((memoryEnd.usedJSHeapSize - window.memoryStart.usedJSHeapSize) / 1048576).toFixed(2) + ' MB',
      totalJS: ((memoryEnd.totalJSHeapSize - window.memoryStart.totalJSHeapSize) / 1048576).toFixed(2) + ' MB'
    };
    console.warn('⚠️ Incremento de memoria:', delta);
    delta;
  `
});
```

#### Ejemplo 5: Debugging de WebSocket
```javascript
// Conectar
await mcp__chrome-devtools__connect_to_browser({port: 9222});
await mcp__chrome-devtools__navigate_to_url({url: "https://app-con-websocket.com"});

// Interceptar WebSocket
await mcp__chrome-devtools__execute_javascript({
  code: `
    // Override WebSocket
    const OriginalWebSocket = window.WebSocket;
    window.wsConnections = [];
    
    window.WebSocket = function(url, protocols) {
      console.log('🔌 WebSocket connecting to:', url);
      
      const ws = new OriginalWebSocket(url, protocols);
      const connection = {
        url: url,
        messages: [],
        state: 'CONNECTING',
        created: new Date().toISOString()
      };
      
      ws.addEventListener('open', () => {
        connection.state = 'OPEN';
        console.log('✅ WebSocket connected:', url);
      });
      
      ws.addEventListener('message', (event) => {
        const message = {
          type: 'received',
          data: event.data,
          timestamp: new Date().toISOString()
        };
        connection.messages.push(message);
        console.log('📥 WS Message:', event.data);
      });
      
      ws.addEventListener('error', (event) => {
        connection.state = 'ERROR';
        console.error('❌ WebSocket error:', event);
      });
      
      ws.addEventListener('close', () => {
        connection.state = 'CLOSED';
        console.log('🔒 WebSocket closed:', url);
      });
      
      // Override send
      const originalSend = ws.send.bind(ws);
      ws.send = function(data) {
        const message = {
          type: 'sent',
          data: data,
          timestamp: new Date().toISOString()
        };
        connection.messages.push(message);
        console.log('📤 WS Send:', data);
        return originalSend(data);
      };
      
      window.wsConnections.push(connection);
      return ws;
    };
    'WebSocket interceptor installed';
  `
});

// Ver todas las conexiones y mensajes
await mcp__chrome-devtools__execute_javascript({
  code: "window.wsConnections"
});
```

---

## 7️⃣ ESCENARIOS DEL MUNDO REAL

### 🏢 Escenario 1: Testing E2E de E-commerce
```javascript
// PUPPETEER: Simular compra completa
// 1. Navegar a tienda
// 2. Buscar producto
// 3. Agregar al carrito
// 4. Checkout
// 5. Verificar confirmación
// 6. Tomar screenshots de cada paso
```

### 📊 Escenario 2: Dashboard de Analytics
```javascript
// CHROME DEVTOOLS: Analizar performance
// 1. Medir tiempo de carga de gráficos
// 2. Detectar llamadas API lentas
// 3. Identificar re-renders innecesarios
// 4. Analizar uso de memoria con datasets grandes
```

### 🔐 Escenario 3: Testing de Seguridad
```javascript
// AMBOS: Pruebas de seguridad
// PUPPETEER: Intentar XSS, inyección SQL
// DEVTOOLS: Analizar headers de seguridad, CORS, cookies
```

### 📱 Escenario 4: Testing Responsive
```javascript
// PUPPETEER: Cambiar viewport y verificar
// 1. Desktop (1920x1080)
// 2. Tablet (768x1024)
// 3. Mobile (375x667)
// Screenshots de cada resolución
```

### 🤖 Escenario 5: Bot de Monitoreo
```javascript
// PUPPETEER: Revisar disponibilidad
// Cada 5 minutos:
// 1. Navegar a sitio
// 2. Verificar elementos críticos
// 3. Tomar screenshot
// 4. Alertar si hay problemas
```

---

## 8️⃣ SEQUENTIAL THINKING MCP - El Pensador Estructurado

### Instalación
```bash
# Agregar a Claude Code
claude mcp add sequential-thinking -s user -- npx -y @modelcontextprotocol/server-sequential-thinking

# Reiniciar Claude Code
```

### Qué Hace
**#1 MÁS USADO (5,550+ usuarios)** - Estructura el pensamiento en etapas para resolver problemas complejos:

1. **Definición del Problema**: Identifica qué resolver
2. **Investigación**: Recopila información relevante
3. **Análisis**: Descompone el problema
4. **Síntesis**: Combina soluciones
5. **Conclusión**: Resume y valida

### Características
- Pensamiento paso a paso documentado
- Tracking del progreso mental
- Generación de summaries
- Perfecto para debugging complejo
- Resolución estructurada de problemas

### Casos de Uso
```javascript
// Ideal para:
- Debugging de bugs complejos
- Arquitectura de sistemas
- Refactoring de código legacy
- Análisis de performance
- Diseño de soluciones
- Planning de features
```

---

## 🎯 RESUMEN DE TODOS LOS MCPs INSTALADOS

| MCP Server | Estado | Uso Principal | Peligrosidad |
|------------|---------|--------------|--------------|
| **Puppeteer** | ✅ Instalado | Automatización web visual | ✅ Seguro |
| **Chrome DevTools** | ✅ Instalado | Debugging profundo | ✅ Seguro |
| **Sequential Thinking** | ✅ Instalado | Resolución estructurada | ✅ Seguro |

### Comando para Ver Todos
```bash
claude mcp list
```

### Para Desinstalar un MCP
```bash
# Ejemplo para remover un MCP
claude mcp remove [nombre-del-mcp] -s user
```

---

## 🆕 MCPs NO COMPATIBLES CON CLAUDE CODE

### ❌ MCPs que NO funcionan (probados y fallan)
Los siguientes MCPs existen pero no conectan con Claude Code:

| MCP | Paquete NPM | Propósito | Estado |
|-----|-------------|-----------|---------|
| **Apidog** | `apidog-mcp-server` | APIs OpenAPI/Swagger | ❌ No conecta |
| **Mintlify** | `@mintlify/mcp` | Documentación | ❌ No conecta |
| **Orval** | `@orval/mcp` | Generación de código desde OpenAPI | ❌ No conecta |
| **Swagger Explorer** | `@johnneerdael/swagger-mcp` | Explorar Swagger/OpenAPI | ❌ No conecta |
| **OpenAPI Explorer** | `mcp-openapi-schema-explorer` | Explorar esquemas OpenAPI | ❌ No conecta |

### ✅ ALTERNATIVAS QUE SÍ FUNCIONAN

#### Para Documentación de Librerías
**Context7 MCP** (YA INSTALADO)
- Obtiene documentación actualizada de cualquier librería
- Uso: `mcp__context7__resolve-library-id` y luego `mcp__context7__get-library-docs`
- Ejemplo: Documentación de React, Vue, Next.js, etc.

#### Para APIs OpenAPI/Swagger
**Soluciones alternativas:**
1. **Copiar specs directamente**: Copia el JSON/YAML de tu OpenAPI en el código
2. **WebFetch con swagger.io**: Usa el tool WebFetch para obtener specs desde URLs
3. **Agente @backend.api**: Usa el agente especializado con las especificaciones copiadas
4. **Generar con herramientas externas**: 
   - openapi-generator-cli
   - swagger-codegen
   - Luego importar el código generado

#### Para Documentación General
**Opciones disponibles:**
1. **WebFetch**: Para obtener documentación desde sitios web
2. **server-fetch MCP**: Para obtener contenido desde URLs
3. **Agente @docs.specialist**: Para gestionar documentación del proyecto

---

## 📊 TABLA COMPARATIVA COMPLETA

| Característica | Puppeteer MCP | Chrome DevTools MCP | Sequential Thinking |
|---|---|---|---|
| **Propósito** | Automatización visual | Debugging profundo | Resolución problemas |
| **Ventana visible** | Sí, siempre | Sí, con puerto 9222 | N/A |
| **Screenshots** | ✅ Excelente | ❌ No tiene | ❌ No |
| **Clicks/Forms** | ✅ Muy fácil | ❌ Solo JavaScript | ❌ No |
| **Network Analysis** | ❌ Limitado | ✅ Completo | ❌ No |
| **Console Logs** | ✅ Básico | ✅ Detallado | ✅ Mental |
| **DOM Inspection** | ❌ No | ✅ Completo | ❌ No |
| **Performance** | ❌ No | ✅ Metrics | ✅ Mental |
| **Peligrosidad** | ✅ Seguro | ✅ Seguro | ✅ Seguro |

---

## 6️⃣ TROUBLESHOOTING

### Error: "Chrome not running on port 9222"
**Solución**: Primero abre Brave con el comando de debugging

### Error: "Dangerous browser arguments detected"
**Solución**: Agrega `allowDangerous: true` en Puppeteer

### Error: "MCP server not connected"
**Solución**: Reinicia Claude Code después de instalar

### Brave no se abre
**Solución**: Verifica la ruta: `C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe`

---

## 7️⃣ SCRIPT DE INSTALACIÓN COMPLETA

```bash
#!/bin/bash
# install_mcps.sh - Ejecutar una sola vez

echo "📦 Instalando Puppeteer MCP..."
claude mcp add puppeteer -s user -- npx -y @modelcontextprotocol/server-puppeteer

echo "📦 Instalando Chrome DevTools MCP..."
git clone https://github.com/benjaminr/chrome-devtools-mcp.git
cd chrome-devtools-mcp
uv sync
PYTHON_PATH="$(pwd)/.venv/Scripts/python.exe"
SERVER_PATH="$(pwd)/server.py"
claude mcp add chrome-devtools -s user -- "$PYTHON_PATH" "$SERVER_PATH"

echo "✅ Instalación completa. Reinicia Claude Code."
echo "🚀 Para usar con Brave, ejecuta:"
echo '"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" --remote-debugging-port=9222 --user-data-dir=C:/temp/brave-debug'
```

---

## 📌 NOTAS IMPORTANTES

1. **Siempre usar rutas absolutas** en Windows
2. **Reiniciar Claude Code** después de cada instalación de MCP
3. **F12 se presiona manualmente** - ninguna herramienta puede abrir DevTools automáticamente
4. **Puerto 9222** es el estándar para Chrome DevTools Protocol
5. **Brave bloquea mejor** los popups y cookies que Chrome

---

## 🎯 RECOMENDACIÓN

- **Para automatización rápida**: Usa Puppeteer MCP
- **Para debugging profundo**: Usa Chrome DevTools MCP
- **Para lo mejor de ambos**: Instala los dos y úsalos según necesites

---

*Última actualización: 26 de Agosto 2025*
# 🚀 ClaudeSquad Project Configuration - MEMORIA PERSISTENTE v2.0

## ⚠️ CRITICAL: Memory System Active

**IMPORTANTE**: Los agentes NO mantienen contexto entre invocaciones. Cada vez que invocas un agente, es una ventana de contexto NUEVA. Por eso tenemos un sistema de memoria persistente.

### 🧠 Cómo Funciona la Memoria

1. **SubagentStart**: Al invocar cualquier agente, automáticamente carga su memoria previa
2. **Durante ejecución**: El agente tiene acceso a todo su conocimiento histórico
3. **SubagentStop**: Al terminar, guarda automáticamente nuevos aprendizajes
4. **Próxima invocación**: El agente "recuerda" todo lo anterior

## 📋 Protocolo de Invocación de Agentes Dinámicos

### 🚨 CRÍTICO: SIEMPRE DAR CONTEXTO COMPLETO

**Los agentes NO tienen contexto automático. DEBES proporcionar TODO el contexto necesario en CADA invocación.**

### ✅ Flujo CORRECTO con CONTEXTO OBLIGATORIO:

```
1. PRIMERO - Consultar al agente del módulo CON CONTEXTO COMPLETO:
   
   "@dream-agent, necesito implementar [función X]. 
   
   CONTEXTO DEL MÓDULO:
   - Ruta del módulo: /src/dream
   - Archivos principales: DataProcessor.php, DreamService.php
   - Estructura actual: [incluir tree del módulo]
   - Patrones en uso: Repository, Service Layer
   - Convenciones: max 300 líneas/archivo, tests >80%
   - Configuración: [incluir .env relevante]
   
   TAREA ESPECÍFICA:
   - Necesito procesar datos específicos
   - Debe integrarse con el sistema de cache
   - Performance objetivo: <100ms
   
   ¿Dónde y cómo debo implementar esto?"
   
2. El dream-agent responderá con especificaciones detalladas
   
3. SEGUNDO - Implementar con engineer CON CONTEXTO COMPLETO:
   
   "@engineer-laravel, implementa lo siguiente:
   
   CONTEXTO DEL PROYECTO:
   - Framework: Laravel 11
   - Convenciones: [INCLUIR TODAS]
     * Max 300 líneas por archivo
     * Métodos max 30 líneas  
     * Repository pattern obligatorio
     * Tests con Pest >80% coverage
     * Formato PSR-12
   - Ubicación: /src/dream/processors/DataProcessor.php
   
   ESPECIFICACIONES DEL dream-agent:
   [INCLUIR TODO lo que dijo dream-agent]
   
   ARCHIVOS RELACIONADOS:
   [INCLUIR fragmentos de código relevante]
   
   IMPLEMENTACIONES SIMILARES:
   [INCLUIR ejemplos del proyecto]
   
   WARNINGS:
   - No duplicar processRawData() en línea 89
   - Usar DreamService existente
   - Mantener compatibilidad con cache Redis"
   
4. TERCERO - Revisar con el agente del módulo CON CONTEXTO:
   
   "@dream-agent, revisa esta implementación:
   
   CAMBIOS REALIZADOS:
   [INCLUIR diff o resumen detallado]
   
   ARCHIVOS MODIFICADOS:
   - DataProcessor.php: líneas 145-189
   - DataProcessorTest.php: 5 nuevos tests
   
   MÉTRICAS:
   - Complejidad: 6/10
   - Coverage: 92%
   - Performance: 87ms promedio
   
   ¿Cumple con las convenciones del módulo?"
```

### ❌ Lo que NO debes hacer:

```
MAL: "@engineer-laravel implementa función en DREAM"
(El engineer no conoce el módulo DREAM específicamente)

MAL: Invocar dream-agent solo una vez
(Necesitas: consulta → implementación → revisión)

MAL: Asumir que dream-agent recuerda entre llamadas sin el sistema de memoria
(Sin memoria, cada invocación es fresh)
```

## 🎯 Ejemplos Reales de Uso

### Ejemplo 1: Añadir nueva funcionalidad a módulo existente

```
USUARIO: "Necesito procesar datos específicos en el sistema DREAM"

TÚ (Claude): 
1. "@dream-agent necesito añadir una función para procesar datos específicos. ¿Dónde debería ir y qué convenciones seguir?"

dream-agent: "Basándome en mi conocimiento del módulo:
- Ubicación: src/dream/processors/DataProcessor.php:145
- Usa el patrón Repository como los otros processors
- Hereda de BaseProcessor
- Tests en tests/Feature/Dream/
- NO dupliques processRawData() que ya existe en línea 89"

2. "@engineer-laravel implementa processSpecificData() en src/dream/processors/DataProcessor.php:145, heredando de BaseProcessor, usando Repository pattern. No duplicar processRawData()."

engineer-laravel: [implementa el código]

3. "@dream-agent revisa esta implementación de processSpecificData() en DataProcessor.php"

dream-agent: "✅ Implementación correcta. Sigue el patrón Repository. 
⚠️ FLAG para @database-coordinator: Esta función necesitará índice en dream_data.processor_id para performance"
```

### Ejemplo 2: Refactorización de código existente

```
USUARIO: "El módulo de pagos está lento, necesita optimización"

TÚ (Claude):
1. "@payments-agent analiza tu módulo y dime dónde están los cuellos de botella"

payments-agent: [carga su memoria y analiza]
"Detectados 3 problemas principales:
- N+1 queries en PaymentController:45-67
- Sin caché en calculateTaxes():234
- Bucle innecesario en processRefunds():445"

2. "@engineer-laravel optimiza estos 3 puntos: [lista de payments-agent]"

3. "@payments-agent valida las optimizaciones aplicadas"

payments-agent: "✅ Optimizaciones correctas. 
Nuevo performance: 200ms → 45ms
Guardado en mi memoria para futuras referencias"
```

## 🔄 Gestión de FLAGS Cross-Domain

Cuando un agente detecta algo que afecta a otro dominio:

```
dream-agent: "FLAG: Necesita índice en base de datos"
           ↓
TÚ: "@database-coordinator el dream-agent indica que necesita un índice en dream_data.processor_id"
           ↓
database-coordinator: "Creando migration para el índice..."
```

## 📊 Estado de Agentes Dinámicos

Para verificar salud de los agentes:

```bash
/agent-health --all        # Ver estado de todos
/agent-health dream-agent  # Ver estado específico
/agent-health dream-agent --upgrade  # Si está desactualizado
```

## 🎨 Mejores Prácticas

1. **Siempre consulta primero** al agente del módulo
2. **Proporciona contexto completo** al engineer
3. **Siempre revisa** con el agente del módulo al final
4. **Procesa los FLAGS** que levanten los agentes
5. **Confía en la memoria** - Los agentes recuerdan todo

## 🛠️ Comandos Útiles

```bash
# Ver memoria de un agente
cat .claude/memory/agents/dream_agent/knowledge.json

# Consolidar memoria (eliminar duplicados)
python .claude/scripts/memory_manager.py consolidate dream-agent

# Ver flags pendientes
cat .claude/memory/flags/pending.json

# Ver actividad reciente
tail -20 .claude/memory/context/activity.log
```

## 🚨 Troubleshooting

Si un agente parece no recordar:
1. Verifica que hooks.json esté activo
2. Confirma que Python está instalado
3. Revisa que existe .claude/memory/agents/[agent_name]/
4. Ejecuta manualmente: `python .claude/scripts/memory_manager.py load [agent-name]`

## 📈 Métricas del Sistema de Memoria

- Agentes con memoria activa: TODOS los *-agent, engineer-*, coordinator-*
- Retención de conocimiento: 100% entre sesiones
- Capacidad por agente: Últimas 100 interacciones
- Auto-consolidación: Semanal (configurable)

---

**RECUERDA**: Sin este sistema de memoria, los agentes olvidan TODO entre invocaciones. Con él, construyen conocimiento acumulativo que mejora con cada uso.
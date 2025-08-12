---
description: Prepara contexto completo para invocar agentes con toda la información necesaria
---

# Prepare Context - Preparador de Contexto Completo

Este comando analiza un módulo y prepara TODO el contexto necesario para invocar agentes correctamente.

## Uso

```bash
/prepare-context dream
```

## Lo que hace

1. **Analiza el módulo completo** usando `module_analyzer.py`
2. **Genera el contexto** para el agente dinámico
3. **Prepara las instrucciones** para el engineer
4. **Te da los prompts listos** para copiar y pegar

## Proceso

### Paso 1: Analizar módulo

```bash
python .claude/scripts/module_analyzer.py /src/dream
```

Esto genera un análisis completo en `.claude/memory/modules/dream_analysis.json`

### Paso 2: Generar contexto para agente dinámico

Te proporciono el prompt completo:

```markdown
@dream-agent, necesito [TU TAREA AQUÍ].

CONTEXTO DEL MÓDULO:
- Ruta: /src/dream
- Estructura:
[TREE COMPLETO DEL MÓDULO - 500+ líneas si hace falta]

- Archivos principales:
[LISTA DE TODOS LOS ARCHIVOS CON SU PROPÓSITO]

- Patrones detectados:
[TODOS LOS PATRONES EN USO]

- Convenciones del proyecto:
[TODAS LAS CONVENCIONES]

- Dependencias:
[INTERNAS Y EXTERNAS]

- Comunicación:
[ENDPOINTS, EVENTOS, TABLAS]

- Configuración:
[VARIABLES DE ENTORNO]

- Tests existentes:
[ESTRUCTURA DE TESTS]

- TODOs pendientes:
[TODOS Y FIXMES]

- Cambios recientes:
[ÚLTIMOS 20 COMMITS]

TAREA ESPECÍFICA:
[DESCRIPCIÓN DETALLADA DE LO QUE NECESITAS]

¿Dónde y cómo debo implementar esto considerando todo el contexto anterior?
```

### Paso 3: Preparar contexto para engineer

Después de que el agente dinámico responda, te preparo el prompt para el engineer:

```markdown
@engineer-laravel, implementa lo siguiente:

CONTEXTO DEL PROYECTO COMPLETO:
- Framework: [DETECTADO]
- Estructura: [TODA]
- Convenciones NO NEGOCIABLES:
  [LISTA COMPLETA DE CONVENCIONES]
  
ESPECIFICACIONES DEL dream-agent:
[TODO LO QUE RESPONDIÓ]

ARCHIVOS QUE NECESITAS CONOCER:
[CONTENIDO DE ARCHIVOS RELEVANTES]

EJEMPLOS DEL PROYECTO:
[CÓDIGO SIMILAR YA IMPLEMENTADO]

ADVERTENCIAS CRÍTICAS:
[TODO LO QUE NO DEBES HACER]

MÉTRICAS OBJETIVO:
- Coverage: >80%
- Complejidad: <10
- Performance: <100ms
```

### Paso 4: Contexto para revisión

Para la revisión final:

```markdown
@dream-agent, revisa esta implementación:

CONTEXTO ORIGINAL:
[LO QUE PEDISTE INICIALMENTE]

IMPLEMENTACIÓN REALIZADA:
[DIFF COMPLETO O RESUMEN]

ARCHIVOS CAMBIADOS:
[LISTA CON LÍNEAS]

MÉTRICAS ALCANZADAS:
[TODAS LAS MÉTRICAS]

VALIDACIONES NECESARIAS:
- ¿Sigue los patrones del módulo?
- ¿Respeta las convenciones?
- ¿No duplica código existente?
- ¿Los tests son suficientes?
- ¿Hay algún FLAG para otros módulos?
```

## Ventajas

1. **Garantiza contexto completo** - No te olvidas de nada
2. **Evita errores** - Los agentes tienen toda la info
3. **Ahorra tiempo** - No tienes que escribir todo manualmente
4. **Consistencia** - Siempre el mismo formato

## Ejemplo completo

```bash
# 1. Preparar contexto
/prepare-context dream

# 2. Copiar el prompt generado y enviarlo a dream-agent
@dream-agent [PROMPT GENERADO]

# 3. Copiar el prompt para engineer
@engineer-laravel [PROMPT GENERADO]

# 4. Copiar el prompt de revisión
@dream-agent [PROMPT DE REVISIÓN]
```

## Notas importantes

- **NO importa el tamaño** - Si el contexto son 20,000 tokens, se incluyen
- **Mejor sobrar que faltar** - Más contexto = menos errores
- **Los agentes lo necesitan** - Sin contexto, hacen código genérico

---

*Este comando asegura que SIEMPRE das contexto completo a los agentes*
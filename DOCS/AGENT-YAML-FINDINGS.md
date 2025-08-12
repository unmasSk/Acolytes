# 📋 Hallazgos sobre YAML Frontmatter en Claude Code Agents

## Investigación realizada el 2024-12-09

### ✅ Campos CONFIRMADOS como válidos

Según la investigación y pruebas realizadas, estos campos funcionan:

```yaml
---
name: agent-name           # REQUERIDO - Identificador único
description: Agent purpose  # REQUERIDO - Descripción para activación
tools: Read, Write, Edit   # OPCIONAL - Herramientas disponibles
model: opus                # OPCIONAL - Modelo a usar (opus/sonnet/haiku)
---
```

### ⚠️ Campos CUSTOM que NO causan errores

Claude Code **IGNORA** campos desconocidos sin generar errores. Estos campos los usamos para organización interna:

```yaml
---
version: 2.0.0              # IGNORADO - Útil para versionado interno
category: coordinator       # IGNORADO - Útil para categorización
priority: critical          # IGNORADO - Útil para priorización
activation: manual          # IGNORADO - Documenta cuándo se activa
expertise_level: expert     # IGNORADO - Nivel de expertise
knowledge_scope: complete   # IGNORADO - Alcance del conocimiento
quality_level: production   # IGNORADO - Nivel de calidad esperado
---
```

### 🔍 Evidencia encontrada

1. **NO hay errores de validación** - Los 73 agentes cargan sin problemas
2. **Práctica común** - Proyecto wshobson usa `model` extensivamente
3. **Parser permisivo** - YAML parsers típicamente ignoran campos desconocidos
4. **IDE sin warnings** - VS Code/Cursor no muestra errores en los archivos

### ⚠️ Correcciones aplicadas

#### ❌ INCORRECTO
```yaml
model: sonnet-3.5  # NO usar versiones específicas
model: opus-4.1    # NO usar versiones específicas
```

#### ✅ CORRECTO  
```yaml
model: sonnet      # Solo el nombre del modelo
model: opus        # Solo el nombre del modelo
model: haiku       # Solo el nombre del modelo
```

### 📊 Resumen

| Campo | Estado | Uso |
|-------|--------|-----|
| name | ✅ Válido | Requerido |
| description | ✅ Válido | Requerido |
| tools | ✅ Válido | Opcional |
| model | ✅ Funciona | Opcional (no documentado pero funciona) |
| version | ⚠️ Ignorado | Organizacional |
| category | ⚠️ Ignorado | Organizacional |
| priority | ⚠️ Ignorado | Organizacional |
| activation | ⚠️ Ignorado | Documentación |
| expertise_level | ⚠️ Ignorado | Documentación |
| knowledge_scope | ⚠️ Ignorado | Documentación |
| quality_level | ⚠️ Ignorado | Documentación |

### 💡 Recomendación

**MANTENER los campos custom** porque:
1. No causan errores
2. Proveen metadata útil para organización
3. Podrían ser útiles en futuras versiones
4. Documentan el propósito y uso de cada agente

### 🔮 Futuro

Si Claude Code empieza a validar estrictamente, podemos:
1. Mover los campos custom a comentarios
2. Crear un archivo `.metadata.json` separado
3. Usar solo los campos válidos

---

*Documento creado para registrar los hallazgos de la investigación sobre campos YAML válidos en Claude Code agents*
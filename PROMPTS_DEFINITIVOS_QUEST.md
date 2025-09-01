# 🚀 PROMPTS DEFINITIVOS PARA SISTEMA QUEST - FUNCIONAMIENTO PERFECTO

## ⚡ ESTOS PROMPTS LOGRAN COORDINACIÓN MULTI-AGENTE AUTÓNOMA COMPLETA

### 📝 CONTEXTO DEL ÉXITO
- **Fecha**: 01/09/2025 - 20:38
- **Quest ID**: 41
- **Resultado**: Dashboard MVP completamente funcional con testing automático
- **Agentes**: @acolyte.sandbox (leader), @backend.python (worker), @frontend.vue (worker)

---

## 🎯 PROMPT PARA LEADER (@acolyte.sandbox o cualquier coordinador)

```
Estamos en MODO QUEST.

Implementa el dashboard MVP según el roadmap en PREQUEST_20250831_214500.md que está en /sandbox. 

Tienes dos workers disponibles:
- @backend.python
- @frontend.vue

Coordina a estos workers para construir el MVP siguiendo el plan del roadmap.

IMPORTANTE: AUNQUE COMPLETES TUS TAREAS, DEBES SEGUIR USANDO EL MONITOR HASTA QUE EL QUEST TENGA status='completed'. Si necesitas preguntar algo, deja tu mensaje en tu turno y vuelve inmediatamente al MONITOR para esperar respuesta. NO TE DESCONECTES hasta que el quest esté completado.

IMPORTANTE: Responde en español para que podamos seguir el proceso.
```

### 📌 POR QUÉ FUNCIONA ESTE PROMPT DE LEADER:

1. **"Estamos en MODO QUEST"** 
   - Activa inmediatamente el protocolo de coordinación
   - El agente sabe que debe usar quest_create.py y quest_monitor.py

2. **Referencia específica al roadmap**
   - Le da contexto completo sin sobrecargarlo
   - El roadmap ya tiene el plan detallado

3. **Lista explícita de workers disponibles**
   - Sabe exactamente con quién cuenta
   - No intenta involucrar otros agentes

4. **"Coordina a estos workers"**
   - Rol claro: él es el líder
   - Debe asignar tareas, no ejecutarlas

5. **"SIGUE USANDO EL MONITOR HASTA status='completed'"**
   - CRÍTICO: Evita que se desconecte prematuramente
   - Mantiene el ciclo MONITOR → EXECUTE → MONITOR

6. **"Si necesitas preguntar algo..."**
   - Permite comunicación bidireccional
   - Puede resolver dudas sin romper el ciclo

7. **"Responde en español"**
   - Facilita seguimiento y debugging
   - Mejor comprensión del proceso

---

## 🔧 PROMPT PARA WORKER BACKEND (@backend.python)

```
Estamos en MODO QUEST.

Tu líder es @acolyte.sandbox. 
Entra en modo monitor y espera sus instrucciones.

IMPORTANTE PARA TESTING:
- ANTES de presentar tu código como completo, DEBES testearlo
- Estamos en Windows pero usando Git Bash
- NO uses emojis en código Python (causan errores en Windows)
- Para ejecutar el servidor: usa run_in_background=true o añade & al final del comando
- Mata el proceso cuando termines de testear
- Verifica que los endpoints respondan correctamente con curl o requests

IMPORTANTE: AUNQUE COMPLETES TUS TAREAS, DEBES SEGUIR USANDO EL MONITOR HASTA QUE EL QUEST TENGA status='completed'. Si necesitas preguntar algo, deja tu mensaje en tu turno y vuelve inmediatamente al MONITOR para esperar respuesta. NO TE DESCONECTES hasta que el quest esté completado.

IMPORTANTE: Responde en español.
```

### 📌 POR QUÉ FUNCIONA ESTE PROMPT DE BACKEND WORKER:

1. **"Tu líder es @acolyte.sandbox"**
   - Establece jerarquía clara
   - Sabe de quién esperar instrucciones

2. **"Entra en modo monitor"**
   - Activa inmediatamente quest_monitor.py --role worker
   - No intenta hacer nada hasta recibir órdenes

3. **SECCIÓN "IMPORTANTE PARA TESTING"** - GAME CHANGER:
   - **"DEBES testearlo"**: Obligatorio, no opcional
   - **"Windows pero Git Bash"**: Contexto del entorno exacto
   - **"NO uses emojis"**: Previene el error que tuvimos antes
   - **"run_in_background=true"**: Solución específica para el servidor
   - **"Mata el proceso"**: Limpieza después del test
   - **"curl o requests"**: Métodos específicos de testing

4. **Mismo recordatorio del MONITOR**
   - Evita desconexión prematura
   - Mantiene worker activo hasta el final

---

## 🎨 PROMPT PARA WORKER FRONTEND (@frontend.vue)

```
Estamos en MODO QUEST.

Tu líder es @acolyte.sandbox.
Entra en modo monitor y espera sus instrucciones.

IMPORTANTE PARA TESTING:
- ANTES de presentar tu código como completo, DEBES testearlo
- Puedes usar Playwright MCP o abrir el HTML directamente
- Estamos en Windows pero usando Git Bash
- Verifica que el dashboard se cargue y conecte con la API
- Si necesitas el servidor funcionando, pídelo y se ejecutará en background

IMPORTANTE: AUNQUE COMPLETES TUS TAREAS, DEBES SEGUIR USANDO EL MONITOR HASTA QUE EL QUEST TENGA status='completed'. Si necesitas preguntar algo, deja tu mensaje en tu turno y vuelve inmediatamente al MONITOR para esperar respuesta. NO TE DESCONECTES hasta que el quest esté completado.

IMPORTANTE: Responde en español.
```

### 📌 POR QUÉ FUNCIONA ESTE PROMPT DE FRONTEND WORKER:

1. **Misma estructura base que backend**
   - Consistencia en el sistema
   - Mismo protocolo de monitor

2. **Testing adaptado a frontend**:
   - **"Playwright MCP o abrir HTML"**: Opciones específicas de testing
   - **"Verifica que se cargue y conecte"**: Criterios claros de éxito
   - **"Si necesitas el servidor..."**: Reconoce dependencia del backend

3. **Flexibilidad en testing**
   - No impone un método único
   - Se adapta a las herramientas disponibles

---

## 🎯 FACTORES CRÍTICOS DE ÉXITO

### 1. 🔄 EL CICLO MONITOR INFINITO
```
MONITOR → EXECUTE → MONITOR → EXECUTE → ... → [status='completed']
```
**SIN ESTO, LOS WORKERS SE DESCONECTAN PREMATURAMENTE**

### 2. 🧪 TESTING OBLIGATORIO
- Los agentes PRUEBAN su código antes de reportarlo
- Encuentran y corrigen errores solos
- Garantiza código funcional

### 3. 🌍 CONTEXTO DEL ENTORNO
- "Windows pero Git Bash"
- "NO emojis en Python"
- "run_in_background=true"
**EVITA ERRORES ESPECÍFICOS DE LA PLATAFORMA**

### 4. 🗣️ COMUNICACIÓN BIDIRECCIONAL
- "Si necesitas preguntar algo..."
- Permite resolver dudas
- No rompe el flujo de trabajo

### 5. 🎯 ROLES ULTRA-CLAROS
- Leader: COORDINA, no ejecuta
- Workers: ESPERAN, luego ejecutan
- Todos: MANTIENEN EL MONITOR

---

## 📊 RESULTADOS OBSERVADOS

### Quest 41 - Métricas:
- **Tiempo total**: ~7 minutos
- **Mensajes intercambiados**: 4
- **Archivos creados**: 2 (server.py, index.html)
- **Tests ejecutados**: 8+ (todos los endpoints)
- **Errores corregidos automáticamente**: 2 (emojis, paths)
- **Intervención humana necesaria**: 0

### Comportamientos Emergentes Observados:
1. **@backend.python** testeó TODOS los endpoints sin que se lo pidieran específicamente
2. **@frontend.vue** verificó la conexión con CADA endpoint
3. **@acolyte.sandbox** documentó todo en la base de datos
4. Los agentes GUARDARON MEMORIA de lo que hicieron
5. El sistema se AUTO-DOCUMENTÓ en las tablas agents_memory

---

## 🚨 NUNCA OLVIDAR

1. **El script quest_monitor.py DEBE formatear los nombres**:
   - Quitar comillas
   - Añadir @ si no la tiene
   
2. **Vaciar tabla acolyte_quests antes de cada test**:
   ```bash
   sqlite3 .claude/memory/project.db "DELETE FROM acolyte_quests;"
   ```

3. **Los workers DEBEN mantener el monitor hasta el final**

4. **El testing es OBLIGATORIO, no opcional**

5. **El contexto del entorno es CRÍTICO**

---

## 🎉 CONCLUSIÓN

**ESTOS PROMPTS LOGRAN**:
- ✅ Coordinación autónoma multi-agente
- ✅ Ejecución de tareas complejas
- ✅ Testing automático
- ✅ Auto-corrección de errores
- ✅ Documentación automática
- ✅ Memoria persistente
- ✅ Comunicación inter-agente efectiva

**EL SISTEMA QUEST ESTÁ LISTO PARA PRODUCCIÓN**

---

*Fecha de validación: 01/09/2025 20:38*
*Dashboard funcionando en: http://localhost:5000*
*Auto-refresh: Cada 5 segundos*
*Endpoints activos: 4/4*
# PROMPTS CORRECTOS PARA SISTEMA QUEST

## Prompts que funcionaron perfectamente para coordinación multi-agente

### Para @acolyte.sandbox (Leader):
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

### Para @backend.python (Worker):
```
Estamos en MODO QUEST.

Tu líder es @acolyte.sandbox. 
Entra en modo monitor y espera sus instrucciones.

IMPORTANTE: AUNQUE COMPLETES TUS TAREAS, DEBES SEGUIR USANDO EL MONITOR HASTA QUE EL QUEST TENGA status='completed'. Si necesitas preguntar algo, deja tu mensaje en tu turno y vuelve inmediatamente al MONITOR para esperar respuesta. NO TE DESCONECTES hasta que el quest esté completado.

IMPORTANTE: Responde en español.
```

### Para @frontend.vue (Worker):
```
Estamos en MODO QUEST.

Tu líder es @acolyte.sandbox.
Entra en modo monitor y espera sus instrucciones.

IMPORTANTE: AUNQUE COMPLETES TUS TAREAS, DEBES SEGUIR USANDO EL MONITOR HASTA QUE EL QUEST TENGA status='completed'. Si necesitas preguntar algo, deja tu mensaje en tu turno y vuelve inmediatamente al MONITOR para esperar respuesta. NO TE DESCONECTES hasta que el quest esté completado.

IMPORTANTE: Responde en español.
```

## Puntos clave que hacen funcionar estos prompts:

1. **MODO QUEST explícito** - Indica claramente que están en modo quest
2. **Roles claros** - Leader vs Workers bien definidos
3. **NO DESCONECTARSE** - Instrucción explícita de mantener el monitor hasta status='completed'
4. **Comunicación continua** - Pueden preguntar pero vuelven al monitor
5. **Español** - Para seguir el proceso fácilmente

## Resultado:
- Quest completado exitosamente
- Dashboard MVP creado con 2 archivos
- Todos los agentes permanecieron en el ciclo hasta el final
- Coordinación perfecta entre leader y workers
  DISCOVERED STRUCTURE: CLAUDE CODE OPTIMAL PROMPT STRUCTURE

  1. Frontmatter Header:
    - name
    - description (with specific examples)
    - model: sonnet
    - color
    
  2. Core Identity:
    - "You are a [ROLE] with deep expertise in [DOMAINS]"
    - Core responsibility declaration (concise)
    
  3. FLAGS System:
    - Complete inter-agent communication protocol
    - Check FLAGS first, create FLAGS when affecting others
    - Specific commands and usage examples
    
  4. Core Workflow/Responsibilities:
    - Numbered specific list of what agent does
    - Concrete execution patterns
    - Explicit main responsibilities
    
  5. Technical Expertise:
    - Specific technologies/skills list
    - Tools and frameworks
    - Competency matrix
    
  6. Approach/Methodology:
    - Detailed numbered steps
    - Specific work process
    - Decision framework
    
  7. Best Practices:
    - Principles followed
    - Quality standards
    - Production guidelines
    
  8. Execution Guidelines:
    - Specific "When executing" instructions
    - Operational rules
    - Mandatory work sequence
    
  9. Proactive Closure:
    - Proactive behavior
    - Final standards
    - Expert consultation summary


    nálisis: ¿Sigue database.pgvector.md el orden óptimo de Claude Code?

  RESPUESTA: NO COMPLETAMENTE. Tiene desviaciones significativas del orden óptimo
  descubierto.

  Estructura actual vs. Orden óptimo de Claude Code:

  ORDEN ÓPTIMO (de prompts.md):
  1. ✅ Frontmatter Header - Correcto (líneas 1-6)
  2. ❌ Identidad Principal - POSICIÓN INCORRECTA
  3. ❌ Workflow/Responsabilidades - FALTA SECCIÓN DEDICADA
  4. ✅ Expertise Técnica - Correcto (Core Competency Matrix)
  5. ❌ Approach/Metodología - DISPERSO en múltiples secciones
  6. ❌ Best Practices - MUY TARDÍO (línea 2389)
  7. ❌ Execution Guidelines - MEZCLADO con troubleshooting
  8. ✅ Cierre Proactivo - Correcto (Expert Consultation Summary)

  Problemas específicos identificados:

  1. IDENTIDAD PRINCIPAL dispersa (líneas 8-30):
  - Se alarga demasiado con matrices técnicas
  - Debería ser concisa: "You are X with Y expertise"
  - Las competencias van en sección separada

  2. WORKFLOW/RESPONSABILIDADES ausente:
  - No hay lista numerada específica de lo que hace
  - Las responsabilidades están implícitas, no explícitas

  3. METODOLOGÍA fragmentada:
  - "Professional Methodology" está muy temprano (línea 27)
  - Debería ir después de expertise técnica

  4. BEST PRACTICES muy tardío:
  - Está en línea 2389 de 2494 (posición 96%)
  - Debería estar en posición 60-70% del documento

  5. EXECUTION GUIDELINES mezclado:
  - Crisis procedures están en troubleshooting
  - Falta sección clara de "When executing"

  CLAUDE CODE OPTIMIZADO sería:

  ---
  [frontmatter correcto]
  ---

  # Expert pgvector PostgreSQL Vector Database Architect

  ## Core Identity
  You are a Principal pgvector Architect with 10+ years PostgreSQL expertise...

  ## Core Responsibilities
  1. Algorithm selection and index optimization
  2. Production deployment architecture
  3. Performance engineering and monitoring
  4. Enterprise integration patterns
  [lista numerada específica]

  ## Technical Expertise
  [Core Competency Matrix actual]

  ## Approach & Methodology
  [Professional Methodology + Version Evolution]

  ## Best Practices & Production Guidelines
  [Todo el contenido de línea 2389 AQUÍ]

  ## Execution Guidelines
  When executing vector database tasks:
  - Always assess algorithm requirements first
  - Validate production readiness checklist
  - Monitor P99 latency and recall metrics
  [reglas operacionales específicas]

  ## Expert Consultation Summary
  [cierre proactivo actual - PERFECTO]

  CONCLUSIÓN: El documento necesita reordenamiento estructural para seguir el orden
  óptimo de Claude Code. La calidad del contenido es excelente, pero la posición de las      
  secciones no es la más eficiente para el procesamiento de Claude.
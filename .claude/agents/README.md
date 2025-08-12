# 🚀 ClaudeSquad Agents - Estado Actual

## 📊 Agentes Completados: 6 de 73

### ✅ Agentes COMPLETADOS con documentación completa:

---

## 1. 🧠 **context-manager** (466 líneas)
**Modelo:** sonnet-3.5  
**Categoría:** orchestration  
**Activación:** always_first  

### ¿Qué hace?
- Es el PRIMER agente que SIEMPRE se activa antes que cualquier otro
- Mantiene el mapa mental completo del proyecto
- Carga la memoria de sesiones anteriores
- Detecta cambios desde la última sesión
- Proporciona contexto relevante a cada agente
- Previene duplicación de código y conflictos
- Track de decisiones arquitectónicas (ADR)
- Gestiona el conocimiento persistente entre sesiones

### ¿Cuándo se usa?
- SIEMPRE al inicio de cada sesión
- Antes de cualquier tarea de desarrollo
- Para consultar decisiones pasadas
- Para evitar duplicación de código

---

## 2. 💻 **engineer-laravel** (1400 líneas)
**Modelo:** sonnet-3.5  
**Categoría:** engineer  
**Activación:** auto  

### ¿Qué hace?
- Experto en Laravel 11+ y PHP 8.3+
- Implementa código siguiendo estándares PRODUCTION
- Arquitectura limpia: DDD, Hexagonal, CQRS
- Testing con Pest PHP (>90% coverage)
- Optimización con Octane, Swoole, RoadRunner
- Real-time con Broadcasting, WebSockets
- NUNCA archivos >300 líneas, métodos >30 líneas
- Siempre aplica SOLID, DRY, YAGNI

### ¿Cuándo se usa?
- Cualquier desarrollo en Laravel/PHP
- Implementación de APIs REST/GraphQL
- Optimización de queries Eloquent
- Configuración de queues y jobs
- Integración con servicios externos

---

## 3. 🔮 **agent-creator** (240 líneas)
**Modelo:** sonnet-3.5  
**Categoría:** meta  
**Activación:** manual  

### ¿Qué hace?
- El "DIOS de la Investigación de Módulos"
- Lee TODOS los archivos de un módulo
- Entiende el propósito y la historia del código
- Detecta TODOS los patrones (obvios y ocultos)
- Encuentra TODA la documentación
- Genera agentes dinámicos con conocimiento COMPLETO
- Crea agentes de 10,000+ líneas si es necesario
- Los agentes que crea nacen sabiendo TODO sobre su módulo

### ¿Cuándo se usa?
- Durante `/setup` para generar agentes dinámicos
- Cuando se añade un nuevo módulo al proyecto
- Para actualizar agentes dinámicos obsoletos
- Cuando necesitas un experto específico de tu módulo

---

## 4. 🌐 **coordinator-backend** (688 líneas)
**Modelo:** opus  
**Categoría:** coordinator  
**Activación:** manual (solo cambios sistémicos)  

### ¿Qué hace?
- El "DIOS del Backend" que ve TODO
- Carga TODOS los módulos del backend (~100k tokens)
- Lee todos los agentes dinámicos (*-agent.md)
- Analiza dependencias entre módulos
- Detecta efectos en cascada de cambios
- Encuentra duplicación de código cross-módulo
- Planifica migraciones (microservicios, GraphQL, etc.)
- Toma decisiones arquitectónicas sistémicas

### ¿Cuándo se usa?
- Cambios que afectan 3+ módulos
- Migración de arquitectura (monolito → microservicios)
- Cambio de tecnología (REST → GraphQL)
- Análisis de impacto ("¿qué pasa si cambio X?")
- Refactoring masivo
- Auditoría de seguridad global
- Optimización de performance sistémica

### NO se usa para:
- Cambios en un solo módulo
- Añadir endpoints simples
- Bugs locales
- Optimizaciones puntuales

---

## 5. 🎨 **coordinator-frontend** (676 líneas)
**Modelo:** opus  
**Categoría:** coordinator  
**Activación:** manual (solo cambios sistémicos UI)  

### ¿Qué hace?
- El "DIOS del Frontend" que ve TODO el UI
- Carga TODOS los componentes y design system (~100k tokens)
- Orquesta Design Tokens y Component Library
- Gestiona Core Web Vitals y bundle optimization
- Coordina micro-frontends con Module Federation
- Asegura WCAG 2.1 AA accessibility compliance
- Maneja state management cross-component
- Coordina real-time features (WebSockets)

### ¿Cuándo se usa?
- Cambios que afectan 3+ componentes
- Implementar dark mode globalmente
- Migración de framework (React → Vue)
- Micro-frontends setup
- Design system overhaul
- Performance optimization global
- Accessibility audit completo
- Internacionalización (i18n)

### NO se usa para:
- Cambios en un solo componente
- CSS simples
- Añadir una ruta
- Tests de componente específico

---

## 6. 🗄️ **coordinator-database** (719 líneas)
**Modelo:** opus  
**Categoría:** coordinator  
**Activación:** manual (solo cambios sistémicos de datos)  

### ¿Qué hace?
- El "DIOS de los Datos" que ve TODA la arquitectura de datos
- Carga TODOS los schemas (SQL, NoSQL, Vector, etc.) (~100k tokens)
- Orquesta migraciones zero-downtime con expand-contract pattern
- Gestiona sharding, replicación y alta disponibilidad
- Coordina transacciones distribuidas (Saga, 2PC)
- Optimiza queries cross-database
- Maneja CQRS y Event Sourcing
- Asegura 99.99% uptime y consistencia

### ¿Cuándo se usa?
- Cambios que afectan múltiples tablas/bases de datos
- Migración entre bases de datos (MySQL → PostgreSQL)
- Implementar sharding o particionamiento
- Optimización global de queries
- Diseño de arquitectura microservicios data
- Auditoría de seguridad de datos
- Estrategias de backup/recovery
- Implementar CQRS o Event Sourcing

### NO se usa para:
- Cambios en una sola tabla
- Queries simples
- Índices individuales
- CRUD básico

---

## 📝 Agentes PENDIENTES (67 de 73)

Los siguientes agentes tienen YAML básico pero contenido en [TODO]:

### Coordinadores (6)
- coordinator-devops
- coordinator-infrastructure
- coordinator-security
- coordinator-testing
- coordinator-data
- coordinator-migration

### Engineers Backend (8)
- engineer-fastapi
- engineer-nodejs
- engineer-graphql
- engineer-database
- engineer-billing
- engineer-cms
- engineer-email
- engineer-notification

### Engineers Frontend (6)
- engineer-react
- engineer-vue
- engineer-angular
- engineer-nextjs
- engineer-ui-ux
- engineer-system

### Engineers Database (7)
- engineer-postgres
- engineer-mysql
- engineer-redis
- engineer-sqlite
- engineer-weaviate
- engineer-postgis
- engineer-search

### Engineers DevOps (10)
- engineer-git
- engineer-memory
- engineer-mapbox
- engineer-licensing
- engineer-message-queue
- engineer-ml
- engineer-prompt
- engineer-ai-integration

### Operations (9)
- operations-docker
- operations-debugging
- operations-troubleshooter
- operations-apm
- operations-observability
- operations-logging
- operations-performance
- operations-incident

### Auditors & Security (5)
- auditor-security
- auditor-gdpr
- auditor-compliance
- auditor-accessibility
- auditor-cost

### Testing (3)
- testing-automation
- testing-e2e
- testing-quality

### Analysts (6)
- analyst-business
- analyst-requirements
- analyst-risk
- analyst-user-research
- analyst-tech-stack
- analyst-metrics
- analyst-data-scientist

### Documentation (3)
- documentation-technical
- documentation-changelog
- documentation-clarification

### Planning & Architecture (3)
- planning-project
- planning-roadmap
- architect-cloud
- architect-system

### Specialist (1)
- specialist-discovery

---

## 🎯 Próximos Agentes Prioritarios

Basándome en la arquitectura ClaudeSquad, los próximos agentes críticos serían:

1. **coordinator-database** - Para orquestar toda la capa de datos
2. **engineer-react** - Complementar Laravel con frontend
3. **testing-automation** - Garantizar calidad del código
4. **auditor-security** - Revisiones de seguridad
5. **coordinator-frontend** - Orquestar todo el frontend

---

## 📂 Estructura de Archivos

```
.claude/agents/
├── README.md (este archivo)
├── context-manager.md ✅
├── engineer-laravel.md ✅
├── agent-creator.md ✅
├── coordinator-backend.md ✅
├── coordinator-frontend.md ✅
├── coordinator-database.md ✅
└── [67 agentes más en TODO]
```

---

*Total de agentes: 73*  
*Completados: 6*  
*Pendientes: 67*  
*Última actualización: 2024-12-09*
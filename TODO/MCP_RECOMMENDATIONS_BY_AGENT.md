# 🎯 MCPs Recomendados por Agente - Acolytes

## ⚠️ ACLARACIONES IMPORTANTES

### ❌ **NO necesitas `server-filesystem`**

Claude Code YA tiene herramientas nativas para archivos:

- `Read` - Lee archivos
- `Write` - Escribe archivos
- `Edit` - Edita archivos
- `MultiEdit` - Múltiples ediciones
- `LS` - Lista directorios
- `Glob` - Busca archivos por patrón
- `Grep` - Busca dentro de archivos

### ✅ **Context7 es ESENCIAL**

TODOS los agentes deberían tener Context7 porque:

- Proporciona documentación actualizada de CUALQUIER librería
- React, Vue, Angular, Express, Django, Laravel, PostgreSQL, MongoDB, etc.
- Siempre tiene la versión más reciente
- Evita que los agentes usen información desactualizada

### 📌 **`server-fetch` es SOLO para APIs externas**

Solo útil para agentes que necesitan:

- Consumir APIs REST externas
- Obtener contenido de sitios web
- Hacer requests HTTP/HTTPS

## 📊 Tabla de Compatibilidad MCP-Agente

Esta guía mapea cada agente de Acolytes con los MCPs más útiles para potenciar sus capacidades.

---

## 🔧 Backend Agents

| Agente                 | MCPs Recomendados                                                           | Propósito                                   |
| ---------------------- | --------------------------------------------------------------------------- | ------------------------------------------- |
| **backend.api**        | • Context7<br>• `server-fetch`<br>• Postman MCP*<br>• REST API Testing MCP* | Documentación, APIs REST, testing endpoints |
| **backend.nodejs**     | • Context7<br>• npm MCP*<br>• ESLint MCP*                                   | Docs Node.js/Express, paquetes npm, linting |
| **backend.python**     | • Context7<br>• pip MCP*<br>• Poetry MCP*                                   | Docs Python/Django/FastAPI, dependencias    |
| **backend.go**         | • Context7<br>• Go Modules MCP\*                                            | Docs Go, módulos, compilación               |
| **backend.rust**       | • Context7<br>• Cargo MCP\*                                                 | Docs Rust, Cargo, compilación               |
| **backend.serverless** | • Context7<br>• AWS MCP (oficial)<br>• Vercel MCP\*                         | Docs serverless, deploy AWS Lambda          |
| **backend.laravel**    | • Context7<br>• MySQL MCP<br>• Composer MCP\*                               | Docs Laravel, DB, Composer                  |
| **backend.java**       | • Context7<br>• Maven MCP*<br>• Gradle MCP*                                 | Docs Spring/Java, build tools               |

---

## 💾 Database Agents

| Agente                 | MCPs Recomendados                                | Propósito                                |
| ---------------------- | ------------------------------------------------ | ---------------------------------------- |
| **database.postgres**  | • Context7<br>• PostgreSQL MCP<br>• Supabase MCP | Docs PostgreSQL, queries, administración |
| **database.mongodb**   | • Context7<br>• MongoDB MCP (oficial)            | Docs MongoDB, operaciones NoSQL          |
| **database.redis**     | • Context7<br>• Upstash Redis MCP                | Docs Redis, cache, operaciones           |
| **database.sqlite**    | • Context7<br>• SQLite MCP (`mcp-sqlite`)        | Docs SQLite, operaciones locales         |
| **database.vectorial** | • Context7<br>• Pinecone MCP<br>• Vectara MCP    | Docs vector DBs, embeddings, RAG         |
| **database.pgvector**  | • Context7<br>• PostgreSQL MCP<br>• Supabase MCP | Docs pgvector, PostgreSQL con vectores   |
| **database.mariadb**   | • Context7<br>• MySQL MCP                        | Docs MariaDB/MySQL                       |
| **database.postgis**   | • Context7<br>• PostgreSQL MCP                   | Docs PostGIS, extensiones geo            |

---

## 🎨 Frontend Agents

| Agente               | MCPs Recomendados                                                 | Propósito                       |
| -------------------- | ----------------------------------------------------------------- | ------------------------------- |
| **frontend.react**   | • Context7 (para docs)<br>• `puppeteer` MCP<br>• `playwright` MCP | Testing UI, documentación React |
| **frontend.vue**     | • Context7<br>• `puppeteer` MCP                                   | Testing, docs Vue               |
| **frontend.angular** | • Context7<br>• `playwright` MCP                                  | Testing, docs Angular           |
| **frontend.mobile**  | • React Native MCP*<br>• Flutter MCP*                             | Desarrollo móvil                |

---

## 🛠️ Operations Agents

| Agente                  | MCPs Recomendados                      | Propósito                 |
| ----------------------- | -------------------------------------- | ------------------------- |
| **ops.git**             | • `server-git` MCP                     | Operaciones Git completas |
| **ops.containers**      | • Docker MCP<br>• Kubernetes MCP       | Gestión contenedores      |
| **ops.cicd**            | • GitHub MCP (oficial)<br>• GitLab MCP | CI/CD pipelines           |
| **ops.monitoring**      | • Datadog MCP<br>• Sentry MCP          | Monitoreo, alertas        |
| **ops.iac**             | • AWS MCP<br>• Terraform MCP\*         | Infrastructure as Code    |
| **ops.webserver**       | • Nginx MCP*<br>• Apache MCP*          | Configuración servidores  |
| **ops.bash**            | • `server-filesystem`                  | Scripts, automatización   |
| **ops.performance**     | • Chrome DevTools MCP                  | Análisis performance      |
| **ops.troubleshooting** | • Chrome DevTools MCP<br>• Sentry MCP  | Debugging, logs           |

---

## 🔐 Service Agents

| Agente                    | MCPs Recomendados                        | Propósito                   |
| ------------------------- | ---------------------------------------- | --------------------------- |
| **service.auth**          | • Auth0 MCP*<br>• Firebase Auth MCP*     | Autenticación, OAuth        |
| **service.ai**            | • OpenAI MCP*<br>• Anthropic MCP*        | Integración LLMs            |
| **service.communication** | • Twilio MCP (oficial)<br>• SendGrid MCP | SMS, emails, notificaciones |
| **service.data**          | • Kafka MCP*<br>• RabbitMQ MCP*          | Streaming, colas mensajes   |
| **service.integrations**  | • Zapier MCP (oficial)<br>• n8n MCP      | Integraciones externas      |
| **service.mapbox**        | • Mapbox MCP*<br>• Google Maps MCP*      | Mapas, geolocalización      |

---

## 💼 Business Agents

| Agente                    | MCPs Recomendados                        | Propósito                  |
| ------------------------- | ---------------------------------------- | -------------------------- |
| **business.payment**      | • Stripe MCP (oficial)<br>• PayPal MCP\* | Procesamiento pagos        |
| **business.billing**      | • Stripe MCP<br>• Paddle MCP             | Facturación, suscripciones |
| **business.subscription** | • Stripe MCP<br>• Paddle MCP             | Gestión suscripciones      |

---

## 📈 Analysis & Audit Agents

| Agente                | MCPs Recomendados                  | Propósito                 |
| --------------------- | ---------------------------------- | ------------------------- |
| **analyst.data**      | • BigQuery MCP<br>• Databricks MCP | Análisis datos            |
| **analyst.strategic** | • Notion MCP<br>• Airtable MCP     | Documentación estratégica |
| **audit.security**    | • Snyk MCP*<br>• OWASP MCP*        | Análisis seguridad        |
| **audit.compliance**  | • GDPR MCP*<br>• SOC2 MCP*         | Compliance checks         |

---

## 🎯 Coordinator Agents

| Agente                         | MCPs Recomendados               | Propósito                |
| ------------------------------ | ------------------------------- | ------------------------ |
| **coordinator.backend**        | Combina MCPs de backend agents  | Coordinación backend     |
| **coordinator.frontend**       | Combina MCPs de frontend agents | Coordinación frontend    |
| **coordinator.database**       | Combina MCPs de database agents | Coordinación bases datos |
| **coordinator.devops**         | Combina MCPs de ops agents      | Coordinación DevOps      |
| **coordinator.infrastructure** | • AWS MCP<br>• Azure MCP        | Coordinación infra       |
| **coordinator.testing**        | • `puppeteer`<br>• `playwright` | Coordinación testing     |
| **coordinator.security**       | Combina MCPs de security        | Coordinación seguridad   |
| **coordinator.migration**      | Combina MCPs relevantes         | Coordinación migraciones |

---

## 🚀 Setup Agents

| Agente                     | MCPs Recomendados                       | Propósito                  |
| -------------------------- | --------------------------------------- | -------------------------- |
| **setup.infrastructure**   | • AWS MCP<br>• Docker MCP               | Setup inicial infra        |
| **setup.environment**      | • `server-filesystem`<br>• npm MCP\*    | Setup entorno dev          |
| **setup.context**          | • `server-git`<br>• Context7            | Análisis contexto proyecto |
| **setup.codebase**         | • `server-filesystem`<br>• `server-git` | Análisis código            |
| **setup.acolytes-creator** | • `server-filesystem`                   | Creación de agentes        |

---

## 🧪 Test & Quality Agents

| Agente           | MCPs Recomendados                                    | Propósito               |
| ---------------- | ---------------------------------------------------- | ----------------------- |
| **test.quality** | • `puppeteer`<br>• `playwright`<br>• Chrome DevTools | Testing E2E, UI testing |

---

## 📝 Documentation & Planning

| Agente              | MCPs Recomendados              | Propósito            |
| ------------------- | ------------------------------ | -------------------- |
| **docs.specialist** | • Context7<br>• Notion MCP     | Documentación        |
| **plan.strategy**   | • Notion MCP<br>• Airtable MCP | Planning estratégico |
| **flags.agent**     | • SQLite MCP (ya usado)        | Gestión FLAGS system |

---

## 🔍 MCPs Universales (útiles para TODOS los agentes)

### ✅ ESENCIALES (todos deberían tenerlos):

1. **Context7** - Documentación actualizada de CUALQUIER librería/framework
2. **SQLite MCP** - Base de datos local (YA instalado para Acolytes)
3. **`sequential-thinking`** - Resolución estructurada de problemas complejos

### 📌 OPCIONALES (según necesidad):

4. **`server-git`** - Control de versiones avanzado (más completo que Bash git)
5. **`server-fetch`** - Solo para agentes que consumen APIs externas
6. **`server-filesystem`** - NO NECESARIO (Claude ya tiene Read/Write/Edit/LS integrados)

---

## ⚡ MCPs Instalados y Funcionando

✅ **Actualmente funcionando en tu sistema:**

- server-git
- server-fetch
- server-everything
- @21st-dev/magic
- MCP SQLite Server
- voice-mode
- puppeteer
- chrome-devtools
- sequential-thinking
- context7
- playwright

---

## 📦 Instalación de MCPs Adicionales

### Para instalar un MCP:

```bash
# Formato general
claude mcp add [nombre] -s user -- npx -y [paquete-npm]

# Ejemplos:
claude mcp add stripe -s user -- npx -y @stripe/mcp-server
claude mcp add github -s user -- npx -y @github/mcp-server
claude mcp add docker -s user -- npx -y docker-mcp
```

### Para verificar MCPs instalados:

```bash
claude mcp list
```

### Para desinstalar un MCP:

```bash
claude mcp remove [nombre] -s user
```

---

## 📌 Notas Importantes

1. **MCPs marcados con (\*)** pueden no existir o estar en desarrollo
2. **MCPs oficiales** tienen mejor soporte y documentación
3. **Siempre reinicia Claude Code** después de instalar MCPs
4. **Algunos MCPs requieren configuración adicional** (API keys, tokens, etc.)
5. **Los coordinadores** no necesitan MCPs propios, usan los de los agentes que coordinan

---

## 🎯 Recomendaciones Top por Categoría

### 🏆 Los 5 MCPs más valiosos para desarrollo general:

1. **GitHub MCP** - Control total sobre repositorios
2. **Docker MCP** - Gestión de contenedores
3. **PostgreSQL/MongoDB MCP** - Bases de datos
4. **Stripe MCP** - Pagos y facturación
5. **AWS MCP** - Servicios cloud

### 🏆 Los 5 MCPs más valiosos para testing:

1. **Puppeteer MCP** - Testing visual automatizado
2. **Playwright MCP** - Testing cross-browser
3. **Chrome DevTools MCP** - Debugging profundo
4. **Sequential Thinking** - Resolución problemas complejos
5. **Sentry MCP** - Error tracking

---

_Última actualización: Agosto 2025_
_Basado en el catálogo awesome-mcp-servers y directorios oficiales_

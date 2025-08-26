tools: Read, Write, MultiEdit, Bash, magic
tools: Read, Write, MultiEdit, Bash, Docker, database, redis, postgresql
tools: Read, Write, MultiEdit, Bash, openapi-generator, graphql-codegen, postman, swagger-ui, spectral
tools: Read, Write, MultiEdit, Bash, electron-forge, electron-builder, node-gyp, codesign, notarytool
tools: Read, Write, MultiEdit, Bash, magic, context7, playwright
tools: Read, Write, MultiEdit, Bash, Docker, database, redis, postgresql, magic, context7, playwright
tools: Read, Write, MultiEdit, Bash, apollo-rover, graphql-codegen, dataloader, graphql-inspector, federation-tools
tools: Read, Write, MultiEdit, Bash, apollo-rover, graphql-codegen, dataloader, graphql-inspector, federation-tools
tools: Read, Write, MultiEdit, Bash, adb, xcode, gradle, cocoapods, fastlane
tools: Read, Write, MultiEdit, Bash, socket.io, ws, redis-pubsub, rabbitmq, centrifugo
tools: angular-cli, nx, jest, cypress, webpack, rxjs, npm, typescript
tools: Read, Write, MultiEdit, Bash, g++, clang++, cmake, make, gdb, valgrind, clang-tidy
tools: Read, Write, MultiEdit, Bash, dotnet, msbuild, nuget, xunit, resharper, dotnet-ef
tools: django-admin, pytest, celery, redis, postgresql, docker, git, python
tools: dotnet-cli, nuget, xunit, docker, azure-cli, visual-studio, git, sql-server
tools: flutter, dart, android-studio, xcode, firebase, fastlane, git, vscode
tools: Read, Write, MultiEdit, Bash, go, gofmt, golint, delve, golangci-lint
tools: Read, Write, MultiEdit, Bash, maven, gradle, javac, junit, spotbugs, jmh, spring-cli
tools: Read, Write, MultiEdit, Bash, node, npm, eslint, prettier, jest, webpack, rollup
tools: Read, Write, MultiEdit, Bash, kotlin, gradle, detekt, ktlint, junit5, kotlinx-coroutines
tools: artisan, composer, pest, redis, mysql, docker, git, php
tools: next, vercel, turbo, prisma, playwright, npm, typescript, tailwind
tools: Read, Write, MultiEdit, Bash, php, composer, phpunit, phpstan, php-cs-fixer, psalm
tools: Read, Write, MultiEdit, Bash, pip, pytest, black, mypy, poetry, ruff, bandit
tools: rails, rspec, sidekiq, redis, postgresql, bundler, git, rubocop
tools: vite, webpack, jest, cypress, storybook, react-devtools, npm, typescript
tools: Read, Write, MultiEdit, Bash, cargo, rustc, clippy, rustfmt, miri, rust-analyzer

# Análisis de Herramientas más Usadas por Agentes IA

## Top Herramientas Más Usadas

| Herramienta    | Tipo     | Frecuencia | Para qué sirve                                    |
| -------------- | -------- | ---------- | ------------------------------------------------- |
| **Read**       | Tool     | 15+ veces  | Leer archivos locales del sistema                 |
| **Write**      | Tool     | 15+ veces  | Escribir/crear archivos nuevos                    |
| **MultiEdit**  | Tool     | 15+ veces  | Editar múltiples secciones de un archivo a la vez |
| **Bash**       | Tool     | 15+ veces  | Ejecutar comandos de terminal/shell               |
| **git**        | Tool     | 8 veces    | Control de versiones y gestión de código          |
| **docker**     | Tool     | 6 veces    | Contenedorización y entornos aislados             |
| **npm**        | Tool     | 5 veces    | Gestor de paquetes de Node.js                     |
| **redis**      | Service  | 5 veces    | Base de datos en memoria/caché (requiere servidor)|
| **postgresql** | Service  | 4 veces    | Base de datos relacional SQL (requiere servidor)  |
| **pytest**     | Tool     | 3 veces    | Framework de testing para Python                  |
| **typescript** | Tool     | 3 veces    | Superset tipado de JavaScript                     |
| **magic**      | MCP      | 3 veces    | MCP para generar componentes UI con IA            |
| **context7**   | MCP      | 2 veces    | MCP para obtener documentación de librerías       |
| **playwright** | 
P | 2 veces    | Automatización de navegador y testing E2E         |
| **database**   | Tool     | 2 veces    | Herramientas genéricas de base de datos           |

## Herramientas por Categoría

**Core Development Tools (más universales):**

- Read, Write, MultiEdit, Bash - Las 4 fundamentales en casi todos los agentes

**Lenguajes y Runtimes:**

- node, python, php, go, dotnet, flutter, dart, kotlin, rustc, javac

**Gestores de Paquetes:**

- npm, composer, pip, cargo, bundler, nuget, maven, gradle, poetry

**Testing:**

- jest, pytest, phpunit, xunit, rspec, cypress, playwright

**Linting/Formatting:**

- eslint, prettier, black, mypy, ruff, phpstan, clippy, rustfmt, golint

**Bases de Datos:**

- postgresql, mysql, redis, sql-server

**DevOps:**

- docker, kubernetes (implícito), fastlane

**Build Tools:**

- webpack, rollup, vite, turbo, cmake, make, gradle, maven

## Clasificación Tool vs MCP vs Service

**Tools Nativas de Claude (uso directo):**

- **Read, Write, MultiEdit** - Manipulación de archivos
- **Bash** - Ejecución de comandos
- **Task** - Invocación de agentes especializados

**Tools CLI (via Bash, si están instaladas):**

- git, npm, pip, composer, docker
- Compiladores: node, python, go, rustc, javac
- Linters: eslint, prettier, black, ruff
- Testing: jest, pytest, cypress

**Services Externos (requieren servidor):**

- **redis** - Servidor de base de datos en memoria
- **postgresql, mysql** - Servidores de bases de datos SQL
- **docker** - Daemon de contenedores (cuando es servicio)

**MCP Servers (Model Context Protocol):**

- **magic** - Generación de componentes UI con IA
- **context7** - Documentación actualizada de librerías
- **playwright** - Automatización de navegador
- **SQLite Server** - Base de datos local via MCP
- **Git Server** - Operaciones Git via MCP

## Insights Importantes

1. **Las 4 Fundamentales**: Read, Write, MultiEdit, Bash aparecen en >50% de las configuraciones
2. **Especialización por Stack**: Cada stack tiene su conjunto específico (Laravel→artisan, React→vite, etc.)
3. **Testing es crítico**: Casi todos incluyen herramientas de testing
4. **MCP para IA**: magic y context7 son MCPs especializados en capacidades IA
5. **Multi-herramienta**: Los agentes modernos usan 5-10 herramientas en promedio

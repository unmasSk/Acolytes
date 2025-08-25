# 🧠 GIT_GRAFO_NEURAL - Análisis de Repositorios con Grafos

## 📚 Referencia Original
**GraphRepo**: https://github.com/xserban/GraphRepo

## 🎯 ¿Qué es GraphRepo?

GraphRepo es una herramienta de minería de repositorios que **transforma cualquier repositorio Git en una base de datos de grafos Neo4j**, permitiendo análisis avanzados sobre la estructura, evolución y relaciones del código fuente.

## 🔧 Tecnologías Utilizadas

- **Python 3.5+** - Lenguaje principal
- **Neo4j** - Base de datos de grafos
- **PyDriller** - Para minería de repositorios Git
- **Docker** - Para configuración y despliegue

## 📊 Arquitectura del Sistema

```
Repositorio Git → PyDriller → Procesamiento → Neo4j → Consultas Cypher → Insights
```

## 🌐 Modelo de Grafos

### Nodos Principales
```cypher
// Tipos de nodos en el grafo
(:Commit) - Representa cada commit
(:File) - Representa cada archivo
(:Developer) - Representa cada desarrollador
(:Method) - Representa métodos/funciones
(:Class) - Representa clases
(:Branch) - Representa ramas
```

### Relaciones
```cypher
// Relaciones entre nodos
(Developer)-[:AUTHORED]->(Commit)
(Commit)-[:MODIFIES]->(File)
(File)-[:CONTAINS]->(Method)
(File)-[:CONTAINS]->(Class)
(Commit)-[:PARENT_OF]->(Commit)
(File)-[:RENAMED_TO]->(File)
(File)-[:DEPENDS_ON]->(File)
```

## 🚀 Instalación y Configuración

### 1. Requisitos Previos
```bash
# Instalar Docker
docker --version

# Instalar Python 3.5+
python --version

# Clonar GraphRepo
git clone https://github.com/xserban/GraphRepo.git
cd GraphRepo
```

### 2. Configurar Neo4j con Docker
```bash
# Ejecutar Neo4j en Docker
docker run \
    --name neo4j-graphrepo \
    -p 7474:7474 -p 7687:7687 \
    -d \
    -v $HOME/neo4j/data:/data \
    -v $HOME/neo4j/logs:/logs \
    -v $HOME/neo4j/import:/var/lib/neo4j/import \
    -v $HOME/neo4j/plugins:/plugins \
    --env NEO4J_AUTH=neo4j/password \
    neo4j:latest
```

### 3. Instalar Dependencias Python
```bash
pip install -r requirements.txt
```

### 4. Configurar GraphRepo
```python
# config.py
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"
REPOSITORY_PATH = "/path/to/your/repo"
```

## 💡 Casos de Uso para ClaudeSquad

### 1. Análisis de Evolución de Agentes
```cypher
// Encontrar archivos de agentes más modificados
MATCH (c:Commit)-[:MODIFIES]->(f:File)
WHERE f.path CONTAINS '.claude/agents/'
RETURN f.name, COUNT(c) as modifications
ORDER BY modifications DESC
LIMIT 10
```

### 2. Detección de Archivos Acoplados
```cypher
// Archivos que siempre cambian juntos
MATCH (c:Commit)-[:MODIFIES]->(f1:File)
MATCH (c)-[:MODIFIES]->(f2:File)
WHERE f1.id < f2.id
RETURN f1.name, f2.name, COUNT(c) as co_changes
ORDER BY co_changes DESC
LIMIT 20
```

### 3. Análisis de Contribuciones
```cypher
// Quién trabaja en qué parte del sistema
MATCH (d:Developer)-[:AUTHORED]->(c:Commit)-[:MODIFIES]->(f:File)
WHERE f.path CONTAINS '.claude/'
RETURN d.name, f.path, COUNT(c) as contributions
ORDER BY contributions DESC
```

### 4. Detección de Hotspots
```cypher
// Archivos con alta frecuencia de cambios y bugs
MATCH (c:Commit)-[:MODIFIES]->(f:File)
WHERE c.message CONTAINS 'fix' OR c.message CONTAINS 'bug'
RETURN f.name, COUNT(c) as bug_fixes
ORDER BY bug_fixes DESC
LIMIT 10
```

### 5. Análisis de Dependencias
```cypher
// Grafo de dependencias entre módulos
MATCH (f1:File)-[:IMPORTS]->(f2:File)
WHERE f1.path CONTAINS '.claude/scripts/'
RETURN f1.name, f2.name
```

## 🔍 Consultas Específicas para ClaudeSquad

### Evolución del Sistema FLAGS
```cypher
// Analizar evolución del sistema FLAGS
MATCH (c:Commit)-[:MODIFIES]->(f:File)
WHERE f.content CONTAINS 'FLAGS' 
AND c.date > datetime('2025-08-01')
RETURN c.date, c.message, f.name
ORDER BY c.date
```

### Análisis de Hooks
```cypher
// Ver evolución de hooks y su estabilidad
MATCH (c:Commit)-[:MODIFIES]->(f:File)
WHERE f.path CONTAINS '.claude/hooks/'
RETURN f.name, 
       COUNT(c) as total_changes,
       COUNT(CASE WHEN c.message CONTAINS 'fix' THEN 1 END) as fixes
ORDER BY total_changes DESC
```

### Relaciones entre Agentes
```cypher
// Qué agentes se modifican juntos
MATCH (c:Commit)-[:MODIFIES]->(a1:File), 
      (c)-[:MODIFIES]->(a2:File)
WHERE a1.path CONTAINS '.claude/agents/' 
AND a2.path CONTAINS '.claude/agents/'
AND a1.id < a2.id
RETURN a1.name, a2.name, COUNT(c) as co_modifications
ORDER BY co_modifications DESC
```

## 📈 Visualizaciones Posibles

### 1. Grafo de Arquitectura
```cypher
// Visualizar arquitectura del proyecto
MATCH (f:File)
WHERE f.path CONTAINS '.claude/'
RETURN f
```

### 2. Red de Colaboración
```cypher
// Red de desarrolladores y sus áreas de trabajo
MATCH (d:Developer)-[:AUTHORED]->(c:Commit)-[:MODIFIES]->(f:File)
RETURN d, f
LIMIT 100
```

### 3. Timeline de Evolución
```cypher
// Evolución temporal del proyecto
MATCH (c:Commit)
WHERE c.date > datetime('2025-08-01')
RETURN c.date, COUNT(c) as commits_per_day
ORDER BY c.date
```

## 🎯 Beneficios para ClaudeSquad

1. **Comprensión Profunda**: Entender relaciones ocultas entre componentes
2. **Detección de Patrones**: Identificar archivos que siempre cambian juntos
3. **Análisis de Calidad**: Encontrar archivos problemáticos (muchos fixes)
4. **Optimización**: Identificar candidatos para refactoring
5. **Documentación Visual**: Generar diagramas de arquitectura automáticos
6. **Análisis de Equipo**: Ver especialización de contribuidores
7. **Predicción**: Predecir qué archivos podrían necesitar cambios

## 🛠️ Scripts de Utilidad

### Script de Indexación para ClaudeSquad
```python
# index_claudesquad.py
from graphrepo import GraphRepo

def index_claudesquad():
    """Indexar el repositorio ClaudeSquad en Neo4j"""
    
    config = {
        'neo4j_uri': 'bolt://localhost:7687',
        'neo4j_user': 'neo4j',
        'neo4j_password': 'password',
        'repository_path': 'C:/Users/bextia/Desktop/acolyte/ClaudeSquad',
        'branch': 'main'
    }
    
    gr = GraphRepo(config)
    
    # Indexar repositorio completo
    gr.index_repository()
    
    # Agregar análisis específicos para ClaudeSquad
    gr.analyze_agents()
    gr.analyze_flags_system()
    gr.analyze_hooks()
    
    print("Indexación completa!")

if __name__ == "__main__":
    index_claudesquad()
```

### Consultas Automatizadas
```python
# analyze_claudesquad.py
from neo4j import GraphDatabase

class ClaudeSquadAnalyzer:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def find_critical_files(self):
        """Encontrar archivos críticos del sistema"""
        with self.driver.session() as session:
            result = session.run("""
                MATCH (c:Commit)-[:MODIFIES]->(f:File)
                WHERE f.path CONTAINS '.claude/'
                RETURN f.name, COUNT(DISTINCT c) as changes,
                       COUNT(DISTINCT c.author) as authors
                ORDER BY changes * authors DESC
                LIMIT 10
            """)
            return result.values()
    
    def analyze_agent_coupling(self):
        """Analizar acoplamiento entre agentes"""
        with self.driver.session() as session:
            result = session.run("""
                MATCH (c:Commit)-[:MODIFIES]->(a1:File),
                      (c)-[:MODIFIES]->(a2:File)
                WHERE a1.path CONTAINS 'agents'
                AND a2.path CONTAINS 'agents'
                AND a1.id < a2.id
                RETURN a1.name, a2.name, COUNT(c) as coupling_score
                ORDER BY coupling_score DESC
            """)
            return result.values()
    
    def close(self):
        self.driver.close()
```

## 🚨 Consideraciones Importantes

1. **Privacidad**: GraphRepo indexa TODO el historial de Git
2. **Rendimiento**: La indexación inicial puede tomar tiempo en repos grandes
3. **Espacio**: Neo4j puede requerir bastante espacio para repos grandes
4. **Actualización**: Necesita re-indexar periódicamente para mantener actualizado

## 📊 Métricas Clave a Monitorear

- **Complejidad Ciclomática** por archivo
- **Churn Rate** (frecuencia de cambios)
- **Coupling Score** (acoplamiento entre archivos)
- **Bug Density** (bugs por línea de código)
- **Knowledge Distribution** (distribución del conocimiento)
- **Technical Debt Indicators** (indicadores de deuda técnica)

## 🔮 Futuras Extensiones

1. **Integración con FLAGS**: Crear FLAGS automáticos basados en patrones detectados
2. **Predicción con ML**: Predecir qué archivos necesitarán cambios
3. **Análisis de Sentimiento**: Analizar mensajes de commit para detectar frustración
4. **Detección de Anomalías**: Identificar commits o patrones inusuales
5. **Recomendaciones**: Sugerir refactoring basado en métricas

## 📝 Notas de Implementación

Para ClaudeSquad específicamente, sería útil:

1. Crear vistas personalizadas para:
   - Sistema de agentes
   - Sistema FLAGS
   - Hooks y su estabilidad
   - Evolución de la base de datos

2. Automatizar análisis periódicos para detectar:
   - Nuevos hotspots
   - Degradación de calidad
   - Oportunidades de refactoring

3. Integrar con el sistema de memoria SQLite para:
   - Guardar métricas históricas
   - Crear FLAGS automáticos
   - Alimentar decisiones de arquitectura

---

**Última actualización**: 2025-08-25
**Creado por**: Claude con referencia a GraphRepo
**Estado**: Documentación inicial - Pendiente implementación
# 🔧 Configuración n8n-mcp para flow.massk.me

## Añadir a claude_desktop_config.json:

```json
{
  "mcpServers": {
    // ... otros servidores ...
    "n8n-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "n8n-mcp"
      ],
      "env": {
        "N8N_API_URL": "https://flow.massk.me",
        "N8N_API_KEY": "tu-api-key-aqui"
      }
    }
  }
}
```

## Pasos para configurar:

1. **En tu servidor n8n (cuando esté online):**
   - Accede a flow.massk.me
   - Ve a Settings → API
   - Genera un API Key
   - Copia el key

2. **En tu PC local:**
   - Edita `C:\Users\bextia\AppData\Roaming\Claude\claude_desktop_config.json`
   - Añade la configuración de arriba
   - Reemplaza "tu-api-key-aqui" con tu API key real
   - Reinicia Claude Code

## Características cuando esté conectado:

- ✅ **Crear workflows** desde Claude
- ✅ **Actualizar workflows** existentes
- ✅ **Validar workflows** antes de deployment
- ✅ **Trigger webhooks** para ejecutar workflows
- ✅ **Listar workflows** y sus configuraciones
- ✅ **Documentar automáticamente** tus flows

## Info sobre tu setup:

- **Servidor**: Unraid (físico en tienda)
- **n8n**: Corriendo en Docker
- **URL**: flow.massk.me
- **Estado**: Actualmente offline

## Comandos útiles cuando esté conectado:

```python
# Listar workflows
mcp__n8n-mcp__n8n_list_workflows()

# Crear workflow
mcp__n8n-mcp__n8n_create_workflow(workflow_json)

# Validar workflow
mcp__n8n-mcp__n8n_validate_workflow(workflow_json)

# Trigger webhook
mcp__n8n-mcp__n8n_trigger_webhook_workflow(webhook_id, data)
```
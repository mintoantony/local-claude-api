# Local Claude API

A lightweight REST API wrapper around Claude Code that allows applications, Postman, scripts, and automation tools to interact with your existing Claude Code subscription via HTTP.

Unlike the Anthropic SDK, this solution does **not** require an Anthropic API key. It uses the locally authenticated Claude CLI installation.

## Architecture

```text
Application / Postman
          |
          v
      FastAPI
          |
          v
     Claude CLI
          |
          v
 Claude Subscription
```

## Prerequisites

### 1. Install Claude Code

Verify Claude is installed:

```bash
claude --version
```

If successful, you'll see a version number.

### 2. Log in to Claude

```bash
claude login
```

Verify authentication:

```bash
claude -p "Hello Claude"
```

If Claude responds, authentication is working.

### 3. Install Python

Recommended:

```bash
Python 3.10+
```

Verify:

```bash
python --version
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn
```

---

# API Implementation

Save as:

```text
api.py
```



---

# Running the API

Start the server:

```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

Expected output:

```text
INFO: Uvicorn running on http://0.0.0.0:8000
```

---

# Testing

## Browser

Open:

```text
http://localhost:8000
```

Expected response:

```json
{
  "status": "ok"
}
```

---

## Swagger UI

FastAPI automatically generates API documentation.

Open:

```text
http://localhost:8000/docs
```

From here you can:

- View endpoints
- Send requests
- Inspect responses
- Test without Postman

---

# Postman Documentation

## Health Check

### Request

**Method**

```http
GET
```

**URL**

```text
http://localhost:8000/
```

### Response

```json
{
  "status": "ok"
}
```

---

## Ask Claude

### Request

**Method**

```http
POST
```

**URL**

```text
http://localhost:8000/ask
```

### Headers

```text
Content-Type: application/json
```

### Body

```json
{
  "prompt": "Explain Retrieval Augmented Generation"
}
```

### Sample Response

```json
{
  "response": "Retrieval Augmented Generation (RAG) is..."
}
```

---

# Example Postman Collection

```json
{
  "info": {
    "name": "Local Claude API"
  },
  "item": [
    {
      "name": "Health Check",
      "request": {
        "method": "GET",
        "url": "http://localhost:8000/"
      }
    },
    {
      "name": "Ask Claude",
      "request": {
        "method": "POST",
        "header": [
          {
            "key": "Content-Type",
            "value": "application/json"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{ \"prompt\": \"Hello Claude\" }"
        },
        "url": "http://localhost:8000/ask"
      }
    }
  ]
}
```

Import this JSON into Postman to create a starter collection.

---

# Sample cURL Commands

## Health Check

```bash
curl http://localhost:8000/
```

---

## Ask Claude

Linux / macOS

```bash
curl -X POST \
http://localhost:8000/ask \
-H "Content-Type: application/json" \
-d '{"prompt":"Explain MCP"}'
```

Windows PowerShell

```powershell
curl.exe -X POST `
http://localhost:8000/ask `
-H "Content-Type: application/json" `
-d "{\"prompt\":\"Explain MCP\"}"
```

---

# Python Client Example

```python
import requests

response = requests.post(
    "http://localhost:8000/ask",
    json={
        "prompt": "What is MCP?"
    }
)

print(response.json())
```

---

# Troubleshooting

## Claude CLI Not Found

Error:

```text
RuntimeError: Claude CLI not found in PATH
```

Verify:

```bash
claude --version
```

If this fails, install or add Claude to your PATH.

---

## Authentication Issues

Verify Claude authentication:

```bash
claude -p "Hello Claude"
```

If prompted to authenticate:

```bash
claude login
```

---

## Timeout Errors

Long prompts may exceed the configured timeout.

Current timeout:

```python
timeout=300
```

Increase as required.

---

# Future Enhancements

Possible improvements:

- Conversation history
- Streaming responses
- OpenAI-compatible endpoints
- API key protection
- Docker support
- HTTPS support
- Logging and monitoring
- Multi-user sessions
- AGENTS.md context injection
- MCP integration

---

# License

Internal use / proof-of-concept.
Modify and distribute as required.
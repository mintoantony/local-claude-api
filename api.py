from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import shutil

app = FastAPI(title="Local Claude API")

claude_exe = (
    shutil.which("claude")
    or shutil.which("claude.cmd")
    or shutil.which("claude.exe")
)

if not claude_exe:
    raise RuntimeError("Claude CLI not found in PATH")


class Question(BaseModel):
    prompt: str


@app.get("/")
def health():
    return {"status": "ok"}


@app.post("/ask")
def ask(question: Question):
    try:
        result = subprocess.run(
            [claude_exe, "-p", question.prompt],
            capture_output=True,
            text=True,
            timeout=300
        )

        if result.returncode != 0:
            raise HTTPException(
                status_code=500,
                detail=result.stderr
            )

        return {
            "response": result.stdout.strip()
        }

    except subprocess.TimeoutExpired:
        raise HTTPException(
            status_code=504,
            detail="Claude request timed out"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
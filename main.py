import os
import subprocess

port = os.environ.get("PORT", "8000")

subprocess.run(
    [
        "tooluniverse-smcp",
        "--transport", "sse",
        "--host", "0.0.0.0",
        "--port", str(port),
        "--compact-mode",
        "--name", "ToolUniverse MCP (Render)"
    ],
    check=True
)

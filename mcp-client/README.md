# This is a MCP project demo
- author:liwei liu
- SJTU

## file structure
---
## 项目运行教程
- `conda activate mcp`
- `uv venv (myenvname)`
- `.venv\Scripts\activate`
- `uv run mcp-client.py server.py`
---
**注意**：使用模型必须支持mcp调用，如qwen-plus, 百炼平台的deepseek系列暂不支持（截止6月底）
## uv 命令使用

- 创建项目
```bash
uv init project-name
``` 
- 安装依赖
```bash
uv add mcp openai python-dotenv httpx
``` 
- 运行项目
```bash
uv run mcp-client.py server.py
``` 
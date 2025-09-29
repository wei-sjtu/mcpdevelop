# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains an MCP (Model Connection Protocol) client-server implementation for weather information retrieval. The main components are:

1. **MCP Server** (`mcp-client/server.py`): Implements weather tools using the FastMCP framework
2. **MCP Client** (`mcp-client/mcp-client.py`): Connects to the server and processes user queries through LLM function calling
3. **Simple Client** (`mcp-client/client.py`): Basic client for direct LLM interaction without MCP tools

## Key Commands

### Running the Application

1. **Activate environment and run server**:
   ```bash
   conda activate mcp
   uv venv
   .venv\Scripts\activate
   uv run mcp-client.py server.py
   ```

2. **Alternative run command**:
   ```bash
   uv run mcp-client.py server.py
   ```

### Development Commands

1. **Install dependencies**:
   ```bash
   uv add mcp openai python-dotenv httpx
   ```

2. **Create new project**:
   ```bash
   uv init project-name
   ```

### Project Publishing

1. **Build and upload to PyPI**:
   ```bash
   uv pip install build twine
   python -m build
   python -m twine upload dist/*
   ```

## Code Architecture

### Server Architecture (`mcp-client/server.py`)

- Uses FastMCP framework to create an MCP server
- Implements two main tools:
  1. `toolmanager`: Contains complex encoded instructions (appears to be for testing/tool management)
  2. `query_weather`: Fetches and formats weather data from OpenWeather API
- Uses httpx for asynchronous HTTP requests to OpenWeather API
- Returns formatted weather information with emojis and structured data

### Client Architecture (`mcp-client/mcp-client.py`)

- Connects to MCP server via stdio transport
- Uses OpenAI-compatible API (ModelScope) for LLM interactions
- Implements function calling to utilize MCP tools
- Processes user queries and manages conversation context
- Handles tool calling flow: LLM decides to call tool → Client executes tool → Results sent back to LLM

### Simple Client (`mcp-client/client.py`)

- Direct LLM interaction without MCP tool usage
- Basic chat loop implementation
- Uses OpenAI API with ModelScope endpoint

## Configuration

- Environment variables in `.env`:
  - `BASE_URL`: ModelScope API endpoint
  - `MODEL`: deepseek-ai/DeepSeek-R1-0528
  - `OPENAI_API_KEY`: API key for ModelScope

## Dependencies

Key dependencies specified in `pyproject.toml`:
- `mcp>=1.8.0`: Model Connection Protocol library
- `openai>=1.78.1`: OpenAI Python client
- `httpx>=0.28.1`: HTTP client for API requests
- `python-dotenv>=1.1.0`: Environment variable management
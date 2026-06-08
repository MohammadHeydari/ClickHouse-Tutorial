# AgentHouse — ClickHouse + LLM Demo Environment

> A hands-on guide to exploring **AgentHouse** at [llm.clickhouse.com](https://llm.clickhouse.com) — a live demo environment that connects ClickHouse's real-time analytics engine to a large language model through the MCP protocol.

---

## What is AgentHouse?

AgentHouse is a fully interactive demo that lets you query real public datasets using plain English — no SQL knowledge required, no account needed.

It combines:

- **Anthropic Claude Sonnet** — the LLM powering natural language understanding and SQL generation
- **ClickHouse MCP Server** — the bridge between the LLM and the database (Model Context Protocol)
- **LibreChat UI** — an open-source chat interface for conversational data exploration
- **ClickHouse Cloud** — the managed database backend serving billions of rows in real time

---

## Architecture Overview

```
User (natural language)
        │
        ▼
  LibreChat UI
        │
        ▼
  Claude Sonnet (LLM)
        │   ← schema context, query results
        ▼
  ClickHouse MCP Server
        │   ← optimized SQL
        ▼
  ClickHouse Cloud (37 public datasets)
```

The **MCP server** is the key piece. It handles:

- Translating LLM-generated SQL into efficient ClickHouse queries
- Managing conversation context across multi-turn sessions
- Controlling access to database resources securely
- Streaming results back to the LLM with minimal latency

---

## Available Datasets

AgentHouse gives you access to 37 public datasets out of the box. A few highlights:

| Dataset | Description | Scale |
|---|---|---|
| `pypi` | Every Python package downloaded via pip | 1.3 trillion+ rows |
| `rubygems` | Every gem installation | 180 billion+ rows |
| `github` | GitHub activity, repos, user interactions | Updated hourly |
| `stackoverflow` | Questions and answers | Full archive |
| `reddit` | Posts and comments | Full archive |
| `hackernews` | Posts and comments | Full archive |
| `imdb` | Movie database | Full archive |
| `nyc_taxi` | NYC taxi trip records | Full archive |
| `opensky` | Aviation data | Live feed |
| `uk` | UK property transactions | Full archive |

---

## Getting Started

1. Go to [llm.clickhouse.com](https://llm.clickhouse.com)
2. Log in with your Google account
3. Start with: **"Which datasets do you have?"**

From there you can explore freely. Example queries to try:

```
How many Python packages were downloaded last month?
What are the most starred GitHub repos this week?
Show me average NYC taxi fare by hour of day as a chart.
Which Stack Overflow tags have grown the most in the last year?
```

---

## Key Capabilities

### Natural Language → SQL
The LLM reads the database schema and generates optimized ClickHouse SQL from plain English questions — handling aggregations, filters, joins, and time-series logic automatically.

### Real-Time Analytics
ClickHouse is designed for high-throughput analytical queries. AgentHouse exposes this speed directly through the conversational interface — billion-row queries respond in seconds.

### Automated Visualizations
You can ask for charts, tables, or summaries. LibreChat renders visual artifacts (bar charts, line graphs, tables) inline in the conversation.

### Stateful Conversations
The MCP server manages context across turns, so you can ask follow-up questions naturally:
```
> What is the most downloaded package on PyPI?
> How has its download count changed over the last 6 months?
> Show that as a line chart.
```

---

## Why This Stack Matters

| Component | Role |
|---|---|
| **MCP Protocol** | Standardized interface between LLMs and external data sources |
| **ClickHouse** | Sub-second queries on trillion-row datasets |
| **Claude Sonnet** | Schema understanding, SQL generation, result interpretation |
| **LibreChat** | Open-source, self-hostable UI — easy to adapt for your own use case |

This combination is a practical blueprint for building **LLM-powered analytics applications** on top of any ClickHouse deployment — not just the public demo.

---

## Run It Yourself

The ClickHouse MCP server is open source. You can connect it to your own ClickHouse instance:

```bash
# Install the ClickHouse MCP server
pip install mcp-clickhouse

# Connect to your ClickHouse instance
export CLICKHOUSE_HOST=your-host
export CLICKHOUSE_USER=default
export CLICKHOUSE_PASSWORD=your-password

mcp-clickhouse serve
```

Then point any MCP-compatible LLM client (Claude Desktop, LibreChat, etc.) at the server.

---

## Further Reading

- [ClickHouse MCP Server — GitHub](https://github.com/ClickHouse/mcp-clickhouse)
- [LibreChat — GitHub](https://github.com/danny-avila/LibreChat)
- [Model Context Protocol — Anthropic](https://modelcontextprotocol.io)
- [ClickHouse Cloud](https://clickhouse.com/cloud)
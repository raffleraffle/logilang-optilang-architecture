# LogiLang ↔ OptiLang Architecture

This repository implements a two-layer language architecture for LLM systems:

## Languages

### LogiLang
- Verbatim, immutable event logging language
- Stores **exact user and assistant messages**
- No interpretation, no summarization
- Acts as the single source of truth

### OptiLang
- Semantic intermediate representation (IR)
- Derived from LogiLang
- Used for reasoning, tools, agents, training, and memory

## Why this exists

Most LLM systems destroy information early by:
- Summarizing
- Embedding
- Normalizing text

This architecture **preserves raw meaning first**, then derives semantics later.

## Components

- Logger service → writes LogiLang events
- Derivation service → converts LogiLang → OptiLang
- Scripts → integrity, replay, auditing
- Specs → formal language definitions

## Quick start (local)

```bash
pip install flask
python services/logger/app.py
python services/derivation/derive.py
```

## Philosophy

Never destroy information you might want to reinterpret later.

This repo is meant to be a research-grade foundation, not a toy demo.

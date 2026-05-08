# CLAUDE.md — Entity Agents (Python)

This file provides guidance to Claude Code when working with code in this repository.

---

## Quick Reference

| Info | Value |
|------|-------|
| **Project** | Entity Agents (Python) |
| **Language** | Python 3.10+ |
| **Build** | Setuptools |
| **Linting** | Ruff, Black |
| **Test Framework** | pytest + pytest-asyncio |
| **Current Branch** | `main` |

---

## Project Type

Tags: `python`, `library`

**Phase gates:** Follow the global phase gate checklist — code review, audit, QA, pen tests, deploy. See `~/.claude/CLAUDE.md` § Working Methodology.

**Code development principles:** Follow the global principles — think before coding, simplicity first, surgical changes, goal-driven execution. See `~/.claude/CLAUDE.md` § Code Development Principles.

---

## Directory Structure

```
entity-agents-python/
├── CLAUDE.md
├── pyproject.toml
├── shared/
├── sydney/
├── amber/
├── tango/
├── brettjr/
├── valentina/
├── victoria/
├── sophie/
├── asheton/
├── denisy/
├── quinn/
├── shelly/
└── vera/
```

## Setup

```bash
pip install -e .
pip install -e ".[dev]"
```

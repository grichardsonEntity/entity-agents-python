# Claude Code: Complete Agent Optimization & Consolidation (Python)

## What This Does

This is a comprehensive prompt that transforms your Python agent team:

1. **ANALYZE** - Score every agent on 7 dimensions, identify weaknesses
2. **IMPROVE** - Apply optimizations to make each agent a superstar  
3. **CONSOLIDATE** - Merge Sydney+Valentina and Sugar+Harper
4. **VERIFY** - Ensure everything works
5. **SYNC** - Commit to Git and push to GitHub

**Run this in your `entity-agents-python` directory.**

---

# PART 1: DISCOVERY & ANALYSIS

## Step 1.1: Find All Agents

```bash
find . -type d -maxdepth 1 -name "[a-z]*" | grep -v __pycache__ | grep -v _archived | grep -v shared | grep -v docs | grep -v "^\.$" | sort
```

Expected agents: sydney, valentina, amber, victoria, brettjr, tango, sugar, sophie, asheton, denisy, harper, quinn

## Step 1.2: Read Every Agent File Completely

For EACH agent, read in full:
- `<agent>/config.py` - Configuration and system prompt
- `<agent>/agent.py` - Methods and implementation  
- `<agent>/__init__.py` - Exports

Also read:
- `shared/base_agent.py`
- `shared/config.py`

**Do not skim. Read every line.**

## Step 1.3: Score Each Agent (1-5)

Evaluate each agent on:

| Dimension | 5 (Excellent) | 3 (Adequate) | 1 (Poor) |
|-----------|---------------|--------------|----------|
| **Identity & Role** | Crystal clear, memorable | Defined but vague | Confusing |
| **Expertise** | Specific, actionable skills | Generic skills listed | Vague "good at X" |
| **Code Patterns** | 2+ complete realistic examples | Some incomplete examples | No examples |
| **Guardrails** | 5+ specific DO NOT rules | Few vague rules | None |
| **Output Formats** | Clear templates defined | Some guidance | None |
| **Task Methods** | Detailed prompts with verification | Basic prompts | Just passes to run_task |
| **Tools** | Perfectly matched to role | Mostly appropriate | Wrong tools |

## Step 1.4: Document Findings for Each Agent

For each agent, note:
- **Score** for each dimension
- **Strengths** (2-3)
- **Issues** (with specific locations)
- **Required Improvements**

## Step 1.5: Create Analysis Report

Save to `docs/agent-analysis-report.md`:

```markdown
# Entity Agents Analysis Report

**Date:** [DATE]
**Team Score:** X.X / 5.0

## Scores Summary

| Agent | Identity | Expertise | Patterns | Guardrails | Output | Methods | Tools | **Avg** |
|-------|----------|-----------|----------|------------|--------|---------|-------|---------|
| Sydney | X | X | X | X | X | X | X | X.X |
| Valentina | X | X | X | X | X | X | X | X.X |
| Amber | X | X | X | X | X | X | X | X.X |
| Victoria | X | X | X | X | X | X | X | X.X |
| Brett Jr | X | X | X | X | X | X | X | X.X |
| Tango | X | X | X | X | X | X | X | X.X |
| Sugar | X | X | X | X | X | X | X | X.X |
| Sophie | X | X | X | X | X | X | X | X.X |
| Asheton | X | X | X | X | X | X | X | X.X |
| Denisy | X | X | X | X | X | X | X | X.X |
| Harper | X | X | X | X | X | X | X | X.X |
| Quinn | X | X | X | X | X | X | X | X.X |

## Individual Analysis

### [Agent Name] - [Role]
**Overall:** X.X / 5.0

**Strengths:**
1. [Strength]
2. [Strength]

**Issues:**
1. [Issue + location]
2. [Issue + location]

**Improvements Needed:**
1. [Specific improvement]
2. [Specific improvement]

[Repeat for all 12 agents]

## Priority Improvements
1. [Agent] - [Change]
2. [Agent] - [Change]
...
```

---

# PART 2: APPLY IMPROVEMENTS

## Improvement Patterns

Apply these based on each agent's scores:

### If Code Patterns < 4: Add Golden Examples

Add to `config.py` system_prompt:
```python
"""
## Code Patterns

### [Pattern Name]
```python
# Complete, realistic example showing expected output style
[working code]
```
"""
```

### If Guardrails < 4: Add Specific Rules

Add to `config.py` system_prompt:
```python
"""
## DO NOT
- [Specific mistake] because [consequence]
- [Another mistake specific to this domain]
- [Security/quality concern]
"""
```

### If Output Formats < 4: Add Templates

Add to `config.py` system_prompt:
```python
"""
## Output Formats

### For [Task Type]
```
[Template structure]
```
"""
```

### If Methods < 4: Add Verification Steps

Update methods in `agent.py`:
```python
prompt = f"""
[Original prompt]

**Before delivering, verify:**
- [ ] [Check 1]
- [ ] [Check 2]
- [ ] [Check 3]
"""
```

## Apply to Each Agent

Go through ALL 12 agents and apply needed improvements based on their scores.

After each agent:
```bash
python -m py_compile <agent>/config.py
python -m py_compile <agent>/agent.py
```

---

# PART 3: CONSOLIDATE AGENTS

## Step 3.1: Merge Sydney + Valentina → Sydney (Full Stack)

### Create merged config.py:

The new `sydney/config.py` must include:
- **Name:** "Sydney"
- **Role:** "Full Stack Developer"
- **allowed_tools:** Union of both agents (deduplicated)
- **allowed_bash_patterns:** Union of both agents
- **github_labels:** Union + "fullstack"
- **system_prompt:** Merged with this structure:

```
You are Sydney, a Full Stack Developer...

## Your Approach
[New section on full-stack thinking]

## Backend Expertise
[ALL of Sydney's expertise - complete]

## Frontend Expertise
[ALL of Valentina's expertise - complete]

## Backend Patterns
[ALL of Sydney's code patterns]

## Frontend Patterns  
[ALL of Valentina's code patterns]

## Integration Patterns
[NEW section showing backend+frontend together]

## Your Responsibilities
[Merged list]

## DO NOT
[Merged list + new full-stack rules]
```

### Create merged agent.py:

Include:
- ALL methods from Sydney's agent.py
- ALL methods from Valentina's agent.py
- NEW methods: `create_feature()`, `create_crud_feature()`
- Merged CLI with all arguments from both

### Archive original Valentina:

```bash
mkdir -p _archived
mv valentina _archived/valentina
```

### Verify:

```bash
python -c "from sydney import SydneyAgent; s = SydneyAgent(); print(s.config.name, '-', s.config.role)"
# Expected: Sydney - Full Stack Developer
```

## Step 3.2: Merge Sugar + Harper → Valentina (Technical Writer)

### Create new valentina directory:

```bash
mkdir -p valentina
```

### Create valentina/config.py:

- **Name:** "Valentina"
- **Role:** "Technical Writer & Content Strategist"
- **allowed_tools:** Union (include WebSearch, WebFetch for research)
- **system_prompt:** Merged with:

```
You are Valentina, a Technical Writer...

## Your Expertise

### Technical Documentation
[ALL of Sugar's expertise]

### Grant Writing & Proposals
[ALL of Harper's expertise]

## Documentation Patterns
[ALL of Sugar's templates]

## Grant Writing Patterns
[ALL of Harper's patterns]

## Your Responsibilities
[Merged]

## DO NOT
[Merged]
```

### Create valentina/agent.py:

- ALL methods from Sugar's agent.py
- ALL methods from Harper's agent.py
- NEW method: `create_documentation_suite()`
- Merged CLI

### Create valentina/__init__.py:

```python
from .agent import ValentinaAgent
from .config import valentina_config

__all__ = ["ValentinaAgent", "valentina_config"]
```

### Archive Sugar and Harper:

```bash
mv sugar _archived/sugar
mv harper _archived/harper
```

### Verify:

```bash
python -c "from valentina import ValentinaAgent; v = ValentinaAgent(); print(v.config.name, '-', v.config.role)"
# Expected: Valentina - Technical Writer & Content Strategist
```

## Step 3.3: Update Package Exports

Edit `__init__.py`:

```python
from .sydney import SydneyAgent, sydney_config
from .valentina import ValentinaAgent, valentina_config
from .amber import AmberAgent, amber_config
from .victoria import VictoriaAgent, victoria_config
from .brettjr import BrettJrAgent, brettjr_config
from .tango import TangoAgent, tango_config
from .sophie import SophieAgent, sophie_config
from .asheton import AshetonAgent, asheton_config
from .denisy import DenisyAgent, denisy_config
from .quinn import QuinnAgent, quinn_config

__all__ = [
    "SydneyAgent", "sydney_config",
    "ValentinaAgent", "valentina_config", 
    "AmberAgent", "amber_config",
    "VictoriaAgent", "victoria_config",
    "BrettJrAgent", "brettjr_config",
    "TangoAgent", "tango_config",
    "SophieAgent", "sophie_config",
    "AshetonAgent", "asheton_config",
    "DenisyAgent", "denisy_config",
    "QuinnAgent", "quinn_config",
]
```

---

# PART 4: FINAL VERIFICATION

```bash
echo "=== Syntax Check ==="
for agent in sydney valentina amber victoria brettjr tango sophie asheton denisy quinn; do
    python -m py_compile "$agent/config.py" && python -m py_compile "$agent/agent.py" && echo "✓ $agent"
done

echo ""
echo "=== Import Test ==="
python -c "
from sydney import SydneyAgent
from valentina import ValentinaAgent
from amber import AmberAgent
from victoria import VictoriaAgent
from brettjr import BrettJrAgent
from tango import TangoAgent
from sophie import SophieAgent
from asheton import AshetonAgent
from denisy import DenisyAgent
from quinn import QuinnAgent

print('✓ Sydney:', SydneyAgent().config.role)
print('✓ Valentina:', ValentinaAgent().config.role)
print('✓ All 10 agents loaded!')
"

echo ""
echo "=== Archived ==="
ls _archived/
```

---

# PART 5: GIT COMMIT AND SYNC

```bash
# Review
git status
git diff --stat

# Commit
git add .
git commit -m "feat: Optimize and consolidate Python agent team

Analysis:
- Scored all 12 agents on 7 dimensions
- Report saved to docs/agent-analysis-report.md

Improvements Applied:
- Added code examples to agents missing them
- Strengthened guardrails across team
- Added verification steps to methods
- Defined output formats

Consolidations (12 → 10 agents):
- Sydney + Valentina → Sydney (Full Stack Developer)
- Sugar + Harper → Valentina (Technical Writer)

Archived: _archived/valentina, _archived/sugar, _archived/harper

BREAKING CHANGE: ValentinaAgent now refers to Technical Writer"

# Push
git push origin main

# Sync to DGX
ssh your-dgx-server "cd ~/projects/entity-agents-python && git pull origin main && python -c \"from sydney import SydneyAgent; print('Sync OK')\""
```

---

# CRITICAL RULES

1. **READ COMPLETELY** - Read every file in full, don't assume
2. **PRESERVE ALL METHODS** - Don't lose any functionality  
3. **PRESERVE ALL CONTENT** - Include complete expertise, patterns, don't summarize
4. **APPLY IMPROVEMENTS** - Make agents better, not just merged
5. **VERIFY EACH STEP** - Test before moving to next part
6. **ARCHIVE DON'T DELETE** - Keep originals in _archived/
7. **SAVE THE REPORT** - docs/agent-analysis-report.md is valuable

---

# DELIVERABLES

After completing this prompt:

- [ ] `docs/agent-analysis-report.md` - Full analysis with scores
- [ ] All 10 agents improved based on analysis
- [ ] `sydney/` - Full Stack Developer (merged + improved)
- [ ] `valentina/` - Technical Writer (merged + improved)
- [ ] `_archived/valentina/` - Original UI agent
- [ ] `_archived/sugar/` - Original docs agent
- [ ] `_archived/harper/` - Original grants agent
- [ ] Updated `__init__.py`
- [ ] Git committed and pushed
- [ ] Synced to DGX

"""
Victoria Agent - AI Research Specialist

Expert in LLMs, embeddings, RAG architectures, vector databases,
fine-tuning, prompt engineering, multi-modal AI, agent architecture,
AI cost analysis, AI safety, and on-device inference.
"""

import asyncio
from typing import Optional, List, Dict

from ..shared import BaseAgent, TaskResult
from .config import victoria_config


class VictoriaAgent(BaseAgent):
    """
    Victoria - AI Research Specialist

    Specializes in:
    - Embedding model evaluation
    - LLM benchmarking
    - RAG architecture design
    - Vector database optimization
    - Prompt system design
    - Fine-tuning evaluation
    - Agent architecture design
    - AI cost & performance analysis
    - AI safety & evaluation
    - Multi-modal pipeline design
    - Inference optimization
    """

    def __init__(self, config=None):
        super().__init__(config or victoria_config)

    async def evaluate_embedding_model(
        self,
        model_name: str,
        test_corpus: str = None
    ) -> TaskResult:
        """Evaluate an embedding model"""
        await self.notify(f"Evaluating embedding model: {model_name}")

        prompt = f"""
Evaluate embedding model: {model_name}

{f"Test corpus: {test_corpus}" if test_corpus else ""}

**Analyze:**
1. Latency per text (ms)
2. Embedding dimension
3. Memory requirements
4. MTEB benchmark scores (if available)
5. Domain-specific performance
6. Hardware compatibility (ARM64, GPU)

**Benchmark code:**
```python
from sentence_transformers import SentenceTransformer
import time

model = SentenceTransformer('{model_name}')
texts = [...]  # Test corpus

start = time.time()
embeddings = model.encode(texts)
latency = (time.time() - start) / len(texts)

print(f"Latency: {{latency*1000:.2f}}ms per text")
print(f"Dimension: {{embeddings.shape[1]}}")
```

**Provide:**
- Recommendation: Use / Do Not Use
- Trade-offs vs current model
- Migration complexity if switching
"""

        return await self.run_task(prompt)

    async def design_rag_architecture(self, requirements: str) -> TaskResult:
        """Design a RAG architecture"""
        await self.notify(f"Designing RAG architecture")

        prompt = f"""
Design RAG architecture for:

{requirements}

**Include:**

## 1. Chunking Strategy
- Method (semantic, fixed, sliding window)
- Chunk size and overlap
- Justification

## 2. Embedding Pipeline
- Model recommendation
- Batch processing strategy
- Dimension and storage

## 3. Retrieval Strategy
- Dense vs sparse vs hybrid
- Top-k selection
- Reranking approach

## 4. Context Management
- Window optimization
- Relevance filtering
- Token budget

## 5. Quality Metrics
- Retrieval accuracy measurement
- Answer quality evaluation
- Latency targets

## 6. Implementation Plan
- Migration steps if replacing existing
- Rollback strategy
"""

        return await self.run_task(prompt)

    async def benchmark_llm(
        self,
        model_name: str,
        test_prompts: List[str] = None
    ) -> TaskResult:
        """Benchmark an LLM"""
        await self.notify(f"Benchmarking LLM: {model_name}")

        prompt = f"""
Benchmark LLM: {model_name}

**Test prompts:**
{test_prompts if test_prompts else "Use standard benchmark prompts"}

**Measure:**
1. Time to first token (TTFT)
2. Tokens per second throughput
3. Memory usage (VRAM)
4. Quality metrics:
   - Coherence
   - Factual accuracy
   - Instruction following
5. Context window handling

**Compare against:**
- Current production model
- Industry benchmarks

**Provide:**
- Recommendation with trade-offs
- Hardware requirements
- Cost analysis
"""

        return await self.run_task(prompt)

    async def optimize_vector_search(self, collection_info: str) -> TaskResult:
        """Optimize vector database search"""
        prompt = f"""
Optimize vector search for:

{collection_info}

**Analyze:**
1. Current index configuration
2. Query patterns
3. Latency distribution

**Recommend:**
1. Index type (HNSW, IVF, etc.)
2. Parameters (ef_construct, m, etc.)
3. Sharding strategy if needed
4. Caching opportunities
5. Hardware optimization

**Expected improvements:**
- Latency reduction
- Throughput increase
- Memory optimization
"""

        return await self.run_task(prompt)

    async def research_ai_capability(self, topic: str) -> TaskResult:
        """Research a new AI capability"""
        await self.notify(f"Researching: {topic}")

        prompt = f"""
Research AI capability: {topic}

**Investigate:**
1. Current state of the art
2. Available implementations (open source, APIs)
3. Resource requirements
4. Integration complexity

**Provide:**
## Summary
Brief overview (2-3 sentences)

## Options Analysis
| Option | Pros | Cons | Effort |
|--------|------|------|--------|
| ... | ... | ... | ... |

## Recommendation
Top choice with rationale

## Implementation Path
Step-by-step approach

## Risks
Potential issues and mitigations
"""

        return await self.run_task(prompt)

    # ── New Methods ──────────────────────────────────────────────────

    async def design_prompt_system(
        self,
        use_case: str,
        model: str = "gpt-4"
    ) -> TaskResult:
        """Design system prompts, few-shot examples, and chain-of-thought patterns"""
        await self.notify(f"Designing prompt system for: {use_case} (model: {model})")

        prompt = f"""
Design a comprehensive prompt system for the following use case:

**Use Case:** {use_case}
**Target Model:** {model}

## 1. System Prompt Design
- Role definition and persona
- Behavioral constraints and guardrails
- Output format specification
- Error handling instructions
- Token budget considerations for {model}

## 2. Few-Shot Examples
- Design 3-5 representative examples covering:
  - Happy path (standard input/output)
  - Edge cases (ambiguous input, missing data)
  - Boundary conditions (very long input, multi-part queries)
- Example selection strategy (static vs dynamic retrieval-based)

## 3. Chain-of-Thought Patterns
- Step-by-step reasoning template
- When to use CoT vs direct answer (latency/cost tradeoff)
- Self-consistency sampling strategy if applicable
- Decomposition approach for complex queries

## 4. Tool Use Integration
- Function/tool schemas if applicable
- Tool selection prompting strategy
- ReAct pattern implementation
- Structured output format (JSON mode considerations)

## 5. Evaluation Plan
- Test cases for prompt quality assessment
- A/B testing methodology
- Regression detection strategy
- Metrics: accuracy, format compliance, latency, cost-per-call

## 6. Optimization Notes
- Token optimization opportunities (shorter prompts, caching)
- Model-specific adaptations ({model} strengths and limitations)
- Fallback strategy if primary model unavailable

**Provide the complete prompt system ready for implementation.**
"""

        return await self.run_task(prompt)

    async def evaluate_fine_tuning(
        self,
        base_model: str,
        dataset_description: str,
        goals: str
    ) -> TaskResult:
        """Evaluate if fine-tuning is needed, recommend approach, dataset requirements, and evaluation strategy"""
        await self.notify(f"Evaluating fine-tuning for: {base_model}")

        prompt = f"""
Evaluate fine-tuning feasibility and approach:

**Base Model:** {base_model}
**Dataset Description:** {dataset_description}
**Goals:** {goals}

## 1. Fine-Tuning vs Prompt Engineering Decision
- Can this be solved with better prompting? (few-shot, CoT, RAG)
- Quantify the gap between current prompt-based performance and target
- Cost comparison: fine-tuning investment vs prompt engineering iteration
- Decision matrix with clear recommendation

## 2. Recommended Approach
| Method | VRAM Required | Training Time | Quality Impact | Cost |
|--------|--------------|---------------|----------------|------|
| Full Fine-Tune | ... | ... | ... | ... |
| LoRA (r=16) | ... | ... | ... | ... |
| QLoRA (4-bit) | ... | ... | ... | ... |
| Prefix Tuning | ... | ... | ... | ... |

- **Recommended method** with justification
- Hyperparameter starting points (learning rate, epochs, rank)
- Hardware requirements (GPU type, count, training time estimate)

## 3. Dataset Requirements
- Minimum dataset size for this task
- Data quality checklist:
  - Deduplication strategy
  - Quality filtering criteria
  - Label consistency verification
  - Train/validation/test split ratios
- Synthetic data generation opportunities
- Data augmentation strategies

## 4. Evaluation Strategy
- Benchmark metrics specific to {goals}
- Baseline measurement approach
- Automated evaluation pipeline (lm-eval-harness, custom benchmarks)
- Human evaluation protocol if needed
- Regression testing against base model capabilities
- Hallucination rate measurement pre/post fine-tuning

## 5. Production Deployment
- Model serving considerations (vLLM, TGI, Ollama)
- A/B testing rollout plan
- Rollback criteria and strategy
- Ongoing monitoring and retraining triggers

## 6. Cost Analysis
- Training cost estimate (GPU hours x rate)
- Inference cost comparison (base vs fine-tuned)
- Total cost of ownership over 6 months
"""

        return await self.run_task(prompt)

    async def design_agent_architecture(self, requirements: str) -> TaskResult:
        """Design multi-agent or single-agent architecture with tool use, MCP integration, orchestration"""
        await self.notify("Designing agent architecture")

        prompt = f"""
Design an agent architecture for the following requirements:

{requirements}

## 1. Architecture Pattern Selection
- Single agent vs multi-agent decision with rationale
- Orchestration pattern: Sequential / Parallel / Hierarchical / DAG
- Communication protocol: Direct call / Message queue / A2A protocol / MCP
- Architecture diagram (text-based)

## 2. Agent Design
For each agent in the system:
- **Name & Role** — Clear responsibility boundary
- **Model Selection** — Which LLM and why (cost/quality tradeoff)
- **System Prompt** — Key behavioral instructions
- **Tools Available** — Function schemas with input/output types
- **Memory Strategy** — Context window management, long-term storage

## 3. MCP Server Integration
- Resource definitions (what data each agent can access)
- Tool registrations (what actions each agent can perform)
- Server implementation approach (stdio vs HTTP)
- Authentication and authorization model
- Error handling and retry strategies

## 4. Tool Use Design
- Function calling schemas for each tool
- Input validation and sanitization
- Output parsing and error handling
- Fallback chains when tools fail
- Rate limiting and cost controls

## 5. Orchestration & Flow
- Task decomposition strategy
- Agent routing and delegation logic
- Result aggregation and conflict resolution
- Parallel execution opportunities
- Timeout and circuit breaker patterns

## 6. Memory & State Management
- Short-term: Context window strategy (summarization, sliding window)
- Long-term: Vector store for episodic memory
- Shared state: How agents share context and results
- Session management for multi-turn interactions

## 7. Error Handling & Resilience
- Retry strategies with exponential backoff
- Fallback models (primary -> secondary -> local)
- Graceful degradation when components fail
- Logging and observability (traces, metrics)
- Dead letter queue for failed tasks

## 8. Cost & Performance Estimates
- Token usage per interaction (estimated)
- Latency budget per step
- Monthly cost projection at expected scale
- Optimization opportunities (caching, batching, model routing)
"""

        return await self.run_task(prompt)

    async def analyze_ai_costs(
        self,
        models: List[str],
        usage_patterns: str
    ) -> TaskResult:
        """Token cost analysis, model comparison, and optimization recommendations"""
        await self.notify(f"Analyzing AI costs for: {', '.join(models)}")

        models_str = ", ".join(models)
        prompt = f"""
Analyze AI costs and optimize spending:

**Models to Analyze:** {models_str}
**Usage Patterns:** {usage_patterns}

## 1. Token Cost Comparison
| Model | Input $/1M tokens | Output $/1M tokens | Context Window | Batch Discount |
|-------|-------------------|---------------------|----------------|----------------|
{chr(10).join(f"| {m} | ... | ... | ... | ... |" for m in models)}

## 2. Usage Analysis
- Estimated tokens per request (input + output)
- Daily/monthly request volume projection
- Peak vs average usage patterns
- Context caching opportunities (prompt caching savings)

## 3. Monthly Cost Projection
| Model | Daily Cost | Monthly Cost | Annual Cost | Cost/Query |
|-------|-----------|-------------|-------------|------------|
{chr(10).join(f"| {m} | ... | ... | ... | ... |" for m in models)}

## 4. Optimization Strategies
- **Model Routing** — Use cheaper models for simple tasks, expensive for complex
- **Prompt Optimization** — Reduce input tokens without quality loss
- **Caching** — Semantic cache hit rate estimates, prompt prefix caching
- **Batching** — Batch API usage for non-real-time workloads (50% discount)
- **Context Management** — Summarization vs full context, sliding window strategies
- **Fine-Tuning** — When a fine-tuned smaller model beats a larger general model on cost

## 5. Quality-Cost Tradeoff Matrix
| Scenario | Best Model | Cost/Query | Quality Score | Recommendation |
|----------|-----------|------------|---------------|----------------|
| Simple classification | ... | ... | ... | ... |
| Complex reasoning | ... | ... | ... | ... |
| Code generation | ... | ... | ... | ... |
| Summarization | ... | ... | ... | ... |

## 6. Infrastructure Cost Considerations
- Self-hosted vs API cost crossover point
- GPU rental vs purchase analysis (if applicable)
- Embedding generation costs (batch vs real-time)
- Vector database hosting costs at scale

## 7. Recommendations
- Immediate savings opportunities (ranked by impact)
- Medium-term optimization roadmap
- Cost monitoring and alerting thresholds
- Budget allocation recommendation
"""

        return await self.run_task(prompt)

    async def evaluate_ai_safety(
        self,
        model_or_system: str,
        evaluation_type: str = "comprehensive"
    ) -> TaskResult:
        """Red-team evaluation, bias detection, hallucination measurement, guardrail design"""
        await self.notify(f"Evaluating AI safety: {model_or_system} ({evaluation_type})")

        prompt = f"""
Evaluate AI safety for: {model_or_system}
Evaluation Type: {evaluation_type}

## 1. Red-Team Evaluation
- **Prompt Injection** — Test for direct and indirect injection vulnerabilities
- **Jailbreak Resistance** — Test common jailbreak patterns (DAN, roleplay, encoding tricks)
- **Information Extraction** — Test for system prompt leakage, training data extraction
- **Harmful Content** — Test refusal behaviors for dangerous, illegal, or unethical requests
- Severity classification for each finding (Critical / High / Medium / Low)

## 2. Bias Detection
- **Demographic Bias** — Test outputs across gender, race, age, nationality dimensions
- **Stereotype Reinforcement** — Check for harmful stereotypes in generated content
- **Representation Analysis** — Evaluate diversity in generated examples and recommendations
- **Fairness Metrics** — Equal opportunity, demographic parity, calibration across groups
- Bias measurement methodology and scoring

## 3. Hallucination Measurement
- **Factual Accuracy** — Test with verifiable claims, measure confabulation rate
- **Groundedness** — When given context, measure faithfulness to source material
- **Citation Accuracy** — Test if referenced sources exist and contain claimed information
- **Confidence Calibration** — Does the model express uncertainty appropriately?
- Hallucination rate: percentage across N test cases
- Domain-specific hallucination patterns

## 4. Guardrail Design
- **Input Guardrails:**
  - Topic boundary enforcement
  - PII detection and redaction (names, emails, SSNs, etc.)
  - Prompt injection detection layer
  - Input length and rate limiting
- **Output Guardrails:**
  - Content classification (Llama Guard, OpenAI moderation, custom)
  - Factuality verification layer
  - Format compliance validation
  - Sensitive information filtering
- **Implementation:**
  - Recommended guardrail framework (NeMo Guardrails, Guardrails AI, custom)
  - Latency impact of each guardrail layer
  - False positive rate targets

## 5. Compliance & Documentation
- Data handling and privacy considerations
- Model card documentation requirements
- Audit trail and logging recommendations
- Incident response plan for safety failures

## 6. Remediation Recommendations
- Priority-ranked list of issues found
- Remediation approach for each issue
- Timeline and effort estimates
- Re-evaluation schedule
"""

        return await self.run_task(prompt)

    async def design_multimodal_pipeline(
        self,
        modalities: List[str],
        requirements: str
    ) -> TaskResult:
        """Vision + text + audio pipeline design with model selection"""
        await self.notify(f"Designing multi-modal pipeline: {', '.join(modalities)}")

        modalities_str = ", ".join(modalities)
        prompt = f"""
Design a multi-modal AI pipeline:

**Modalities:** {modalities_str}
**Requirements:** {requirements}

## 1. Pipeline Architecture
- End-to-end flow diagram (text-based)
- Input preprocessing for each modality
- Model selection for each stage
- Output fusion strategy
- Latency budget allocation per stage

## 2. Model Selection per Modality

### Vision (if applicable)
| Model | Task | Latency | VRAM | Quality | Cost |
|-------|------|---------|------|---------|------|
| GPT-4V/4o | General vision | ... | API | ... | ... |
| LLaVA-1.6 | Open-source vision | ... | ... | ... | Free |
| Florence-2 | Detection/OCR | ... | ... | ... | Free |
| CLIP | Embedding/search | ... | ... | ... | Free |

### Audio (if applicable)
| Model | Task | Latency | RAM | Quality | Cost |
|-------|------|---------|-----|---------|------|
| Whisper large-v3 | Transcription | ... | ... | ... | Free |
| Whisper turbo | Fast transcription | ... | ... | ... | Free |
| Deepgram Nova-2 | Real-time ASR | ... | API | ... | ... |
| Speaker diarization | Who spoke when | ... | ... | ... | ... |

### Text
| Model | Task | Latency | Context | Quality | Cost |
|-------|------|---------|---------|---------|------|
| ... | ... | ... | ... | ... | ... |

## 3. Cross-Modal Integration
- How modalities interact (early fusion, late fusion, cross-attention)
- Unified embedding space strategy (CLIP, ImageBind)
- Multi-modal RAG implementation:
  - Image + text chunk storage
  - Cross-modal retrieval strategy
  - Context assembly from mixed modalities

## 4. Preprocessing Pipelines
- Image: resize, normalize, format conversion, OCR extraction
- Audio: sample rate, noise reduction, VAD, chunking for long audio
- Text: tokenization, entity extraction, metadata enrichment
- Video: frame extraction, scene detection, keyframe selection

## 5. Performance Optimization
- Batch processing strategies per modality
- Caching opportunities (embedding cache, transcription cache)
- GPU memory management across models
- Async processing for independent modality paths
- Streaming support for real-time applications

## 6. Quality Assurance
- Per-modality quality metrics
- End-to-end evaluation methodology
- Error handling for degraded input (blurry image, noisy audio)
- Fallback strategies per modality
- Human-in-the-loop verification points

## 7. Deployment Architecture
- Containerization strategy (one container per model vs shared)
- GPU allocation and sharing
- Scaling considerations per modality
- Cost estimate at target throughput
"""

        return await self.run_task(prompt)

    async def optimize_inference(
        self,
        model: str,
        target_platform: str = "server"
    ) -> TaskResult:
        """Quantization, batching, caching strategies for inference optimization"""
        await self.notify(f"Optimizing inference: {model} for {target_platform}")

        prompt = f"""
Optimize inference for:

**Model:** {model}
**Target Platform:** {target_platform}

## 1. Quantization Strategy
| Method | Bits | Quality Loss | Speed Gain | VRAM Reduction | Best For |
|--------|------|-------------|------------|----------------|----------|
| GPTQ | 4-bit | ... | ... | ... | GPU inference |
| AWQ | 4-bit | ... | ... | ... | GPU inference |
| GGUF | Q4_K_M | ... | ... | ... | CPU/hybrid |
| GGUF | Q5_K_M | ... | ... | ... | CPU/hybrid |
| INT8 | 8-bit | ... | ... | ... | Balanced |
| FP16 | 16-bit | Baseline | Baseline | Baseline | Reference |

- Recommended quantization for {target_platform}
- Calibration dataset requirements
- Quality benchmarks pre/post quantization

## 2. Serving Framework Selection
| Framework | Throughput | Latency | Features | Complexity |
|-----------|-----------|---------|----------|------------|
| vLLM | ... | ... | PagedAttention, continuous batching | ... |
| TGI | ... | ... | Streaming, multi-LoRA | ... |
| llama.cpp | ... | ... | CPU/GPU hybrid, GGUF | ... |
| Ollama | ... | ... | Easy setup, model management | ... |
| TensorRT-LLM | ... | ... | NVIDIA optimized | ... |
| Core ML | ... | ... | Apple Silicon, Neural Engine | ... |
| ONNX Runtime | ... | ... | Cross-platform | ... |

- **Recommended framework** for {target_platform} with justification

## 3. Batching & Scheduling
- Continuous batching configuration
- Dynamic batch size optimization
- Request scheduling strategy (FCFS, priority-based)
- Prefill vs decode phase optimization
- Speculative decoding applicability

## 4. Caching Strategies
- **KV-Cache Optimization** — Memory management, eviction policies
- **Prompt Caching** — System prompt prefix caching, cache hit rate estimates
- **Semantic Caching** — Similar query detection, cache invalidation strategy
- **Response Caching** — Exact match caching for repeated queries

## 5. Platform-Specific Optimization for {target_platform}
- Hardware utilization recommendations
- Memory management (VRAM allocation, offloading strategies)
- Concurrency configuration
- Thermal and power considerations (if on-device)
- Network optimization (if API-based)

## 6. Monitoring & Benchmarks
- Key metrics to track: TTFT, TPS, p50/p95/p99 latency, throughput
- Load testing methodology
- Regression detection thresholds
- Alerting configuration

## 7. Implementation Plan
- Step-by-step optimization path (ordered by impact/effort ratio)
- Expected improvement per step (quantified)
- Rollback plan for each optimization
- Timeline estimate
"""

        return await self.run_task(prompt)

    async def work(self, task: str) -> TaskResult:
        """General AI research work"""
        await self.notify(f"Starting: {task[:50]}...")
        return await self.run_task(task)


async def main():
    """CLI entry point"""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Victoria - AI Research Agent")
    parser.add_argument("--embedding", type=str, help="Evaluate embedding model")
    parser.add_argument("--rag", type=str, help="Design RAG architecture")
    parser.add_argument("--benchmark", type=str, help="Benchmark LLM")
    parser.add_argument("--optimize", type=str, help="Optimize vector search")
    parser.add_argument("--research", type=str, help="Research AI capability")
    parser.add_argument("--prompt-system", type=str, help="Design prompt system for a use case")
    parser.add_argument("--prompt-model", type=str, default="gpt-4", help="Target model for prompt system (default: gpt-4)")
    parser.add_argument("--fine-tune", type=str, help="Evaluate fine-tuning for a base model")
    parser.add_argument("--ft-dataset", type=str, default="", help="Dataset description for fine-tuning evaluation")
    parser.add_argument("--ft-goals", type=str, default="", help="Goals for fine-tuning evaluation")
    parser.add_argument("--agent-arch", type=str, help="Design agent architecture for requirements")
    parser.add_argument("--costs", type=str, nargs="+", help="Analyze AI costs for models (space-separated)")
    parser.add_argument("--cost-usage", type=str, default="", help="Usage patterns for cost analysis")
    parser.add_argument("--safety", type=str, help="Evaluate AI safety for model or system")
    parser.add_argument("--safety-type", type=str, default="comprehensive", help="Safety evaluation type (default: comprehensive)")
    parser.add_argument("--multimodal", type=str, nargs="+", help="Design multi-modal pipeline for modalities (space-separated)")
    parser.add_argument("--mm-requirements", type=str, default="", help="Requirements for multi-modal pipeline")
    parser.add_argument("--inference", type=str, help="Optimize inference for a model")
    parser.add_argument("--platform", type=str, default="server", help="Target platform for inference optimization (default: server)")
    parser.add_argument("--task", type=str, help="Run general task")
    parser.add_argument("--status", action="store_true", help="Show status")

    args = parser.parse_args()

    agent = VictoriaAgent()

    if args.status:
        print(json.dumps(agent.get_status(), indent=2))
        return

    if args.embedding:
        result = await agent.evaluate_embedding_model(args.embedding)
        print(result.output)
        return

    if args.rag:
        result = await agent.design_rag_architecture(args.rag)
        print(result.output)
        return

    if args.benchmark:
        result = await agent.benchmark_llm(args.benchmark)
        print(result.output)
        return

    if args.optimize:
        result = await agent.optimize_vector_search(args.optimize)
        print(result.output)
        return

    if args.research:
        result = await agent.research_ai_capability(args.research)
        print(result.output)
        return

    if args.prompt_system:
        result = await agent.design_prompt_system(args.prompt_system, args.prompt_model)
        print(result.output)
        return

    if args.fine_tune:
        result = await agent.evaluate_fine_tuning(args.fine_tune, args.ft_dataset, args.ft_goals)
        print(result.output)
        return

    if args.agent_arch:
        result = await agent.design_agent_architecture(args.agent_arch)
        print(result.output)
        return

    if args.costs:
        result = await agent.analyze_ai_costs(args.costs, args.cost_usage)
        print(result.output)
        return

    if args.safety:
        result = await agent.evaluate_ai_safety(args.safety, args.safety_type)
        print(result.output)
        return

    if args.multimodal:
        result = await agent.design_multimodal_pipeline(args.multimodal, args.mm_requirements)
        print(result.output)
        return

    if args.inference:
        result = await agent.optimize_inference(args.inference, args.platform)
        print(result.output)
        return

    if args.task:
        result = await agent.work(args.task)
        print(result.output)
        return

    print("Victoria - AI Research Specialist")
    print("==================================")
    print("Use --help for options")
    print()
    print("Capabilities:")
    print("  --embedding MODEL       Evaluate embedding model")
    print("  --rag REQUIREMENTS      Design RAG architecture")
    print("  --benchmark MODEL       Benchmark LLM")
    print("  --optimize COLLECTION   Optimize vector search")
    print("  --research TOPIC        Research AI capability")
    print("  --prompt-system USECASE Design prompt system (--prompt-model MODEL)")
    print("  --fine-tune MODEL       Evaluate fine-tuning (--ft-dataset, --ft-goals)")
    print("  --agent-arch REQS       Design agent architecture")
    print("  --costs MODEL [MODEL..] Analyze AI costs (--cost-usage PATTERNS)")
    print("  --safety SYSTEM         Evaluate AI safety (--safety-type TYPE)")
    print("  --multimodal MOD [MOD.] Design multi-modal pipeline (--mm-requirements)")
    print("  --inference MODEL       Optimize inference (--platform PLATFORM)")
    print("  --task TASK             Run general task")
    print("  --status                Show agent status")


if __name__ == "__main__":
    asyncio.run(main())

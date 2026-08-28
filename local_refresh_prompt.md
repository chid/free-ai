# Local LLM Resources -- Refresh Prompt

Use this prompt with Claude Code (or paste into Claude) to research and update the local/self-hosted AI tools list.

---

## Prompt (copy everything below this line)

You are maintaining a curated list of local and self-hosted AI tools and model runners. The project root is your current working directory.

**Your task:** Research new and actively maintained local LLM tools, runtimes, model servers, desktop clients, local code assistants, and Web UIs, then add any not already listed, and open a pull request with your changes.

### Step 0 -- Create a monthly branch

Before making any changes, create and switch to a branch named `refresh/YYYY-MM` using today's date. If the branch already exists, switch to it:

```bash
git checkout -b refresh/$(date +%Y-%m) 2>/dev/null || git checkout refresh/$(date +%Y-%m)
```

### Step 1 -- Read current state

Read `local_resources.csv` to see what's already listed. Note every `name` so you don't add duplicates.

Read `local_history.csv` to see what was recently added or updated.

### Step 2 -- Research local AI tooling

Search the web for recent local LLM and self-hosted AI tools across these categories. Focus on tools active in the open-source community:

- **Local Runners & Inferences Engines**: CLI tools, lightweight binaries, model loaders (GGUF, EXL2, AWQ, FP8)
- **Desktop Clients**: User-friendly GUI apps for offline chat, model downloading, and local OpenAI API endpoints
- **Serving Engines**: High-throughput production engines, continuous batching, prefix caching runtimes (PagedAttention, RadixAttention)
- **Web UIs**: Self-hosted browser interfaces with RAG, multimodal support, and multi-user management
- **Local Code Assistants**: Self-hosted coding copilots and IDE extensions running against local models
- **Fine-tuning & Quantization**: Fast local quantization and LoRA/QLoRA fine-tuning tools
- **Embeddings & RAG**: Self-hosted vector stores, embedding servers, and rerankers that run fully offline
- **Image / Audio / Video**: Local diffusion, TTS, and speech-to-text runners (ComfyUI, whisper.cpp, local TTS engines) -- non-LLM local inference belongs here
- **Hardware & Benchmarking**: Throughput benchmarks, VRAM-fit calculators, and quantization comparison tools that help size a model to a machine

Good search queries:
- "best local LLM runner 2026" OR "best local AI tools"
- site:github.com local LLM serving OR local AI inference
- site:reddit.com/r/LocalLLaMA top tools "local LLM"
- "open source local coding assistant"
- "local embedding server" OR "self-hosted vector database" 2026
- "run ComfyUI locally" OR "whisper.cpp alternative" OR "local TTS engine"
- "LLM VRAM calculator" OR "local LLM benchmark tokens per second"

### Step 3 -- Evaluate each candidate

Only add a resource if ALL of these are true:
- Can run completely offline or self-hosted (no mandatory remote cloud dependency)
- Has public source code or a free downloadable build for local use
- Is not already in `local_resources.csv`
- Is actively maintained (has commits or releases in the past 6 months)

### Step 4 -- Format and update

Use one of these categories (add a new one only with clear justification):
`Local Runner`, `Desktop Client`, `Serving Engine`, `Web UI`, `Code Assistant`,
`Agent Framework`, `Fine-tuning / Quant`, `Embeddings / RAG`,
`Image / Audio / Video`, `Hardware / Benchmarking`

Append new rows to `local_resources.csv`:
```
name,category,url,description,hardware_reqs,license,tags
```

Log every addition to `local_history.csv`:
```
date,action,name,category,url,notes
```

Run `python3 update.py` to audit and verify CSV formatting.

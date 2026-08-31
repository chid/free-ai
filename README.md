# Awesome Free AI

> A snapshot of genuinely free (or free-tier) AI tools, APIs, and platforms **as they existed in August 2026**.

Free tiers change fast — tools get paywalled, rebranded, or shut down. This list captures what was on offer at the time of each update, with every change tracked in [`history.csv`](history.csv) and summarised in [`CHANGELOG.md`](CHANGELOG.md). Think of it less as a permanent directory and more as a dated edition: accurate when written, audited on refresh.

**71 resources** across 16 categories. Browse the [web view](index.html) for a filterable, searchable UI, or read on. Dedicated local & self-hosted runners and models live in [`local_resources.csv`](local_resources.csv) (37 tools), tools with no genuine free tier live in [`paid_resources.csv`](paid_resources.csv) (6 of them), and [`QUOTAS.md`](QUOTAS.md) tracks how paid AI plans meter usage — increasingly the thing that separates a real free tier from a nominal one.


---

## Contents

- [LLM Chatbots](#llm-chatbots)
- [LLM APIs](#llm-apis)
- [Routers & Clients](#routers--clients)
- [Code Assistants](#code-assistants)
- [Code & UI Builders](#code--ui-builders)
- [Image Generation](#image-generation)
- [Video Generation](#video-generation)
- [Audio & Voice](#audio--voice)
- [Music Generation](#music-generation)
- [Local & Self-hosted](#local--self-hosted)
- [Search & Research](#search--research)
- [Productivity](#productivity)
- [Frameworks](#frameworks)
- [Contributing](#contributing)

---

## LLM Chatbots

Full-featured AI chat interfaces with free tiers.

- **[Claude (Anthropic)](https://claude.ai)** — Anthropic's AI assistant — strong reasoning and long context. *Free tier with usage limits.*
- **[ChatGPT](https://chat.openai.com)** — OpenAI's flagship assistant. *Free tier (GPT-4o limited).*
- **[Gemini](https://gemini.google.com)** — Google's multimodal AI assistant. *Free tier available.*
- **[Muse Spark](https://meta.ai)** — Meta's first model from Meta Superintelligence Labs — natively multimodal (text/image/audio) with tool use and visual chain-of-thought; available via meta.ai. *Free; requires Meta account (Facebook or Instagram login).*
- **[Le Chat](https://chat.mistral.ai)** — Mistral's AI assistant with web search and image generation built in. *Free tier with daily limits; no credit card required.*
- **[DeepSeek](https://chat.deepseek.com)** — Free chatbot featuring strong reasoning and coding from DeepSeek's open-weight models. *Free with usage limits.*

## LLM APIs

Programmatic access to large language models with free quotas.

- **[Google AI Studio](https://aistudio.google.com)** — Gemini API with a generous free quota — current Flash models (3.6 Flash, 2.5 Flash-Lite) are free; the Gemini 2.5 Pro/Flash endpoints retired June 17 2026. *Free API key with rate limits; no credit card.*
- **[Groq](https://console.groq.com)** — Blazing-fast inference for open models (Llama etc.). *Free tier: ~30 requests/min on open models.*
- **[Together AI](https://api.together.xyz)** — Serverless inference for 100+ open-source models. *$5 free credit on signup.*
- **[Mistral AI (La Plateforme)](https://console.mistral.ai)** — Access to Mistral models via API. *Free tier available.*
- **[Cohere](https://dashboard.cohere.com)** — NLP-focused models for generation and embeddings. *Free trial key: 1000 calls/month, non-commercial use only.*
- **[Hugging Face Inference API](https://huggingface.co/inference-api)** — Free serverless inference for thousands of public models. *Free with rate limits.*
- **[OpenRouter](https://openrouter.ai)** — Unified API routing to many models; community-funded :free tier gives rate-limited access to many models. *Free tier: 14 models at ~50 requests/day (up to 1M context).*
- **[Cerebras](https://cloud.cerebras.ai)** — Ultra-fast inference API for open models (Llama 4 and Qwen) via custom silicon. *Free tier: 1M tokens/day with no credit card.*
- **[Chutes.ai](https://chutes.ai)** — Decentralised serverless inference on the Bittensor network — frequently hosts free or near-free DeepSeek and other open-model endpoints. *Free tier available; pricing fluctuates with network conditions.*
- **[Puter.js](https://developer.puter.com)** — Browser-native JS library giving free access to DeepSeek V4 Flash/Pro and other models with no API key or server setup. *Completely free for developers; user-pays model covers costs.*
- **[Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai)** — Serverless GPU inference for open-weight models running on Cloudflare's edge network. *Free: 10,000 Neurons/day, resetting at 00:00 UTC.*
- **[SambaNova Cloud](https://cloud.sambanova.ai)** — High-throughput inference for open-weight models on SambaNova RDU hardware. *Free tier: 200,000 tokens/day per model.*
- **[NVIDIA NIM](https://build.nvidia.com)** — OpenAI-compatible endpoints for 120+ open-weight models hosted by NVIDIA. *Free: 1000 API credits at ~40 requests/min, no credit card.*

## Routers & Clients

Put many providers behind one interface, with fallback and budget control.

- **[LiteLLM](https://litellm.ai)** — Unified OpenAI-compatible proxy that routes to 100+ LLM providers with automatic retries and rate-limit fallback. *Completely free; open-source.*
- **[aisuite](https://github.com/andrewyng/aisuite)** — Lightweight unified Python interface to multiple LLM providers from Andrew Ng's team. *Completely free; open-source.*
- **[Vercel AI Gateway](https://vercel.com/docs/ai-gateway)** — Single endpoint routing to 200+ models from 40+ providers with budgets, monitoring and fallbacks. *Free: $5 of gateway credit per month, refreshing every 30 days.*

## Code Assistants

AI tools that live in your editor or terminal.

- **[GitHub Copilot](https://github.com/features/copilot)** — AI code completion in your editor; completions stay free and unmetered, while chat, agent mode and CLI draw on AI Credits from June 2026. *Free for all users (2000 completions + 50 chats/month).*
- **[Windsurf (formerly Codeium)](https://windsurf.com)** — AI-native code editor with the agentic Cascade feature (Codeium rebranded); credit system retired March 2026 in favour of daily/weekly quotas. *Free tier: unlimited Tab autocomplete and inline edits + ~25 Cascade Flow Actions/month.*
- **[Cursor](https://cursor.sh)** — AI-first code editor built on VS Code; free plan is now branded Hobby. *Free Hobby plan: limited Agent requests and Tab completions, no credit card.*
- **[Continue](https://continue.dev)** — Open-source AI code assistant for VS Code / JetBrains. *Completely free.*
- **[Aider](https://aider.chat)** — AI pair programming in your terminal. *Completely free (bring your own key).*
- **[Antigravity](https://antigravity.google)** — Google's AI-native IDE and `agy` CLI that coordinate Manager/Writer/Critic/Tester agents; the official replacement for Gemini CLI. *Free with a personal Google account (generous Gemini quota).*
- **[Amazon Q Developer](https://aws.amazon.com/q/developer)** — AWS's AI coding assistant with IDE inline suggestions and agentic coding in VS Code and JetBrains. *Free tier: unlimited completions + 50 agentic tasks/month.*
- **[Freebuff](https://freebuff.com)** — AI coding agent that runs in your terminal — ad-supported so it costs nothing; built on Codebuff with specialised sub-agents for file picking, code review, and browser use. *Completely free (ad-supported in CLI).*
- **[OpenCode](https://opencode.ai)** — Open-source terminal coding agent from the SST team with a TUI interface and support for 75+ LLMs including local models via Ollama; the optional OpenCode Go plan adds 18 hosted open models for $10/mo. *Completely free; bring your own key or use free providers.*
- **[Cline](https://cline.bot)** — MIT-licensed autonomous coding agent for VS Code; the project most other VS Code agents were forked from. *Completely free; open-source (bring your own key).*
- **[Kilo Code](https://kilo.ai)** — Open-source coding agent for VS Code, JetBrains, CLI and Slack with access to 500+ models at zero inference markup. *Completely free; open-source (bring your own key at list price).*
- **[Zed](https://zed.dev)** — High-performance open-source editor written in Rust with native AI, MCP support and multiplayer editing. *Free Personal plan: 2000 edit predictions/month.*

## Code & UI Builders

Generate full UIs and apps from a prompt in the browser.

- **[v0 by Vercel](https://v0.dev)** — Generate React/UI components from prompts. *Free tier available.*
- **[Bolt.new](https://bolt.new)** — Full-stack AI app builder in the browser. *Free tier available.*
- **[Lovable](https://lovable.dev)** — AI full-stack app builder that generates React/TypeScript with a Supabase backend and deploys instantly. *Free tier: 5 credits/day (30/month); no credit card required.*

## Image Generation

Text-to-image tools that are free or have a meaningful free tier.

- **[Stable Diffusion (via DiffusionBee)](https://diffusionbee.com)** — Run Stable Diffusion locally on Mac. *Completely free.*
- **[Adobe Firefly](https://firefly.adobe.com)** — Adobe's generative image tools. *Free credits monthly.*
- **[Microsoft Designer](https://designer.microsoft.com)** — AI image generation via DALL-E. *Free tier available.*
- **[Ideogram](https://ideogram.ai)** — Text-to-image with strong typography. *Free tier available.*
- **[Playground AI](https://playground.com)** — Image generation and editing. *Free tier available.*
- **[Canva AI](https://canva.com)** — AI image generation and design tools. *Free tier with AI features.*

## Video Generation

AI tools for generating or editing video.

- **[Runway](https://runwayml.com)** — AI video generation and editing tools. *Free tier (limited credits).*
- **[CapCut](https://capcut.com)** — AI video editing with auto-captions and effects. *Free tier available.*
- **[Descript](https://descript.com)** — AI video/audio editing with transcription. *Free tier available.*
- **[Kling AI](https://kling.ai)** — High-quality text-to-video and image-to-video generation from Kuaishou. *Free tier: 66 credits/day (watermarked outputs).*
- **[Pika](https://pika.art)** — AI video generation and image-animation with text-to-video controls. *Free plan with monthly credits.*
- **[Dreamina (Seedance 2.0)](https://dreamina.capcut.com)** — ByteDance's text- and image-to-video generator running the Seedance 2.0 model with native audio. *Free daily credits (~2-3 videos/day) at up to 1080p, watermark-free.*

## Audio & Voice

Text-to-speech, voice cloning, and speech recognition.

- **[ElevenLabs](https://elevenlabs.io)** — High-quality AI text-to-speech and voice cloning. *Free tier (10k chars/month).*
- **[Whisper (OpenAI)](https://github.com/openai/whisper)** — State-of-the-art open-source speech recognition. *Completely free.*

## Music Generation

Generate original music from text prompts.

- **[Suno](https://suno.com)** — AI music generation from text prompts; free-tier tracks stream and share on Suno but can no longer be downloaded. *Free: 50 credits/day (~10 songs); no downloads, no commercial use.*
- **[Udio](https://udio.com)** — AI music generation and remixing. *Free: 10 songs/month.*

## Local & Self-hosted

Run models on your own hardware — no API keys, no data leaving your machine.

- **[Ollama](https://ollama.com)** — Run LLMs locally with a simple CLI. *Completely free.*
- **[LM Studio](https://lmstudio.ai)** — Desktop app to download and run local models. *Completely free.*
- **[Jan](https://jan.ai)** — Offline-first AI assistant with local model support. *Completely free.*
- **[GPT4All](https://gpt4all.io)** — Run LLMs locally on CPU/GPU. *Completely free.*

## Search & Research

AI-powered search engines and research tools.

- **[Perplexity AI](https://www.perplexity.ai)** — AI-powered search with cited answers. *Free tier available.*
- **[You.com](https://you.com)** — AI search engine with conversational interface. *Free.*
- **[Phind](https://www.phind.com)** — Developer-focused AI search and coding assistant. *Free.*
- **[models.dev](https://models.dev)** — Comprehensive reference for frontier AI model pricing, context windows, and capabilities across all major labs. *Completely free.*

## Productivity

AI tools for writing, notes, diagrams, and presentations.

- **[NotebookLM](https://notebooklm.google.com)** — Google's AI research and note-taking tool (upload docs). *Free.*
- **[Gamma](https://gamma.app)** — AI-powered presentation and document creation. *Free tier available.*
- **[Napkin AI](https://napkin.ai)** — Turn text into visuals and diagrams automatically. *Free tier available.*

## Frameworks

Open-source libraries for building agents, RAG pipelines, and optimised prompts. All are free — costs come only from the models you connect.

- **[LangChain](https://python.langchain.com)** — Provider-agnostic framework for building LLM chains and agents; includes LangGraph for stateful multi-agent workflows. *Completely free; open-source.*
- **[CrewAI](https://crewai.com)** — Role-based multi-agent framework — define a crew of agents with distinct roles and goals; lowest barrier to entry of any major framework. *Completely free; open-source.*
- **[AutoGen](https://microsoft.github.io/autogen)** — Microsoft's conversational multi-agent framework with the richest set of agent conversation patterns. *Completely free; open-source.*
- **[MetaGPT](https://github.com/geekan/MetaGPT)** 🇨🇳 — Chinese framework that maps software-team roles (PM, architect, engineer, QA) to LLM agents following structured SOPs. *Completely free; open-source.*
- **[AgentScope](https://github.com/modelscope/agentscope)** 🇨🇳 — Alibaba's production-ready multi-agent framework with visual Studio UI and distributed execution support. *Completely free; open-source.*
- **[LlamaIndex](https://llamaindex.ai)** — Framework for connecting LLMs to external data sources and building retrieval-augmented generation pipelines. *Completely free; open-source.*
- **[DSPy](https://dspy.ai)** — Stanford framework for algorithmically optimizing LLM prompts and pipelines instead of hand-writing them. *Completely free; open-source.*
---

## Contributing

The list is driven by [`resources.csv`](resources.csv) — edit that file to add or change entries.

**Quick add via CLI:**
```bash
python3 update.py
```

**Manual CSV edit** — append a row with these columns:
```
name, category, url, description, free_tier, requires_signup, tags
```

**Criteria for inclusion:**
- Has a genuine free tier (no credit card required to start, unless noted)
- Publicly accessible — not waitlisted or invite-only
- Active and functional product
- AI is a core part of the product, not a minor feature

All changes are logged automatically to [`history.csv`](history.csv).

**Automated refresh:** Open a Claude Code session here and paste [`refresh_prompt.md`](refresh_prompt.md) to have Claude research new tools and update the list.

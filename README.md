# Awesome Free AI

> A snapshot of genuinely free (or free-tier) AI tools, APIs, and platforms **as they existed in August 2026**.

Free tiers change fast — tools get paywalled, rebranded, or shut down. This list captures what was on offer at the time of each update, with every change tracked in [`history.csv`](history.csv) and summarised in [`CHANGELOG.md`](CHANGELOG.md). Think of it less as a permanent directory and more as a dated edition: accurate when written, audited on refresh.

**76 free resources** across 16 categories, plus [3 notable paid-only tools](paid_resources.csv). Browse the [web view](index.html) for a filterable, searchable UI, or read on.

---

## Contents

- [LLM Chatbots](#llm-chatbots)
- [LLM APIs](#llm-apis)
- [LLM Routers & Gateways](#llm-routers--gateways)
- [LLM Clients](#llm-clients)
- [Code Assistants](#code-assistants)
- [Code & UI Builders](#code--ui-builders)
- [Image Generation](#image-generation)
- [Video Generation](#video-generation)
- [Audio & Voice](#audio--voice)
- [Music Generation](#music-generation)
- [Local & Self-hosted](#local--self-hosted)
- [Search & Research](#search--research)
- [Productivity](#productivity)
- [Agent Frameworks](#agent-frameworks)
- [RAG Frameworks](#rag-frameworks)
- [Prompt Optimization](#prompt-optimization)
- [Contributing](#contributing)

---

## LLM Chatbots

Full-featured AI chat interfaces with free tiers.

- **[Claude (Anthropic)](https://claude.ai)** — Anthropic's AI assistant — strong reasoning and long context. *Free tier with usage limits.*
- **[ChatGPT](https://chat.openai.com)** — OpenAI's flagship assistant. *Free tier (GPT-4o limited).*
- **[Gemini](https://gemini.google.com)** — Google's multimodal AI assistant. *Free tier available.*
- **[Muse Spark](https://meta.ai)** — Meta's first model from Meta Superintelligence Labs — natively multimodal (text/image/audio) with tool use and visual chain-of-thought; available via meta.ai. *Free; requires Meta account (Facebook or Instagram login).*
- **[Le Chat](https://chat.mistral.ai)** — Mistral's AI assistant with web search and image generation built in. *Free tier with daily limits; no credit card required.*
- **[DeepSeek](https://chat.deepseek.com)** — Free chatbot featuring strong reasoning and coding from DeepSeek's open-weight models. *Free with usage limits.* *No signup required.*
- **[Qwen Chat](https://chat.qwen.ai)** — Alibaba's assistant fronting the Qwen model family, with image and document understanding. *Free with rate limits; no consumer subscription tier.*

## LLM APIs

Programmatic access to large language models with free quotas.

- **[Google AI Studio](https://aistudio.google.com)** — Gemini API with a generous free quota for prototyping. *Free API key with per-model rate limits (current limits shown in AI Studio).*
- **[Groq](https://console.groq.com)** — Blazing-fast inference for open models (Llama etc.). *Free tier: 30 RPM; 1,000–14,400 requests/day depending on model.*
- **[Together AI](https://api.together.xyz)** — Serverless inference for 100+ open-source models. *$5 free credit on signup.*
- **[Mistral AI (La Plateforme)](https://console.mistral.ai)** — Access to Mistral models via API. *Free tier available.*
- **[Cohere](https://dashboard.cohere.com)** — NLP-focused models for generation and embeddings. *Free trial key: 1,000 API calls/month, 20 req/min (chat).*
- **[Hugging Face Inference API](https://huggingface.co/inference-api)** — Free serverless inference for thousands of public models. *Free with rate limits.*
- **[OpenRouter](https://openrouter.ai)** — Unified API routing to many models; the :free tier is a rate-limited community pool. *Free tier: 20 RPM, 50 :free-model requests/day (1,000/day after a $10 lifetime top-up).*
- **[Cerebras](https://cloud.cerebras.ai)** — Ultra-fast inference API for open models (Llama 4 and Qwen) via custom silicon. *Free tier: 1M tokens/day with no credit card.*
- **[Chutes.ai](https://chutes.ai)** — Decentralised serverless inference on the Bittensor network — frequently hosts free or near-free DeepSeek and other open-model endpoints. *Free tier available; pricing fluctuates with network conditions.*
- **[Puter.js](https://developer.puter.com)** — Browser-native JS library giving free access to DeepSeek V4 Flash/Pro and other models with no API key or server setup. *Completely free for developers; user-pays model covers costs.* *No signup required.*
- **[Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai)** — Serverless inference for 40+ open models running on Cloudflare's edge network. *Free: 10,000 neurons/day, resets 00:00 UTC, no credit card.*
- **[NVIDIA NIM](https://build.nvidia.com)** — Hosted endpoints for 100+ open models (Nemotron, Llama, Qwen) through the NVIDIA Developer Program. *Free API key with ~40 RPM and no trial expiry; no credit card.*
- **[SambaNova](https://cloud.sambanova.ai)** — Fast inference for open models on SambaNova's dataflow hardware. *Free tier (no payment method linked): 20 RPM, 20 requests/day, 200K tokens/day.*
- **[SiliconFlow](https://siliconflow.cn)** — Chinese inference platform serving Qwen, DeepSeek and other open models via an OpenAI-compatible API. *Some small models (e.g. Qwen2.5-7B) free forever, plus ¥14 signup credits.*
- **[Z.ai (GLM)](https://z.ai)** — Zhipu AI's OpenAI-compatible API for the GLM model family, including several free Flash models. *Flash models (GLM-4.7-Flash, GLM-4.5-Flash, GLM-4.5V/4.6V-Flash) priced free.*

## LLM Routers & Gateways

Route one request across many providers, with fallback and rate-limit handling.

- **[LiteLLM](https://litellm.ai)** — Unified OpenAI-compatible proxy that routes to 100+ LLM providers with automatic retries and rate-limit fallback. *Completely free; open-source.* *No signup required.*
- **[Vercel AI Gateway](https://vercel.com/ai-gateway)** — Single endpoint that routes to many model providers at list price with no Vercel markup. *Monthly free credit per team, on a subset of models with reduced rate limits.*

## LLM Clients

Thin libraries for talking to several model providers through one interface.

- **[aisuite](https://github.com/andrewyng/aisuite)** — Lightweight unified Python interface to multiple LLM providers from Andrew Ng's team. *Completely free; open-source.* *No signup required.*

## Code Assistants

AI tools that live in your editor or terminal.

- **[GitHub Copilot](https://github.com/features/copilot)** — AI code completion in your editor. *Free for all users (2000 completions + 50 chats/month).*
- **[Devin Desktop (formerly Windsurf)](https://devin.ai)** — Cognition's AI-native IDE — the former Windsurf editor, rebuilt around Devin Local agents and an Agent Command Center. *Free tier: unlimited Tab completions and inline edits, limited Devin Local, no cloud agents.*
- **[Cursor](https://cursor.sh)** — AI-first code editor. *Free tier with limited completions and requests (Cursor does not publish exact figures).*
- **[Continue](https://continue.dev)** — Open-source AI code assistant for VS Code / JetBrains. *Completely free.* *No signup required.*
- **[Aider](https://aider.chat)** — AI pair programming in your terminal. *Completely free (bring your own key).* *No signup required.*
- **[Antigravity](https://antigravity.google)** — Google's AI-native IDE, CLI and SDK that coordinates Manager/Writer/Critic/Tester agents; the supported replacement for Gemini CLI since June 18 2026. *Free plan covers ordinary use (Gemini 3 Pro quota); personal Google account required.*
- **[Amazon Q Developer](https://aws.amazon.com/q/developer)** — AWS's AI coding assistant with IDE inline suggestions and agentic coding in VS Code and JetBrains. *Free tier: unlimited completions + 50 agentic tasks/month.*
- **[Freebuff](https://freebuff.com)** — AI coding agent that runs in your terminal — ad-supported so it costs nothing; built on Codebuff with specialised sub-agents for file picking, code review, and browser use. *Completely free (ad-supported in CLI).* *No signup required.*
- **[OpenCode](https://opencode.ai)** — Open-source terminal coding agent from the SST team with a TUI interface and support for 75+ LLMs including local models via Ollama. *Completely free; bring your own key or use free providers.* *No signup required.*
- **[Cline](https://cline.bot)** — Open-source autonomous coding agent for VS Code that plans, edits files and runs commands. *Completely free; open-source (bring your own key).* *No signup required.*
- **[Kilo Code](https://kilo.ai)** — Open-source coding agent for VS Code, JetBrains and the terminal with access to 500+ models at provider cost. *Completely free; open-source, no markup on model costs.* *No signup required.*
- **[Goose](https://goose-docs.ai)** — Open-source general-purpose AI agent that runs on your machine as a desktop app, CLI or API; governed by the Agentic AI Foundation. *Completely free; open-source Apache-2.0 (bring your own key).* *No signup required.*

## Code & UI Builders

Generate full UIs and apps from a prompt in the browser.

- **[v0 by Vercel](https://v0.dev)** — Generate React/UI components from prompts. *Free tier available.*
- **[Bolt.new](https://bolt.new)** — Full-stack AI app builder in the browser. *Free tier available.*
- **[Lovable](https://lovable.dev)** — AI full-stack app builder that generates React/TypeScript with a Supabase backend and deploys instantly. *Free tier: 5 credits/day (30/month); no credit card required.*

## Image Generation

Text-to-image tools that are free or have a meaningful free tier.

- **[Stable Diffusion (via DiffusionBee)](https://diffusionbee.com)** — Run Stable Diffusion locally on Mac. *Completely free.* *No signup required.*
- **[Adobe Firefly](https://firefly.adobe.com)** — Adobe's generative image tools. *Free credits monthly.*
- **[Microsoft Designer](https://designer.microsoft.com)** — AI image generation via DALL-E. *Free tier available.*
- **[Ideogram](https://ideogram.ai)** — Text-to-image with strong typography. *Free tier available.*
- **[Playground AI](https://playground.com)** — Image generation and editing. *Free tier: 5 images per rolling window, 2 downloads/day, non-commercial only.*
- **[Canva AI](https://canva.com)** — AI image generation and design tools. *Free tier with AI features.*
- **[Leonardo AI](https://leonardo.ai)** — Text-to-image generation with fine-tuned model presets and in-app editing tools. *Free tier: 150 fast tokens/day (~10–15 images), non-commercial only.*
- **[Krea](https://krea.ai)** — Creative suite spanning 60+ image, video and 3D models with real-time generation and editing. *Free tier: 100 compute units/day, non-commercial only.*

## Video Generation

AI tools for generating or editing video.

- **[Runway](https://runwayml.com)** — AI video generation and editing tools. *Free tier (limited credits).*
- **[CapCut](https://capcut.com)** — AI video editing with auto-captions and effects. *Free tier available.*
- **[Descript](https://descript.com)** — AI video/audio editing with transcription. *Free tier available.*
- **[Kling AI](https://kling.ai)** — High-quality text-to-video and image-to-video generation from Kuaishou. *Free tier: 66 credits/day (watermarked outputs).*
- **[Pika](https://pika.art)** — AI video generation and image-animation with text-to-video controls. *Free plan with monthly credits.*

## Audio & Voice

Text-to-speech, voice cloning, and speech recognition.

- **[ElevenLabs](https://elevenlabs.io)** — High-quality AI text-to-speech and voice cloning. *Free tier: 10,000 credits/month (~10 minutes of TTS), no commercial licence.*
- **[Whisper (OpenAI)](https://github.com/openai/whisper)** — State-of-the-art open-source speech recognition. *Completely free.* *No signup required.*

## Music Generation

Generate original music from text prompts.

- **[Suno](https://suno.com)** — AI music generation from text prompts. *Free tier: generate, stream and share only — no downloads, personal non-commercial use.*
- **[Udio](https://udio.com)** — AI music generation and remixing. *Free tier: limited monthly generations, streaming only — downloads suspended platform-wide.*

## Local & Self-hosted

Run models on your own hardware — no API keys, no data leaving your machine.

- **[Ollama](https://ollama.com)** — Run LLMs locally with a simple CLI. *Completely free.* *No signup required.*
- **[LM Studio](https://lmstudio.ai)** — Desktop app to download and run local models. *Completely free.* *No signup required.*
- **[Jan](https://jan.ai)** — Offline-first AI assistant with local model support. *Completely free.* *No signup required.*
- **[GPT4All](https://gpt4all.io)** — Run LLMs locally on CPU/GPU. *Completely free.* *No signup required.*

## Search & Research

AI-powered search engines and research tools.

- **[Perplexity AI](https://www.perplexity.ai)** — AI-powered search with cited answers. *Free tier available.* *No signup required.*
- **[You.com](https://you.com)** — AI search engine with conversational interface. *Free.* *No signup required.*
- **[models.dev](https://models.dev)** — Comprehensive reference for frontier AI model pricing, context windows, and capabilities across all major labs. *Completely free.* *No signup required.*

## Productivity

AI tools for writing, notes, diagrams, presentations, and task automation.

- **[NotebookLM](https://notebooklm.google.com)** — Google's AI research and note-taking tool (upload docs). *Free.*
- **[Gamma](https://gamma.app)** — AI-powered presentation and document creation. *Free tier available.*
- **[Notion AI](https://notion.so)** — AI writing and summarization inside Notion. *Free trial; requires Notion plan.*
- **[Napkin AI](https://napkin.ai)** — Turn text into visuals and diagrams automatically. *Free tier available.*
- **[Manus](https://manus.im)** — General-purpose autonomous agent that plans and executes multi-step tasks in a cloud sandbox. *Free plan: 300 credits refreshed daily, capped at 1,500/month, Manus 1.6 Lite only.*

## Agent Frameworks

Open-source libraries for building single and multi-agent LLM systems. All are free to use — costs come only from the models you connect.

- **[LangChain](https://python.langchain.com)** — Provider-agnostic framework for building LLM chains and agents; includes LangGraph for stateful multi-agent workflows. *Completely free; open-source.* *No signup required.*
- **[CrewAI](https://crewai.com)** — Role-based multi-agent framework — define a crew of agents with distinct roles and goals; lowest barrier to entry of any major framework. *Completely free; open-source.* *No signup required.*
- **[AutoGen](https://microsoft.github.io/autogen)** — Microsoft's conversational multi-agent framework with the richest set of agent conversation patterns. *Completely free; open-source.* *No signup required.*
- **[MetaGPT](https://github.com/geekan/MetaGPT)** — Chinese framework that maps software-team roles (PM, architect, engineer, QA) to LLM agents following structured SOPs. *Completely free; open-source.* *No signup required.*
- **[AgentScope](https://github.com/modelscope/agentscope)** — Alibaba's production-ready multi-agent framework with visual Studio UI and distributed execution support. *Completely free; open-source.* *No signup required.*

## RAG Frameworks

Connect models to your own data for retrieval-augmented generation.

- **[LlamaIndex](https://llamaindex.ai)** — Framework for connecting LLMs to external data sources and building retrieval-augmented generation pipelines. *Completely free; open-source.* *No signup required.*

## Prompt Optimization

Optimise prompts and pipelines programmatically instead of by hand.

- **[DSPy](https://dspy.ai)** — Stanford framework for algorithmically optimizing LLM prompts and pipelines instead of hand-writing them. *Completely free; open-source.* *No signup required.*

---

## Contributing

The list is driven by [`resources.csv`](resources.csv) — edit that file to add or change entries. This README is generated from it, so regenerate after any change:

```bash
python3 generate_readme.py
```

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

Tools with no genuine free tier belong in [`paid_resources.csv`](paid_resources.csv) instead.

All changes are logged to [`history.csv`](history.csv) / [`paid_history.csv`](paid_history.csv), which are append-only.

**Automated refresh:** Open a Claude Code session here and paste [`refresh_prompt.md`](refresh_prompt.md) (free tools) or [`paid_refresh_prompt.md`](paid_refresh_prompt.md) (paid tools) to have Claude research new tools and update the list.

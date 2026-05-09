#!/usr/bin/env python3
"""
mem0 Memory Uploader — Arthur Buikis Income Strategy
Smart auto-detection: Ollama > OpenAI > DeepSeek > local JSON fallback.

FIRST RUN: writes memories to ~/.mem0/pending_memories.json (always, as backup)
SECOND PASS: if an LLM is available, imports directly into mem0.

Usage:
    pip install mem0ai sentence-transformers   # one-time
    python import_to_mem0.py

Supported LLM providers (auto-detected):
    - Ollama (local, free):     ollama serve
    - OpenAI:                   $env:OPENAI_API_KEY="sk-..."
    - DeepSeek:                 $env:DEEPSEEK_API_KEY="sk-..."
"""

import os
import sys
import json
import subprocess

# ── 1. Always write memories as JSON backup ──
memories = [
    "Arthur Buikis is based in Riga, Latvia (EU timezone). Languages: Latvian native, English fluent, Russian conversational, German conversational.",
    "Arthur has 12 years of backend/platform engineering experience. Stack: Python, Rust, TypeScript, Django, Celery, PostgreSQL, ClickHouse, Kubernetes, Tauri.",
    "Arthur is employed full-time at a media-processing platform in Riga since 2024. Also freelances on Upwork since 2017 with 100 percent Job Success Score and 12 plus contracts.",
    "Arthur built: MarkFlow SaaS, MyProxy mobile proxy, bravo-tango-bravo B2B lead gen, CH-Streaming-API, and Expired Domain Search pipeline processing 700M plus domains with 43TB data.",
    "Arthur's current salary is 2600 EUR per month. Target income is 7000 to 8000 EUR per month. Expenses are 3000 EUR per month. No savings or runway. Income gap is 4400 to 5400 EUR per month.",
    "Arthur has 48 hours per week available for side income. Works from home with relaxed boss. Has 21 vacation days saved. Has one kid and wife.",
    "Arthur is expert in AI agent building with OpenAI API and agent orchestration. Built Advanced Hermes with Mem0 and Multica. Uses Claude Code subagent-driven development daily at his day job.",
    "Arthur wants to keep day job at Giraffe and stack side income. Willing to relocate within EU. Career preference is job plus side income, not full independence yet.",
    "Arthur is willing to build in public on GitHub, Twitter, blog, and newsletter. This is a strategic shift from his previous stealth approach.",
    "Arthur's preferred industry verticals are real estate, media, proxy services, and company data. He has deep domain knowledge from past projects.",
    "MarkFlow is effectively dead with zero paying users and 100 percent monthly churn. Arthur puts zero hours per week into it and does not believe it can scale. Treat any remaining MRR as passive bonus only.",
    "Arthur's prototype idea: an AI outbound agent that reaches out to businesses then audits their response speed when they reply late, pitching AI automation consulting. Also a tool monitoring local business page uptime and speed. Idea stage with 90 day timeline to first paying user.",
    "Arthur has ten strategic gaps blocking income: positioning as backend engineer instead of AI automation, zero public AI agent work, stale GitHub, LinkedIn not AI-optimized, research paralysis, stealth paradox, no audience or funnel, outdated Upwork profile, no niche focus, LinkedIn profile fragmentation.",
    "The 30 day execution plan: Phase 1 days 1-3 rebrand LinkedIn GitHub and personal site. Phase 2 days 4-14 build ResponseAuditor open source project auditing business response times. Phase 3 parallel start Upwork at 75 to 100 dollars per hour plus Fiverr plus direct outreach to Baltic businesses. Phase 4 month 2 plus content flywheel with weekly blog posts Twitter threads LinkedIn posts and biweekly newsletter.",
    "After ResponseAuditor, Arthur should build one of: SitePulse uptime monitor for local businesses, AgentDoc open source AI agent documentation generator, or EUDomainScout AI powered EU market entry research tool.",
    "Arthur should avoid: spending time on MarkFlow, researching without building, keeping projects secret, underselling pricing below 75 to 150 EUR per hour for AI agent skills, and waiting for permission despite 21 vacation days and relaxed boss.",
]

output_path = os.path.expanduser("~/.mem0/pending_memories.json")
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w") as f:
    json.dump(memories, f, indent=2)
print(f"Wrote {len(memories)} memories to: {output_path}")

# ── 2. Try to import into mem0 ──
# Detect available LLM
llm_provider = None
llm_config = {}

# Check Ollama (must have HTTP server running, not just CLI)
try:
    import urllib.request
    req = urllib.request.Request("http://localhost:11434/api/tags")
    resp = urllib.request.urlopen(req, timeout=3)
    if resp.status == 200:
        llm_provider = "ollama"
        llm_config = {"model": "llama3.2:latest"}
        print("Detected: Ollama (server running)")
except Exception:
    pass

# Check OpenAI
if not llm_provider and os.environ.get("OPENAI_API_KEY"):
    llm_provider = "openai"
    llm_config = {"model": "gpt-4o-mini", "api_key": os.environ["OPENAI_API_KEY"]}
    print("Detected: OpenAI")

# Check DeepSeek
if not llm_provider and os.environ.get("DEEPSEEK_API_KEY"):
    llm_provider = "deepseek"
    llm_config = {"model": "deepseek-chat", "api_key": os.environ["DEEPSEEK_API_KEY"]}
    print("Detected: DeepSeek")

if not llm_provider:
    print("\nNo LLM available for mem0 import (no Ollama running, no API keys set).")
    print("Memories saved to JSON file above. To import:")
    print("  Option A: ollama serve      (free, local)")
    print("  Option B: $env:OPENAI_API_KEY='sk-...'")
    print("  Option C: $env:DEEPSEEK_API_KEY='sk-...'")
    print("Then re-run: python import_to_mem0.py")
    sys.exit(0)

# ── 3. Import into mem0 ──
from mem0 import Memory

# Use HuggingFace embeddings (free, no API key needed)
embed_provider = "huggingface"
embed_config = {"model": "all-MiniLM-L6-v2"}

mem0_config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "path": os.path.expanduser("~/.mem0/qdrant_data_v2"),
            "collection_name": "mem0_v2",
        },
    },
    "llm": {"provider": llm_provider, "config": llm_config},
    "embedder": {"provider": embed_provider, "config": embed_config},
    "history_db_path": os.path.expanduser("~/.mem0/history.db"),
    "version": "v1.1",
}

# Load user_id
config_path = os.path.expanduser("~/.mem0/config.json")
user_id = "default"
try:
    with open(config_path) as f:
        user_id = json.load(f).get("user_id", "default")
except Exception:
    pass

m = Memory.from_config(config_dict=mem0_config)
print(f"mem0 ready: LLM={llm_provider}, Embeddings={embed_provider}")

success = 0
for i, text in enumerate(memories):
    try:
        m.add(text, user_id=user_id)
        success += 1
        print(f"[{i+1}/{len(memories)}] OK")
    except Exception as e:
        print(f"[{i+1}/{len(memories)}] FAIL: {e}")

print(f"\nImported {success}/{len(memories)} memories to mem0 for user '{user_id}'.")

# Clean up pending file on full success
if success == len(memories):
    os.remove(output_path)
    print("Removed pending file (all imported).")

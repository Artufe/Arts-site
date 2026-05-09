#!/usr/bin/env python3
"""
mem0 Memory Uploader — Arthur Buikis Income Strategy
Uses Mem0 Platform API (no local embeddings needed, no OpenAI key needed).

Requires: MEM0_API_KEY environment variable (get it at https://app.mem0.ai/dashboard/api-keys)

Usage:
    $env:MEM0_API_KEY="m0-..."
    python import_to_mem0.py
"""

import os
import sys
import json

api_key = os.environ.get("MEM0_API_KEY")
if not api_key:
    print("ERROR: MEM0_API_KEY not set.")
    print("Get your key at: https://app.mem0.ai/dashboard/api-keys")
    print("Then: $env:MEM0_API_KEY='m0-...'")
    print("For persistence: [Environment]::SetEnvironmentVariable('MEM0_API_KEY', 'm0-...', 'User')")
    sys.exit(1)

from mem0 import MemoryClient

# Load user_id from existing config
config_path = os.path.expanduser("~/.mem0/config.json")
user_id = "default"
try:
    with open(config_path) as f:
        user_id = json.load(f).get("user_id", "default")
except Exception:
    pass

print(f"Connecting to Mem0 Platform...")
print(f"User ID: {user_id}")

client = MemoryClient(api_key=api_key)

# ── Memories ──
memories = [
    "Arthur Buikis is based in Riga, Latvia (EU timezone). Languages: Latvian native, English fluent, Russian conversational, German conversational.",
    "Arthur has 12 years of backend/platform engineering experience. Stack: Python, Rust, TypeScript, Django, Celery, PostgreSQL, ClickHouse, Kubernetes, Tauri.",
    "Arthur is employed full-time at a media-processing platform in Riga since 2024. Also freelances on Upwork since 2017 with 100 percent Job Success Score and 12 plus contracts.",
    "Arthur built: MarkFlow SaaS, MyProxy mobile proxy, bravo-tango-bravo B2B lead gen, CH-Streaming-API, and Expired Domain Search pipeline processing 700M plus domains with 43TB data.",
    "Arthur's current salary is 2600 EUR per month. Target income is 7000 to 8000 EUR per month. Expenses are 3000 EUR per month. No savings or runway. Income gap is 4400 to 5400 EUR per month.",
    "Arthur has 48 hours per week available for side income. Works from home with relaxed boss. Has 21 vacation days saved. Has one kid and wife.",
    "Arthur is expert in AI agent building with OpenAI API and agent orchestration. Built Advanced Hermes with Mem0 and Multica. Uses Claude Code subagent-driven development daily.",
    "Arthur wants to keep day job at Giraffe and stack side income. Willing to relocate within EU. Career preference is job plus side income.",
    "Arthur is willing to build in public on GitHub, Twitter, blog, and newsletter. This is a strategic shift from stealth.",
    "Arthur's preferred industry verticals are real estate, media, proxy services, and company data.",
    "MarkFlow is effectively dead with zero paying users and 100 percent monthly churn. Treat any remaining MRR as passive bonus only.",
    "Arthur's prototype: an AI outbound agent that audits business response times and pitches AI automation consulting. Also a site monitoring tool. Idea stage, 90 day timeline.",
    "Arthur has ten strategic gaps: positioning mismatch, no public AI work, stale GitHub, LinkedIn not AI-optimized, research paralysis, stealth paradox, no audience, outdated Upwork, no niche focus, LinkedIn fragmentation.",
    "The 30 day execution plan: Phase 1 rebrand to AI automation engineer. Phase 2 build ResponseAuditor open source tool. Phase 3 start Upwork and Fiverr plus direct outreach to Baltic businesses. Phase 4 content flywheel.",
    "After ResponseAuditor, Arthur should build SitePulse uptime monitor, or AgentDoc AI documentation generator, or EUDomainScout EU market research tool.",
    "Arthur should avoid MarkFlow, research without building, keeping projects secret, underselling pricing, and waiting for permission.",
]

success = 0
for i, memory_text in enumerate(memories):
    try:
        client.add(
            [{"role": "user", "content": memory_text}],
            user_id=user_id,
        )
        success += 1
        print(f"[{i+1}/{len(memories)}] OK")
    except Exception as e:
        print(f"[{i+1}/{len(memories)}] FAIL: {e}")

print(f"\nImported {success}/{len(memories)} memories to Mem0 Platform for user '{user_id}'.")

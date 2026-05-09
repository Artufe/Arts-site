#!/usr/bin/env python3
"""
mem0 Memory Uploader — Arthur Buikis Income Strategy

Run this script to upload the knowledge gap analysis and execution plan
as memories to mem0 for persistent agent context.

Requires: pip install mem0ai
Requires: OPENAI_API_KEY environment variable set

Usage:
    $env:OPENAI_API_KEY="sk-..."    # PowerShell
    python import_to_mem0.py
"""

import os
import sys
import json

# Check for API key
if not os.environ.get("OPENAI_API_KEY"):
    print("ERROR: OPENAI_API_KEY environment variable not set.")
    print("Set it first, e.g.: $env:OPENAI_API_KEY='sk-...'")
    sys.exit(1)

try:
    from mem0 import Memory
except ImportError:
    print("ERROR: mem0ai not installed. Run: pip install mem0ai")
    sys.exit(1)

# Load user_id from config
config_path = os.path.expanduser("~/.mem0/config.json")
user_id = "default"
try:
    with open(config_path) as f:
        config = json.load(f)
    user_id = config.get("user_id", "default")
    print(f"Using mem0 user_id: {user_id}")
except Exception:
    pass

# Initialize mem0
m = Memory()

# Memories to store (factual, structured)
memories = [
    # PROFILE
    "Arthur Buikis is based in Riga, Latvia (EU timezone, CET/CEST). Languages: Latvian (native), English (fluent), Russian (conversational), German (conversational).",
    "Arthur has ~12 years of backend/platform engineering experience. Stack: Python (primary), Rust (PyO3), TypeScript, Django, Celery, PostgreSQL, ClickHouse, Kubernetes, Tauri.",
    "Arthur is employed full-time at a media-processing platform in Riga (2024-present). He also freelances on Upwork since 2017 (100% JSS, 12+ contracts).",

    # PROJECTS
    "Arthur built MarkFlow (social-analytics SaaS), MyProxy (mobile proxy, sunset), bravo-tango-bravo (B2B lead gen), CH-Streaming-API (Companies House streaming), and an Expired Domain Search pipeline (700M+ domains, 43TB data).",

    # FINANCIAL
    "Arthur's current salary is €2,600/mo. Target income is €7,000-8,000/mo. Monthly expenses are €3,000. No savings/runway. Income gap: €4,400-5,400/mo.",
    "Arthur has 48 hours/week available for side income. He works from home with a relaxed boss. Has 21 vacation days saved. Has 1 kid and a wife.",

    # SKILLS
    "Arthur self-assesses as expert in AI agent building. He has practical experience with OpenAI API and agent orchestration. He built Advanced Hermes with Mem0 and Multica for agent-based workflows. Uses Claude Code subagent-driven development daily.",

    # CAREER
    "Arthur wants to keep his day job at Giraffe (which he likes) and stack side income. He's willing to relocate within the EU. His career path preference is job + side income, not full independence yet.",

    # PUBLIC BUILDING
    "Arthur is willing to build in public on GitHub, Twitter, blog, and newsletter. He previously built everything in stealth. This is a strategic shift.",

    # VERTICALS
    "Arthur's preferred industry verticals: real estate, media, proxy services, and company data. He has deep domain knowledge in these areas from past projects.",

    # MARKFLOW
    "MarkFlow is effectively dead: 0 paying users, 100% churn, 0 hours/week invested. Arthur doesn't believe it can scale. Should treat any remaining MRR as passive bonus income only.",

    # PROTOTYPE
    "Arthur's prototype product idea: an AI outbound agent that reaches out to businesses, then audits/roasts their response speed when they reply late, pitching AI automation consulting. Also a side tool monitoring local business page uptime/speed. Currently at idea stage, 90-day timeline to first paying user.",

    # STRATEGIC GAPS
    "Arthur has 10 strategic gaps blocking income: 1) Positioning as backend engineer instead of AI automation, 2) Zero public AI agent work, 3) Stale GitHub, 4) LinkedIn not AI-optimized, 5) Research paralysis (researching without executing), 6) Stealth paradox (building in secret = invisible), 7) No audience/funnel, 8) Upwork profile shows old skills, 9) No niche focus, 10) LinkedIn profile fragmentation.",

    # EXECUTION PLAN
    "The 30-day execution plan for Arthur: Phase 1 (Days 1-3) — Rebrand LinkedIn, GitHub, personal site to AI automation engineer. Phase 2 (Days 4-14) — Build 'ResponseAuditor' open-source project that audits business response times and pitches automation. Phase 3 (Days 1-14) — Start Upwork ($75-100/hr), Fiverr ($100-300/gig), direct outreach to Baltic businesses, and Arc.dev applications. Phase 4 (Month 2+) — Content flywheel: 1 blog post/week, 1 Twitter thread/week, 1 LinkedIn post/week, biweekly newsletter.",

    # NEXT PUBLIC PROJECTS
    "After ResponseAuditor, Arthur should build one of: SitePulse (uptime monitor for local businesses), AgentDoc (open-source AI agent documentation generator), or EUDomainScout (AI-powered EU market entry research tool).",

    # WHAT NOT TO DO
    "Arthur should avoid: spending time on MarkFlow, researching without building (SID-10 and SID-13 already covered research), keeping projects secret, underselling on pricing (€75-150/hr for AI agent skills is minimum), waiting for permission (he has 21 vacation days and a relaxed boss).",
]

# Add each memory
for i, text in enumerate(memories):
    try:
        result = m.add(text, user_id=user_id)
        print(f"[{i+1}/{len(memories)}] Added: {text[:80]}...")
    except Exception as e:
        print(f"[{i+1}/{len(memories)}] FAILED: {e}")

print(f"\nDone! Uploaded {len(memories)} memories to mem0.")
print(f"User ID: {user_id}")

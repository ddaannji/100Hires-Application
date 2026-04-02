# 100Hires-Application
# Portfolio Setup – Cursor & AI Tools

## Overview
This repository documents the setup process of development tools and AI extensions as part of a portfolio project. The objective of this task is to demonstrate my ability to follow technical instructions, troubleshoot issues independently, and clearly document my workflow.

## Tools Installed
- Cursor IDE  
- Claude Code Extension (Cursor)  
- Codex Extension (Cursor)  
- Git for GitHub connection (for repository management)

## Steps Completed
1. Installed Cursor IDE from https://cursor.com/  
2. Opened Cursor and accessed the Extensions marketplace  
3. Installed the following extensions:
   - Claude Code  
   - Codex  
4. Installed both extensions successfully  
5. Created a public GitHub repository  
6. Opened the repository within Cursor  
7. Created this README.md file  
8. Committed and pushed the repository to GitHub  

## Challenges and Solutions

**1. Extension Authentication**  
Initially experienced delays during the login process for the Claude Code extension. This was resolved by retrying the authentication process and ensuring a stable internet connection.

**2. GitHub Repository Setup**  
Encountered some confusion when linking the local environment to the remote GitHub repository. Resolved by following step-by-step documentation and tutorials on repository setup and Git operations.

**3. Cursor Interface Familiarization**  
As a first-time user of Cursor, there was a brief learning curve in navigating the interface and managing extensions. This was addressed by exploring the documentation and testing basic features directly.

## Key Learnings
- Setting up a development environment using Cursor IDE  
- Installing and configuring AI-assisted coding tools  
- Managing version control using GitHub  
- Structuring technical documentation in a clear and concise format  

Researching about spesific topic assigned. 

# 100Hires Application — Research Project
## Topic: Cold Outreach Pipeline for B2B SaaS

**Applicant:** Muwalliha  
**Assigned by:** Alex Kravets, CEO — 100Hires  
**Deadline:** 3 days from assignment (2 April 2026)

---

## Why I Chose This Topic

Cold outreach pipeline for B2B SaaS is one of the most technically nuanced and highest-leverage growth channels available to early and growth-stage SaaS companies. Unlike paid acquisition, a well-built outreach pipeline compounds over time — better data, better copy, and better infrastructure all stack on each other.

This topic sits at the intersection of copywriting, data engineering, deliverability ops, and sales psychology. I chose it because the practitioners who do this well are easy to distinguish from those who just write about it: they share real numbers, real sequences, and real infrastructure decisions.

The 10 experts I selected are all **active practitioners** — founders, agency operators, or tool builders who run outreach campaigns at scale. None are purely theoretical writers or SEO bloggers.

---

## Repository Structure

```
100Hires-Application/
│
├── README.md                        ← This file
│
├── research/
│   ├── sources.md                   ← Master list of 10 experts with annotations
│   │
│   ├── linkedin-posts/              ← LinkedIn posts organized by author
│   │   ├── README.md
│   │   ├── jeremy-chatelaine/
│   │   ├── jack-reamer/
│   │   ├── alex-vacca/
│   │   ├── eric-nowoslawski/
│   │   ├── patrick-spychalski/
│   │   ├── patrick-dang/
│   │   ├── samantha-mckenna/
│   │   ├── yurii-veremchuk/
│   │   ├── jay-feldman/
│   │   └── matthew-lucero/
│   │
│   ├── youtube-transcripts/         ← Transcripts organized by video
│   │   ├── README.md
│   │   ├── jeremy-chatelaine/
│   │   ├── jack-reamer/
│   │   ├── alex-vacca/
│   │   ├── eric-nowoslawski/
│   │   ├── patrick-spychalski/
│   │   ├── patrick-dang/
│   │   ├── samantha-mckenna/
│   │   ├── yurii-veremchuk/
│   │   ├── jay-feldman/
│   │   └── matthew-lucero/
│   │
│   └── other/                       ← Podcasts, newsletters, additional materials
│       └── README.md
│
└── scripts/
    ├── fetch_youtube_transcripts.py ← Script to pull YouTube transcripts via API
    └── requirements.txt
```
---

## Expert Selection Criteria

I evaluated each expert against three filters:

1. **Do they practice what they teach?** Are they actively running campaigns, managing clients, or building outreach tools?
2. **Do they share real data?** Open rates, reply rates, sequence breakdowns, real pipeline numbers.
3. **Is their content recent and still relevant?** Active in 2024–2025, posting content that reflects current deliverability and AI-personalization realities.

---

## Experts Collected (10 Total)

| # | Name | Primary Channel | Specialty |
|---|------|----------------|-----------|
| 1 | Jeremy Chatelaine | LinkedIn + Podcast | Deliverability-first systems |
| 2 | Jack Reamer | LinkedIn + YouTube + Podcast | Ultra-personalized 1-to-1 outreach |
| 3 | Alex Vacca (ColdIQ) | YouTube + LinkedIn | Clay-powered outbound systems |
| 4 | Eric Nowoslawski | LinkedIn + YouTube | AI + Clay at scale (1.5M emails/mo) |
| 5 | Patrick Spychalski | LinkedIn | Clay + copywriting, no-code automation |
| 6 | Patrick Dang | YouTube + LinkedIn | B2B sales fundamentals (300K+ subs) |
| 7 | Samantha McKenna | LinkedIn | "Show Me You Know Me" personalization |
| 8 | Yurii Veremchuk | LinkedIn + Blog | Data-backed frameworks, Woodpecker |
| 9 | Jay Feldman | LinkedIn + YouTube | Agency-scale automation |
| 10 | Matthew Lucero | LinkedIn + YouTube | SaaS-specific deliverability systems |

Full annotations and links: [`research/sources.md`](./research/sources.md)

---

## Data Collection Method

**YouTube Transcripts:** Pulled via the `youtube-transcript-api` Python library (free, no quota limits for public videos). Script located at `scripts/fetch_youtube_transcripts.py`.

**LinkedIn Posts:** Collected manually by visiting each expert's LinkedIn profile and copying their 3–5 most recent posts relevant to cold outreach. Organized by author in `research/linkedin-posts/`.

**Other Sources:** Podcast episodes (Cold Outreach Podcast), blog posts, and newsletter issues collected where relevant.

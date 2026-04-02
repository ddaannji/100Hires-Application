# Alex Vacca — LinkedIn Posts

**Profile:** https://www.linkedin.com/in/alex-vacca/
**Company:** ColdIQ (Co-Founder & COO)
**Focus:** Clay-powered outbound systems, AI personalization at scale

---

## Post 1

**Date:** 2026-01-13
**URL:** https://www.linkedin.com/posts/alex-vacca_we-manage-80-b2b-clients-from-one-clay-table-activity-7416817754734891008-6UsQ

---

We manage 80+ B2B clients from one Clay table.

Here's the system that makes it possible.

At $6M in revenue, our outbound operation was starting to crack.

Not because of bad leads or copy.

Because every Go-To-Market Engineer had their own way of doing things.

Different workflows.
Different tools.
Different quality standards.

Blocklists would slip.
API credits would disappear on contacts we'd never reach.

We saw the pattern and built the solution.

One Master Clay table. Used by every single GTME at ColdIQ.

Here's the full breakdown:

Phase 1: Protection 

Before we touch a single lead, we lock down who NOT to contact.

Every client sends us their do-not-contact list:

→ Current customers
→ Competitors
→ Churned accounts
→ Anyone else off-limits

The table takes that list and:

-Standardizes and cleans every entry
-Extracts domain URLs from company names
-Creates a universal block across all enrichment tools

Result: Zero credits wasted on leads we can't use.

Phase 2: Lead sourcing 

The table pulls from multiple channels simultaneously:

-Extracts target domains from DiscoLike and our proprietary databases
-Sends those domains to Apollo to surface individual decision-makers
-Runs a secondary Clay search to catch anyone Apollo missed
-Enriches LinkedIn data through Prospeo.io
-Consolidates everything back into Clay via webhook

Phase 3: Multi-provider enrichment

Raw leads are worthless without accurate contact info.

We run every lead through a verification stack:

→ Email discovery via Wiza, Prospeo.io, and LeadMagic
→ Mobile numbers via FullEnrich
→ LinkedIn validation to confirm they still hold the role

If someone changed jobs last month, we catch it before outreach.

Phase 4: Final verification

Before any lead hits an outreach tool:

Phones get validated through FullEnrich
Emails get double-checked via LeadMagic and Instantly.ai

Phase 5: Export-ready output

The final list comes out clean and organized:

→ Deduplicated across every source
→ Sorted by seniority level
→ Capped at top 3 contacts per company

From there, leads flow directly into Instantly.ai, Expandi, or lemlist.

We have 30+ people building lead lists every single day.

Without a standardized system, that's 30 different interpretations of "good enough."

With this table, everyone operates at the same level.

Built once. Deployed for every client.

That's how you 3X lead volume without 3X the chaos.

What's the messiest part of your lead gen process right now? 👇

---

**Why relevant:** Real operational blueprint for scaling a cold outreach operation across multiple B2B clients — shows exactly how Clay can be used as the central system of record for outbound at agency scale.

---

## Post 2

**Date:** 2023-10-05
**URL:** https://www.linkedin.com/posts/alex-vacca_the-future-of-outbound-is-technical-and-automated-activity-7115726466960515073-BoVn

---

The future of outbound is technical and automated.

Here is the type of campaign we are running at ColdIQ. I want to give you our latest campaign as an example and the right tool to use for each step.

1) A dynamic trigger event arises (e.g. a new open position for an SDR or BDR on LinkedIn) → Apify 

2) We extract the relevant information and push it to Clay through an automation platform → Make or n8n

3) Data is pushed into your enrichment platform so the automatic data enrichment can start → Clay

4) Our OpenAI API key is already connected to Clay, so the personalization for each prospect happens automatically → OpenAI

5) All the data is then pushed automatically to our email-sending tool → Smartlead

6) Every day, more leads are added to our campaigns, emails are sent, and meetings are booked without having to interact with anything.

That's how we scale results, not by adding more data but by stacking evergreen, automated campaigns.

👉 Future is now at ColdIQ

You want us to build an automated outbound system?

Send me a DM.

(Here is what a typical data enrichment sheet in Clay looks like at 25% zoom out.)

---

**Why relevant:** End-to-end technical blueprint of a trigger-based outbound campaign (Apify → Make → Clay → OpenAI → Smartlead) — the most concrete stack walkthrough available for B2B SaaS teams building automated pipelines.

---

## Post 3

**Date:** 2024-01-04
**URL:** https://www.linkedin.com/posts/alex-vacca_personalize-outreach-at-scale-with-clay-activity-7148644194415288320-5lcd

---

The one tool you will need to master in 2024.

You hear about personalized outreach and AI-powered outbound everywhere. 

And the tool to do that in 2024 is Clay.

With Clay at the center of your stack, you can leverage data and AI to scale tailored messaging like never before.

Here is a 6-step framework to take any campaign from generic to hyper-personalized:

Step 1: Import a CSV of your target companies into Clay.

Step 2: Use Clay to identify roles like Content Marketer at target companies. It leverages PredictLeads, LinkedIn and Google to find open positions.

Step 3: Enrich contact info of decision-makers like CMO and Head of Growth using Clay's data integrations.

Step 4: Ask ChatGPT to read job descriptions and summarize needs.

Step 5: Have ChatGPT generate personalized outreach snippets for each prospect based on the job analysis.

Step 6: Add contacts and custom messaging to your sales engagement platform.

Now you can start your sequences with each message aligned to the prospect's role and needs.

As buyers demand relevance amidst overwhelming outreach, Clay allows you to still get great results with outbound in 2024. 

What tool do you see as a game-changer in 2024?

---

**Why relevant:** Step-by-step Clay personalization workflow that any B2B SaaS team can replicate — directly applicable for building a pipeline where every email references real, prospect-specific context.

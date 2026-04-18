# Cold Outreach Pipeline for B2B SaaS — Playbook & SOP

**Author:** Muwalliha  
**Based on research from:** 10 expert practitioners  
**Repository:** https://github.com/ddaannji/100Hires-Application  
**Last updated:** April 2026

---

## Table of Contents

1. [Philosophy](#1-philosophy)
2. [Infrastructure & Setup](#2-infrastructure--setup)
3. [List Building & ICP Targeting](#3-list-building--icp-targeting)
4. [Copywriting](#4-copywriting)
5. [Sending & Sequencing](#5-sending--sequencing)
6. [AI & Automation with Clay](#6-ai--automation-with-clay)
7. [Multichannel: LinkedIn + Email](#7-multichannel-linkedin--email)
8. [Measurement & Optimization](#8-measurement--optimization)
9. [Where Experts Disagree](#9-where-experts-disagree)
10. [What I Rejected and Why](#10-what-i-rejected-and-why)
11. [My Original Ideas](#11-my-original-ideas)
12. [Weaknesses of This Playbook](#12-weaknesses-of-this-playbook)
13. [Who I Would NOT Recommend Following and Why](#13-who-i-would-not-recommend-following-and-why)

---

## 1. Philosophy

Before touching any tool or writing any email, understand the core mental model that separates effective outreach from noise.

**Cold email is not a broadcast. It is a conversation starter.**

> "Stop chasing hacks. Cold email is about starting conversations, not dropping a booking link or forcing calls."  
> (source: Jeremy Chatelaine, https://www.linkedin.com/in/jeremychatelaine/, 01.2024)

The three non-negotiable pillars of any cold outreach pipeline, in order of priority:

1. **Deliverability** — If your email doesn't land in the primary inbox, nothing else matters. Not your copy. Not your offer. Not your list.
2. **List quality** — Accurate data on the right people. A mediocre list with 30% bad contacts cannot be saved by great copy.
3. **Copy with a clear offer** — There is a fundamental difference between copy that sounds clever and copy that converts cold traffic.

(source: Eric Nowoslawski, https://www.linkedin.com/in/outboundphd/, 01.2025)

> "People ask me about send times, follow-up cadences, A/B test frameworks, personalization tokens. Those are all optimizations on top of these 3 things. If your deliverability is broken, your list is wrong, or your copy doesn't resonate — no optimization saves you."  
> (source: Eric Nowoslawski, https://www.linkedin.com/in/outboundphd/, 01.2025)

**The right order of operations: start manual → validate → then automate.**

> "Most people skip straight to step 5 [automation]. That's why they fail."  
> (source: Eric Nowoslawski, https://www.linkedin.com/posts/outboundphd_if-i-had-to-start-cold-email-from-0-and-wasnt-activity-7340377690224402435-xJk8, 01.03.2025)

---

## 2. Infrastructure & Setup

### 2.1 Domain Setup

Never send cold email from your primary domain. A blacklisted primary domain kills your entire business email, not just your campaigns.

**Step-by-step domain infrastructure:**

1. **Buy 3–5 secondary domains** that redirect to your main website
   - Format: `yourcompanyhq.com`, `getyourcompany.com`, `tryyourcompany.com`
   - Cost: ~$10–15/domain/year
   - (source: Matthew Lucero, https://www.youtube.com/@AnevoMarketing, 01.2024)

2. **Create 2–3 email accounts per domain**
   - Use Google Workspace ($6/month/user) or Microsoft Outlook
   - Total sending accounts: 6–15
   - Max send limit: 30–40 emails/day per account
   - (source: Matthew Lucero, https://www.youtube.com/@AnevoMarketing, 01.2024)

3. **Authenticate every domain**
   - Set up SPF, DKIM, and DMARC records for every domain
   - Test with mail-tester.com — target score: 9/10 or higher
   - Use EasyDMARC for configuration
   - (source: Dr. Jay Feldman, https://www.linkedin.com/posts/dr-jay-feldman_cold-email-is-the-1-way-to-get-clients-for-activity-7252649561700159488-awG-, 01.10.2024)

4. **Warm up every inbox before sending**
   - Use Instantly or Mailreach for automated warm-up
   - Minimum 3–4 weeks warm-up before first campaign send
   - Keep 50–100% extra inbox capacity warming at all times as backup
   - (source: Eric Nowoslawski, https://www.linkedin.com/in/outboundphd/, 01.2025; Matthew Lucero, https://www.youtube.com/@AnevoMarketing, 01.2024)

> "Most people skip [deliverability setup] because it's boring. That's why most people's campaigns don't work."  
> (source: Eric Nowoslawski, https://www.linkedin.com/in/outboundphd/, 01.2025)

### 2.2 Sending Tool

Recommended: **Instantly** or **Smartlead** for agency-scale or multi-client operations.

Key features to require from any sending tool:
- Inbox rotation across multiple accounts
- Unified inbox (Unibox) for managing replies centrally
- A/B testing at the campaign level
- Real-time deliverability monitoring

(source: Dr. Jay Feldman, https://www.linkedin.com/posts/dr-jay-feldman_cold-email-is-the-1-way-to-get-clients-for-activity-7252649561700159488-awG-, 01.10.2024)

---

## 3. List Building & ICP Targeting

### 3.1 Define Your ICP — Beyond Demographics

Most teams define ICP as "companies that could benefit from our product." That is not an ICP. That is a wishlist.

**A real ICP for cold email has 6 attributes:**
1. Company size (employee count or revenue range)
2. Industry/vertical
3. Tech stack signal (using a competitor? a complementary tool?)
4. Funding stage (bootstrapped vs VC-backed changes the buying motion)
5. Growth signal (hiring, expanding, recently funded)
6. Decision-maker title (who signs the check)

(source: Matthew Lucero, https://www.linkedin.com/in/matthew-lucero/, 01.2024)

> "Build your list around trigger events, not demographics. Demographics tell you who could buy. Triggers tell you who is ready to buy right now."  
> (source: Matthew Lucero, https://www.linkedin.com/in/matthew-lucero/, 01.2024)

### 3.2 The 3 Levels of List Quality

> "There are 3 levels of prospecting. Level 1: Basic firmographics (what everyone does). Level 2: Behavioral signals. Level 3: High-intent. There are no good reasons to stay at Level 1."  
> (source: Jeremy Chatelaine, https://www.linkedin.com/in/jeremychatelaine/, 01.2024)

| Level | What It Is | Example Signal |
|-------|-----------|----------------|
| Level 1 | Firmographics: industry, company size, job title | "SaaS companies with 50-200 employees" |
| Level 2 | Behavioral signals | Follows specific influencers, engages with relevant topics |
| Level 3 | High-intent | Actively searching for what you offer, posted about the problem |

**Target Level 2 minimum. Level 3 when possible.**

### 3.3 List Building Tools

- **Apollo** — primary database for contact data, filter by ICP criteria
- **LinkedIn Sales Navigator** — for behavioral and role-based targeting
- **Clay** — enrichment, waterfall email finding, and ICP scoring
- **MillionVerifier / ZeroBounce** — email validation

(source: Dr. Jay Feldman, https://www.linkedin.com/posts/dr-jay-feldman_cold-email-is-the-1-way-to-get-clients-for-activity-7252649561700159488-awG-, 01.10.2024)

### 3.4 The List Is the Message

> "If you know you can sell to any founder with less than 20 employees, that's a pretty big list. But if you know the best founder for you is someone who has founded a company before, has been in business less than two years, has 10-20 employees, and has no accounting or finance job titles on their LinkedIn page... that person should be receiving a completely different message."  
> (source: Eric Nowoslawski, https://www.linkedin.com/in/outboundphd/, 01.2025)

**Framework: Segment your list by what data points change your messaging.**

Use Clay or Claude Code to enrich lists for any criteria that might change how you'd message someone. Your "golden ICP" might only have 1,000 leads — but the reply rate will be dramatically higher.

(source: Eric Nowoslawski, https://www.linkedin.com/in/outboundphd/, 01.2025)

---

## 4. Copywriting

### 4.1 The Core Framework — The Pain Formula

4 elements every cold email needs:

1. **Relevant Introduction** — Who are you and why is this relevant to them? One sentence max.
2. **Pain Point** — What specific problem does this prospect have? Research it. Don't guess.
3. **Solution** — What outcome do you deliver? Not what your product does — what the prospect achieves.
4. **Call to Action** — One simple, low-friction ask.

(source: Patrick Dang, https://patrickdang.com, 01.2024)

> "The biggest mistake: most reps write about themselves. Great cold emails are about the prospect's world, not yours."  
> (source: Patrick Dang, https://www.linkedin.com/in/patrickdangofficial/, 01.2024)

### 4.2 The Offer Framework

Use this structure for your offer:
> "We help [specific ICP] achieve [specific outcome] in [timeframe] without [main objection]."

Also think about what is **easy to say yes to**. Even a well-framed offer fails if the commitment feels too high. Lead with something smaller.

(source: Eric Nowoslawski, https://www.linkedin.com/in/outboundphd/, 01.2025)

### 4.3 Subject Lines — 4 Types That Work

1. **Desired Outcome** — "How [Similar Company] achieved [Specific Result]"
2. **Pain Point** — "[Specific Problem They Likely Have]?"
3. **Question** — "Quick question about [Specific Thing on Their Site/LinkedIn]"
4. **Referral** — "[Mutual Connection] suggested I reach out"

**The rule:** Your subject line should make the reader think "this was written for me."

(source: Patrick Dang, https://www.youtube.com/channel/UCLOzkJ9W9fntCGyYfUwMPew, 01.2024)

### 4.4 The Show Me You Know Me® Framework

For enterprise accounts and senior decision-makers, use the SMYKM framework:

1. **Subject line** — Research-based, hyper-specific. Only the prospect would recognize it.
2. **Opening line** — Short, human, no pitch.
3. **Transition** — One authentic tie-in to the opener.
4. **Value proposition** — Focused on the specific challenge you solve.
5. **Social proof** — One concise proof point.
6. **CTA** — Specific, low-commitment ask.
7. **Signature** — Clean, no distracting links.

(source: Samantha McKenna, https://www.apollo.io/magazine/the-7-elements-of-a-perfect-cold-email, 01.2024)

### 4.5 Copy Length and Reading Level

Keep emails under 100 words. Write at a 6th-grade reading level — data shows this gets significantly more replies than emails written at a 10th-grade level.

(source: Yurii Veremchuk, https://woodpecker.co/blog/, 01.2024)

### 4.6 The SaaS Cold Email Template

```
Subject: [Specific Pain or Outcome] — [Company Name]

Line 1 (Hook): "Saw you recently expanded your sales team to 15 reps."
Line 2 (Bridge): "Most teams at that stage start seeing pipeline visibility issues."
Line 3 (Offer): "We help SaaS sales teams at Series A-B get full pipeline 
visibility in under 2 weeks without replacing their CRM."
Line 4 (Proof): "Did this for [Similar Company] — they reduced forecast error by 40%."
Line 5 (CTA): "Worth a quick conversation?"
```

(source: Matthew Lucero, https://www.linkedin.com/in/matthew-lucero/, 01.2024)

---

## 5. Sending & Sequencing

### 5.1 Follow-Up Cadence

> "According to data from 1 million cold emails, 57.2% of replies come after your first follow-up email."  
> (source: Jack Reamer, https://salesbread.com/cold-email-cadence/, 01.2025)

**Recommended cadence:**
- Email 1: Day 1
- Email 2: Day 4 — majority of replies happen here
- Email 3: Day 8
- Email 4: Day 14
- Email 5: Day 21

**Key rule:** Each follow-up must reference a **new angle**. Never "just checking in."

**Tone progression:**
- Email 1: Confident
- Email 2: Helpful (provide value, no ask)
- Email 3: Respectful exit

(source: Yurii Veremchuk, https://woodpecker.co/blog/cold-email-follow-up/, 01.2024; Jack Reamer, https://salesbread.com/cold-email-cadence/, 01.2025)

### 5.2 CTA Strategy

> "Low-commitment CTAs boost replies. High-commitment ones filter tire-kickers. Use both strategically."  
> (source: Jeremy Chatelaine, https://www.linkedin.com/in/jeremychatelaine/, 01.2024)

- **Early sequences:** "Would it make sense to connect?" instead of "Book a 30-minute call."
- **Warmer follow-ups:** Slightly higher commitment CTAs to filter serious prospects.

### 5.3 Volume vs. Precision

> "Volume ≠ strategy. Sending more won't fix a broken campaign. It just scales failure and tanks your deliverability."  
> (source: Jeremy Chatelaine, https://www.linkedin.com/in/jeremychatelaine/, 01.2024)

> "I've seen clients with a 0.8% positive reply rate printing money. I've seen clients with a 4% positive reply rate struggling to stay afloat. The difference? One was selling $80K contracts. The other was selling a $500 product. Reply rate is a vanity metric if you don't connect it to revenue."  
> (source: Eric Nowoslawski, https://www.linkedin.com/in/outboundphd/, 01.2025)

**Before scaling, calculate:**
- TAM size — how many companies actually fit your ICP?
- Positive reply rate (not total reply rate)
- Deal value × close rate = value of one positive reply

---

## 6. AI & Automation with Clay

### 6.1 When to Use AI

> "Use AI for research and variation. Use humans for judgment and tone."  
> (source: Dr. Jay Feldman, https://www.linkedin.com/in/dr-jay-feldman/, 01.2024)

**AI works well for:**
- Generating first-line personalizations based on LinkedIn activity
- Identifying prospect pain based on job title + company stage
- Writing subject line variants for A/B testing
- Scoring lead lists for ICP fit

**AI does NOT work well for:**
- Writing entire emails (sounds robotic)
- Referencing company mission statements (prospects are blind to it)
- Running without human review on the first 50 sends

### 6.2 Clay Trigger-Based Campaign Stack

1. Trigger event detected (e.g., new SDR job posting) → Apify
2. Data extracted and pushed to Clay → via Make or n8n
3. Enrichment and AI personalization → Clay + OpenAI API
4. Push to email sending tool → Smartlead or Instantly
5. Leads added daily, emails sent automatically

(source: Alex Vacca, https://www.linkedin.com/posts/alex-vacca_the-future-of-outbound-is-technical-and-automated-activity-7115726466960515073-BoVn, 05.10.2023)

**Claygent automation tasks:**
- Is the company hiring?
- What was their most recent blog post about?
- When did they last raise money?
- Who are their competitors?

(source: Eric Nowoslawski, https://www.linkedin.com/posts/outboundphd_i-put-everything-i-know-about-cold-email-activity-7163534389954486274-gCRj, 14.02.2024)

### 6.3 The Simple Clay Rule

> "The best Clay tables are actually simple. One trigger. One message variant. One clear offer. Everything else is noise."  
> (source: Patrick Spychalski, https://www.linkedin.com/posts/patrickspychalski_clay-has-been-slowly-de-ranking-automated-activity-7265008719002845186-F4HZ, 01.10.2024)

Don't build complex Clay tables before validating your offer manually. Clay amplifies what's working — it cannot fix what isn't.

---

## 7. Multichannel: LinkedIn + Email

### 7.1 Why Multichannel

> "Channel fit matters. Email, LinkedIn, phone — go where your prospect is active. Multi-channel always outperforms single-channel."  
> (source: Jeremy Chatelaine, https://www.linkedin.com/in/jeremychatelaine/, 01.2024)

### 7.2 LinkedIn Outreach — The CCQ Method

**C — Compliment:** Reference something specific about their profile or recent post  
**C — Commonality:** Find a genuine shared connection, industry, or experience  
**Q — Question:** Ask one specific, non-salesy question that invites a response

**Example connection request:**
> "Noticed you recently posted about scaling outbound without adding headcount. We've been working through the same problem. Would love to connect and exchange notes."

(source: Jack Reamer, https://salesbread.com/linkedin-outreach-agency/, 01.2025)

### 7.3 Content-to-Outreach Signal

> "Content creates the signal. Outreach converts it."  
> (source: Jack Reamer, https://www.linkedin.com/in/jackreamer/, 01.2025)

Review who engages with your LinkedIn content and matches your ICP — then reach out first. Try:
> "Thanks for checking out the post. [Personal Note on their company/role]. Anything I can help with when it comes to [solving pain]?"

### 7.4 The SMYKM Multichannel Sequence

1. **Email 1** — Full SMYKM email with researched subject line and specific value prop
2. **LinkedIn DM** — Short, casual reference to the email. Not a pitch.
3. **LinkedIn comment** — Engage with their content to stay visible
4. **Email 2** — Follow up referencing something NEW from their LinkedIn or company news

(source: Samantha McKenna, https://www.linkedin.com/posts/samsalesli_samsales-samsales-activity-7322964999373545472-pG6f, 01.2025)

---

## 8. Measurement & Optimization

### 8.1 Metrics That Matter

| Metric | Healthy Range | Red Flag |
|--------|--------------|----------|
| Open rate | 27–45% | Below 20% = deliverability issue |
| Reply rate | 5–10% | Below 3% = list or copy problem |
| Bounce rate | Below 3% | Above 5% = list needs cleaning |
| **Positive reply rate** | **Track above all else** | Compare to deal value |

(source: Yurii Veremchuk, https://woodpecker.co/blog/, 01.2024)

> "How much is one positive reply actually worth to your business? That number changes everything about how you run outbound."  
> (source: Eric Nowoslawski, https://www.linkedin.com/in/outboundphd/, 01.2025)

### 8.2 When NOT to Optimize

> "If you've sent 1,000 cold emails and you're already changing your copy, swapping your lead list and rebuilding your infrastructure... slow down."  
> (source: Matthew Lucero, https://www.linkedin.com/in/matthew-lucero/, 01.2024)

1,000 emails is not enough data. Wait for at least 200–500 sends per variant before drawing conclusions.

### 8.3 A/B Testing Framework

- Send 100 emails with Offer A
- Send 100 emails with Offer B (same copy, different outcome/timeframe/objection)
- Whichever gets 2x positive replies in the first week — scale that one only

(source: Dr. Jay Feldman, https://www.linkedin.com/in/dr-jay-feldman/, 01.2024)

---

## 9. Where Experts Disagree

### 9.1 Deliverability: Still a Problem or Solved by AI?

**Jeremy Chatelaine** argues that deliverability in 2025 is largely solved due to AI and automated inbox switching — teams should shift focus to list quality and message.  
(source: Jeremy Chatelaine, https://quickmail.com/podcast, 01.2025)

**Eric Nowoslawski** argues that deliverability remains the #1 priority — daily monitoring, inbox rotation, and maintaining excess warm capacity are non-negotiable operational disciplines.  
(source: Eric Nowoslawski, https://www.linkedin.com/in/outboundphd/, 01.2025)

**My take:** I side with Eric. Deliverability being "easier" does not mean it is solved. For any team sending at scale, treat deliverability as an always-on operational concern. Jeremy's point may be valid for small-scale senders, but at volume the cost of being wrong is too high.

---

### 9.2 AI Personalization: Scale It or Be Careful?

**Eric Nowoslawski** advocates for aggressive AI personalization at scale — using Clay + GPT-4 to generate personalized first lines for 1.5M emails/month.  
(source: Eric Nowoslawski, https://lk.linkedin.com/posts/outboundphd_email-deliverability-tips-from-sending-700k-activity-7061325893499015168-N2SH, 08.05.2023)

**Samantha McKenna** argues that AI personalization fails at the enterprise level because senior buyers are blind to the same "research" every SDR does.  
(source: Samantha McKenna, https://www.linkedin.com/posts/samsalesli_smykm-samsales-activity-7131648145704284160-8Bo0, 18.11.2023)

**My take:** Both are right for different contexts. For high-volume SMB/mid-market outbound, AI personalization at scale is legitimate. For enterprise accounts where one deal is worth $50K+, human-crafted SMYKM is non-negotiable. Match personalization investment to deal economics.

---

### 9.3 Simple vs. Complex Clay Workflows

**Patrick Spychalski** argues the best Clay tables are simple — one trigger, one message, one offer. Complexity makes it harder to diagnose what's working.  
(source: Patrick Spychalski, https://www.linkedin.com/posts/patrickspychalski_clay-has-been-slowly-de-ranking-automated-activity-7265008719002845186-F4HZ, 01.10.2024)

**Alex Vacca (ColdIQ)** builds sophisticated multi-step Clay workflows with waterfall enrichment, ICP scoring, and do-not-contact filtering across 80+ clients.  
(source: Alex Vacca, https://www.linkedin.com/posts/alex-vacca_we-manage-80-b2b-clients-from-one-clay-table-activity-7416817754734891008-6UsQ, 13.01.2026)

**My take:** Spychalski is right for teams getting started. Vacca is right for agencies managing multiple clients at scale. Rule: start simple, add complexity only when you have a validated offer and a specific data gap that complexity solves.

---

## 10. What I Rejected and Why

### 10.1 Loom Video CTAs as a Default

Several practitioners mention Loom video CTAs as a way to stand out in cold email.

**Why I rejected it:** Matthew Lucero explicitly notes that "Loom CTAs will get you more positive replies — but they'll also convert to calls at a lower rate." (source: Matthew Lucero, https://www.linkedin.com/in/matthew-lucero/, 01.2024). For a B2B SaaS pipeline where the goal is booked meetings — not reply volume — optimizing for replies at the cost of call conversion is the wrong trade-off. The production overhead is also significant at volume.

### 10.2 High-Volume "Spray and Pray" as a Strategy

Common advice in low-quality cold email communities recommends sending 10,000+ emails per week as the primary growth lever.

**Why I rejected it:** Every practitioner in this research set explicitly warns against this. Eric Nowoslawski: "Volume ≠ strategy. Sending more won't fix a broken campaign. It just scales failure." (source: Eric Nowoslawski, https://www.linkedin.com/in/outboundphd/, 01.2025). High volume tanks deliverability and destroys reply rates — for everyone sending from those domains, including the legitimate campaigns.

---

## 11. My Original Ideas

### The "Inbound Signal Stack" for B2B SaaS

Every B2B SaaS product generates behavioral signals that most outbound teams ignore: free trial signups who didn't convert, users who hit a paywall, companies where one employee signed up but the account wasn't expanded, pricing page visitors who didn't book a demo.

**The idea:** Build a Clay table that pulls these inbound product signals and routes them into a warm outreach sequence — not cold email, but semi-warm outreach that references the specific product behavior.

Example:
> "Hi [Name] — noticed someone from [Company] tried [Feature X] last week but didn't complete the setup. Most teams hit a wall at that step because of [common blocker]. Happy to walk you through it in 10 minutes if that would be useful."

**Why it could work:** Reply rates on semi-warm emails referencing specific product behavior should be dramatically higher than cold outreach because the prospect has already demonstrated intent. None of the 10 experts I researched explicitly covers this pattern — they all treat outbound as separate from product. For B2B SaaS specifically, this gap is a real opportunity. The same infrastructure (Clay, Smartlead, domain setup) applies — only the signal source changes.

---

## 12. Weaknesses of This Playbook

**1. The research base skews toward agencies and educators, not in-house SaaS operators.**
Most experts (ColdIQ, SalesBread, Anevo, Dr. Jay Feldman) are agencies running outbound for clients or educators teaching it. The perspective of an in-house B2B SaaS growth team — with product access, customer data, and longer sales cycles — is underrepresented.

**2. The Clay-heavy approach assumes a technical operator.**
Several sections assume comfort with Clay, webhooks, Make/n8n, and Claygent. For non-technical founders or small teams without a GTM engineer, this playbook will feel inaccessible.

**3. The personalization frameworks assume LinkedIn-active prospects.**
SMYKM and CCQ depend on the prospect having visible LinkedIn activity. For industries where decision-makers are not on LinkedIn (manufacturing, construction, some healthcare), these frameworks fail.

**4. Benchmarks may be outdated.**
Reply rate and open rate benchmarks cited from Woodpecker and SalesBread are based on historical data. Gmail and Outlook filtering continues to evolve rapidly.

**5. The "Inbound Signal Stack" in Section 11 is untested.**
This is a logical hypothesis, not a proven playbook component. It should be treated as such.

---

## 13. Who I Would NOT Recommend Following and Why

### Dr. Jay Feldman

I included Dr. Jay Feldman in this research set because his content on cold email infrastructure is tactically solid and his claimed experience (15M+ revenue from cold email) is compelling. However, I would not recommend him as a primary source for three reasons:

**1. Verification is difficult.**
Unlike Jeremy Chatelaine (who built QuickMail, a verifiable product), Alex Vacca (whose ColdIQ has documented client case studies), or Eric Nowoslawski (who shows real campaign dashboards), Dr. Jay Feldman's claims are self-reported without third-party corroboration.

**2. The content is formulaic, not deep.**
His posts follow a repeatable structure (numbered list → hook → CTA) that performs well on LinkedIn but rarely goes beyond surface-level advice. Compare his "4-step cold email machine" to Eric Nowoslawski's multi-step Clay workflows or Patrick Spychalski's nuanced Clay critique — the depth gap is significant.

**3. His identity was difficult to verify during research.**
During this research process, I initially confused him with Jay Feldman (a real estate agent) and Jay Feldman (Co-Founder of Otter PR). This confusion itself is a signal: his personal brand is not well-established enough in the cold outreach practitioner community for a researcher to immediately identify him. The practitioners who genuinely shape this space (Chatelaine, Nowoslawski, Vacca) are unambiguous.

**Recommendation:** Use his content as a useful checklist and starting point for infrastructure setup, but validate every recommendation against the deeper work of Nowoslawski, Vacca, or Chatelaine before applying it to a real campaign.

---

*Playbook compiled by Muwalliha | April 2026*  
*Sources: [research/sources.md](./research/sources.md)*  
*LinkedIn posts: [research/linkedin-posts/](./research/linkedin-posts/)*

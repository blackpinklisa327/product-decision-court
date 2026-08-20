# Product Decision Court

Put a consequential product decision on trial.

Product Decision Court is an **Agent Skill for ChatGPT Work and Codex**. It builds the strongest case for and against a product bet, resolves conflicting advice based on the conditions of the case, and issues one ruling: **build, test, defer, reject, scale, or stop**.

It is designed for decisions such as:

- Should we build a major customer's custom request?
- Should we invest in acquisition or repair retention?
- Is an AI copilot ready to become an autopilot?
- Should we launch now or delay for quality?
- Should we follow a competitor or differentiate?
- Should we scale a bet or stop investing?

## Install in ChatGPT

GitHub does not currently provide an **Add to ChatGPT** button for standalone skills. Install the skill by uploading it to a ChatGPT Work conversation:

1. On this GitHub page, select **Code**, then **Download ZIP**.
2. Open a new **ChatGPT Work** conversation.
3. Attach the downloaded ZIP.
4. Enter:

   ```text
   Install Product Decision Court as a skill.
   ```

5. After ChatGPT confirms installation, open a new conversation if needed and invoke:

   ```text
   @Product Decision Court
   ```

You can also describe the decision normally. ChatGPT can select the skill automatically when the request matches it.

> **Important:** This repository is the standalone skill source. It is not a plugin, so it will not appear in the public Plugins directory and GitHub cannot install it into ChatGPT with one click.

## Install in Codex

Ask Codex to install the skill directly from this repository:

```text
$skill-installer install the skill from:
https://github.com/blackpinklisa327/product-decision-court
```

Then invoke it with:

```text
$product-decision-court
```

## Install in Claude Code

For a project-scoped Claude Code installation, copy or clone this repository into:

```text
.claude/skills/product-decision-court/
```

Then invoke it with:

```text
/product-decision-court
```

## What makes it different

A generic AI answer often gives reasonable pros and cons without making the call. Product Decision Court requires:

1. The real decision and the load-bearing assumption
2. A credible prosecution and defense
3. The conditions under which conflicting advice is right
4. One structurally different 10x alternative
5. A ruling with scope and timing
6. The cheapest decisive test
7. The evidence that would reverse the ruling

## Evidence library

The repository contains two evidence tiers:

- **20 audited precedents** with a principle, causal mechanism, landmine, tradeoff, and source attribution
- **285 provisional evidence clusters** used to discover additional perspectives and disagreements

Provisional clusters are not presented as consensus or attributed as synthesized claims. The raw podcast transcripts are intentionally not included.

## Try it

Ask:

> Use Product Decision Court. Should we spend six weeks building this enterprise customer's custom request?

You can also invoke it for a specific decision type:

> Put our plan to promote this AI copilot to autopilot through Product Decision Court. Default to medium length.

## Retrieve precedents directly

```bash
python3 scripts/retrieve_precedents.py \
  --query "custom enterprise customer request distracts roadmap" \
  --limit 8
```

## Repository structure

```text
SKILL.md
agents/openai.yaml
scripts/retrieve_precedents.py
references/audited_precedents.csv
references/provisional_clusters.csv
references/evidence-policy.md
```

## Current maturity

This is a usable first release, not a finished claim that all 305 records are equally trustworthy. The 20 audited precedents can support direct reasoning and careful attribution. The 285 provisional clusters broaden discovery but still require further synthesis and auditing before becoming canonical judgment cards.

## Source note

The decision patterns were derived from a public archive of Lenny's Podcast transcripts. Product Decision Court does not reproduce or redistribute the transcript archive, and the podcast is an evidence source rather than the product's public identity.

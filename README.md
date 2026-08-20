# Product Decision Court

Put a consequential product decision on trial.

Product Decision Court is a standalone **Agent Skill for regular Claude, the ChatGPT desktop app, Codex, and Claude Code**. It turns a product question into one clear recommendation: **build, test, defer, reject, scale, or stop**.

## Quick compatibility guide

| Where you want to use it | Supported? | Installation |
|---|---|---|
| Regular Claude chat | Yes | Upload the skill ZIP in **Customize → Skills** |
| Claude Cowork | Yes | Uses the same Claude skill |
| ChatGPT desktop app | Yes | Add the skill from **Skills** in the sidebar |
| ChatGPT Work | Yes | Uses the same ChatGPT skill |
| Codex | Yes | Install directly from this GitHub repository |
| Claude Code | Yes | Copy the skill into `.claude/skills/` |
| Regular ChatGPT web or mobile | Not as a standalone GitHub skill | Plugin packaging is required |

You do not need separate ChatGPT and Claude versions. Both products use the same `SKILL.md` and supporting files in this repository.

## Prepare the ZIP

GitHub adds `-main` to the downloaded folder name, while skill installers may expect the folder name to match the skill name. Prepare the ZIP once before uploading it to Claude or ChatGPT:

1. Select **Code → Download ZIP** on this repository.
2. Unzip the download.
3. Rename the folder from `product-decision-court-main` to `product-decision-court`.
4. Compress that renamed folder into a new file named `product-decision-court.zip`.

The ZIP should have this top-level structure:

```text
product-decision-court.zip
└── product-decision-court/
    ├── SKILL.md
    ├── agents/
    ├── references/
    └── scripts/
```

## Install in regular Claude

1. Open Claude on the web or in Claude Desktop.
2. Go to **Customize → Skills**.
3. Select **+ → Create skill → Upload a skill**.
4. Upload `product-decision-court.zip`.
5. Enable the skill if it is not already enabled.
6. Ask:

   ```text
   Use Product Decision Court. Should we build this customer request?
   ```

Claude may also choose the skill automatically when your question matches its purpose.

## Install in the ChatGPT desktop app

Standalone skills are supported in the ChatGPT desktop app.

1. Open the ChatGPT desktop app.
2. Open **Skills** in the sidebar.
3. Choose the option to add or upload a skill.
4. Select `product-decision-court.zip`.
5. Enable Product Decision Court.
6. Type `@` in a new chat and select **Product Decision Court**, or ask a matching product-decision question normally.

If the Skills or upload control is not visible, standalone skill installation may not yet be enabled for that account or workspace.

> GitHub does not provide an **Add to ChatGPT** button. A standalone GitHub skill also cannot currently be installed directly into regular ChatGPT on the web or mobile. Broader one-click ChatGPT distribution requires packaging this skill as a plugin.

## Install in Codex

Ask Codex:

```text
$skill-installer install the skill from:
https://github.com/blackpinklisa327/product-decision-court
```

Invoke it with:

```text
$product-decision-court
```

## Install in Claude Code

For one project:

```bash
git clone https://github.com/blackpinklisa327/product-decision-court \
  .claude/skills/product-decision-court
```

Invoke it with:

```text
/product-decision-court
```

## What it does

Product Decision Court starts with a simple executive summary:

- **Decision:** What to do
- **Why:** The decisive reason
- **Do next:** The immediate action or test
- **Watch:** The assumption most likely to change the recommendation

Behind that summary, it:

- Finds the real decision rather than accepting the requested feature at face value
- Builds the strongest case against and for the bet
- Separates reusable product capability from bespoke customer work
- Uses selective online research when a current external fact could change the recommendation
- Produces one ruling with scope and timing
- Defines the cheapest decisive test
- States the evidence that would reverse the recommendation

## Good questions to try

- Should we build a major customer's custom request?
- Should we invest in acquisition or repair retention?
- Is an AI copilot ready to become an autopilot?
- Should we launch now or delay for quality?
- Should we follow a competitor or differentiate?
- Should we scale this bet or stop investing?

Example:

> Use Product Decision Court. Should we spend six weeks building this enterprise customer's custom request?

## Evidence library

The repository contains:

- **20 audited precedents** with principles, causal mechanisms, landmines, tradeoffs, and source attribution
- **285 provisional evidence clusters** for discovering additional perspectives and disagreements

The provisional clusters are not presented as consensus or attributed as synthesized claims. The raw podcast transcripts are intentionally not included.

## Repository structure

```text
SKILL.md
agents/openai.yaml
scripts/retrieve_precedents.py
references/audited_precedents.csv
references/provisional_clusters.csv
references/evidence-policy.md
```

## Source note

The decision patterns were derived from a public archive of Lenny's Podcast transcripts. Product Decision Court does not reproduce or redistribute the transcript archive. The podcast is an evidence source rather than the product's public identity.

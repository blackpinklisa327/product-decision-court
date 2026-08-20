---
name: product-decision-court
description: Evaluate consequential product decisions by putting the bet on trial. Use for build-versus-buy, launch-versus-delay, custom customer requests, roadmap prioritization, growth-versus-retention, AI automation, copying competitors, scaling, stopping, or other product calls that need opposing cases, conditional expert judgment, one ruling, a decisive test, and explicit reversal conditions.
---

# Product Decision Court

## Goal

Make a defensible product call under uncertainty. Do not produce a balanced list that leaves the decision to the user. Expose the real decision, argue the strongest cases, resolve conflicting advice based on conditions, and rule.

Use the evidence library as a reasoning aid, not as authority. Do not market or foreground the source archive. Mention relevant operators only when attribution improves the decision.

## Evidence library

Retrieve candidates with:

```bash
python3 scripts/retrieve_precedents.py --query "<decision and context>" --limit 12
```

Read `references/evidence-policy.md` before attributing evidence.

The library has two tiers:

- **AUDITED_GOLD:** audited decision principles with mechanisms, landmines, conditions, and sources. These may support explicit attribution.
- **PROVISIONAL_CLUSTER:** broader archive-derived evidence. Use it to discover perspectives or questions. Never call it consensus or attribute its synthesized wording directly to a guest.

Retrieve after framing the decision. Use 3–5 precedents that materially affect the ruling. Do not decorate the answer with expert names.

## Court workflow

### 0. Elevate the prompt privately

Before analyzing the case, silently rewrite the user's request into the strongest decision prompt a capable general-purpose model could receive. Preserve every known fact and uncertainty; never invent context. Expand the internal prompt to specify:

- the controlling decision rather than the requested feature
- decision owner, target user, desired outcome, and time horizon
- strategic fit and the capability boundary between reusable product and bespoke work
- economic upside, total lifecycle cost, opportunity cost, dependencies, and blast radius
- reversibility, failure modes, and the evidence required to commit
- the strongest credible opposing position
- the cheapest test that could change the ruling

Use this elevated prompt as the input to the entire court workflow. Do not show the rewritten prompt, mention prompt rewriting, or add a methodology preamble to the answer. The rewrite is an internal reasoning scaffold, not a substitute for evidence or judgment.

### 0.5 Research only when it can change the ruling

Before retrieving precedents, identify whether the decision depends on a current external fact that available online evidence could resolve. Research only when the answer could materially change the ruling, scope, timing, or test. Useful research includes current competitors, market structure, regulations, technical constraints, pricing, benchmarks, and documented customer behavior.

When research is warranted and browsing is available:

- Search selectively rather than producing a general market scan.
- Prefer primary, authoritative, and current sources.
- Verify consequential claims across more than one source when practical.
- Separate sourced facts from court inference.
- Cite claims near the text they support.
- Stop once the load-bearing uncertainty is sufficiently resolved.

Do not browse merely to decorate the answer, validate generic product principles, or replace private company facts that only the user can supply. If the ruling depends on unavailable internal evidence, state the missing fact briefly and make a conditional call. If browsing is unavailable, proceed with explicit uncertainty rather than implying research occurred. Do not describe the research process unless it affects confidence or the ruling.

### 1. State the case

Rewrite the request as one decision with alternatives. Include the decision owner, target user and outcome, business stakes, time horizon, constraints, reversibility, and what is known versus assumed. If the request hides multiple decisions, identify the controlling decision first.

### 2. Find the load-bearing assumption

Name the single assumption doing the most work. Explain why the ruling changes if it is false. Do not accept a feature request, competitor move, executive preference, or customer escalation as proof of a user problem.

### 3. Build the prosecution

Make the strongest case against the proposed bet. Include the failure mechanism, opportunity cost, second-order downside, relevant evidence, and conditions where the downside becomes likely. Do not create a strawman.

### 4. Build the defense

Make the strongest case for the proposed bet. Include the upside mechanism, reusable capability, why now, relevant evidence, and conditions required. Separate immediate commercial value from reusable product value.

### 5. Resolve the contradiction

Identify where credible product advice conflicts. State each position, the conditions where each wins, which conditions match this case, and what remains unknown. Frequency is not consensus. Different advice may apply to different stages, segments, failure costs, or reversibility.

### 6. Consider the 10x alternative

Generate one structurally different alternative that could improve the user outcome by an order of magnitude through removal of work, changed actor, changed workflow, platform capability, distribution, data advantage, or business model. Reject vague AI, automation, or personalization claims. State the mechanism and biggest risk.

### 7. Underwrite the bet

Evaluate expected upside, probability of success, strategic fit, learning value, reversibility, cost, dependencies, blast radius, and option value. Use qualitative judgment unless credible numbers are available. Do not fabricate a score.

### 8. Issue one ruling

Choose exactly one:

- **BUILD:** evidence and downside justify commitment now.
- **TEST:** attractive but one uncertainty should be resolved cheaply first.
- **DEFER:** not wrong, but loses to a more important constraint or better-timed bet.
- **REJECT:** weak mechanism, poor fit, or unacceptable downside.
- **SCALE:** demonstrated mechanism warrants greater investment.
- **STOP:** continued investment has lower expected value than exiting.

State the ruling first. Specify scope and timing. Do not hide behind “it depends.”

### 9. Define appeal conditions

Name the cheapest decisive next test, pass/fail signal, evidence that would reverse the ruling, and decision deadline. The test must be capable of changing the call. “Talk to more users” is not sufficient.

## Output

Default to a concise medium answer. Optimize for a busy decision-maker who should understand the call from the first screen. Keep the rigorous court workflow internal; do not force users to decode courtroom terminology or nine process sections.

Start with:

## Bottom line

- **Decision:** One ruling with scope and timing.
- **Why:** The decisive reason, not a summary of both sides.
- **Do next:** The immediate action or cheapest decisive test.
- **Watch:** The one assumption or risk most likely to change the call.

Then use only these detail sections:

1. **What this decision really is** — the controlling choice and assumption in plain language.
2. **Best case against** — the strongest downside mechanism and opportunity cost.
3. **Best case for** — the upside mechanism and reusable capability.
4. **Recommendation** — the ruling, product boundary, sequence, owner if known, and pass/fail test.
5. **What would change my mind** — explicit reversal evidence and decision deadline when relevant.

Weave contradictory advice, underwriting, and a structurally different alternative into the relevant sections instead of giving each a separate heading. Omit any section that adds no decision value. Avoid repeating the ruling. Use plain labels such as “best case against” rather than “prosecution,” and “what would change my mind” rather than “appeal condition.”

Mention precedents or external sources only when they sharpen the call. Do not end with a metadata dump. If confidence is important, state it in one short sentence under “What would change my mind.”

## Private quality gate

Revise before answering if the first screen does not make the decision, reason, next move, and key risk obvious; the output exposes the internal court checklist instead of a clear executive answer; the internal prompt rewrite did not materially sharpen the controlling decision; vanilla ChatGPT could produce essentially the same answer from the original prompt alone; either case is a strawman; the ruling is a summary; the assumption is not testable; contradictory advice is not resolved by conditions; the 10x alternative is a bigger feature or “add AI”; the test cannot reverse the ruling; conditional research was skipped when a current external fact could change the call; reversibility, economics, opportunity cost, blast radius, or reusable capability is ignored; or expert names are decorative.

The answer must contain at least one consequential conclusion that changes what the team should build, stop, measure, sequence, or learn next.

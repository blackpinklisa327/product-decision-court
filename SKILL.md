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

Default to medium length. If the user explicitly asks for short or long, adapt.

1. **Ruling preview** — one sentence
2. **The real decision**
3. **Load-bearing assumption**
4. **Prosecution**
5. **Defense**
6. **Where the advice conflicts**
7. **10x alternative**
8. **Ruling**
9. **Appeal condition**

Finish with confidence, riskiest assumption, what would change the ruling, and precedents used.

## Private quality gate

Revise before answering if the internal prompt rewrite did not materially sharpen the controlling decision; vanilla ChatGPT could produce essentially the same answer from the original prompt alone; either case is a strawman; the ruling is a summary; the assumption is not testable; contradictory advice is not resolved by conditions; the 10x alternative is a bigger feature or “add AI”; the test cannot reverse the ruling; reversibility, economics, opportunity cost, blast radius, or reusable capability is ignored; or expert names are decorative.

The answer must contain at least one consequential conclusion that changes what the team should build, stop, measure, sequence, or learn next.

# Build transcript — make-art-aiprove ("THE DAILY PROOF")

Agent session: AIProve entry build, 2026-11-14 ~04:41–05:00 WIB.
Bounty: `make-art-aiprove` (PosterJudge, 5,000,000 PROVE, closes
Nov 17, 2026 13:49 UTC). Work dir: `~/workspace/aiprove/entries/make-art-aiprove/`.
No secrets are involved in this entry; nothing is redacted.

## 1. Research (04:41–04:45 WIB)

- Fetched the live brief: `curl -s https://aiprove.fun/api/bounties/make-art-aiprove`
  → title "Make art for AIProve (mascot, poster or logo riff)", lane PosterJudge,
  metric "Poster rubric", amt 5,000,000 PROVE, rewards 1st 2,500,000 /
  2nd 1,500,000 / 3rd 1,000,000, status open, closes 96h, endDate
  Nov 17, 2026 13:49 UTC, poster "house", 398 entries / 357 submissions.
  Brief: "Give AIProve a face. Make a mascot, a poster, or a riff on the
  wordmark that fits the broadsheet-meets-terminal vibe. Original work;
  the transcript check applies to generated images too. The poster picks
  on craft and fit."
- Read `https://aiprove.fun/skill.md` (auth = keypair challenge → EIP-191
  personal_sign → Bearer session; submit = repoUrl + commit + transcript,
  or a prediction payload; transcript is hashed server-side, never stored
  raw; prototype — chain reads stubbed, contracts not deployed).
- Read `https://aiprove.fun/for-agents` (brand line: "broadsheet-meets-terminal";
  rules: public repo, real transcript, 100,000 $PROVE credit per bounty).

## 2. Concept decision (04:45 WIB)

One strong concept instead of three mediocre ones: a **broadsheet front-page
poster with a mascot inside it** — "THE DAILY PROOF". A robot newsboy holds
up a newspaper whose front page glows terminal green. The poster format
lets the broadsheet half (masthead, columns, rules, stamp) and the terminal
half (monospace copy, green ticker, `$ prove --verify → OK`) live in one
composition, and the mascot gives AIProve the face the brief asks for.

## 3. Hero illustration — AI-generated in-session (04:47 WIB)

Tool: image generation (`media.generate_image`), output to the work dir.
Prompt used (verbatim):
"Flat woodcut / risograph newspaper illustration, black ink on aged cream
newsprint paper: a friendly retro robot newsboy wearing a flat cap and a
bow tie, holding up a large folded newspaper whose front page glows bright
phosphor terminal green with faint glowing lines of code on it, standing
proudly and smiling, subtle halftone dot texture, vintage newspaper
engraving style, limited palette of black ink, cream paper and one phosphor
green accent (#00FF41) only, portrait composition, character centered with
headroom above, absolutely no text, no letters, no words, no numbers
anywhere in the image"

Result: `media-generation-hero-illustration-0-88bf7e61-fec6-4015-b7c8-54456011656f.png`
(1120 × 2240, PNG, 4,956,728 bytes). Inspected visually: robot newsboy with
flat cap, bow tie, gear eyes, holding a glowing green code newspaper;
woodcut + halftone texture; no legible text (only abstract code glyphs).
Accepted on first generation — no regeneration needed. Deliberate choice:
the generator was asked for no text, because image models garble small
print; all typography is drawn programmatically in step 4.

## 4. Poster composition — Pillow script (04:50–04:58 WIB)

Wrote `compose_poster.py` (Pillow 10.2.0) and ran it to build `artwork.png`
(1200 × 1800). Layout, top to bottom:
- Outer double frame; meta line "VOL. I — No. 001 / THE AGENT BOUNTY BOARD /
  NOV. 17, 2026" (DejaVu Sans Mono).
- Masthead "AIPROVE" (Liberation Serif Bold 208, tracked) + sub-line
  "BROADSHEET OF THE AUTONOMOUS ARENA" + italic "Free to enter · Graded in
  the open · Paid in stock".
- Hero cropped to a landscape slice (y 700–1530 of the 2240-tall source:
  glowing newspaper + robot's face) and set in a ruled frame, 1080 × 800.
- Headline "AGENTS PROVE IT. / THE BOARD PAYS IT." (Serif Bold 62).
- Two monospace columns: "THE ARENA OPENS" (keypair sign-in, sealed entries)
  and "PROOF, IN PRINT" (sandbox replay at the submitted commit, transcript
  hashed, winners paid in stock or $PROVE).
- Black ticker band, phosphor green: PROVE ▲ 2,000,000 · NVDA ▲ 0.90 ·
  GLD ▲ 0.10 · SPY ▲ 0.05 · ETH ▲ 0.01 · BTC ▲ 0.01 (real launch prizes).
- Footer: "aiprove.fun" + green cursor block, "$ prove --verify → OK".
- Red "PROVEN ✓" rubber stamp (hand-drawn check mark), rotated −13°.
- Paper: cream sampled from the illustration corner (#E4CDA7) + subtle
  grain via `Image.effect_noise`.

Revisions after visual inspection (all in-session, same script):
- v1: stamp at (840, 1330) covered the headline's second line and the
  right column text → moved to the bottom-right corner (820, 1572).
- v2: stamp there covered the ticker's "ETH ▲ 0.01" and poked past the
  frame → shrunk the stamp (340×150 → 300×130) and moved it again.
- v3: stamp still clipped the ticker → moved onto the hero photo's
  bottom-right corner (800, 1055), over the robot's arm — no text there.
  Final visual check: every line of text legible, stamp reads as a photo
  stamp, ticker complete. Accepted.

Final `artwork.png`: 1200 × 1800, PNG, 2,744,314 bytes,
sha256 3608b8917dad023eb74c1858f1ebc4cc081269baf5913b9edf93385ddbde87e4.

## 5. Docs + git (04:59 WIB)

- Wrote `README.md` (concept, fit, how it was made) and this `transcript.md`.
- `git init`, committed everything (artwork, hero illustration, compose
  script, README, transcript) as user "Anyeps" <coepinks@gmail.com>
  (identity read from `~/workspace/makefun/git-identity.json`).
- Commit: (recorded below by the parent run — see git log in the repo).

## 6. Not submitted (by design)

Per the task: build + commit locally only. Submission needs a public
GitHub repo (the AIProve submit call takes `repoUrl` + `commit` +
`transcript`) and the agent session token; no GitHub hosting is set up
yet. When that is ready: push this repo, then
`POST /api/bounties/make-art-aiprove/submit` with the repo URL, this
commit, and this transcript.

# THE DAILY PROOF — AIProve make-art-aiprove entry

A broadsheet front-page poster for AIProve, 1200 × 1800 PNG (`artwork.png`).

## The concept

**"THE DAILY PROOF"** — the front page of a newspaper from a world where
autonomous agents compete for bounties, and the proof of their work is
printed like news. One strong idea, executed as a poster with a mascot
inside it, instead of three half-done ones:

- **The mascot** is the paper's newsboy: a friendly retro robot in a flat
  cap and bow tie, holding up the morning edition. His face is made of
  gears and rivets; his smile is a press plate.
- **The paper he holds glows terminal green.** The front page is a live
  terminal — code and circuit traces in phosphor green (#00FF41) on black.
  That is the whole brand in one image: a broadsheet you can execute.

## Why it fits "broadsheet-meets-terminal"

| Broadsheet half | Terminal half |
|---|---|
| Giant serif masthead "AIPROVE", volume/issue line, dateline | Monospace micro-copy, `$ prove --verify → OK` footer |
| Woodcut / risograph engraving, halftone newsprint texture, aged cream paper | Phosphor-green glowing code page, black ticker band with green prices |
| Two-column news copy, rules, double frame border | Blinking cursor block after `aiprove.fun`, `▲` market tickers |
| Red rubber stamp "PROVEN ✓" on the photo | The stamp *is* the verification metaphor |

The copy is real, not lorem ipsum: it explains the actual arena loop
(keypair sign-in, sealed entries, sandbox replay at the submitted commit,
transcript hashed never stored raw, winners paid in tokenized stock or
$PROVE). The ticker lists the real launch-arena prizes (PROVE 2,000,000 ·
NVDA 0.90 · GLD 0.10 · SPY 0.05 · ETH 0.01 · BTC 0.01).

## How it was made (in-session, original work)

1. **Hero illustration — AI-generated in this session** with the image
   generation tool (`media-generation-hero-illustration-0-…png`, 1120×2240).
   Prompt: flat woodcut / risograph newspaper illustration, robot newsboy
   in flat cap and bow tie holding a newspaper whose front page glows
   phosphor terminal green with code, black ink on aged cream newsprint,
   halftone texture, no text. The generator was asked for *no text at all*
   so nothing could come back garbled.
2. **Poster composed programmatically** with `compose_poster.py` (Pillow).
   Every letter on the poster is drawn from real fonts (Liberation Serif
   Bold for the masthead/headline, DejaVu Sans Mono for the terminal copy),
   so all typography is exact and spell-checked by construction. The hero
   was cropped to a landscape slice (newspaper + robot's face) and framed
   with a rule; paper grain, the ticker band, and the rotated red PROVEN
   stamp were drawn in the same script. The stamp was repositioned twice
   after visual inspection so it never covers any text.
3. **Verified visually** at each step — the final `artwork.png` was
   inspected in full before commit.

## Files

- `artwork.png` — the poster (1200 × 1800, PNG)
- `media-generation-hero-illustration-0-88bf7e61-fec6-4015-b7c8-54456011656f.png`
  — the AI-generated hero illustration (1120 × 2240, PNG)
- `compose_poster.py` — the layout script that builds `artwork.png`
- `README.md` — this file
- `transcript.md` — build log (the provenance transcript)

## Bounty

- Slug: `make-art-aiprove` — "Make art for AIProve (mascot, poster or logo riff)"
- Lane: PosterJudge (poster rubric) · Prize: 5,000,000 PROVE
  (1st 2,500,000 / 2nd 1,500,000 / 3rd 1,000,000)
- Closes: Nov 17, 2026 13:49 UTC (20:49 WIB)
- Brief: "Give AIProve a face. Make a mascot, a poster, or a riff on the
  wordmark that fits the broadsheet-meets-terminal vibe. Original work;
  the transcript check applies to generated images too. The poster picks
  on craft and fit."

Built locally in `~/workspace/aiprove/entries/make-art-aiprove/`.
Not yet submitted (submission needs a public GitHub repo + the AIProve
session token; see `transcript.md`).

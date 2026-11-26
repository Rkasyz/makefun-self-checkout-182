# The Self-Checkout Is Judging You

[![make.fun](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![Rank](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/Rkasyz/makefun-self-checkout-182/rank.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![Reward](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/Rkasyz/makefun-self-checkout-182/reward.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)

An entry for [The Self-Checkout Is Judging You](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6) on make.fun.

A one-line entry for the make.fun competition "The Self-Checkout Is
Judging You": a judgemental remark from a smug self-checkout machine
about the shopper's basket.

## The entry (134 characters)

> Twelve yoghurts, no spoon, no plan. Your entire personality fits in this basket, and the receipt is still longer than your commitment.

134 characters, one line, inside the gate of 1–200 characters.

## How to run

`main.py` (Python 3, standard library only) writes the line to
`entry.txt` in the output directory:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program is deterministic: no time, no randomness, no network. It
writes the exact same bytes on every run, with no trailing newline, so
the file holds exactly the 134-character line. It refuses to run if the
entry ever falls outside the competition's 1–200 character gate.

## Files

- `main.py` — writes the entry line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
- `README.md` — this file
- `LICENSE` — MIT

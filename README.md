# Worst Fix Ever: Funniest Commit Message

[![Make.fun](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![Rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/aldy007x/worst-fix/rank.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![Reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/aldy007x/worst-fix/reward.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

Entry for the [Worst Fix Ever: Funniest Commit Message](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722) on make.fun — a single commit message for a bug fix that made everything worse, judged pairwise by an AI comedy writer.

## The entry

> fix: speed up login by skipping the password check; login now instant, and optional

83 characters — inside the contest's 100-character cap.

## How it works

`main.py` (Python stdlib only, no network, deterministic) writes the commit message to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `./output/`) and self-checks the contest gate before exiting: the entry must be UTF-8 text of 1 to 100 characters and not only whitespace.

```sh
python3 main.py
cat output/entry.txt
```

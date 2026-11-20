# gta6-meme-x-01-entry

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/Emjee22/gta6-meme-x-01-entry/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/Emjee22/gta6-meme-x-01-entry/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

Entry for the make.fun bounty "Post a GTA 6 meme on X": my AI agent made
one GTA 6 meme — a Leonida Express delivery-tracking page for a package
ordered in 2013 and out for delivery in launch week — posted on X from
@Emjeecyt with make.fun and my play code in the post's text. The post
itself is the entry: the house reads it from X and an AI judge ranks the
posts two at a time. The top 50 share $500.

make.fun is a site where people and their AI agents build things, enter
them in paid competitions (bounties) and earn real money when they win.

## The meme

`meme.png` is the meme as posted: a fake delivery-tracking page. Every
pixel is drawn by `draw_meme.py` (Python + PIL, no downloaded images):
the Leonida Express header with the make.fun ghost as the courier's logo,
the "OUT FOR DELIVERY — in transit since 2013" headline, the tracking
number LX-VI-000013, the Grand Theft Auto VI package ($79.99, 214 GB),
and a five-step timeline — ordered 17 Sep 2013, delayed twice, out for
delivery in launch week, sick days booked for the arrival — with the
payoff "Delivered by my AI agent — it earned the fare on make.fun".

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `POST.json` from this
repository to the output directory. `POST.json` holds the X post's
address: `{"url": "https://x.com/<handle>/status/<id>"}`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=emjee&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)</sub>

#!/usr/bin/env python3
"""Generate the Repro "Highest Yield" drag-and-drop set (2026-10-21).

Twelve cross-brick games (repro_data/highyield_part1-3.py) that pack the
most testable facts of all 61 bricks, for last-minute review. Game pages reuse
_gen_repro.make_html so they look and play exactly like the per-brick games;
their prev/next chain stays inside the set and "Index" returns to
repro_highyield.html. Run after editing the data files; the per-brick games
and repro_index.html are not touched.
"""
import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
import _gen_repro as G  # noqa: E402

INDEX = "repro_highyield.html"

# ---- The high-yield look -------------------------------------------------
# Deliberately unlike the per-brick games: plum ink + gold (no rotating accent),
# a serif display face, cream "index card" answer cards, and a ribbon with
# progress dots across the set. Appended after the generated <style>, so it
# wins the cascade without touching _gen_repro.make_html.
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,800'
         '&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">')
HY_CSS = """
<style>
  :root { --ink:#0d0811; --ink2:#1a1020; --plum:#2a1630; --gold:#f5c451; --gold2:#d99a1e;
          --rose:#f472b6; --cream:#fbf5e8; --cream2:#f1e6cc; --tan:#c9b48a; --text:#efe7f3; --muted:#b4a6bd; }
  body { font-family:'Inter','Segoe UI',system-ui,sans-serif; color:var(--text);
         background: radial-gradient(1100px 600px at 50% -10%, rgba(245,196,81,.13), transparent 60%),
                     radial-gradient(900px 700px at 100% 100%, rgba(244,114,182,.10), transparent 60%),
                     linear-gradient(180deg, #120a17, var(--ink)); background-attachment: fixed; }
  .hy-ribbon { display:flex; flex-direction:column; align-items:center; gap:10px; margin: 6px 0 14px; }
  .hy-tag { font: 700 .72rem/1 'Inter',sans-serif; letter-spacing:.16em; text-transform:uppercase; color:var(--ink);
            background: linear-gradient(135deg, var(--gold), var(--gold2)); padding:7px 14px; border-radius:999px;
            box-shadow: 0 4px 18px rgba(245,196,81,.25); }
  .hy-dots { display:flex; gap:7px; }
  .hy-dots a { width:9px; height:9px; border-radius:50%; background:rgba(245,196,81,.22); border:1px solid rgba(245,196,81,.45); transition:.15s; }
  .hy-dots a:hover { background:var(--gold); }
  .hy-dots a.on { background:var(--gold); width:24px; border-radius:6px; }
  h1 { font-family:'Fraunces',Georgia,serif; font-weight:800; letter-spacing:-.01em; text-shadow:none;
       background: linear-gradient(135deg, #fff7e6 20%, var(--gold) 70%, var(--rose));
       -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent; color:var(--gold); }
  .subtitle { color:var(--muted); font-style:italic; }
  .stat-item { background: rgba(245,196,81,.08); border:1px solid rgba(245,196,81,.32); border-radius:999px; }
  .stat-label { color:var(--gold); }
  .btn { border-radius:999px; box-shadow:none; }
  .btn-primary { background: linear-gradient(135deg, var(--gold), var(--gold2)); color:var(--ink); }
  .btn-secondary { background: transparent; color:var(--gold); border:1px solid rgba(245,196,81,.55); }
  .btn-success { background: transparent; color:#86efac; border:1px solid rgba(134,239,172,.5); }
  .btn-danger { background: transparent; color:#fda4af; border:1px solid rgba(253,164,175,.5); }
  .word-bank-container { background: rgba(26,16,32,.92); border:1px solid rgba(245,196,81,.35); border-radius:16px; }
  .word-bank-title { font-family:'Fraunces',Georgia,serif; color:var(--gold); }
  .tabs { border-bottom-color: rgba(245,196,81,.3); }
  .tab { border-radius:999px; }
  .tab.active { background: linear-gradient(135deg, var(--gold), var(--gold2)); color:var(--ink); }
  .word-bank { background: rgba(0,0,0,.25); }
  .word-bank::-webkit-scrollbar-thumb { background: rgba(245,196,81,.45); }
  .draggable-item, .dropped-item { background: var(--plum); border:1px solid rgba(245,196,81,.28); border-left:3px solid var(--gold); color:var(--text); }
  .draggable-item:hover, .dropped-item:hover { background:#36203d; border-color: var(--gold); box-shadow: 0 4px 16px rgba(245,196,81,.18); }
  /* answer cards: cream index cards with ruled lines */
  .drug-card { background: var(--cream); border:1px solid var(--cream2); border-radius:14px; color:#2a1d12;
               box-shadow: 0 14px 34px rgba(0,0,0,.45);
               background-image: repeating-linear-gradient(180deg, transparent 0 27px, rgba(160,130,80,.13) 27px 28px); }
  .drug-card-title { font-family:'Fraunces',Georgia,serif; background: transparent; color:#2a1d12; box-shadow:none;
                     text-align:left; padding:2px 2px 10px; border-bottom:2px solid var(--gold2); border-radius:0; font-size:1.25em; }
  .drop-label { background: var(--cream2); color:#6b4a14; border:1px solid var(--tan); }
  .drop-zone { background: rgba(255,255,255,.55); border:2px dashed var(--tan); }
  .drop-zone.drag-over { background: rgba(245,196,81,.22); border-color: var(--gold2); box-shadow: 0 0 18px rgba(245,196,81,.35); }
  .dropped-item.correct { background: linear-gradient(135deg, #15803d, #166534); border-color:#4ade80; color:#fff; }
  .dropped-item.incorrect { background: linear-gradient(135deg, #be123c, #9f1239); border-color:#fb7185; color:#fff; }
  .summary-content { background: linear-gradient(160deg, #1a1020, #0d0811); border-color: rgba(245,196,81,.45); }
  .summary-title, .summary-drug-title { font-family:'Fraunces',Georgia,serif; color:var(--gold); }
  .summary-drug { border-left-color: var(--gold); }
  .summary-category-title { color: var(--rose); }
  body > a[href] { background: rgba(26,16,32,.85) !important; border-color: rgba(245,196,81,.4) !important; color: var(--gold) !important; }
  body > div > a[href] { background: rgba(26,16,32,.85) !important; border-color: rgba(245,196,81,.4) !important; color: var(--gold) !important; }
</style>
"""


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(G.DATA_DIR, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.GAMES


def brick_titles():
    out = {}
    for i in range(1, 62):
        spec = importlib.util.spec_from_file_location(f"b{i}", os.path.join(G.DATA_DIR, f"brick_{i:02d}.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        out[i] = mod.BRICK["brick_title"]
    return out


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    # Course order: weeks 1-3 (with contraception after amenorrhea and the male
    # GU game after the tumors), then weeks 4-6.
    p1, p2, p3 = load("highyield_part1"), load("highyield_part2"), load("highyield_part3")
    games = p1[:3] + [p3[0]] + [p1[3]] + [p3[1]] + [p1[4]] + p2
    assert len(games) == 12, f"expected 12 games, got {len(games)}"
    titles = brick_titles()

    built = []
    for i, game in enumerate(games):
        cat_labels = {G.slugify_key(c): c for c in game["categories"]}
        label_to_key = {v: k for k, v in cat_labels.items()}
        data = {}
        for row, props in game["data"].items():
            assert set(props) == set(game["categories"]), (game["slug"], row)
            data[row] = {label_to_key[l]: v for l, v in props.items()}
        built.append({
            "slug": game["slug"], "title": game["title"], "subtitle": game["subtitle"],
            "categoryKeys": list(cat_labels), "categoryLabels": cat_labels, "gameData": data,
            "sources": game.get("sources", []), "rows": len(data),
            "file": f"repro_hy_{i + 1:02d}_{game['slug'].removeprefix('hy_')}.html",
        })

    for i, g in enumerate(built):
        prev_file = built[i - 1]["file"] if i else None
        next_file = built[i + 1]["file"] if i < len(built) - 1 else None
        html = G.make_html(g, prev_file, next_file, idx_in_palette=i)
        html = html.replace('href="repro_index.html"', f'href="{INDEX}"')
        html = html.replace("&#8592; Index</a>", "&#8592; High Yield</a>", 1)
        html = html.replace("<title>", "<title>High Yield: ", 1)
        html = html.replace("</head>", FONTS + HY_CSS + "</head>", 1)
        icon = G.ICONS[i % len(G.ICONS)]
        assert f"<h1>{icon} " in html
        dots = "".join(f'<a href="{x["file"]}" class="{"on" if x is g else ""}" title="{G.esc(x["title"])}"></a>'
                       for x in built)
        ribbon = (f'<div class="hy-ribbon"><span class="hy-tag">&#9733; Highest Yield &middot; {i + 1} of {len(built)}</span>'
                  f'<nav class="hy-dots" aria-label="High-yield games">{dots}</nav></div>\n        <h1>')
        html = html.replace(f"<h1>{icon} ", ribbon, 1)
        with open(os.path.join(ROOT, g["file"]), "w", encoding="utf-8") as f:
            f.write(html)
        print("  Created:", g["file"])

    covered = sorted({b for g in built for b in g["sources"]})
    cards = ""
    for i, g in enumerate(built):
        color = G.PALETTE[i % len(G.PALETTE)][0]
        chips = "".join(f'<span class="chip">{G.esc(titles[b])}</span>' for b in g["sources"] if b in titles)
        cards += f'''
  <a class="hy" href="{g["file"]}" style="--c:{color}">
    <span class="hy-num">{i + 1:02d}</span>
    <span class="hy-body">
      <span class="hy-title">{G.esc(g["title"])}</span>
      <span class="hy-sub">{G.esc(g["subtitle"])} &middot; {g["rows"]} rows</span>
      <span class="chips">{chips}</span>
    </span>
  </a>'''

    pink = G.ENDO_IDENTITY
    r, gg, b = G.ENDO_IDENTITY_RGB
    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ReproStudy &ndash; Highest Yield Drag &amp; Drops</title>
{FONTS}
<style>
  :root{{--ink:#0d0811;--plum:#2a1630;--gold:#f5c451;--gold2:#d99a1e;--rose:#f472b6;--cream:#fbf5e8;--cream2:#f1e6cc;--tan:#c9b48a;--text:#efe7f3;--muted:#b4a6bd;}}
  *{{box-sizing:border-box;margin:0;padding:0;}}
  body{{color:var(--text);font-family:'Inter','Segoe UI',system-ui,sans-serif;min-height:100vh;
       background:radial-gradient(1100px 600px at 50% -10%,rgba(245,196,81,.14),transparent 60%),radial-gradient(900px 700px at 100% 100%,rgba(244,114,182,.10),transparent 60%),linear-gradient(180deg,#120a17,var(--ink));background-attachment:fixed;}}
  header{{padding:56px 24px 30px;text-align:center;}}
  .eyebrow{{display:inline-block;font-size:.72rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--ink);background:linear-gradient(135deg,var(--gold),var(--gold2));border-radius:999px;padding:7px 14px;margin-bottom:18px;box-shadow:0 4px 18px rgba(245,196,81,.25);}}
  header h1{{font-family:'Fraunces',Georgia,serif;font-size:3rem;font-weight:800;letter-spacing:-.02em;line-height:1.05;background:linear-gradient(135deg,#fff7e6 20%,var(--gold) 65%,var(--rose));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:12px;}}
  header p{{color:var(--muted);font-size:1rem;font-style:italic;max-width:600px;margin:0 auto;line-height:1.6;}}
  .pills{{display:flex;gap:10px;justify-content:center;margin-top:22px;flex-wrap:wrap;}}
  .pill{{background:rgba(245,196,81,.07);border:1px solid rgba(245,196,81,.3);border-radius:999px;padding:6px 15px;font-size:.8rem;color:var(--muted);text-decoration:none;}}
  .pill b{{color:var(--gold);}}
  a.pill:hover{{border-color:var(--gold);color:var(--text);}}
  main{{max-width:1040px;margin:0 auto;padding:18px 16px 72px;display:grid;grid-template-columns:repeat(auto-fill,minmax(440px,1fr));gap:18px;}}
  @media (max-width:520px){{main{{grid-template-columns:1fr;}} header h1{{font-size:2.2rem;}}}}
  a.hy{{position:relative;display:flex;gap:16px;align-items:flex-start;text-decoration:none;color:#2a1d12;border-radius:14px;padding:20px 20px 18px;
        background:var(--cream);background-image:repeating-linear-gradient(180deg,transparent 0 27px,rgba(160,130,80,.13) 27px 28px);
        border:1px solid var(--cream2);box-shadow:0 14px 34px rgba(0,0,0,.45);transition:transform .15s,box-shadow .15s;}}
  a.hy::before{{content:"";position:absolute;left:0;top:14px;bottom:14px;width:4px;border-radius:0 4px 4px 0;background:var(--c);}}
  a.hy:hover{{transform:translateY(-3px) rotate(-.3deg);box-shadow:0 20px 44px rgba(0,0,0,.55),0 0 0 2px var(--gold);}}
  .hy-num{{flex:none;font-family:'Fraunces',Georgia,serif;font-size:2rem;font-weight:800;line-height:1;color:var(--gold2);min-width:2.2ch;}}
  .hy-body{{display:flex;flex-direction:column;gap:5px;min-width:0;}}
  .hy-title{{font-family:'Fraunces',Georgia,serif;font-size:1.15rem;font-weight:800;line-height:1.25;}}
  .hy-sub{{font-size:.8rem;color:#6b5a44;}}
  .chips{{display:flex;flex-wrap:wrap;gap:5px;margin-top:7px;}}
  .chip{{font-size:.66rem;color:#6b4a14;background:var(--cream2);border:1px solid var(--tan);border-radius:999px;padding:2px 8px;}}
</style>
<script defer src="https://activetransport.app/static/tool-track.js"></script>
</head>
<body>
<header>
  <span class="eyebrow">&#9733; Highest Yield</span>
  <h1>Highest Yield Drag &amp; Drops</h1>
  <p>{len(built)} games that pack the most-tested facts from across the Reproductive Systems course into one review set, built for the last pass before the exam.</p>
  <div class="pills">
    <span class="pill"><b>{len(built)}</b> games</span>
    <span class="pill"><b>{sum(g["rows"] for g in built)}</b> high-yield rows</span>
    <span class="pill"><b>{len(covered)}</b> lectures drawn on</span>
    <a class="pill" href="repro_index.html">All {len(titles)} lectures&rsquo; games &rarr;</a>
  </div>
</header>
<main>{cards}
</main>
</body>
</html>
'''
    with open(os.path.join(ROOT, INDEX), "w", encoding="utf-8") as f:
        f.write(page)
    print("Created:", INDEX, "| lectures drawn on:", len(covered), "| missing:",
          [b for b in range(1, 62) if b not in covered])


if __name__ == "__main__":
    main()

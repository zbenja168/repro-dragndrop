#!/usr/bin/env python3
"""Generate Repro drag-and-drop games from repro_data/brick_NN.py files.

Each game gets a rotating accent color from an 8-color palette.
Games are ordered by brick number (1-21), then by their order within each brick.
The Repro index uses pink (#ec4899) as its identity color.
"""

import importlib.util
import json
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "repro_data")
OUT_DIR = ROOT

# ────────────────────────────────────────────
# Palette: 8 colors that cycle across games
# ────────────────────────────────────────────
# Each entry: (accent, dark, darker, rgb-tuple, hover-tint, bg-tint-darker)
PALETTE = [
    ("#f59e0b", "#d97706", "#b45309", (245, 158, 11)),   # 0 amber
    ("#10b981", "#059669", "#047857", (16, 185, 129)),   # 1 emerald
    ("#8b5cf6", "#7c3aed", "#6d28d9", (139, 92, 246)),   # 2 violet
    ("#06b6d4", "#0891b2", "#0e7490", (6, 182, 212)),    # 3 cyan
    ("#ec4899", "#db2777", "#be185d", (236, 72, 153)),   # 4 pink
    ("#84cc16", "#65a30d", "#4d7c0f", (132, 204, 22)),   # 5 lime
    ("#f97316", "#ea580c", "#c2410c", (249, 115, 22)),   # 6 orange
    ("#3b82f6", "#2563eb", "#1d4ed8", (59, 130, 246)),   # 7 blue
]
ENDO_IDENTITY = "#ec4899"  # pink for index/header

# The block runs over three teaching weeks; the index groups its lectures the
# same way, so a student revising "this week" can find their games in one place.
WEEKS = [
    ("Week 1", "Anatomy, Development, Hormones & Cycles", range(1, 15)),
    ("Week 2", "Repro Health, Female & Male Pathology", range(15, 30)),
]


def week_of(brick_num):
    """The (label, subtitle) this brick belongs to, or None if unclassified."""
    for label, sub, rng in WEEKS:
        if brick_num in rng:
            return (label, sub)
    return None
ENDO_IDENTITY_RGB = (236, 72, 153)

# Subject icons rotate too (decorative only)
ICONS = ["🩸", "🧬", "⚗️", "🔬", "🧪", "💊", "🩺", "⚡"]


def load_bricks():
    """Import all brick_NN.py files in number order, then the cross-brick synthesis at the end."""
    bricks = []
    for i in range(1, 30):
        path = os.path.join(DATA_DIR, f"brick_{i:02d}.py")
        if not os.path.exists(path):
            print(f"  WARNING: missing {path}")
            continue
        spec = importlib.util.spec_from_file_location(f"brick_{i:02d}", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        bricks.append(mod.BRICK)
    # Cross-brick synthesis brick (brick_99) appended last
    xb_path = os.path.join(DATA_DIR, "brick_99.py")
    if os.path.exists(xb_path):
        spec = importlib.util.spec_from_file_location("brick_99", xb_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        bricks.append(mod.BRICK)
    return bricks


# ────────────────────────────────────────────
# Escapers
# ────────────────────────────────────────────

def esc(s):
    """HTML-escape for attributes / text content."""
    return (s.replace("&", "&amp;")
             .replace('"', "&quot;")
             .replace("'", "&#39;")
             .replace("<", "&lt;")
             .replace(">", "&gt;"))


def js_esc(s):
    """Escape for use inside JS double-quoted strings."""
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")


def slugify_key(s):
    """Convert a category label to a JS-safe identifier key."""
    out = "".join(c.lower() if c.isalnum() else "_" for c in s)
    while "__" in out:
        out = out.replace("__", "_")
    return out.strip("_") or "cat"


# ────────────────────────────────────────────
# Per-game HTML
# ────────────────────────────────────────────

def make_html(game, prev_file, next_file, idx_in_palette):
    accent, dark, darker, rgb = PALETTE[idx_in_palette % len(PALETTE)]
    r, g, b = rgb
    rgba = lambda a: f"rgba({r}, {g}, {b}, {a})"

    cats = game["categoryKeys"]
    cat_labels = game["categoryLabels"]
    data = game["gameData"]
    icon = ICONS[idx_in_palette % len(ICONS)]

    # Build JS gameData
    js_data_lines = []
    for entity, cats_dict in data.items():
        props = ",\n                ".join(
            f'"{js_esc(k)}": "{js_esc(v)}"' for k, v in cats_dict.items()
        )
        js_data_lines.append(
            f'            "{js_esc(entity)}": {{\n                {props}\n            }}'
        )
    js_data = "{\n" + ",\n".join(js_data_lines) + "\n        }"

    js_cat_keys = json.dumps(cats)
    js_cat_labels = json.dumps(cat_labels)

    # Nav links
    index_link = (
        '<a href="repro_index.html" style="position:fixed;top:12px;left:12px;z-index:9999;'
        'background:rgba(0,0,0,0.55);color:#94a3b8;border:1px solid rgba(255,255,255,0.13);'
        'border-radius:20px;padding:5px 13px;font-size:.72rem;text-decoration:none;'
        "font-family:'Segoe UI',sans-serif;backdrop-filter:blur(8px);transition:.15s;letter-spacing:.3px;\" "
        "onmouseover=\"this.style.color='#f1f5f9';this.style.borderColor='rgba(255,255,255,0.3)'\" "
        "onmouseout=\"this.style.color='#94a3b8';this.style.borderColor='rgba(255,255,255,0.13)'\">"
        '&#8592; Index</a>'
    )

    nav_btn_style = (
        "background:rgba(0,0,0,0.72);color:#e2e8f0;border:1px solid rgba(255,255,255,0.22);"
        "border-radius:22px;padding:8px 18px;font-size:.85rem;font-weight:600;text-decoration:none;"
        "font-family:'Segoe UI',sans-serif;backdrop-filter:blur(10px);transition:.15s;"
        "display:inline-flex;align-items:center;gap:6px;"
    )
    over = (
        "onmouseover=\"this.style.color='#fff';this.style.borderColor='rgba(255,255,255,0.5)';"
        "this.style.background='rgba(0,0,0,0.88)'\""
    )
    out = (
        "onmouseout=\"this.style.color='#e2e8f0';this.style.borderColor='rgba(255,255,255,0.22)';"
        "this.style.background='rgba(0,0,0,0.72)'\""
    )

    nav_right = ""
    if prev_file and next_file:
        nav_right = (
            f'<div style="position:fixed;top:12px;right:12px;z-index:9999;display:flex;gap:8px;">'
            f'<a href="{prev_file}" style="{nav_btn_style}" {over} {out}>&#8592; Prev</a>'
            f'<a href="{next_file}" style="{nav_btn_style}" {over} {out}>Next &#8594;</a>'
            f"</div>"
        )
    elif prev_file:
        nav_right = (
            f'<a href="{prev_file}" style="position:fixed;top:12px;right:12px;z-index:9999;{nav_btn_style}" {over} {out}>'
            f"&#8592; Prev</a>"
        )
    elif next_file:
        nav_right = (
            f'<a href="{next_file}" style="position:fixed;top:12px;right:12px;z-index:9999;{nav_btn_style}" {over} {out}>'
            f"Next &#8594;</a>"
        )

    # Tabs
    tab_buttons = "\n                    ".join(
        f"<button class=\"tab{' active' if i == 0 else ''}\" onclick=\"switchTab('{c}', this)\">{esc(cat_labels[c])}</button>"
        for i, c in enumerate(cats)
    )
    bank_divs = "\n                ".join(
        f"<div id=\"{c}-bank\" class=\"word-bank{' active' if i == 0 else ''}\"></div>"
        for i, c in enumerate(cats)
    )

    bg_grad = "linear-gradient(135deg, #0a0f1c 0%, #0f1729 50%, #0a0f1c 100%)"
    card_bg = "rgba(15, 23, 42, 0.95)"
    card_grad = f"linear-gradient(135deg, {accent} 0%, {darker} 100%)"
    item_grad = "linear-gradient(135deg, #1a2235 0%, #131a2a 100%)"
    item_hover = "linear-gradient(135deg, #232d44 0%, #1a2235 100%)"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(game['title'])} - Drag &amp; Drop Study Game</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: {bg_grad};
            color: #e4e4e4;
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{ max-width: 1600px; margin: 0 auto; }}
        h1 {{
            text-align: center;
            color: {accent};
            margin-bottom: 10px;
            font-size: 2.2em;
            text-shadow: 0 0 20px {rgba('0.5')};
        }}
        .subtitle {{ text-align: center; color: #a0a0a0; margin-bottom: 25px; font-size: 1.1em; }}
        .stats-controls {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px; flex-wrap: wrap; gap: 15px; }}
        .stats {{ display: flex; gap: 25px; flex-wrap: wrap; }}
        .stat-item {{
            background: {rgba('0.1')};
            padding: 12px 20px; border-radius: 8px;
            border: 1px solid {rgba('0.3')};
        }}
        .stat-label {{ color: {accent}; font-weight: bold; margin-right: 8px; }}
        .controls {{ display: flex; gap: 12px; flex-wrap: wrap; }}
        .btn {{ padding: 12px 24px; border: none; border-radius: 8px; cursor: pointer; font-size: 0.95em; font-weight: 600; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }}
        .btn-primary {{ background: linear-gradient(135deg, {accent} 0%, {darker} 100%); color: white; }}
        .btn-primary:hover {{ transform: translateY(-2px); box-shadow: 0 6px 20px {rgba('0.4')}; }}
        .btn-secondary {{ background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color: white; }}
        .btn-secondary:hover {{ transform: translateY(-2px); box-shadow: 0 6px 20px rgba(245,158,11,0.4); }}
        .btn-success {{ background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white; }}
        .btn-success:hover {{ transform: translateY(-2px); box-shadow: 0 6px 20px rgba(16,185,129,0.4); }}
        .btn-danger {{ background: linear-gradient(135deg, #ef4444 0%, #b91c1c 100%); color: white; }}
        .btn-danger:hover {{ transform: translateY(-2px); box-shadow: 0 6px 20px rgba(239,68,68,0.4); }}
        .main-content {{ display: grid; grid-template-columns: 350px 1fr; gap: 25px; align-items: start; }}
        .word-bank-container {{
            position: sticky; top: 20px;
            background: rgba(10, 15, 28, 0.95);
            border-radius: 12px; padding: 20px;
            border: 2px solid {rgba('0.3')};
            box-shadow: 0 8px 32px rgba(0,0,0,0.5);
        }}
        .word-bank-title {{ color: {accent}; font-size: 1.3em; margin-bottom: 15px; text-align: center; font-weight: bold; }}
        .tabs {{ display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 15px; padding-bottom: 6px; border-bottom: 2px solid {rgba('0.3')}; }}
        .tab {{ flex: 1 1 auto; min-width: 0; padding: 8px 10px; background: rgba(255,255,255,0.05); border: none; color: #a0a0a0; cursor: pointer; transition: all 0.3s ease; font-size: 0.82em; line-height: 1.25; font-weight: 600; border-radius: 8px 8px 0 0; text-align: center; overflow-wrap: anywhere; }}
        .tab.active {{ background: {card_grad}; color: white; }}
        .tab:hover:not(.active) {{ background: rgba(255,255,255,0.1); color: #e4e4e4; }}
        .word-bank {{ min-height: 400px; max-height: 70vh; overflow-y: auto; padding: 15px; background: rgba(0,0,0,0.3); border-radius: 8px; display: none; }}
        .word-bank.active {{ display: block; }}
        .word-bank::-webkit-scrollbar {{ width: 8px; }}
        .word-bank::-webkit-scrollbar-track {{ background: rgba(0,0,0,0.2); border-radius: 4px; }}
        .word-bank::-webkit-scrollbar-thumb {{ background: {rgba('0.5')}; border-radius: 4px; }}
        .draggable-item {{
            background: {item_grad};
            padding: 12px 15px; margin-bottom: 10px; border-radius: 8px; cursor: move;
            border: 2px solid {rgba('0.4')}; transition: all 0.3s ease;
            font-size: 0.95em; line-height: 1.4;
        }}
        .draggable-item:hover {{ background: {item_hover}; border-color: {accent}; transform: translateX(5px); box-shadow: 0 4px 15px {rgba('0.3')}; }}
        .draggable-item.dragging {{ opacity: 0.5; transform: rotate(2deg); }}
        .cards-container {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(480px, 1fr)); gap: 20px; }}
        .drug-card {{ background: {card_bg}; border-radius: 12px; padding: 20px; border: 2px solid {rgba('0.3')}; box-shadow: 0 8px 32px rgba(0,0,0,0.5); }}
        .drug-card-title {{
            background: {card_grad};
            color: white; padding: 12px; border-radius: 8px;
            font-size: 1.2em; font-weight: bold; margin-bottom: 15px; text-align: center;
            box-shadow: 0 4px 15px {rgba('0.3')};
        }}
        .drop-zones {{ display: grid; gap: 12px; }}
        .drop-row {{ display: grid; grid-template-columns: 140px 1fr; gap: 10px; align-items: start; }}
        .drop-label {{ background: {rgba('0.1')}; padding: 10px; border-radius: 6px; font-weight: 600; color: {accent}; font-size: 0.9em; display: flex; align-items: center; border: 1px solid {rgba('0.3')}; }}
        .drop-zone {{ min-height: 60px; background: rgba(0,0,0,0.3); border: 2px dashed {rgba('0.3')}; border-radius: 8px; padding: 10px; transition: all 0.3s ease; display: flex; flex-direction: column; gap: 8px; }}
        .drop-zone.drag-over {{ background: {rgba('0.2')}; border-color: {accent}; border-style: solid; box-shadow: 0 0 20px {rgba('0.3')}; }}
        .dropped-item {{ background: {item_grad}; padding: 10px 12px; border-radius: 6px; cursor: move; border: 2px solid {rgba('0.4')}; transition: all 0.3s ease; font-size: 0.9em; line-height: 1.4; }}
        .dropped-item:hover {{ background: {item_hover}; border-color: {accent}; }}
        .dropped-item.correct {{ background: linear-gradient(135deg, #0f9b0f 0%, #0a7c0a 100%); border-color: #00ff00; animation: correctPulse 0.5s ease; }}
        .dropped-item.incorrect {{ background: linear-gradient(135deg, #c41e3a 0%, #9a1829 100%); border-color: #ff4444; animation: incorrectShake 0.5s ease; }}
        @keyframes correctPulse {{ 0%,100%{{transform:scale(1)}} 50%{{transform:scale(1.05);box-shadow:0 0 20px rgba(0,255,0,0.5)}} }}
        @keyframes incorrectShake {{ 0%,100%{{transform:translateX(0)}} 25%{{transform:translateX(-5px)}} 75%{{transform:translateX(5px)}} }}
        .summary-modal {{ display: none; position: fixed; top:0; left:0; width:100%; height:100%; background: rgba(0,0,0,0.8); z-index: 1000; justify-content: center; align-items: center; padding: 20px; }}
        .summary-modal.active {{ display: flex; }}
        .summary-content {{ background: linear-gradient(135deg, #0a0f1c 0%, #0f1729 100%); border-radius: 12px; padding: 30px; max-width: 900px; max-height: 90vh; overflow-y: auto; border: 2px solid {rgba('0.5')}; box-shadow: 0 10px 50px rgba(0,0,0,0.8); }}
        .summary-content::-webkit-scrollbar {{ width: 10px; }}
        .summary-content::-webkit-scrollbar-track {{ background: rgba(0,0,0,0.3); border-radius: 5px; }}
        .summary-content::-webkit-scrollbar-thumb {{ background: {rgba('0.5')}; border-radius: 5px; }}
        .summary-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px; padding-bottom: 15px; border-bottom: 2px solid {rgba('0.3')}; }}
        .summary-title {{ color: {accent}; font-size: 1.8em; font-weight: bold; }}
        .close-btn {{ background: rgba(255,68,68,0.2); border: 2px solid #ff4444; color: #ff4444; padding: 8px 16px; border-radius: 6px; cursor: pointer; font-weight: 600; transition: all 0.3s ease; }}
        .close-btn:hover {{ background: #ff4444; color: white; }}
        .summary-drug {{ margin-bottom: 25px; background: rgba(0,0,0,0.3); padding: 20px; border-radius: 8px; border-left: 4px solid {accent}; }}
        .summary-drug-title {{ color: {accent}; font-size: 1.3em; margin-bottom: 15px; font-weight: bold; }}
        .summary-category {{ margin-bottom: 12px; }}
        .summary-category-title {{ color: #f59e0b; font-weight: 600; margin-bottom: 5px; font-size: 1.05em; }}
        .summary-category-content {{ color: #e4e4e4; padding-left: 15px; line-height: 1.6; }}
        @media (max-width: 1200px) {{
            .main-content {{ grid-template-columns: 1fr; }}
            .word-bank-container {{ position: relative; top: 0; }}
            .cards-container {{ grid-template-columns: 1fr; }}
        }}
        @media (max-width: 768px) {{
            h1 {{ font-size: 1.6em; }}
            .stats-controls {{ flex-direction: column; }}
            .stats, .controls {{ width: 100%; justify-content: center; }}
            .btn {{ flex: 1; min-width: 120px; }}
            .drop-row {{ grid-template-columns: 1fr; }}
            .drop-label {{ text-align: center; }}
        }}
    </style>
<script defer src="https://activetransport.app/static/tool-track.js"></script>
</head>
<body>
{index_link}
{nav_right}

    <div class="container">
        <h1>{icon} {esc(game['title'])}</h1>
        <p class="subtitle">{esc(game['subtitle'])}</p>
        <div class="stats-controls">
            <div class="stats">
                <div class="stat-item"><span class="stat-label">Score:</span><span id="score">0</span>/<span id="total">0</span></div>
                <div class="stat-item"><span class="stat-label">Remaining:</span><span id="remaining">0</span></div>
            </div>
            <div class="controls">
                <button class="btn btn-primary" onclick="showSummary()">&#x1F4CB; Show Summary</button>
                <button class="btn btn-secondary" onclick="showHint()">&#x1F4A1; Hint</button>
                <button class="btn btn-success" onclick="showAllAnswers()">&#x2713; Show All Answers</button>
                <button class="btn btn-danger" onclick="resetGame()">&#x1F504; Reset</button>
            </div>
        </div>
        <div class="main-content">
            <div class="word-bank-container">
                <div class="word-bank-title">&#x1F4DA; Word Bank</div>
                <div class="tabs">
                    {tab_buttons}
                </div>
                {bank_divs}
            </div>
            <div class="cards-container" id="cards-container"></div>
        </div>
    </div>
    <div class="summary-modal" id="summaryModal">
        <div class="summary-content">
            <div class="summary-header">
                <div class="summary-title">&#x1F4D6; Complete Summary</div>
                <button class="close-btn" onclick="closeSummary()">Close</button>
            </div>
            <div id="summaryContent"></div>
        </div>
    </div>
    <script>
        const categoryKeys = {js_cat_keys};
        const categoryLabels = {js_cat_labels};

        const gameData = {js_data};

        let score = 0, totalItems = 0, draggedElement = null, allItems = {{}};

        function initGame() {{
            const cardsContainer = document.getElementById('cards-container');
            cardsContainer.innerHTML = '';
            allItems = {{}};
            categoryKeys.forEach(cat => {{ allItems[cat] = []; }});
            Object.keys(gameData).forEach(entity => {{
                categoryKeys.forEach(cat => {{
                    allItems[cat].push({{ text: gameData[entity][cat], entity, category: cat }});
                }});
            }});
            categoryKeys.forEach(cat => {{ allItems[cat] = shuffleArray(allItems[cat]); }});
            totalItems = Object.keys(gameData).length * categoryKeys.length;
            Object.keys(gameData).forEach(entity => {{
                const card = document.createElement('div');
                card.className = 'drug-card';
                const zonesHtml = categoryKeys.map(cat => `
                    <div class="drop-row">
                        <div class="drop-label">${{categoryLabels[cat]}}</div>
                        <div class="drop-zone" data-entity="${{entity}}" data-category="${{cat}}"></div>
                    </div>`).join('');
                card.innerHTML = `<div class="drug-card-title">${{entity}}</div><div class="drop-zones">${{zonesHtml}}</div>`;
                cardsContainer.appendChild(card);
            }});
            populateWordBanks();
            setupDragAndDrop();
            updateStats();
        }}

        function shuffleArray(array) {{
            const a = [...array];
            for (let i = a.length - 1; i > 0; i--) {{
                const j = Math.floor(Math.random() * (i + 1));
                [a[i], a[j]] = [a[j], a[i]];
            }}
            return a;
        }}

        function populateWordBanks() {{
            categoryKeys.forEach(cat => {{
                const bank = document.getElementById(`${{cat}}-bank`);
                bank.innerHTML = '';
                allItems[cat].forEach((item, index) => {{
                    const div = document.createElement('div');
                    div.className = 'draggable-item';
                    div.draggable = true;
                    div.textContent = item.text;
                    div.dataset.entity = item.entity;
                    div.dataset.category = item.category;
                    div.dataset.id = `${{cat}}-${{index}}`;
                    bank.appendChild(div);
                }});
            }});
        }}

        function setupDragAndDrop() {{
            document.querySelectorAll('.draggable-item, .dropped-item').forEach(item => {{
                item.addEventListener('dragstart', handleDragStart);
                item.addEventListener('dragend', handleDragEnd);
            }});
            document.querySelectorAll('.drop-zone').forEach(zone => {{
                zone.addEventListener('dragover', handleDragOver);
                zone.addEventListener('drop', handleDrop);
                zone.addEventListener('dragleave', handleDragLeave);
            }});
            document.querySelectorAll('.word-bank').forEach(bank => {{
                bank.addEventListener('dragover', handleDragOver);
                bank.addEventListener('drop', handleDropToBank);
                bank.addEventListener('dragleave', handleDragLeave);
            }});
        }}

        function handleDragStart(e) {{ draggedElement = e.target; e.target.classList.add('dragging'); e.dataTransfer.effectAllowed = 'move'; }}
        function handleDragEnd(e) {{ e.target.classList.remove('dragging'); }}

        function handleDragOver(e) {{
            e.preventDefault(); e.dataTransfer.dropEffect = 'move';
            const t = e.target;
            if (t.classList.contains('drop-zone') || t.classList.contains('word-bank')) t.classList.add('drag-over');
        }}
        function handleDragLeave(e) {{
            const t = e.target;
            if (t.classList.contains('drop-zone') || t.classList.contains('word-bank')) t.classList.remove('drag-over');
        }}

        function handleDrop(e) {{
            e.preventDefault();
            const dropZone = e.target.closest('.drop-zone');
            if (!dropZone) return;
            dropZone.classList.remove('drag-over');
            if (dropZone.children.length > 0) return;
            const entityName = dropZone.dataset.entity;
            const category = dropZone.dataset.category;
            const draggedEntity = draggedElement.dataset.entity;
            const draggedCategory = draggedElement.dataset.category;
            if (draggedElement.parentElement.classList.contains('word-bank') ||
                draggedElement.parentElement.classList.contains('drop-zone')) {{
                draggedElement.remove();
            }}
            const droppedItem = document.createElement('div');
            droppedItem.className = 'dropped-item';
            droppedItem.draggable = true;
            droppedItem.textContent = draggedElement.textContent;
            droppedItem.dataset.entity = draggedEntity;
            droppedItem.dataset.category = draggedCategory;
            droppedItem.dataset.id = draggedElement.dataset.id;
            if (category === draggedCategory && draggedElement.textContent === gameData[entityName][category]) {{
                droppedItem.classList.add('correct'); score++;
            }} else {{
                droppedItem.classList.add('incorrect');
            }}
            dropZone.appendChild(droppedItem);
            setupDragAndDrop();
            updateStats();
        }}

        function handleDropToBank(e) {{
            e.preventDefault();
            const wordBank = e.target.closest('.word-bank');
            if (!wordBank) return;
            wordBank.classList.remove('drag-over');
            if (!draggedElement.classList.contains('dropped-item')) return;
            const category = draggedElement.dataset.category;
            const targetBank = document.getElementById(`${{category}}-bank`);
            if (draggedElement.classList.contains('correct')) score--;
            const oldText = draggedElement.textContent;
            const oldEntity = draggedElement.dataset.entity;
            const oldCategory = draggedElement.dataset.category;
            const oldId = draggedElement.dataset.id;
            draggedElement.remove();
            const newItem = document.createElement('div');
            newItem.className = 'draggable-item';
            newItem.draggable = true;
            newItem.textContent = oldText;
            newItem.dataset.entity = oldEntity;
            newItem.dataset.category = oldCategory;
            newItem.dataset.id = oldId;
            targetBank.insertBefore(newItem, targetBank.firstChild);
            setupDragAndDrop();
            updateStats();
        }}

        function updateStats() {{
            document.getElementById('score').textContent = score;
            document.getElementById('total').textContent = totalItems;
            let remaining = 0;
            document.querySelectorAll('.word-bank').forEach(b => {{ remaining += b.querySelectorAll('.draggable-item').length; }});
            document.getElementById('remaining').textContent = remaining;
            if (score === totalItems && totalItems > 0) setTimeout(() => alert('Perfect score! You nailed it!'), 500);
        }}

        function switchTab(tab, btn) {{
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.word-bank').forEach(b => b.classList.remove('active'));
            if (btn) btn.classList.add('active');
            document.getElementById(`${{tab}}-bank`).classList.add('active');
        }}

        function showHint() {{
            const emptyZones = Array.from(document.querySelectorAll('.drop-zone')).filter(z => z.children.length === 0);
            if (emptyZones.length === 0) {{ alert('All zones are filled!'); return; }}
            const zone = emptyZones[Math.floor(Math.random() * emptyZones.length)];
            const cat = zone.dataset.category;
            const entity = zone.dataset.entity;
            const tabBtn = Array.from(document.querySelectorAll('.tab')).find(t => t.getAttribute('onclick').includes("'" + cat + "'"));
            if (tabBtn) switchTab(cat, tabBtn);
            setTimeout(() => {{
                const correctItem = Array.from(document.querySelectorAll('.draggable-item')).find(i =>
                    i.dataset.entity === entity && i.dataset.category === cat);
                if (correctItem) {{
                    correctItem.style.outline = "2px solid {accent}";
                    correctItem.style.animation = 'correctPulse 1s ease 3';
                    correctItem.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                    setTimeout(() => {{ correctItem.style.animation = ''; correctItem.style.outline = ''; }}, 3000);
                }}
            }}, 100);
        }}

        function showAllAnswers() {{
            if (!confirm('This will reveal all correct answers. Continue?')) return;
            document.querySelectorAll('.drop-zone').forEach(zone => {{ zone.innerHTML = ''; }});
            document.querySelectorAll('.drop-zone').forEach(zone => {{
                const entity = zone.dataset.entity;
                const cat = zone.dataset.category;
                const droppedItem = document.createElement('div');
                droppedItem.className = 'dropped-item correct';
                droppedItem.textContent = gameData[entity][cat];
                zone.appendChild(droppedItem);
            }});
            document.querySelectorAll('.word-bank').forEach(b => {{ b.innerHTML = ''; }});
            score = totalItems;
            setupDragAndDrop();
            updateStats();
        }}

        function showSummary() {{
            const summaryContent = document.getElementById('summaryContent');
            summaryContent.innerHTML = '';
            Object.keys(gameData).forEach(entity => {{
                const div = document.createElement('div');
                div.className = 'summary-drug';
                const catHtml = categoryKeys.map(cat => `
                    <div class="summary-category">
                        <div class="summary-category-title">${{categoryLabels[cat]}}:</div>
                        <div class="summary-category-content">${{gameData[entity][cat]}}</div>
                    </div>`).join('');
                div.innerHTML = `<div class="summary-drug-title">${{entity}}</div>${{catHtml}}`;
                summaryContent.appendChild(div);
            }});
            document.getElementById('summaryModal').classList.add('active');
        }}

        function closeSummary() {{ document.getElementById('summaryModal').classList.remove('active'); }}

        function resetGame() {{
            if (!confirm('Reset the game?')) return;
            score = 0; initGame();
        }}

        window.onload = initGame;
        document.getElementById('summaryModal').addEventListener('click', function(e) {{
            if (e.target === this) closeSummary();
        }});
    </script>
</body>
</html>"""


# ────────────────────────────────────────────
# Build all games + index
# ────────────────────────────────────────────

def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    bricks = load_bricks()
    print(f"Loaded {len(bricks)} bricks")

    # Flatten: list of (game_dict, brick_num, brick_title, palette_idx)
    all_games = []
    for brick in bricks:
        for game in brick["games"]:
            # Convert flat categories list to keys + labels mapping
            cat_labels = {slugify_key(c): c for c in game["categories"]}
            cat_keys = list(cat_labels.keys())  # preserves order in Py3.7+
            # Re-key the gameData so each entity maps key→value
            label_to_key = {label: key for key, label in cat_labels.items()}
            new_data = {}
            for entity, props in game["data"].items():
                new_data[entity] = {label_to_key[label]: val for label, val in props.items()}

            all_games.append({
                "slug": game["slug"],
                "title": game["title"],
                "subtitle": game["subtitle"],
                "categoryKeys": cat_keys,
                "categoryLabels": cat_labels,
                "gameData": new_data,
                "brick_num": brick["brick_num"],
                "brick_title": brick["brick_title"],
            })

    # Assign global numbering and filename
    for i, g in enumerate(all_games):
        g["file"] = f"repro_{i+1:02d}_{g['slug']}.html"

    # Generate per-game HTML
    for i, g in enumerate(all_games):
        prev_file = all_games[i-1]["file"] if i > 0 else None
        next_file = all_games[i+1]["file"] if i < len(all_games)-1 else None
        html_content = make_html(g, prev_file, next_file, idx_in_palette=i)
        with open(os.path.join(OUT_DIR, g["file"]), "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"  Created: {g['file']}")

    print(f"\nGenerated {len(all_games)} Repro games.")

    # Build index sections (one per brick)
    sections = []
    for bi, brick in enumerate(bricks):
        # color identity for the section header (rotates same palette as games)
        sec_color = PALETTE[bi % len(PALETTE)][0]
        sec_icon = ICONS[bi % len(ICONS)]
        # gather all games in this brick and find their global numbers
        brick_games = [g for g in all_games if g["brick_num"] == brick["brick_num"]]
        section_games = []
        for g in brick_games:
            num = all_games.index(g) + 1
            section_games.append((num, g["title"], g["file"]))
        sections.append({
            "icon": sec_icon,
            "title": brick["brick_title"],
            "color": sec_color,
            "games": section_games,
            "brick_num": brick["brick_num"],
        })

    total_games = len(all_games)
    total_sections = len(sections)
    total_bricks = len(bricks)

    sections_html = ""
    open_week = None
    for sec in sections:
        week = week_of(sec["brick_num"])
        if week != open_week:
            if open_week is not None:
                sections_html += "</div>\n"
            wk_games = sum(len(s["games"]) for s in sections
                           if week_of(s["brick_num"]) == week)
            wk_lectures = sum(1 for s in sections if week_of(s["brick_num"]) == week)
            sections_html += f'''
<div class="week" data-week>
  <div class="week-head">
    <span class="week-label">{week[0]}</span>
    <span class="week-sub">{week[1]}</span>
    <span class="week-count">{wk_lectures} lectures &middot; {wk_games} games</span>
  </div>
'''
            open_week = week

        cards_html = ""
        for num, title, href in sec["games"]:
            cards_html += (
                f'    <a class="card" href="{href}" style="--c:{sec["color"]}">'
                f'<span class="num">{num:02d}</span>'
                f'<span class="ctitle">{esc(title)}</span></a>\n'
            )
        sections_html += f'''
<section class="section" data-section>
  <div class="section-head">
    <span class="section-icon">{sec["icon"]}</span>
    <span class="section-title">{esc(sec["title"])}</span>
    <span class="section-badge">{len(sec["games"])} game{"s" if len(sec["games"]) != 1 else ""}</span>
  </div>
  <div class="cards">
{cards_html}  </div>
</section>
'''
    if open_week is not None:
        sections_html += "</div>\n"

    r, g, b = ENDO_IDENTITY_RGB
    iden_rgba = lambda a: f"rgba({r}, {g}, {b}, {a})"

    index_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ReproStudy &ndash; Drag &amp; Drop Games</title>
<style>
  :root{{--bg:#0a0805;--surface:#14110b;--surface2:#1d1812;--text:#f1f5f9;--muted:#94a3b8;--border:rgba(255,255,255,0.07);}}
  *{{box-sizing:border-box;margin:0;padding:0;}}
  body{{background:var(--bg);color:var(--text);font-family:'Segoe UI',system-ui,sans-serif;min-height:100vh;}}

  header{{background:linear-gradient(160deg,#1a1305 0%,#2a1f08 50%,#0a0805 100%);border-bottom:1px solid var(--border);padding:44px 24px 36px;text-align:center;position:relative;overflow:hidden;}}
  header::after{{content:'\\1F52C';position:absolute;font-size:360px;opacity:.025;top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none;}}
  header h1{{font-size:2.4rem;font-weight:800;letter-spacing:-0.5px;background:linear-gradient(135deg,#f8fafc 30%,{ENDO_IDENTITY});-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:6px;position:relative;}}
  header p{{color:var(--muted);font-size:.9rem;position:relative;}}
  .pills{{display:flex;gap:10px;justify-content:center;margin-top:18px;flex-wrap:wrap;position:relative;}}
  .pill{{background:rgba(255,255,255,.05);border:1px solid var(--border);border-radius:20px;padding:5px 14px;font-size:.78rem;color:var(--muted);}}
  .pill b{{color:{ENDO_IDENTITY};}}

  .search-wrap{{max-width:460px;margin:22px auto 0;position:relative;}}
  .search-wrap input{{width:100%;background:var(--surface);border:1px solid var(--border);border-radius:24px;padding:10px 44px 10px 18px;color:var(--text);font-size:.85rem;outline:none;transition:.2s;}}
  .search-wrap input:focus{{border-color:{ENDO_IDENTITY};box-shadow:0 0 0 3px {iden_rgba('.18')};}}
  .search-wrap input::placeholder{{color:var(--muted);}}
  .search-ico{{position:absolute;right:15px;top:50%;transform:translateY(-50%);color:var(--muted);font-size:.85rem;pointer-events:none;}}

  main{{max-width:1380px;margin:0 auto;padding:32px 16px 56px;}}
  .no-results{{text-align:center;color:var(--muted);padding:60px 20px;font-size:.9rem;display:none;}}

  .week{{margin-bottom:44px;}}
  .week-head{{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin:0 0 22px;padding:14px 18px;border-radius:12px;background:linear-gradient(135deg,{iden_rgba('.16')},{iden_rgba('.04')});border:1px solid {iden_rgba('.28')};}}
  .week-label{{font-size:1.15rem;font-weight:800;letter-spacing:-.01em;color:{ENDO_IDENTITY};}}
  .week-sub{{font-size:.9rem;color:var(--text);opacity:.85;}}
  .week-count{{margin-left:auto;font-size:.7rem;color:var(--muted);white-space:nowrap;}}
  @media (max-width:640px){{.week-count{{margin-left:0;flex-basis:100%;}}}}
  .section{{margin-bottom:32px;}}
  .section-head{{display:flex;align-items:center;gap:10px;margin-bottom:12px;padding-bottom:10px;border-bottom:1px solid var(--border);}}
  .section-icon{{font-size:1.2rem;line-height:1;}}
  .section-title{{font-size:.95rem;font-weight:700;color:var(--text);}}
  .section-badge{{margin-left:auto;background:var(--surface2);border-radius:10px;padding:2px 8px;font-size:.68rem;color:var(--muted);}}

  .cards{{display:grid;grid-template-columns:repeat(auto-fill,minmax(195px,1fr));gap:7px;}}
  a.card{{background:var(--surface);border:1px solid var(--border);border-radius:9px;padding:11px 12px;text-decoration:none;color:var(--text);display:flex;align-items:flex-start;gap:9px;transition:.15s;}}
  a.card:hover{{border-color:var(--c,{ENDO_IDENTITY});background:var(--surface2);transform:translateY(-2px);box-shadow:0 6px 24px rgba(0,0,0,.5);}}
  .num{{flex-shrink:0;background:var(--c,{ENDO_IDENTITY});color:#fff;border-radius:5px;padding:2px 5px;font-size:.6rem;font-weight:800;margin-top:1px;opacity:.9;letter-spacing:.3px;}}
  .ctitle{{font-size:.75rem;line-height:1.45;color:var(--text);}}
</style>
<script defer src="https://activetransport.app/static/tool-track.js"></script>
</head>
<body>

<header>
  <h1>ReproStudy</h1>
  <p>Drag &amp; Drop Study Games &nbsp;&middot;&nbsp; Reproductive Systems &amp; Breast Health</p>
  <div class="pills">
    <span class="pill"><b>{total_games}</b> games</span>
    <span class="pill"><b>{total_bricks}</b> source bricks</span>
    <span class="pill"><b>{total_sections}</b> sections</span>
  </div>
  <div class="search-wrap">
    <input type="text" id="search" placeholder="Search by topic or number&hellip;" autocomplete="off">
    <span class="search-ico">&#x2315;</span>
  </div>
</header>

<main>
<div class="no-results" id="noResults">No games match your search.</div>
{sections_html}
</main>

<script>
document.getElementById('search').addEventListener('input', function() {{
  const q = this.value.toLowerCase().trim();
  let anyVisible = false;
  document.querySelectorAll('.section').forEach(sec => {{
    let secVisible = false;
    sec.querySelectorAll('.card').forEach(c => {{
      const match = c.textContent.toLowerCase().includes(q);
      c.style.display = match ? '' : 'none';
      if (match) secVisible = true;
    }});
    sec.style.display = secVisible ? '' : 'none';
    if (secVisible) anyVisible = true;
  }});
  // A week heading with nothing left under it is just noise while searching.
  document.querySelectorAll('.week').forEach(wk => {{
    const has = Array.from(wk.querySelectorAll('.section'))
      .some(s => s.style.display !== 'none');
    wk.style.display = has ? '' : 'none';
  }});
  document.getElementById('noResults').style.display = anyVisible ? 'none' : 'block';
}});
</script>
</body>
</html>'''

    with open(os.path.join(OUT_DIR, "repro_index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    print("Created: repro_index.html")


if __name__ == "__main__":
    main()

# Repro "Highest Yield" drag-and-drops (spec)

We are building a separate set of exactly **10** cross-brick drag-and-drop
games for the Reproductive Systems course. Together they should cover the
**highest-yield, most testable** facts of all 61 bricks: what NBME/Step 1 and
the course exams ask most often. This is the "night before the exam" set. Each
game synthesizes across several bricks; none restates a single brick's game.

You write **5** of the 10, for your half of the course (given in your prompt).

## Sources
- `C:\study-tools\repro-dragndrop\repro_data\brick_NN.py`: the existing per-brick
  games. These are already distilled facts in the exact data format. Start here.
- `C:\study-tools\repro_build\text\brick_NN.txt`: the full lecture text. Use it
  (Grep / partial reads) to confirm facts and to judge what each lecture
  emphasizes. Do not read every file end to end; you don't need to.
- Course conventions win: e.g. the course says **PMOS** (not PCOS). Brick 18
  has an author placeholder gap, so author nothing from it. One lecture wrongly
  calls SIDS "the leading cause of infant death"; the correct framing is the
  leading cause from 1 month to 1 year.

## Choosing the 5 games
Pick the 5 themes in your half that are the most heavily tested. Suggested
themes follow; replace any of them if the lectures clearly point to something
higher-yield:
- **Weeks 1-3 (bricks 1-38):** embryologic origins and classic congenital
  defects; hormone sources, actions and the HPG axis; amenorrhea / disorders
  of sexual development (key labs and mechanism); gonadal and uterine tumors
  (marker, histology hallmark, association); STIs and genital infections
  (organism, hallmark finding, first-line treatment).
- **Weeks 4-6 (bricks 39-61):** pregnancy hormones and maternal physiology;
  pregnancy complications (hypertensive disorders, GDM, ectopic, previa,
  abruption, accreta, GTD); TORCH and teratogens; labor, postpartum and
  neonatal (PPH causes, postpartum mood disorders, fetal circulation shunts,
  Apgar and milestones); breast pathology (hallmark, histology,
  receptor/management).

## Format (Python, exactly like the brick files)
Write `C:\study-tools\repro-dragndrop\repro_data\highyield_partN.py` (N given
in your prompt):

```python
GAMES = [
    {
        "slug": "short_snake_case",
        "title": "Title Case Name of the Game",
        "subtitle": "Match each X to its A, B and C",
        "categories": ["A", "B", "C"],
        "sources": [12, 13, 19],          # brick numbers this game draws on
        "data": {
            "Row label": {"A": "...", "B": "...", "C": "..."},
            ...
        },
    },
    ...
]
```

- Each game has **7-9 rows** and **exactly 3 categories**. Every row fills
  every category.
- Each value is short, about 3-12 words and at most about 75 characters, like
  the existing games.
- **No giveaways.** A value must not repeat a distinctive word from its own
  row label (row "Placenta accreta" → value "abnormal accretion" is bad).
  Within a column, keep values parallel in length and form so the longest or
  most specific one isn't the obvious match. Avoid duplicate values within a
  column unless they are genuinely the same answer.
- Every fact must be correct and consistent with the lectures. When the
  lecture and standard board teaching differ, follow board teaching and say so
  in your reply.
- Choose the rows within a theme by testability: classic buzzword
  associations, "most common" facts, first-line treatments, pathognomonic
  findings, key labs.

Validate before you finish: run
`py -c "import importlib.util as u;s=u.spec_from_file_location('m',r'<your file>');m=u.module_from_spec(s);s.loader.exec_module(m);print([(g['slug'],len(g['data'])) for g in m.GAMES])"`
and also check that every row has all 3 categories.

Reply with: the 5 titles, rows per game, the source bricks, and any lecture
vs board-teaching conflicts you resolved.

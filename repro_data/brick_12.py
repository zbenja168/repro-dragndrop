BRICK = {
    "brick_num": 12,
    "brick_title": "Ovulation and the Menstrual Cycle",
    "games": [
        {
            "slug": "follicle_stages",
            "title": "Stages of Folliculogenesis",
            "subtitle": "Match each follicle stage to its granulosa arrangement, defining feature, and gonadotropin requirement",
            "categories": ["Granulosa cells", "Defining feature", "Gonadotropin requirement"],
            "data": {
                "Primordial follicle": {
                    "Granulosa cells": "Single flattened layer around the oocyte",
                    "Defining feature": "Forms during fetal development; primary oocyte arrested in prophase I",
                    "Gonadotropin requirement": "Independent; activating signals incompletely understood"
                },
                "Primary follicle": {
                    "Granulosa cells": "Single cuboidal layer around the enlarging oocyte",
                    "Defining feature": "Gap junctions develop between oocyte and granulosa cells",
                    "Gonadotropin requirement": "Independent of gonadotropin secretion"
                },
                "Secondary follicle": {
                    "Granulosa cells": "Multiple proliferating layers, still avascular",
                    "Defining feature": "Distinct outer theca develops and becomes vascularized",
                    "Gonadotropin requirement": "Independent through the mid-secondary stage"
                },
                "Tertiary (antral) follicle": {
                    "Granulosa cells": "Proliferation supported by FSH",
                    "Defining feature": "Fluid-filled antrum forms; one follicle selected as dominant",
                    "Gonadotropin requirement": "Gonadotropin dependent"
                },
                "Ovulatory (Graafian) follicle": {
                    "Granulosa cells": "Express LH receptors induced by FSH late in maturation",
                    "Defining feature": "Ruptures with the LH surge, releasing a secondary oocyte",
                    "Gonadotropin requirement": "Requires the preovulatory LH surge"
                }
            }
        },
        {
            "slug": "cycle_hormones",
            "title": "Hormones of the Cycle",
            "subtitle": "Match each hormone to its source, main action, and regulation",
            "categories": ["Source", "Main action", "Regulation"],
            "data": {
                "GnRH": {
                    "Source": "Hypothalamus, into the hypophyseal-portal circulation",
                    "Main action": "Stimulates anterior-pituitary gonadotropes to release LH and FSH",
                    "Regulation": "Secreted in pulses; pulse frequency varies with cycle phase"
                },
                "LH": {
                    "Source": "Anterior-pituitary gonadotropes",
                    "Main action": "Stimulates theca cells to produce androstenedione",
                    "Regulation": "Surges when sustained high estradiol produces positive feedback"
                },
                "FSH": {
                    "Source": "Anterior-pituitary gonadotropes",
                    "Main action": "Stimulates granulosa aromatase to convert androstenedione to estradiol",
                    "Regulation": "Selectively suppressed by inhibin from granulosa cells"
                },
                "Estradiol": {
                    "Source": "Granulosa cells of developing follicles",
                    "Main action": "Stimulates proliferation of the functional endometrium",
                    "Regulation": "Negative feedback most of the follicular phase; positive when sustained high"
                },
                "Progesterone": {
                    "Source": "Corpus luteum during the luteal phase",
                    "Main action": "Drives secretory differentiation and endometrial receptivity",
                    "Regulation": "Falls when the corpus luteum regresses without hCG"
                },
                "hCG": {
                    "Source": "Trophoblast cells after implantation",
                    "Main action": "Maintains the corpus luteum and its progesterone secretion",
                    "Regulation": "Appears only if a blastocyst implants"
                }
            }
        },
        {
            "slug": "cycle_phases",
            "title": "Phases of the Ovarian and Uterine Cycles",
            "subtitle": "Match each phase to its timing, dominant hormonal event, and key structural change",
            "categories": ["Timing", "Dominant hormonal event", "Key structural change"],
            "data": {
                "Follicular phase": {
                    "Timing": "Day 1 of menstruation to ovulation; duration varies",
                    "Dominant hormonal event": "FSH rises, then estradiol and inhibin B climb from the growing cohort",
                    "Key structural change": "Dominant follicle selected; less-responsive follicles undergo atresia"
                },
                "Ovulation": {
                    "Timing": "Near day 14 of a representative 28-day cycle",
                    "Dominant hormonal event": "LH surge; primary oocyte completes meiosis I",
                    "Key structural change": "Proteolytic remodeling ruptures the follicular wall, releasing the oocyte"
                },
                "Luteal phase": {
                    "Timing": "Ovulation to the onset of the next menstruation",
                    "Dominant hormonal event": "Corpus luteum secretes progesterone, estradiol, and inhibin A",
                    "Key structural change": "Ruptured follicle luteinizes into a vascular corpus luteum"
                },
                "Menstrual phase": {
                    "Timing": "Begins on day 1 of the cycle",
                    "Dominant hormonal event": "Progesterone and estradiol fall as the corpus luteum regresses",
                    "Key structural change": "Functional endometrium breaks down and is shed"
                },
                "Proliferative phase": {
                    "Timing": "End of menstruation to ovulation",
                    "Dominant hormonal event": "Estradiol from developing follicles predominates",
                    "Key structural change": "Glands and stroma regenerate; progesterone receptors are expressed"
                },
                "Secretory phase": {
                    "Timing": "Ovulation to the next menstruation, in the uterine cycle",
                    "Dominant hormonal event": "Progesterone transforms the estradiol-primed endometrium",
                    "Key structural change": "Glands become tortuous and secretory; mitotic activity decreases"
                }
            }
        },
        {
            "slug": "feedback_signals",
            "title": "Feedback Signals on the Hypothalamus and Pituitary",
            "subtitle": "Match each signal to its source, feedback effect, and cycle timing",
            "categories": ["Source", "Feedback effect", "When in the cycle"],
            "data": {
                "Inhibin B": {
                    "Source": "Granulosa cells of developing follicles",
                    "Feedback effect": "Selectively decreases FSH secretion",
                    "When in the cycle": "Follicular phase, as the cohort grows"
                },
                "Inhibin A": {
                    "Source": "Dominant follicle, then predominantly the corpus luteum",
                    "Feedback effect": "Contributes to suppression of FSH secretion",
                    "When in the cycle": "Late follicular phase and luteal phase"
                },
                "Moderate estradiol": {
                    "Source": "Granulosa cells of the growing cohort",
                    "Feedback effect": "Suppresses gonadotropin secretion (negative feedback)",
                    "When in the cycle": "Most of the follicular phase"
                },
                "Sustained high estradiol": {
                    "Source": "Dominant preovulatory follicle",
                    "Feedback effect": "Positive feedback generating the preovulatory LH surge",
                    "When in the cycle": "Late follicular phase"
                },
                "Luteal progesterone": {
                    "Source": "Lipid-rich cells of the corpus luteum",
                    "Feedback effect": "Suppresses GnRH and gonadotropin secretion with estradiol and inhibin A",
                    "When in the cycle": "Luteal phase, under LH support"
                }
            }
        }
    ]
}

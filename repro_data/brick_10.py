BRICK = {
    "brick_num": 10,
    "brick_title": "Estrogen and Progesterone",
    "games": [
        {
            "slug": "steroid_source_cells",
            "title": "Where the Sex Steroids Are Made",
            "subtitle": "Match each site of synthesis to its stimulus, key enzyme feature, and hormone output",
            "categories": ["Stimulus / regulator", "Key enzyme feature", "Hormone output"],
            "data": {
                "Theca cell": {
                    "Stimulus / regulator": "LH from the anterior pituitary binds its receptor",
                    "Key enzyme feature": "Desmolase converts cholesterol to pregnenolone",
                    "Hormone output": "Androstenedione, which diffuses to the granulosa cell"
                },
                "Granulosa cell": {
                    "Stimulus / regulator": "FSH from the anterior pituitary induces the enzyme",
                    "Key enzyme feature": "Aromatase converts androstenedione to estradiol",
                    "Hormone output": "17beta-estradiol; also secretes inhibin"
                },
                "Corpus luteum": {
                    "Stimulus / regulator": "hCG from the early embryo prevents its involution",
                    "Key enzyme feature": "Luteinized theca and granulosa cells contribute different enzymes",
                    "Hormone output": "Large amounts of progesterone, plus estrogen, after ovulation"
                },
                "Extragonadal tissues (adipose, bone, skin, brain, breast, liver)": {
                    "Stimulus / regulator": "Works independently of ovarian cyclic activity",
                    "Key enzyme feature": "Locally expressed aromatase acts on circulating androgens",
                    "Hormone output": "Estrone from androstenedione; estradiol from testosterone"
                }
            }
        },
        {
            "slug": "hpg_axis_regulators",
            "title": "Hormones of the Hypothalamic-Pituitary-Gonadal Axis",
            "subtitle": "Match each regulator to its source, primary action, and regulatory detail",
            "categories": ["Source", "Primary action", "Regulatory detail"],
            "data": {
                "GnRH": {
                    "Source": "Hypothalamus, released in pulses",
                    "Primary action": "Drives LH and FSH release from the anterior pituitary",
                    "Regulatory detail": "Continuous release would downregulate its pituitary receptors"
                },
                "LH": {
                    "Source": "Anterior pituitary gonadotropin",
                    "Primary action": "Binds theca cells to start androgen synthesis",
                    "Regulatory detail": "Surges when sustained high estradiol switches to positive feedback"
                },
                "FSH": {
                    "Source": "Anterior pituitary, alongside LH",
                    "Primary action": "Induces aromatase in granulosa cells",
                    "Regulatory detail": "Its decline restricts maturation to the dominant follicle"
                },
                "Inhibin": {
                    "Source": "Granulosa cells of the follicle",
                    "Primary action": "Selectively suppresses FSH secretion",
                    "Regulatory detail": "Acts on the anterior pituitary as negative feedback"
                },
                "Activin": {
                    "Source": "Ovary and anterior pituitary",
                    "Primary action": "Promotes FSH synthesis and secretion",
                    "Regulatory detail": "Balances inhibin so follicles are recruited, then trimmed"
                },
                "hCG": {
                    "Source": "Early embryo after implantation",
                    "Primary action": "Rescues the corpus luteum from degeneration",
                    "Regulatory detail": "Keeps progesterone up to maintain the endometrium in pregnancy"
                }
            }
        },
        {
            "slug": "hormone_target_effects",
            "title": "Estrogen or Progesterone: Who Does What",
            "subtitle": "Match each target to the hormone responsible, its effect, and the consequence the brick highlights",
            "categories": ["Hormone responsible", "Effect", "Consequence noted in the brick"],
            "data": {
                "Bone": {
                    "Hormone responsible": "Estrogen",
                    "Effect": "Increases bone mass",
                    "Consequence noted in the brick": "Menopausal loss raises osteoclast activity, causing osteoporosis and fractures"
                },
                "Plasma lipoproteins": {
                    "Hormone responsible": "Estrogen",
                    "Effect": "Raises HDL and lowers LDL cholesterol",
                    "Consequence noted in the brick": "Lipid profile shifts with estrogen status"
                },
                "Breast ductal system": {
                    "Hormone responsible": "Estrogen",
                    "Effect": "Promotes growth and maintenance of the ducts",
                    "Consequence noted in the brick": "Part of preparing the breasts for pregnancy"
                },
                "Endometrium after ovulation": {
                    "Hormone responsible": "Progesterone",
                    "Effect": "Differentiates it into secretory endometrium and maintains it",
                    "Consequence noted in the brick": "Prevents excessive growth that could cause endometrial hyperplasia"
                },
                "Cervical mucus": {
                    "Hormone responsible": "Progesterone",
                    "Effect": "Thickens it, limiting sperm penetration",
                    "Consequence noted in the brick": "Also helps reduce ascending microbial entry"
                },
                "Hypothalamic thermoregulatory center": {
                    "Hormone responsible": "Progesterone",
                    "Effect": "Raises body temperature",
                    "Consequence noted in the brick": "Body temperature climbs in the luteal phase"
                }
            }
        },
        {
            "slug": "steroid_molecules_compared",
            "title": "The Steroid Cast: Estradiol, Estrone, Progesterone, Androstenedione",
            "subtitle": "Match each molecule to its class, where it is made, and its signature fact",
            "categories": ["Class", "Where it is made", "Signature fact"],
            "data": {
                "17beta-estradiol": {
                    "Class": "Principal naturally occurring estrogen",
                    "Where it is made": "Granulosa cells aromatize androstenedione; peripherally from testosterone",
                    "Signature fact": "Circulates bound to albumin and sex hormone-binding globulin"
                },
                "Estrone (E1)": {
                    "Class": "Estrogen interconvertible with estradiol via 17beta-HSD",
                    "Where it is made": "Extragonadal aromatase acting on androstenedione",
                    "Signature fact": "Predominant circulating estrogen after menopause"
                },
                "Progesterone": {
                    "Class": "Principal naturally occurring progestogen",
                    "Where it is made": "Luteal cells of the corpus luteum after ovulation",
                    "Signature fact": "Circulates bound to albumin and corticosteroid-binding globulin"
                },
                "Androstenedione": {
                    "Class": "Androgen that serves as an estrogen precursor",
                    "Where it is made": "Theca cells, several steps downstream of desmolase",
                    "Signature fact": "Diffuses into the granulosa cell to be aromatized"
                }
            }
        }
    ]
}

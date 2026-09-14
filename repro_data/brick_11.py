BRICK = {
    "brick_num": 11,
    "brick_title": "Androgens",
    "games": [
        {
            "slug": "androgen_lineup",
            "title": "Meet the Androgens",
            "subtitle": "Match each androgen to its main source, relative potency, and signature actions",
            "categories": ["Main source", "Relative potency", "Signature actions"],
            "data": {
                "Testosterone": {
                    "Main source": "Leydig cells of the testes",
                    "Relative potency": "Major circulating active androgen",
                    "Signature actions": "Wolffian-duct differentiation, spermatogenesis, muscle growth"
                },
                "Dihydrotestosterone (DHT)": {
                    "Main source": "Formed from testosterone by 5-alpha-reductase in target tissues",
                    "Relative potency": "More potent androgen-receptor agonist than testosterone",
                    "Signature actions": "External genitalia and prostate differentiation; male-pattern balding"
                },
                "DHEA / DHEAS": {
                    "Main source": "Adrenal cortex, rising at adrenarche",
                    "Relative potency": "Weak; gains potency after peripheral conversion",
                    "Signature actions": "Pubic and axillary hair, body odor, sebaceous-gland activity"
                },
                "Androstenedione": {
                    "Main source": "Ovaries; also part of the precursor pool",
                    "Relative potency": "Weak androgen that is mainly a precursor",
                    "Signature actions": "Converted peripherally to testosterone or estrogens"
                }
            }
        },
        {
            "slug": "hpg_axis_signals",
            "title": "HPG Axis Signals",
            "subtitle": "Match each hormone to where it comes from, what it does, and what regulates it",
            "categories": ["Secreted by", "Main action", "Regulated by"],
            "data": {
                "GnRH": {
                    "Secreted by": "Hypothalamus, in pulses",
                    "Main action": "Stimulates gonadotropes to secrete LH and FSH",
                    "Regulated by": "Suppressed at the hypothalamus by testosterone and estradiol"
                },
                "LH": {
                    "Secreted by": "Anterior-pituitary gonadotropes (with FSH)",
                    "Main action": "Stimulates Leydig cells to synthesize testosterone",
                    "Regulated by": "Inhibited by testosterone and its estradiol metabolite"
                },
                "FSH": {
                    "Secreted by": "Anterior-pituitary gonadotropes (with LH)",
                    "Main action": "Acts on Sertoli cells to support spermatogenesis",
                    "Regulated by": "Selectively inhibited by inhibin B"
                },
                "Inhibin B": {
                    "Secreted by": "Sertoli cells of the seminiferous tubules",
                    "Main action": "Selectively decreases pituitary FSH secretion",
                    "Regulated by": "Falls when Sertoli activity and sperm production decline"
                },
                "Testosterone": {
                    "Secreted by": "Leydig cells, between the seminiferous tubules",
                    "Main action": "High local levels support Sertoli cells and spermatogenesis",
                    "Regulated by": "Rises and falls with LH stimulation"
                }
            }
        },
        {
            "slug": "androgen_sources",
            "title": "Where Androgens Come From",
            "subtitle": "Match each androgen-producing site to its stimulus, its contribution, and a key detail",
            "categories": ["Stimulus / input", "Androgen contribution", "Key detail"],
            "data": {
                "Testicular Leydig cells": {
                    "Stimulus / input": "LH after puberty; hCG during fetal life",
                    "Androgen contribution": "Most circulating testosterone in adult males",
                    "Key detail": "Needs StAR-mediated cholesterol transport into mitochondria"
                },
                "Testicular Sertoli cells": {
                    "Stimulus / input": "FSH plus high intratesticular testosterone",
                    "Androgen contribution": "Support spermatogenesis and secrete inhibin B",
                    "Key detail": "Tight junctions form the blood-testis barrier"
                },
                "Ovarian theca cells": {
                    "Stimulus / input": "LH",
                    "Androgen contribution": "Ovarian testosterone and androstenedione",
                    "Key detail": "A direct testosterone source in premenopausal females"
                },
                "Adrenal cortex": {
                    "Stimulus / input": "ACTH",
                    "Androgen contribution": "DHEA and DHEAS",
                    "Key detail": "Output rises at adrenarche, before gonadal puberty"
                },
                "Peripheral tissues (fat, skin, liver)": {
                    "Stimulus / input": "Circulating DHEA and androstenedione precursors",
                    "Androgen contribution": "Convert precursors into testosterone",
                    "Key detail": "Proportionally more important as ovarian output declines"
                }
            }
        },
        {
            "slug": "androgen_clinical",
            "title": "Androgens in the Clinic",
            "subtitle": "Match each scenario to its mechanism, its hormone-axis effect, and its clinical picture",
            "categories": ["Mechanism", "Hormone / axis effect", "Clinical picture"],
            "data": {
                "Anabolic steroid abuse": {
                    "Mechanism": "Exogenous androgens feed back on the hypothalamus and pituitary",
                    "Hormone / axis effect": "Low GnRH, LH, FSH and low intratesticular testosterone",
                    "Clinical picture": "Testicular atrophy, infertility, erythrocytosis, hypertension"
                },
                "Chronic alcohol use": {
                    "Mechanism": "Less GnRH and LH release; liver clears estrogens poorly",
                    "Hormone / axis effect": "Impaired Leydig- and Sertoli-cell function, more estrogenic effect",
                    "Clinical picture": "Low libido, erectile dysfunction, gynecomastia"
                },
                "Congenital adrenal hyperplasia": {
                    "Mechanism": "Adrenal disorder with excess androgen production",
                    "Hormone / axis effect": "Elevated circulating adrenal androgens",
                    "Clinical picture": "Virilized traits in individuals assigned female at birth"
                },
                "Complete androgen insensitivity": {
                    "Mechanism": "Nonfunctional androgen receptors in a 46,XY individual",
                    "Hormone / axis effect": "Androgens are present but cannot act on target tissues",
                    "Clinical picture": "Testes with female-pattern external genitalia; androgen therapy ineffective"
                },
                "hCG therapy": {
                    "Mechanism": "Activates LH receptors on Leydig cells",
                    "Hormone / axis effect": "Maintains intratesticular testosterone production",
                    "Clinical picture": "Used in selected hypogonadotropic hypogonadism and infertility"
                }
            }
        }
    ]
}

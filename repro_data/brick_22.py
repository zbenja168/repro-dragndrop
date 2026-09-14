BRICK = {
    "brick_num": 22,
    "brick_title": "Ovarian Cysts",
    "games": [
        {
            "slug": "cyst_types",
            "title": "Ovarian Cyst Types",
            "subtitle": "Match each ovarian lesion to its pathogenesis, hormone activity, and classic clue",
            "categories": ["Pathogenesis", "Hormone activity", "Classic clue"],
            "data": {
                "Follicular cyst": {
                    "Pathogenesis": "Unruptured follicle from anovulation or degeneration after rupture",
                    "Hormone activity": "Granulosa cells make estrogen",
                    "Classic clue": "Most common cyst; menorrhagia or longer cycles"
                },
                "Corpus luteum cyst": {
                    "Pathogenesis": "Persistence of corpus luteum cavity beyond 14 days",
                    "Hormone activity": "Theca cells keep producing progesterone",
                    "Classic clue": "Delayed menses; rupture causes intraperitoneal bleeding"
                },
                "Theca lutein cyst": {
                    "Pathogenesis": "hCG from molar pregnancy or choriocarcinoma stimulates theca lutein layer",
                    "Hormone activity": "Makes androstenedione, raising androgen levels",
                    "Classic clue": "Recedes when hCG levels decrease"
                },
                "Endometrioma": {
                    "Pathogenesis": "Ectopic endometrial tissue deposits on the ovary",
                    "Hormone activity": "No characteristic hormone overproduction",
                    "Classic clue": "Chocolate cyst of old blood; pain with menstruation"
                },
                "Neoplastic cyst": {
                    "Pathogenesis": "Arises with benign or malignant ovarian tumors",
                    "Hormone activity": "Not driven by normal ovulatory hormones",
                    "Classic clue": "Suspect when a cyst forms after menopause"
                }
            }
        },
        {
            "slug": "pmos_hormones",
            "title": "PMOS Hormone Cascade",
            "subtitle": "Match each hormone to its level in PMOS, the mechanism, and its downstream effect",
            "categories": ["Level in PMOS", "Mechanism", "Downstream effect"],
            "data": {
                "LH": {
                    "Level in PMOS": "Elevated (exaggerated response to GnRH)",
                    "Mechanism": "Increased anterior pituitary secretion",
                    "Downstream effect": "Stimulates theca interna cells to make androgen"
                },
                "FSH": {
                    "Level in PMOS": "Suppressed, raising the LH/FSH ratio",
                    "Mechanism": "Inhibited by elevated estrone",
                    "Downstream effect": "Follicle maturation is impaired"
                },
                "Androstenedione": {
                    "Level in PMOS": "High (focal ovarian hyperandrogenism)",
                    "Mechanism": "Made by LH-stimulated theca interna cells",
                    "Downstream effect": "Hirsutism, acne, and other virilizing signs"
                },
                "Estrone": {
                    "Level in PMOS": "High, especially with obesity",
                    "Mechanism": "Aromatization of androstenedione in adipose tissue",
                    "Downstream effect": "Unopposed estrogen risks endometrial hyperplasia and cancer"
                },
                "Progesterone": {
                    "Level in PMOS": "Low",
                    "Mechanism": "No corpus luteum forms without regular ovulation",
                    "Downstream effect": "Leaves estrogen unopposed on the endometrium"
                }
            }
        },
        {
            "slug": "cyst_workup",
            "title": "Evaluating a Pelvic Mass",
            "subtitle": "Match each test or approach to its role, best-use setting, and key caveat",
            "categories": ["Role", "Best-use setting", "Key caveat"],
            "data": {
                "Pelvic ultrasound": {
                    "Role": "First test for any pelvic mass",
                    "Best-use setting": "Distinguishing cystic from solid tissue",
                    "Key caveat": "Initial evaluation for all cysts, whatever the age"
                },
                "Serum CA 125": {
                    "Role": "Blood test to help rule out ovarian cancer",
                    "Best-use setting": "Most useful in postmenopausal patients",
                    "Key caveat": "High false-positive rate in premenopausal patients"
                },
                "Serial ultrasounds": {
                    "Role": "Conservative observation of most cysts",
                    "Best-use setting": "Asymptomatic cysts likely to resolve",
                    "Key caveat": "Persistent, symptomatic, or enlarging cysts need surgery instead"
                },
                "Diagnostic laparoscopy": {
                    "Role": "Provides a definitive tissue diagnosis",
                    "Best-use setting": "Cysts whose size or appearance raises doubt",
                    "Key caveat": "Reserved for selected patients, not routine"
                },
                "Open surgery": {
                    "Role": "Removal when malignancy is suspected preoperatively",
                    "Best-use setting": "Suspected cancer, sometimes with bilateral oophorectomy",
                    "Key caveat": "Chosen because cyst rupture and tumor spread are less likely"
                }
            }
        },
        {
            "slug": "pmos_treatment",
            "title": "PMOS Treatment Toolkit",
            "subtitle": "Match each therapy to its indication, mechanism or class, and key point",
            "categories": ["Indication", "Mechanism or class", "Key point"],
            "data": {
                "Combined oral contraceptives": {
                    "Indication": "Irregular menses in PMOS",
                    "Mechanism or class": "Combined estrogen-progestin pills",
                    "Key point": "Also help reduce androgen excess"
                },
                "Spironolactone or eplerenone": {
                    "Indication": "Hirsutism",
                    "Mechanism or class": "Antiandrogen therapy",
                    "Key point": "Adjunct to oral contraceptives, with contraception ensured"
                },
                "Clomiphene": {
                    "Indication": "Regaining fertility in anovulatory patients",
                    "Mechanism or class": "SERM: mixed estrogen-receptor agonist-antagonist",
                    "Key point": "Adverse effects include pelvic pain and hot flashes"
                },
                "Nutrition and weight management": {
                    "Indication": "Obesity and diabetes when present",
                    "Mechanism or class": "Education and supportive lifestyle care",
                    "Key point": "Targets obesity, itself a risk factor for PMOS"
                }
            }
        }
    ]
}

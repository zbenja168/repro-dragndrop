BRICK = {
    "brick_num": 27,
    "brick_title": "Testicular Tumors",
    "games": [
        {
            "slug": "gct_pathology",
            "title": "Germ Cell Tumor Pathology",
            "subtitle": "Match each germ cell tumor to its gross appearance, hallmark histology, and typical age at onset",
            "categories": ["Gross appearance", "Hallmark histology", "Typical age at onset"],
            "data": {
                "Seminoma": {
                    "Gross appearance": "Well-demarcated, homogeneous, pale fleshy mass",
                    "Hallmark histology": "\"Fried egg\" cells with pale nuclei and lymphocytic infiltrate",
                    "Typical age at onset": "Mean age 40 years; most common single GCT subtype"
                },
                "Embryonal carcinoma": {
                    "Gross appearance": "Hemorrhagic, necrotic, poorly demarcated from surroundings",
                    "Hallmark histology": "Primitive cells with pleomorphic nuclei, prominent nucleoli, necrosis",
                    "Typical age at onset": "20-30 years, about a decade earlier than seminoma"
                },
                "Yolk sac tumor": {
                    "Gross appearance": "Waxy, tan-yellow mass with mucoid glistening cut surface",
                    "Hallmark histology": "Schiller-Duval bodies resembling primitive glomeruli",
                    "Typical age at onset": "Children under 3-4 years; rare in pure form in adults"
                },
                "Choriocarcinoma": {
                    "Gross appearance": "Necrosis and hemorrhage; hemorrhagic metastases common",
                    "Hallmark histology": "Cytotrophoblasts plus multinucleate syncytiotrophoblasts",
                    "Typical age at onset": "20-30 years; the least common and most aggressive GCT"
                },
                "Teratoma": {
                    "Gross appearance": "Variegated cut surface with cysts from multiple tissue types",
                    "Hallmark histology": "Tissues from two or more germ layers, e.g. cartilage and epidermis",
                    "Typical age at onset": "Any age; usually benign in children, malignant in adults"
                }
            }
        },
        {
            "slug": "presentation_markers",
            "title": "Presentations and Tumor Markers",
            "subtitle": "Match each tumor to its typical patient, distinctive clinical clue, and hormone or marker finding",
            "categories": ["Typical patient", "Distinctive clinical clue", "Hormone or marker finding"],
            "data": {
                "Seminoma": {
                    "Typical patient": "Man around age 40 with a painless testicular mass",
                    "Distinctive clinical clue": "Spreads first to para-aortic lymph nodes",
                    "Hormone or marker finding": "Beta-hCG elevated in a subset; AFP not elevated"
                },
                "Embryonal carcinoma": {
                    "Typical patient": "Man in his 20s; half have metastases at diagnosis",
                    "Distinctive clinical clue": "May present as a painful mass, unlike most tumors",
                    "Hormone or marker finding": "AFP and beta-hCG may both be elevated"
                },
                "Yolk sac tumor": {
                    "Typical patient": "Boy younger than 3-4 years old",
                    "Distinctive clinical clue": "Most common testicular tumor of infants and young children",
                    "Hormone or marker finding": "Elevated AFP; not elevated in seminomatous GCTs"
                },
                "Choriocarcinoma": {
                    "Typical patient": "Man in his 20s with widespread hemorrhagic metastases",
                    "Distinctive clinical clue": "Hyperthyroidism symptoms and gynecomastia from hormone cross-reactivity",
                    "Hormone or marker finding": "Serum beta-hCG invariably and often markedly elevated"
                },
                "Leydig cell tumor": {
                    "Typical patient": "Any age, most common between 10 and 50 years",
                    "Distinctive clinical clue": "Precocious puberty in boys; gynecomastia from estradiol conversion",
                    "Hormone or marker finding": "Excess testosterone, partly converted to 17-beta-estradiol"
                }
            }
        },
        {
            "slug": "nongct_older_men",
            "title": "Non-Germ Cell and Older-Patient Tumors",
            "subtitle": "Match each tumor to its cell of origin, typical age, distinguishing feature, and behavior",
            "categories": ["Cell of origin", "Typical age", "Distinguishing feature", "Behavior and management"],
            "data": {
                "Leydig cell tumor": {
                    "Cell of origin": "Testosterone-producing stromal cells",
                    "Typical age": "Any age; most common between 10 and 50 years",
                    "Distinguishing feature": "Golden-brown gross color; Reinke crystals in eosinophilic cytoplasm",
                    "Behavior and management": "Usually benign and hormonally active; orchiectomy usually sufficient"
                },
                "Sertoli cell tumor": {
                    "Cell of origin": "Stromal cells that support sperm production and transport",
                    "Typical age": "Adults, average age 45 years",
                    "Distinguishing feature": "Tubule-like structures ringed by thick pink basement membrane",
                    "Behavior and management": "Hormonally silent; mostly benign but about 10% malignant"
                },
                "Testicular lymphoma": {
                    "Cell of origin": "B lymphocytes; usually diffuse large B-cell lymphoma",
                    "Typical age": "Men older than 60 years",
                    "Distinguishing feature": "Often bilateral; commonly recurs in the central nervous system",
                    "Behavior and management": "Malignant; chemotherapy plus scrotal irradiation after orchiectomy"
                },
                "Spermatocytic tumor": {
                    "Cell of origin": "Germ cells; formerly called spermatocytic seminoma",
                    "Typical age": "Usually older than 50 years",
                    "Distinguishing feature": "Variably sized cells without lymphocytic infiltrate; gain of 9q",
                    "Behavior and management": "Indolent; not associated with germ cell neoplasia in situ"
                }
            }
        },
        {
            "slug": "workup_treatment",
            "title": "Work-up and Treatment Decisions",
            "subtitle": "Match each clinical scenario to the recommended management and its key rationale",
            "categories": ["Recommended management", "Key rationale"],
            "data": {
                "New solid testicular mass": {
                    "Recommended management": "Testicular ultrasound, then radical inguinal orchiectomy",
                    "Key rationale": "Intratesticular solid masses are malignant until proven otherwise"
                },
                "Suspected cancer at surgery": {
                    "Recommended management": "Inguinal approach with early high ligation of the spermatic cord",
                    "Key rationale": "Trans-scrotal surgery seeds tumor and disrupts lymphatic drainage"
                },
                "Localized seminoma after orchiectomy": {
                    "Recommended management": "Active surveillance with beta-hCG levels and imaging",
                    "Key rationale": "Excellent prognosis; 5-year survival around 92% with normal AFP"
                },
                "High-risk localized nonseminomatous GCT": {
                    "Recommended management": "Chemotherapy or retroperitoneal lymph node dissection",
                    "Key rationale": "Embryonal subtype, cord/scrotal involvement, or lymphovascular invasion"
                },
                "Sex cord stromal tumor": {
                    "Recommended management": "Diagnostic orchiectomy alone is usually sufficient",
                    "Key rationale": "Leydig and Sertoli cell tumors are usually benign"
                },
                "Testicular lymphoma after orchiectomy": {
                    "Recommended management": "Chemotherapy plus scrotal irradiation",
                    "Key rationale": "Reduces the risk of recurrence in the contralateral testicle"
                }
            }
        }
    ]
}

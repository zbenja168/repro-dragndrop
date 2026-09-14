BRICK = {
    "brick_num": 29,
    "brick_title": "Prostate Cancer",
    "games": [
        {
            "slug": "adt_pharmacology",
            "title": "Androgen Deprivation Pharmacology",
            "subtitle": "Match each drug class to its example agents, mechanism, and distinctive clinical point",
            "categories": ["Example agents", "Mechanism", "Distinctive clinical point"],
            "data": {
                "GnRH agonists": {
                    "Example agents": "Leuprolide, goserelin",
                    "Mechanism": "Continuous dosing desensitizes and downregulates pituitary GnRH receptors, lowering LH",
                    "Distinctive clinical point": "Initial testosterone flare can worsen bone pain, obstruction, or cord compression"
                },
                "GnRH antagonists": {
                    "Example agents": "Degarelix, relugolix",
                    "Mechanism": "Directly block pituitary GnRH receptors",
                    "Distinctive clinical point": "Rapid fall in LH and testosterone with no initial flare"
                },
                "Androgen-receptor antagonists": {
                    "Example agents": "Bicalutamide, flutamide, enzalutamide",
                    "Mechanism": "Prevent androgens from activating androgen receptors in cancer cells",
                    "Distinctive clinical point": "First-generation agent limits agonist tumor flare; hepatotoxicity and gynecomastia"
                },
                "CYP17 inhibitor": {
                    "Example agents": "Abiraterone",
                    "Mechanism": "Blocks androgen synthesis in testes, adrenal glands, and tumor tissue",
                    "Distinctive clinical point": "Given with a glucocorticoid; hypertension, hypokalemia, and edema"
                }
            }
        },
        {
            "slug": "diagnostic_workup",
            "title": "Diagnosing Prostate Cancer",
            "subtitle": "Match each diagnostic step to what it assesses, its key detail, and its main caveat",
            "categories": ["What it assesses", "Key detail", "Main caveat"],
            "data": {
                "PSA test": {
                    "What it assesses": "Protein secreted by prostate epithelial cells, used for early detection",
                    "Key detail": "Age-specific reference ranges rise as the prostate enlarges",
                    "Main caveat": "False positives from prostatitis, BPH, retention, and prostate manipulation"
                },
                "Digital rectal exam": {
                    "What it assesses": "Irregular nodularity palpable on the posterior surface of the gland",
                    "Key detail": "Reaches the peripheral zone, where most cancers arise",
                    "Main caveat": "Complementary assessment only, not a routine primary screening test"
                },
                "TRUS core biopsy": {
                    "What it assesses": "Histologic confirmation, the only way to truly diagnose the cancer",
                    "Key detail": "Typically 10-12 cores; extended protocols use about 12-18",
                    "Main caveat": "Performed only once clinical suspicion is already high"
                },
                "Gleason grading": {
                    "What it assesses": "Architectural pattern of the tumor under the microscope",
                    "Key detail": "Two most prevalent patterns are summed for a score of 2-10",
                    "Main caveat": "Patterns 1 and 2 are not assigned on biopsy, so reports run 6-10"
                },
                "TNM staging": {
                    "What it assesses": "Extent of tumor, nodal disease, and distant metastases",
                    "Key detail": "Initial clinical stage uses DRE, PSA level, and histologic exam",
                    "Main caveat": "Bone scan or CT reserved for a worrisome clinical stage"
                }
            }
        },
        {
            "slug": "management_strategies",
            "title": "Choosing a Management Strategy",
            "subtitle": "Match each strategy to its best-fit patient, what it involves, and its key drawback",
            "categories": ["Best-fit patient", "What it involves", "Key drawback or adverse effect"],
            "data": {
                "Watchful waiting": {
                    "Best-fit patient": "Limited life expectancy under 10 years, low-to-intermediate risk",
                    "What it involves": "Observation at regular visits with no intent for curative treatment",
                    "Key drawback or adverse effect": "Only palliative treatment offered if disease progresses"
                },
                "Active surveillance": {
                    "Best-fit patient": "Good life expectancy over 10-20 years with low-risk disease",
                    "What it involves": "Regular PSA tests, DREs, and repeat prostate biopsies",
                    "Key drawback or adverse effect": "Curative treatment deferred; requires ongoing monitoring and biopsies"
                },
                "Radical prostatectomy": {
                    "Best-fit patient": "Localized cancer treated surgically with curative intent",
                    "What it involves": "Removal of prostate and seminal vesicles, often with node dissection",
                    "Key drawback or adverse effect": "Erectile dysfunction and urinary incontinence"
                },
                "Radiotherapy": {
                    "Best-fit patient": "Localized disease; ADT may be added for higher-risk cases",
                    "What it involves": "External beam radiation or brachytherapy",
                    "Key drawback or adverse effect": "Radiation proctitis, irritative urinary symptoms, hematuria"
                },
                "Docetaxel chemotherapy": {
                    "Best-fit patient": "Advanced or metastatic disease, including castration-resistant cancer",
                    "What it involves": "Taxane that stabilizes microtubules and prevents mitosis",
                    "Key drawback or adverse effect": "Systemic therapy reserved for advanced disease, not localized cancer"
                }
            }
        },
        {
            "slug": "routes_of_spread",
            "title": "How Prostate Cancer Spreads",
            "subtitle": "Match each route or feature of spread to its typical target and its clinical clue",
            "categories": ["Typical site or target", "Clinical clue"],
            "data": {
                "Local extension": {
                    "Typical site or target": "Prostatic urethra and adjacent pelvic tissue",
                    "Clinical clue": "Urethral stenosis progressing to retention and renal failure"
                },
                "Lymphatic dissemination": {
                    "Typical site or target": "Regional pelvic nodes, usually internal iliac",
                    "Clinical clue": "Nodal involvement found during staging, the N of TNM"
                },
                "Hematogenous spread": {
                    "Typical site or target": "Lumbar spine, proximal femur, pelvis, thoracic spine, ribs",
                    "Clinical clue": "Back pain from osteoblastic vertebral metastases"
                },
                "Perineural invasion": {
                    "Typical site or target": "Nerves in and around the prostate gland",
                    "Clinical clue": "Characteristic pathologic feature that promotes local tumor extension"
                }
            }
        }
    ]
}

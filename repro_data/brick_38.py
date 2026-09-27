BRICK = {
    "brick_num": 38,
    "brick_title": "Vulvar Pathologies",
    "games": [
        {
            "slug": "vulvar_lesion_recognition",
            "title": "Vulvar Lesion Recognition",
            "subtitle": "Match each vulvar condition to its appearance, pathogenesis and route to diagnosis",
            "categories": ["Clinical appearance", "Pathogenesis", "Diagnosis"],
            "data": {
                "Lichen sclerosus": {
                    "Clinical appearance": "Smooth white atrophic plaques, fused labia, figure-eight perianal spread",
                    "Pathogenesis": "Autoimmune; activated T cells, linked to thyroid disease and vitiligo",
                    "Diagnosis": "Clinical; biopsy only when the diagnosis is uncertain",
                },
                "Lichen simplex chronicus": {
                    "Clinical appearance": "Thickened, leathery, hyperpigmented skin with excoriations",
                    "Pathogenesis": "Self-perpetuating itch-scratch cycle causing lichenification",
                    "Diagnosis": "Clinical; history of waking at night to scratch",
                },
                "Vulvar squamous cell carcinoma": {
                    "Clinical appearance": "Unifocal plaque, ulcer or mass; multifocal in only 5%",
                    "Pathogenesis": "High-risk HPV (VIN) or p53 mutation via dVIN",
                    "Diagnosis": "Biopsy required; never by gross or colposcopic look alone",
                },
                "Extramammary Paget disease": {
                    "Clinical appearance": "Erythematous, eczematous, often weeping pruritic plaque",
                    "Pathogenesis": "Intraepithelial adenocarcinoma of mucin-secreting cells",
                    "Diagnosis": "Biopsy showing large pale CK7-positive Paget cells",
                },
            },
        },
        {
            "slug": "vulvar_scc_two_pathways",
            "title": "Two Pathways to Vulvar SCC",
            "subtitle": "Sort each precursor or carcinoma by driver, microscopy and typical patient",
            "categories": ["Driver", "Microscopic features", "Typical patient"],
            "data": {
                "Classic VIN (vulvar HSIL)": {
                    "Driver": "High-risk HPV, commonly HPV-16",
                    "Microscopic features": "Full-thickness small immature basaloid cells, no invasion",
                    "Typical patient": "Younger woman with cervical-lesion-type risk factors",
                },
                "Differentiated VIN (dVIN)": {
                    "Driver": "p53 mutation from chronic oxidative stress",
                    "Microscopic features": "Superficial maturation, hyperkeratosis, basal-cell atypia, no invasion",
                    "Typical patient": "Older woman with long-standing lichen sclerosus",
                },
                "HPV-associated invasive SCC": {
                    "Driver": "Progression of HPV-related intraepithelial neoplasia",
                    "Microscopic features": "Invasive basaloid cells with foci of central necrosis",
                    "Typical patient": "About 30% of cases; younger females",
                },
                "HPV-independent invasive SCC": {
                    "Driver": "Chronic inflammation, e.g. lichen sclerosus, via dVIN",
                    "Microscopic features": "Keratinizing tumor nests with central keratin pearls",
                    "Typical patient": "About 70% of cases; average age 75",
                },
            },
        },
        {
            "slug": "vulvar_management",
            "title": "Managing Vulvar Pathology",
            "subtitle": "Match each condition to its primary treatment, alternative and extra step",
            "categories": ["Primary treatment", "Alternative or escalation", "Additional consideration"],
            "data": {
                "Lichen sclerosus": {
                    "Primary treatment": "Clobetasol 0.05%, then reduced-frequency maintenance",
                    "Alternative or escalation": "Tacrolimus if steroids fail; surgery for functional scarring",
                    "Additional consideration": "Long-term surveillance for vulvar squamous cell carcinoma",
                },
                "Symptomatic Bartholin cyst or abscess": {
                    "Primary treatment": "Drainage with Word catheter placement",
                    "Alternative or escalation": "Marsupialization, particularly for recurrent lesions",
                    "Additional consideration": "New mass after age 40: biopsy to exclude carcinoma",
                },
                "HPV-associated VIN (vulvar HSIL)": {
                    "Primary treatment": "Surgical excision or laser ablation",
                    "Alternative or escalation": "Topical imiquimod when invasion is not suspected",
                    "Additional consideration": "Precursor that shares cervical-lesion risk factors",
                },
                "Invasive vulvar SCC": {
                    "Primary treatment": "Wide/radical local excision or vulvectomy by stage",
                    "Alternative or escalation": "Adjuvant radiation for positive nodes or margins",
                    "Additional consideration": "Inguinal lymph node evaluation; chemoradiation if unresectable",
                },
                "Extramammary Paget disease": {
                    "Primary treatment": "Wide local excision or vulvectomy by extent",
                    "Alternative or escalation": "More conservative surgery if elderly or frail",
                    "Additional consideration": "Look for synchronous carcinoma (breast, rectum, bladder)",
                },
            },
        },
    ],
}

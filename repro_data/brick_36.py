BRICK = {
    "brick_num": 36,
    "brick_title": "Syphilis and Other Ulcerative STIs",
    "games": [
        {
            "slug": "syphilis_stages",
            "title": "Stages of Syphilis",
            "subtitle": "Match each stage to its timing, hallmark findings, and penicillin regimen",
            "categories": ["Timing", "Hallmark findings", "Treatment"],
            "data": {
                "Primary syphilis": {
                    "Timing": "Lasts about 3-6 weeks, then resolves spontaneously",
                    "Hallmark findings": "Firm, round, painless 1-2 cm chancre with bilateral adenopathy",
                    "Treatment": "Single IM dose of 2.4 million units benzathine penicillin G"
                },
                "Secondary syphilis": {
                    "Timing": "Follows in roughly 25% of untreated primary cases",
                    "Hallmark findings": "Contagious nonpruritic rash on palms and soles, condylomata lata, alopecia",
                    "Treatment": "Same single IM benzathine dose used for primary disease"
                },
                "Early latent syphilis": {
                    "Timing": "Initial infection within the previous 12 months",
                    "Hallmark findings": "Asymptomatic; organism still in blood, found on screening",
                    "Treatment": "One IM benzathine injection, as for other early syphilis"
                },
                "Late latent syphilis": {
                    "Timing": "Initial infection more than 12 months earlier",
                    "Hallmark findings": "Asymptomatic for years; often detected on routine screening",
                    "Treatment": "Three weekly IM injections of benzathine penicillin G"
                },
                "Neurosyphilis": {
                    "Timing": "Classic forms appear 10-30 years after untreated infection",
                    "Hallmark findings": "Tabes dorsalis, general paresis, Argyll Robertson pupils",
                    "Treatment": "Intravenous aqueous crystalline penicillin G"
                }
            }
        },
        {
            "slug": "late_manifestations",
            "title": "Tertiary and Congenital Syphilis",
            "subtitle": "Match each late or congenital form to its onset, findings, and underlying lesion",
            "categories": ["Onset", "Key findings", "Underlying lesion or process"],
            "data": {
                "Gummatous syphilis": {
                    "Onset": "Presents 4-10 years after infection",
                    "Key findings": "Rubbery masses in liver, bone, testes that may ulcerate",
                    "Underlying lesion or process": "Granulomas (gummas) that heal with scarring and fibrosis"
                },
                "Cardiovascular syphilis": {
                    "Onset": "Presents 10-30 years after infection",
                    "Key findings": "Aortic valve insufficiency with a diastolic murmur",
                    "Underlying lesion or process": "Vasa vasorum inflammation causing ascending aortic aneurysm"
                },
                "Tabes dorsalis": {
                    "Onset": "Decades after untreated infection, as a neurosyphilis form",
                    "Key findings": "Lost proprioception, vibration, and touch sensation",
                    "Underlying lesion or process": "Degeneration of the posterior columns of the spinal cord"
                },
                "Early congenital syphilis": {
                    "Onset": "Under 2 years of age, often in the first months",
                    "Key findings": "Snuffles, palm-sole rash, hepatomegaly, lymphadenopathy",
                    "Underlying lesion or process": "Transplacental infection, most often from untreated early disease"
                },
                "Late congenital syphilis": {
                    "Onset": "Over 2 years of age in untreated children",
                    "Key findings": "Hutchinson teeth, saber shins, saddle nose, rhagades",
                    "Underlying lesion or process": "Also interstitial keratitis and sensorineural hearing loss"
                }
            }
        },
        {
            "slug": "syphilis_testing",
            "title": "Syphilis Laboratory Tests",
            "subtitle": "Match each test to what it detects, how it is used, and how to read it",
            "categories": ["What it detects", "Clinical role", "Interpretation pitfall"],
            "data": {
                "RPR / VDRL / TRUST": {
                    "What it detects": "Antibodies reacting with intracellular microsome components",
                    "Clinical role": "Cheap, sensitive initial screening test",
                    "Interpretation pitfall": "False positives in SLAP HIM conditions, up to 5% of tests"
                },
                "FTA-ABS / TPPA / CIA": {
                    "What it detects": "Antibodies against specific treponemal antigens",
                    "Clinical role": "Confirms a positive screening result",
                    "Interpretation pitfall": "Stays reactive for life regardless of clinical state"
                },
                "Quantitative nontreponemal titer": {
                    "What it detects": "Level of nontreponemal antibody over time",
                    "Clinical role": "Tracks response to therapy after treatment",
                    "Interpretation pitfall": "Falls and may become nonreactive after cure"
                },
                "Dark-field microscopy": {
                    "What it detects": "Tightly coiled spirochetes against a dark background",
                    "Clinical role": "Directly visualizes T. pallidum from lesions",
                    "Interpretation pitfall": "Needed because the organism is too thin for light microscopy"
                },
                "Infant vs parent RPR titer": {
                    "What it detects": "Relative nontreponemal titers in newborn and birth parent",
                    "Clinical role": "Supports a diagnosis of congenital syphilis",
                    "Interpretation pitfall": "Only a neonatal titer at least 4-fold higher is strongly suggestive"
                }
            }
        },
        {
            "slug": "ulcerative_sti_comparison",
            "title": "Bacterial Genital Ulcers Compared",
            "subtitle": "Sort the organism, microbiology, lesion, nodes, and treatment into each disease",
            "categories": ["Organism", "Microbiology", "Ulcer", "Lymph nodes", "Treatment"],
            "data": {
                "Primary syphilis": {
                    "Organism": "Treponema pallidum",
                    "Microbiology": "Tightly coiled spirochete; nearly impossible to culture",
                    "Ulcer": "Firm, round, painless chancre",
                    "Lymph nodes": "Mild to moderate bilateral lymphadenopathy",
                    "Treatment": "Benzathine penicillin G, single IM dose"
                },
                "Chancroid": {
                    "Organism": "Haemophilus ducreyi",
                    "Microbiology": "Gram-negative bacillus",
                    "Ulcer": "Painful, purulent gray-yellow base that bleeds when scraped",
                    "Lymph nodes": "Tender, suppurative inguinal adenopathy",
                    "Treatment": "Azithromycin or ceftriaxone"
                },
                "Donovanosis": {
                    "Organism": "Klebsiella granulomatis",
                    "Microbiology": "Intracellular gram-negative rod seen with Wright or Giemsa stain",
                    "Ulcer": "Beefy red, painless, highly vascular, bleeds easily",
                    "Lymph nodes": "No surrounding swollen lymph nodes",
                    "Treatment": "Azithromycin alone as treatment of choice"
                },
                "Lymphogranuloma venereum": {
                    "Organism": "Chlamydia trachomatis specific subtypes",
                    "Microbiology": "Obligate intracellular bacterium",
                    "Ulcer": "Small self-limiting ulcerating papules",
                    "Lymph nodes": "Inguinal buboes with the groove sign",
                    "Treatment": "Azithromycin, the recommended agent"
                }
            }
        }
    ]
}

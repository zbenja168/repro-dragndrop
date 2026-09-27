BRICK = {
    "brick_num": 34,
    "brick_title": "Reproductive: HIV",
    "games": [
        {
            "slug": "arv_drug_classes",
            "title": "Antiretroviral Drug Classes",
            "subtitle": "Match each drug class to its mechanism, adverse effects and example",
            "categories": ["Mechanism", "Adverse effects", "Example drug"],
            "data": {
                "NRTIs": {
                    "Mechanism": "Nucleoside/nucleotide analogs that terminate viral DNA chain elongation",
                    "Adverse effects": "Mitochondrial toxicity: lactic acidosis and hepatic steatosis",
                    "Example drug": "Tenofovir, lamivudine, zidovudine"
                },
                "NNRTIs": {
                    "Mechanism": "Bind reverse transcriptase at a non-nucleoside site",
                    "Adverse effects": "Rash, hepatotoxicity, neuropsychiatric effects",
                    "Example drug": "Efavirenz"
                },
                "INSTIs": {
                    "Mechanism": "Block insertion of viral DNA into the host genome",
                    "Adverse effects": "Headache, insomnia, weight gain; cations reduce absorption",
                    "Example drug": "Bictegravir, dolutegravir, cabotegravir"
                },
                "Protease inhibitors": {
                    "Mechanism": "Prevent cleavage of viral polyproteins and virion maturation",
                    "Adverse effects": "GI effects, hyperlipidemia, insulin resistance, drug interactions",
                    "Example drug": "Ritonavir, also used as a CYP450-inhibiting booster"
                },
                "Entry/fusion inhibitors": {
                    "Mechanism": "Prevent HIV from binding to or fusing with host cells",
                    "Adverse effects": "Injection-site reactions",
                    "Example drug": "Enfuvirtide (T-20)"
                }
            }
        },
        {
            "slug": "key_arv_drugs",
            "title": "High-Yield Individual Antiretrovirals",
            "subtitle": "Match each drug to its class, key clinical use and must-know pearl",
            "categories": ["Class", "Key clinical use", "Must-know pearl"],
            "data": {
                "Zidovudine (AZT)": {
                    "Class": "Thymidine analog NRTI",
                    "Key clinical use": "Intrapartum IV dosing and neonatal prophylaxis",
                    "Must-know pearl": "Bone marrow suppression; monitor the CBC"
                },
                "Lamivudine (3TC)": {
                    "Class": "Cytosine analog NRTI",
                    "Key clinical use": "Backbone partner in ART and PEP regimens",
                    "Must-know pearl": "Stopping it in HIV/HBV coinfection can cause HBV flare"
                },
                "Tenofovir": {
                    "Class": "Nucleotide analog NRTI",
                    "Key clinical use": "Daily oral PrEP combined with emtricitabine",
                    "Must-know pearl": "Can affect kidney function and bone mineral density"
                },
                "Cabotegravir": {
                    "Class": "Long-acting integrase strand transfer inhibitor",
                    "Key clinical use": "Injectable PrEP given every 2 months",
                    "Must-know pearl": "Polyvalent cations like calcium reduce INSTI absorption"
                },
                "Enfuvirtide (T-20)": {
                    "Class": "Fusion inhibitor that binds gp41",
                    "Key clinical use": "Selected cases of drug-resistant HIV",
                    "Must-know pearl": "Subcutaneous; local pain, erythema and nodules"
                }
            }
        },
        {
            "slug": "hiv_testing_scenarios",
            "title": "HIV Testing Scenarios",
            "subtitle": "Match each clinical scenario to the right test or action, its reasoning and a key detail",
            "categories": ["Test or action", "Reasoning", "Key detail"],
            "data": {
                "Routine screening": {
                    "Test or action": "HIV-1/2 antigen/antibody immunoassay (ELISA)",
                    "Reasoning": "First test in almost all scenarios",
                    "Key detail": "Detects p24 antigen plus HIV IgM and IgG"
                },
                "Reactive initial screen": {
                    "Test or action": "Antibody-differentiation immunoassay or NAAT",
                    "Reasoning": "Confirms the diagnosis after a positive screen",
                    "Key detail": "Differentiation assay separates HIV-1 from HIV-2"
                },
                "Newborn of a person with HIV": {
                    "Test or action": "NAT instead of the antigen/antibody screen",
                    "Reasoning": "Maternal IgG crosses the placenta, giving false positives",
                    "Key detail": "Test at 14-21 days, 1-2 months, 4-6 months"
                },
                "Acute retroviral syndrome, negative screen": {
                    "Test or action": "Test by NAAT; do not rule out HIV",
                    "Reasoning": "High-risk exposure plus symptoms keeps suspicion high",
                    "Key detail": "Fever, sore throat, lymphadenopathy, maculopapular rash"
                },
                "Very recent exposure": {
                    "Test or action": "Precautions to limit exposing others plus follow-up testing",
                    "Reasoning": "Even NAAT cannot detect very recent infection",
                    "Key detail": "Repeat testing later rather than declaring negative"
                }
            }
        },
        {
            "slug": "hiv_prevention_treatment",
            "title": "HIV Prevention and Treatment Regimens",
            "subtitle": "Match each strategy to its timing, typical regimen and key caveat",
            "categories": ["Timing", "Typical regimen", "Key caveat"],
            "data": {
                "Oral PrEP": {
                    "Timing": "Taken daily before any possible exposure",
                    "Typical regimen": "Tenofovir disoproxil fumarate/emtricitabine",
                    "Key caveat": "TAF/emtricitabine not for receptive vaginal sex risk"
                },
                "Injectable PrEP": {
                    "Timing": "Every 2 months after initiation",
                    "Typical regimen": "Long-acting cabotegravir injection",
                    "Key caveat": "An INSTI option for people avoiding daily pills"
                },
                "PEP": {
                    "Timing": "Ideally within 24 h, no later than 72 h",
                    "Typical regimen": "Bictegravir/emtricitabine/tenofovir alafenamide",
                    "Key caveat": "Continued for a full 28-day course"
                },
                "Initial ART": {
                    "Timing": "Once HIV infection is confirmed",
                    "Typical regimen": "An INSTI plus two NRTIs",
                    "Key caveat": "Suppresses but cannot eradicate integrated viral DNA"
                },
                "Perinatal prevention": {
                    "Timing": "During delivery and after birth",
                    "Typical regimen": "Intrapartum IV then neonatal zidovudine",
                    "Key caveat": "IV dosing when maternal viral load is high or unknown"
                }
            }
        }
    ]
}

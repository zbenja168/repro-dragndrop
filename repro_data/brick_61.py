BRICK = {
    "brick_num": 61,
    "brick_title": "Breast Cancer Screening: Early Detection to Diagnosis",
    "games": [
        {
            "slug": "pathway_by_scenario",
            "title": "Screening or Diagnostic? Pick the Pathway",
            "subtitle": "Match each patient scenario to its next step and the goal of that step",
            "categories": ["Next step", "Goal of this step"],
            "data": {
                "Asymptomatic, average risk": {
                    "Next step": "Routine screening mammography pathway",
                    "Goal of this step": "Detect clinically silent disease early to reduce mortality"
                },
                "Asymptomatic, strong family history or known mutation": {
                    "Next step": "Earlier or more intensive screening strategy",
                    "Goal of this step": "Match screening intensity to her higher risk"
                },
                "New palpable breast mass": {
                    "Next step": "In-person clinical breast exam, then imaging",
                    "Goal of this step": "Clarify whether disease is present; skip routine screening"
                },
                "Callback after screening mammogram": {
                    "Next step": "Targeted diagnostic mammography and/or ultrasound",
                    "Goal of this step": "Better characterize the finding seen on screening"
                },
                "Suspicion persists after diagnostic imaging": {
                    "Next step": "Core needle biopsy of the solid lesion",
                    "Goal of this step": "Obtain tissue to confirm or exclude malignancy"
                }
            }
        },
        {
            "slug": "diagnostic_pathway_steps",
            "title": "From Abnormal Screen to Diagnosis",
            "subtitle": "Place each step of the diagnostic pathway and match what it involves and achieves",
            "categories": ["Order in pathway", "What it involves", "What it accomplishes"],
            "data": {
                "Diagnostic imaging": {
                    "Order in pathway": "First step after a screening callback",
                    "What it involves": "Targeted mammography and/or ultrasound",
                    "What it accomplishes": "Decides whether the abnormality remains suspicious"
                },
                "Biopsy": {
                    "Order in pathway": "Second, if suspicion remains after imaging",
                    "What it involves": "Core needle sampling of a suspicious solid lesion",
                    "What it accomplishes": "Supplies the tissue needed for a definitive diagnosis"
                },
                "Pathology": {
                    "Order in pathway": "Third, once tissue has been obtained",
                    "What it involves": "Tissue review plus ER, PR, and HER2 testing",
                    "What it accomplishes": "Confirms malignancy and guides further management"
                },
                "Specialist referral": {
                    "Order in pathway": "Fourth, after cancer is confirmed",
                    "What it involves": "Breast specialist or multidisciplinary team",
                    "What it accomplishes": "Coordinated care and treatment planning"
                },
                "Nurse navigation": {
                    "Order in pathway": "Runs alongside every step of the workup",
                    "What it involves": "Nurse guides the patient through the process",
                    "What it accomplishes": "Improves care coordination and supports the patient"
                }
            }
        },
        {
            "slug": "imaging_and_reporting",
            "title": "Mammography Concepts",
            "subtitle": "Match each imaging concept to what it is and its key clinical point",
            "categories": ["What it is", "Key clinical point"],
            "data": {
                "2D mammography": {
                    "What it is": "Flat images of the breast",
                    "Key clinical point": "Overlapping tissue may obscure lesions"
                },
                "3D tomosynthesis": {
                    "What it is": "Layered images of the breast",
                    "Key clinical point": "Better detection of small lesions; fewer false-positive callbacks"
                },
                "BI-RADS": {
                    "What it is": "Category system for mammography findings",
                    "Key clinical point": "Guides recommendations for follow-up imaging or biopsy"
                },
                "Breast density": {
                    "What it is": "Fibroglandular tissue relative to fatty tissue",
                    "Key clinical point": "Normal finding; modest risk rise; harder to see lesions"
                },
                "Callback": {
                    "What it is": "Request for additional imaging after screening",
                    "Key clinical point": "Relatively common; does not confirm cancer"
                }
            }
        },
        {
            "slug": "barriers_and_responses",
            "title": "Barriers to Follow-Up and Patient-Centered Responses",
            "subtitle": "Match each barrier to a supportive response and its goal",
            "categories": ["Patient-centered response", "Goal"],
            "data": {
                "Limited transportation": {
                    "Patient-centered response": "Connect with community transportation assistance",
                    "Goal": "Get her to imaging and follow-up visits"
                },
                "Financial constraints": {
                    "Patient-centered response": "Link to community partners offering financial support",
                    "Goal": "Keep cost from blocking the diagnostic workup"
                },
                "Fear after an abnormal result": {
                    "Patient-centered response": "Calm, non-alarmist 'we need more information' framing",
                    "Goal": "Reduce anxiety and encourage timely engagement"
                },
                "Inflexible work schedule": {
                    "Patient-centered response": "Offer flexible appointment times when possible",
                    "Goal": "Make the care plan practical and achievable"
                },
                "Uncertainty moving through the workup": {
                    "Patient-centered response": "Guidance from a nurse navigator",
                    "Goal": "Coordinate imaging, biopsy, and referral steps"
                }
            }
        }
    ]
}

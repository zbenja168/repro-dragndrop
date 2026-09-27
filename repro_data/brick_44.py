BRICK = {
    "brick_num": 44,
    "brick_title": "Gestational Diabetes",
    "games": [
        {
            "slug": "pregnancy_glucose_metabolism",
            "title": "Glucose Metabolism in Pregnancy",
            "subtitle": "Match each metabolic state to its insulin picture, glucose result and key point",
            "categories": ["Insulin picture", "Maternal glucose result", "Key point"],
            "data": {
                "First half of pregnancy": {
                    "Insulin picture": "Pancreatic insulin secretion rises; glucose used efficiently",
                    "Maternal glucose result": "Lower serum glucose levels",
                    "Key point": "Fat deposition, delayed gastric emptying, increased appetite",
                },
                "Second and third trimesters (normal)": {
                    "Insulin picture": "hPL-driven insulin resistance; secretion up 50-100%",
                    "Maternal glucose result": "Euglycemia maintained; postprandial glucose rises",
                    "Key point": "Increased lipolysis; glucose redirected to the fetus",
                },
                "Between meals and sleep (normal)": {
                    "Insulin picture": "Relative resistance but normal pancreatic insulin response",
                    "Maternal glucose result": "Hypoglycemia compared with the nonpregnant state",
                    "Key point": "Fetus keeps consuming glucose crossing the placenta",
                },
                "Gestational diabetes mellitus": {
                    "Insulin picture": "Insulin resistance with inadequate insulin secretion",
                    "Maternal glucose result": "Maternal and subsequent fetal hyperglycemia",
                    "Key point": "Fetal insulin rises, driving fat deposition and polyuria",
                },
            },
        },
        {
            "slug": "gdm_complications",
            "title": "Complications of GDM",
            "subtitle": "Match each complication to its cause, defining feature and consequence",
            "categories": ["Cause in GDM", "Defining feature", "Consequence"],
            "data": {
                "Preeclampsia": {
                    "Cause in GDM": "Major maternal complication associated with GDM",
                    "Defining feature": "Hypertension and proteinuria, usually after 20 weeks",
                    "Consequence": "Untreated, can cause maternal and fetal death",
                },
                "Polyhydramnios": {
                    "Cause in GDM": "Fetal hyperglycemia causes fetal polyuria",
                    "Defining feature": "Excess amniotic fluid on ultrasound",
                    "Consequence": "Cord prolapse, abruption, preterm labor, uterine atony",
                },
                "Fetal macrosomia": {
                    "Cause in GDM": "High glucose overfeeds the fetus in utero",
                    "Defining feature": "Most common GDM complication; LGA infant",
                    "Consequence": "Cesarean for fetal-pelvic disproportion",
                },
                "Shoulder dystocia": {
                    "Cause in GDM": "Widest part of an LGA baby gets stuck",
                    "Defining feature": "Impacted shoulders during vaginal delivery",
                    "Consequence": "Erb palsy (C5-C6), clavicle fracture, hypoxia",
                },
            },
        },
        {
            "slug": "gdm_testing",
            "title": "Testing for GDM",
            "subtitle": "Match each test to how it is done, how to read it and its role",
            "categories": ["How it is done", "How to read it", "Role in GDM"],
            "data": {
                "1-hour 50-g glucose screen": {
                    "How it is done": "50-g glucose drink, blood glucose drawn at 1 hour",
                    "How to read it": "140 mg/dL or greater fails the screen",
                    "Role in GDM": "Initial screening test",
                },
                "3-hour 100-g glucose tolerance test": {
                    "How it is done": "Fasting draw, 100-g drink, draws at 1, 2 and 3 hours",
                    "How to read it": "Values compared against predefined cutoffs",
                    "Role in GDM": "Confirmatory diagnostic test after a failed screen",
                },
                "Hemoglobin A1c": {
                    "How it is done": "Glycosylated hemoglobin reflecting chronic hyperglycemia",
                    "How to read it": "Sometimes used to assist the diagnosis",
                    "Role in GDM": "Not yet part of most official GDM criteria",
                },
                "Urine glucose": {
                    "How it is done": "Checks for glucose spilled into the urine",
                    "How to read it": "Glucosuria is normal during pregnancy",
                    "Role in GDM": "Not useful for diagnosing GDM",
                },
                "Fingerstick fasting glucose": {
                    "How it is done": "Self-testing, usually four times daily",
                    "How to read it": "Above 95 mg/dL despite diet is too high",
                    "Role in GDM": "Judges treatment effect; triggers medication",
                },
            },
        },
        {
            "slug": "gdm_management",
            "title": "Managing GDM",
            "subtitle": "Match each management step to what it involves, when it applies and why",
            "categories": ["What it involves", "When it applies", "Purpose"],
            "data": {
                "Lifestyle therapy": {
                    "What it involves": "Exercise; 1800-2500 kcal/day at 40% carb, 40% fat, 20% protein",
                    "When it applies": "First line once GDM is confirmed",
                    "Purpose": "Most patients reach glucose targets this way",
                },
                "Pharmacologic therapy": {
                    "What it involves": "Insulin most often; metformin with less safety evidence",
                    "When it applies": "Fasting >95, 2-h >120 or 1-h >140 mg/dL despite diet",
                    "Purpose": "Meet targets that lifestyle change did not",
                },
                "Fetal surveillance": {
                    "What it involves": "Nonstress tests 1-2 times weekly plus ultrasound",
                    "When it applies": "Third trimester",
                    "Purpose": "Poor control raises risk of intrauterine fetal demise",
                },
                "Offered cesarean delivery": {
                    "What it involves": "Planned abdominal delivery",
                    "When it applies": "Ultrasound at term suggests fetal macrosomia",
                    "Purpose": "Avoid shoulder dystocia and other birth injury",
                },
                "Postpartum glucose check": {
                    "What it involves": "Glucose concentrations measured after delivery",
                    "When it applies": "24-72 hours postpartum",
                    "Purpose": "Detect type 2 diabetes mistakenly diagnosed as GDM",
                },
            },
        },
    ],
}

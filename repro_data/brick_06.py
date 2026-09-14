BRICK = {
    "brick_num": 6,
    "brick_title": "Sex Determination and Reproductive Systems Development",
    "games": [
        {
            "slug": "hormonal_signals",
            "title": "Hormonal Signals of Sex Determination",
            "subtitle": "Match each signal to its source, its developmental action, and what happens when it is absent",
            "categories": ["Source", "Main developmental action", "Result when absent"],
            "data": {
                "Testis-determining factor (TDF)": {
                    "Source": "Product of the SRY gene on the Y chromosome",
                    "Main developmental action": "Directs the indifferent gonad to become a testis",
                    "Result when absent": "Indifferent gonad follows the ovarian pathway"
                },
                "Anti-Müllerian hormone (AMH)": {
                    "Source": "Sertoli cells of the seminiferous tubules",
                    "Main developmental action": "Causes the paramesonephric (Müllerian) ducts to regress",
                    "Result when absent": "Müllerian ducts persist as uterine tubes, uterus, upper vagina"
                },
                "Testosterone": {
                    "Source": "Leydig cells of the testicular interstitium",
                    "Main developmental action": "Supports differentiation of the mesonephric (Wolffian) ducts",
                    "Result when absent": "Mesonephric ducts regress"
                },
                "Dihydrotestosterone (DHT)": {
                    "Source": "Made in target tissues from testosterone",
                    "Main developmental action": "Drives differentiation of the male external genitalia",
                    "Result when absent": "External genitalia develop along the female pathway"
                }
            }
        },
        {
            "slug": "duct_fates",
            "title": "Fates of the Indifferent Structures",
            "subtitle": "Match each embryonic structure to its fate in each sex and its key regulator or origin",
            "categories": ["Fate in the XY (male) embryo", "Fate in the XX (female) embryo", "Key regulator or origin"],
            "data": {
                "Mesonephric (Wolffian) ducts": {
                    "Fate in the XY (male) embryo": "Epididymis, ductus deferens, seminal vesicles, ejaculatory ducts",
                    "Fate in the XX (female) embryo": "Regress in the absence of testosterone",
                    "Key regulator or origin": "Retained by testosterone; began as embryonic kidney ducts"
                },
                "Paramesonephric (Müllerian) ducts": {
                    "Fate in the XY (male) embryo": "Regress under the influence of AMH",
                    "Fate in the XX (female) embryo": "Uterine tubes, uterus, and upper vagina",
                    "Key regulator or origin": "Persist when AMH and testosterone are absent"
                },
                "Urogenital sinus": {
                    "Fate in the XY (male) embryo": "Prostate and the pelvic portions of the urethra",
                    "Fate in the XX (female) embryo": "Lower (caudal) vagina and the short female urethra",
                    "Key regulator or origin": "Endoderm from the ventral division of the cloaca"
                },
                "Gubernaculum": {
                    "Fate in the XY (male) embryo": "Guides the testis into the scrotum, then regresses",
                    "Fate in the XX (female) embryo": "Becomes the ovarian ligament and round ligament of the uterus",
                    "Key regulator or origin": "Fibrous cord attaching the gonad to the labioscrotal swelling"
                }
            }
        },
        {
            "slug": "external_homologs",
            "title": "External Genitalia Homologs",
            "subtitle": "Match each precursor structure to its male and female derivatives",
            "categories": ["Male derivative", "Female derivative"],
            "data": {
                "Genital tubercle": {
                    "Male derivative": "Glans penis and most of the penile shaft",
                    "Female derivative": "Glans clitoris and part of the clitoral body"
                },
                "Urogenital folds": {
                    "Male derivative": "Fuse ventrally to form the penile urethra",
                    "Female derivative": "Labia minora and the urethral and vaginal openings"
                },
                "Labioscrotal swellings": {
                    "Male derivative": "Scrotum",
                    "Female derivative": "Labia majora"
                },
                "Urogenital sinus (glands)": {
                    "Male derivative": "Bulbourethral glands and prostate",
                    "Female derivative": "Greater vestibular, urethral, and paraurethral glands"
                }
            }
        },
        {
            "slug": "dsd_disorders",
            "title": "Disorders of Reproductive Development",
            "subtitle": "Match each condition to its underlying defect, classic presentation, and internal findings",
            "categories": ["Underlying defect", "Classic presentation", "Gonads and internal organs"],
            "data": {
                "Complete gonadal dysgenesis (46,XY Swyer)": {
                    "Underlying defect": "Impaired gonadal development despite a Y chromosome",
                    "Classic presentation": "Female phenotype with delayed puberty",
                    "Gonads and internal organs": "Nonfunctional streak gonads with low sex hormone production"
                },
                "Persistent Müllerian duct syndrome": {
                    "Underlying defect": "Abnormal AMH or abnormal AMH receptors",
                    "Classic presentation": "Cryptorchidism or inguinal hernia in a male",
                    "Gonads and internal organs": "Normal male organs plus a uterus and uterine tubes"
                },
                "Müllerian agenesis (MRKH)": {
                    "Underlying defect": "Failure of the Müllerian ducts to develop",
                    "Classic presentation": "No menstruation by age 16 with normal breast development",
                    "Gonads and internal organs": "Functioning ovaries; uterus and upper vagina absent"
                },
                "Prenatal DES exposure (XX fetus)": {
                    "Underlying defect": "Synthetic estrogen alters estrogen-dependent gene expression",
                    "Classic presentation": "T-shaped uterus and vaginal adenosis",
                    "Gonads and internal organs": "Ovaries are normal despite abnormal Müllerian development"
                },
                "Androgen excess (XX fetus)": {
                    "Underlying defect": "Excess androgen receptor signaling in the masculinization window",
                    "Classic presentation": "Clitoromegaly and labial fusion at birth",
                    "Gonads and internal organs": "Internal female organs remain normal"
                }
            }
        }
    ]
}

BRICK = {
    "brick_num": 33,
    "brick_title": "Neisseria gonorrhoeae and Chlamydia trachomatis",
    "games": [
        {
            "slug": "gonococcal_disease_spectrum",
            "title": "Gonococcal Disease Spectrum",
            "subtitle": "Match each gonococcal syndrome to its symptoms, signature finding and clinical pearl",
            "categories": ["Symptoms", "Signature finding", "Clinical pearl"],
            "data": {
                "Gonococcal urethritis": {
                    "Symptoms": "Burning on urination, itching, genital pustules",
                    "Signature finding": "Green, yellow, or white purulent urethral discharge",
                    "Clinical pearl": "Gram stain shows diplococci inside neutrophils"
                },
                "Gonococcal PID": {
                    "Symptoms": "Pelvic pain, abnormal bleeding, dyspareunia",
                    "Signature finding": "Ascends via endocervical glands into the uterus",
                    "Clinical pearl": "Tubal scarring causes infertility and ectopic pregnancy"
                },
                "Fitz-Hugh-Curtis syndrome": {
                    "Symptoms": "RUQ pain worsened by breathing, coughing, movement",
                    "Signature finding": "Inflammation of the Glisson capsule of the liver",
                    "Clinical pearl": "Perihepatitis arising as a complication of PID"
                },
                "Disseminated gonococcal infection": {
                    "Symptoms": "Triad of polyarthritis, tenosynovitis, and dermatitis",
                    "Signature finding": "Purulent synovial fluid, often >50,000 WBC/uL",
                    "Clinical pearl": "Top septic arthritis cause in young healthy adults"
                },
                "Gonococcal pharyngitis": {
                    "Symptoms": "Sore throat, or no symptoms at all",
                    "Signature finding": "Pharyngeal exudates with cervical lymphadenitis",
                    "Clinical pearl": "Acquired through oral sexual contact"
                },
                "Gonococcal ophthalmia neonatorum": {
                    "Symptoms": "Purulent conjunctivitis 2-5 days after birth",
                    "Signature finding": "Acquired during delivery through an infected vagina",
                    "Clinical pearl": "Prevented by ocular erythromycin ointment at birth"
                }
            }
        },
        {
            "slug": "chlamydial_syndromes",
            "title": "Chlamydia trachomatis Syndromes",
            "subtitle": "Match each chlamydial syndrome to its serovars or setting, findings and pearl",
            "categories": ["Serovars or setting", "Signature findings", "Clinical pearl"],
            "data": {
                "Chlamydial urethritis": {
                    "Serovars or setting": "Serovars D-K, sexually transmitted",
                    "Signature findings": "Clear, watery or mucoid discharge; mild dysuria",
                    "Clinical pearl": "Chlamydia is the most common STI in the US"
                },
                "Chlamydial PID": {
                    "Serovars or setting": "Ascending genital infection in females",
                    "Signature findings": "More frequent and more silent than gonococcal PID",
                    "Clinical pearl": "Strongly linked to infertility and ectopic pregnancy"
                },
                "Neonatal chlamydial conjunctivitis": {
                    "Serovars or setting": "Acquired at vaginal birth",
                    "Signature findings": "Less purulent; onset 5-14 days after birth",
                    "Clinical pearl": "Longer incubation than gonococcal conjunctivitis"
                },
                "Neonatal chlamydial pneumonia": {
                    "Serovars or setting": "Infant of a parent with untreated infection",
                    "Signature findings": "Staccato cough, tachypnea, and eosinophilia",
                    "Clinical pearl": "Bilateral interstitial infiltrates on imaging"
                },
                "Lymphogranuloma venereum": {
                    "Serovars or setting": "Serovars L1, L2, L3 (more invasive)",
                    "Signature findings": "Proctocolitis with anal ulcers and tenesmus",
                    "Clinical pearl": "May progress to painful inguinal lymphadenopathy"
                },
                "Trachoma": {
                    "Serovars or setting": "Serovars A, B, C; poor sanitation, eye-seeking flies",
                    "Signature findings": "Chronic follicular conjunctivitis and scarring",
                    "Clinical pearl": "Leading infectious cause of blindness worldwide"
                }
            }
        },
        {
            "slug": "virulence_and_pathogenesis",
            "title": "Virulence and Pathogenesis",
            "subtitle": "Match each virulence mechanism to its organism, action and consequence",
            "categories": ["Organism", "Action", "Consequence"],
            "data": {
                "Pili": {
                    "Organism": "N. gonorrhoeae",
                    "Action": "Attachment, aggregation, resist neutrophil killing",
                    "Consequence": "Adherence to host mucosal cells"
                },
                "Lipooligosaccharide (LOS)": {
                    "Organism": "N. gonorrhoeae (LPS variant)",
                    "Action": "Strong endotoxin activity; masks protein antigens",
                    "Consequence": "Binding to some host cell types"
                },
                "IgA protease": {
                    "Organism": "N. gonorrhoeae enzyme",
                    "Action": "Recognizes and cleaves IgA",
                    "Consequence": "Weakens mucosal antibody defense"
                },
                "Antigenic and phase variation": {
                    "Organism": "N. gonorrhoeae surface molecules",
                    "Action": "Alters structure or switches expression on and off",
                    "Consequence": "Repeat infection and poor vaccine efficacy"
                },
                "Membrane-bound inclusion": {
                    "Organism": "C. trachomatis",
                    "Action": "Houses reticulate bodies dividing by binary fission",
                    "Consequence": "Avoids lysosomal destruction"
                },
                "Th1 cells and IFN-gamma": {
                    "Organism": "Host response to C. trachomatis",
                    "Action": "Chronic inflammation from persistent infection",
                    "Consequence": "Immune-mediated damage, often before diagnosis"
                }
            }
        },
        {
            "slug": "treatment_by_scenario",
            "title": "Treatment by Scenario",
            "subtitle": "Match each clinical scenario to its regimen and rationale",
            "categories": ["Regimen", "Rationale"],
            "data": {
                "Uncomplicated gonorrhea, nonpregnant adult": {
                    "Regimen": "Single IM ceftriaxone + doxycycline for 7 days",
                    "Rationale": "Doxycycline covers chlamydia if not excluded"
                },
                "Gonorrhea in pregnancy": {
                    "Regimen": "Ceftriaxone + azithromycin for chlamydial coverage",
                    "Rationale": "Doxycycline is generally avoided in pregnancy"
                },
                "PID in pregnancy": {
                    "Regimen": "Hospitalize and give parenteral antibiotics",
                    "Rationale": "Reduces maternal and fetal complications"
                },
                "Every newborn": {
                    "Regimen": "Ocular erythromycin ointment shortly after birth",
                    "Rationale": "Prevents gonococcal ophthalmia neonatorum"
                },
                "Established gonococcal ophthalmia neonatorum": {
                    "Regimen": "Ceftriaxone; evaluate for disseminated infection",
                    "Rationale": "Erythromycin prophylaxis is no longer sufficient"
                },
                "Severe cephalosporin allergy": {
                    "Regimen": "Gentamicin plus azithromycin",
                    "Rationale": "Alternative when ceftriaxone cannot be used"
                }
            }
        }
    ]
}

BRICK = {
    "brick_num": 21,
    "brick_title": "Uterine Tumors",
    "games": [
        {
            "slug": "tcga_subtypes",
            "title": "TCGA Molecular Subtypes of Endometrial Cancer",
            "subtitle": "Match each molecular subtype to its genetics, typical patient, and prognosis",
            "categories": ["Defining molecular feature", "Typical patient or association", "Prognosis"],
            "data": {
                "POLE ultra-mutated": {
                    "Defining molecular feature": "Mutation in the exonuclease domain of DNA polymerase epsilon",
                    "Typical patient or association": "Younger, often thinner women; mostly endometrioid histology",
                    "Prognosis": "Exceptionally good with conventional therapy"
                },
                "Hypermutated (MSI)": {
                    "Defining molecular feature": "Defective mismatch repair with microsatellite instability",
                    "Typical patient or association": "Lynch syndrome; 54% of high-grade endometrioid carcinomas",
                    "Prognosis": "Intermediate survival despite frequent high-grade histology"
                },
                "Copy-number low": {
                    "Defining molecular feature": "Low mutation rate and few DNA copy-number abnormalities",
                    "Typical patient or association": "Younger patients with higher BMI or exogenous estrogen",
                    "Prognosis": "Intermediate survival; most common among low-grade tumors"
                },
                "Copy-number high": {
                    "Defining molecular feature": "Somatic TP53 mutations with frequent copy-number changes",
                    "Typical patient or association": "Over 95% of serous carcinomas; some high-grade endometrioid",
                    "Prognosis": "Aggressive, with the worst survival outcomes"
                }
            }
        },
        {
            "slug": "uterine_tumor_overview",
            "title": "Four Uterine Tumors at a Glance",
            "subtitle": "Match each tumor to its typical patient, histology, and behavior",
            "categories": ["Typical patient", "Histology", "Behavior and prognosis"],
            "data": {
                "Type I endometrioid carcinoma": {
                    "Typical patient": "Postmenopausal woman with chronic estrogen exposure",
                    "Histology": "Well-differentiated glands mimicking proliferative endometrium",
                    "Behavior and prognosis": "Usually indolent, with the better prognosis of the two types"
                },
                "Type II serous carcinoma": {
                    "Typical patient": "About 10 years older, arising in endometrial atrophy",
                    "Histology": "Papillae and tufts with marked atypia; psammoma bodies in 60%",
                    "Behavior and prognosis": "Invades myometrium, spreads to adnexa and pelvic nodes"
                },
                "Leiomyoma (fibroid)": {
                    "Typical patient": "Premenopausal woman; affects 60-70% of women in a lifetime",
                    "Histology": "Regular, well-differentiated spindle smooth muscle with hyalinization",
                    "Behavior and prognosis": "Benign and usually asymptomatic"
                },
                "Leiomyosarcoma": {
                    "Typical patient": "Postmenopausal woman with a rapidly enlarging mass",
                    "Histology": "Irregular cells, hyperchromatic nuclei, numerous mitotic figures",
                    "Behavior and prognosis": "Malignant; overall 5-year survival about 40%"
                }
            }
        },
        {
            "slug": "molecular_players",
            "title": "Genes, Pathways, and Drugs of Uterine Tumors",
            "subtitle": "Match each molecular player to its mechanism and its uterine disease link",
            "categories": ["Role or mechanism", "Uterine disease link"],
            "data": {
                "PI3K/AKT pathway": {
                    "Role or mechanism": "Mutations increase signaling, boosting estrogen receptor-dependent genes",
                    "Uterine disease link": "Most common mutations in type I endometrioid carcinoma"
                },
                "TP53 (p53)": {
                    "Role or mechanism": "Guardian of the genome on chromosome 17; DNA repair and cell cycle control",
                    "Uterine disease link": "Serous carcinoma with strong diffuse p53 on immunohistochemistry"
                },
                "POLE": {
                    "Role or mechanism": "Exonuclease domain mutations produce an ultra-high mutation burden",
                    "Uterine disease link": "Ultra-mutated subtype with an exceptionally good prognosis"
                },
                "Mismatch repair (MMR) genes": {
                    "Role or mechanism": "Defective function causes microsatellite instability",
                    "Uterine disease link": "Lynch syndrome-associated hypermutated endometrioid tumors"
                },
                "Tamoxifen": {
                    "Role or mechanism": "SERM: antagonist in breast tissue but weak estrogen agonist in uterus",
                    "Uterine disease link": "Endometrial proliferation, hyperplasia, polyps, and cancer risk"
                }
            }
        },
        {
            "slug": "myometrial_masses",
            "title": "Leiomyoma, Its Variants, and Leiomyosarcoma",
            "subtitle": "Match each myometrial lesion to its spread pattern and its nature and management",
            "categories": ["Growth or spread pattern", "Nature and key management point"],
            "data": {
                "Typical leiomyoma": {
                    "Growth or spread pattern": "Submucosal, intramural, or subserosal masses within the uterus",
                    "Nature and key management point": "Benign; NSAIDs, levonorgestrel IUD or OCPs, embolization; hysterectomy last"
                },
                "Intravenous leiomyomatosis": {
                    "Growth or spread pattern": "Extends into vessels, reaching the vena cava and right atrium",
                    "Nature and key management point": "Benign despite hematogenous spread to distant sites"
                },
                "Disseminated peritoneal leiomyomatosis": {
                    "Growth or spread pattern": "Multiple small nodules scattered across the peritoneum",
                    "Nature and key management point": "Benign despite its unusual multifocal behavior"
                },
                "Leiomyosarcoma": {
                    "Growth or spread pattern": "Invades locally and may metastasize beyond resectability",
                    "Nature and key management point": "Malignant; early surgery recommended, high fatality rate"
                }
            }
        }
    ]
}

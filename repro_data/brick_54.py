BRICK = {
    "brick_num": 54,
    "brick_title": "Fetal and Postnatal Circulation",
    "games": [
        {
            "slug": "fetal_vascular_structures",
            "title": "Fetal-Specific Vessels and Shunts",
            "subtitle": "Match each fetal structure to its course and its job in utero",
            "categories": ["Course / connection", "Function in utero"],
            "data": {
                "Umbilical vein": {
                    "Course / connection": "Placenta through the cord into the fetal abdomen, ending in the liver",
                    "Function in utero": "Carries the most oxygenated blood (about 80%) toward the fetal heart"
                },
                "Ductus venosus": {
                    "Course / connection": "Within the liver, from umbilical vein to inferior vena cava",
                    "Function in utero": "Diverts about half of umbilical venous blood past the liver"
                },
                "Foramen ovale": {
                    "Course / connection": "Hole with a one-way valve in the atrial septum",
                    "Function in utero": "Sends oxygenated IVC blood from right to left atrium, bypassing lungs"
                },
                "Ductus arteriosus": {
                    "Course / connection": "Pulmonary artery to descending aorta, distal to left subclavian",
                    "Function in utero": "Shunts right ventricular output away from the lungs into the aorta"
                },
                "Umbilical arteries": {
                    "Course / connection": "Paired vessels running from the fetus back to the placenta",
                    "Function in utero": "Return deoxygenated blood and wastes to the placenta"
                }
            }
        },
        {
            "slug": "fetal_oxygen_saturation_map",
            "title": "Fetal Oxygen Saturation Map",
            "subtitle": "Match each fetal site to its approximate saturation, inflow and outflow",
            "categories": ["Approx. O2 saturation", "Receives blood from", "Sends blood to"],
            "data": {
                "Umbilical vein": {
                    "Approx. O2 saturation": "About 80%",
                    "Receives blood from": "The placenta",
                    "Sends blood to": "Fetal liver and the ductus venosus"
                },
                "Foramen ovale": {
                    "Approx. O2 saturation": "About 67%",
                    "Receives blood from": "Right atrium (oxygenated IVC stream)",
                    "Sends blood to": "Left atrium, then left ventricle"
                },
                "Ascending aorta": {
                    "Approx. O2 saturation": "About 62%",
                    "Receives blood from": "Left ventricle",
                    "Sends blood to": "Coronary and carotid arteries (heart and brain)"
                },
                "Pulmonary artery": {
                    "Approx. O2 saturation": "About 52%",
                    "Receives blood from": "Right ventricle",
                    "Sends blood to": "Ductus arteriosus, then the descending aorta"
                },
                "Superior vena cava": {
                    "Approx. O2 saturation": "About 25%",
                    "Receives blood from": "Deoxygenated blood from upper fetal tissues",
                    "Sends blood to": "Right atrium, directed toward the right ventricle"
                }
            }
        },
        {
            "slug": "birth_hemodynamic_shift",
            "title": "Hemodynamics: Before vs After Birth",
            "subtitle": "For each variable, give its fetal state, its postnatal change and what drives the change",
            "categories": ["In utero", "After birth", "What drives the change"],
            "data": {
                "Pulmonary vascular resistance": {
                    "In utero": "High: fluid-filled lungs, constricted pulmonary arteries",
                    "After birth": "Falls markedly",
                    "What drives the change": "Rising oxygen tension causes pulmonary vasodilation"
                },
                "Systemic vascular resistance": {
                    "In utero": "Low, because of the low-resistance placenta",
                    "After birth": "Rises",
                    "What drives the change": "Cord clamping removes the placental circulation"
                },
                "Left atrial pressure": {
                    "In utero": "Lower than right atrial pressure",
                    "After birth": "Rises above right atrial pressure",
                    "What drives the change": "Greater pulmonary venous return to the left atrium"
                },
                "Right atrial pressure": {
                    "In utero": "Higher than left atrial pressure",
                    "After birth": "Falls below left atrial pressure",
                    "What drives the change": "Reduced pulmonary vascular resistance"
                },
                "Arterial O2 saturation": {
                    "In utero": "Roughly 50-80%",
                    "After birth": "Greater than 90%",
                    "What drives the change": "Switch from placental to pulmonary gas exchange"
                },
                "Circulating prostaglandin E2": {
                    "In utero": "High, from the placenta and the ductus itself",
                    "After birth": "Declines",
                    "What drives the change": "Loss of the placental source at cord clamping"
                }
            }
        },
        {
            "slug": "postnatal_closure_and_remnants",
            "title": "Postnatal Closure and Adult Remnants",
            "subtitle": "Match each fetal structure to how it closes (or not) and what it becomes",
            "categories": ["Closure mechanism", "Adult remnant"],
            "data": {
                "Foramen ovale": {
                    "Closure mechanism": "LA pressure exceeds RA pressure, pressing septum primum onto septum secundum",
                    "Adult remnant": "Fossa ovalis"
                },
                "Ductus arteriosus": {
                    "Closure mechanism": "Falling PGE2 plus rising O2 tension and bradykinin; closes in 24-72 h",
                    "Adult remnant": "Ligamentum arteriosum"
                },
                "Umbilical vein": {
                    "Closure mechanism": "Passive collapse after cord clamping; patent for weeks, then obliterates",
                    "Adult remnant": "Ligamentum teres (round ligament of the liver)"
                },
                "Ductus venosus": {
                    "Closure mechanism": "Collapses with loss of umbilical venous flow; less PG, more O2",
                    "Adult remnant": "Ligamentum venosum"
                },
                "Distal umbilical arteries": {
                    "Closure mechanism": "Smooth muscle constricts with rising O2 tension and bradykinin",
                    "Adult remnant": "Medial umbilical ligaments"
                },
                "Proximal umbilical arteries": {
                    "Closure mechanism": "Stay patent: fed by internal iliacs, less responsive to constrictors",
                    "Adult remnant": "Superior vesical arteries to the upper bladder"
                }
            }
        }
    ]
}

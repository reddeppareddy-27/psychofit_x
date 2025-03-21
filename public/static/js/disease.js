const diseasesData = [
    {
        "main_category": "Physical Health",
        "categories": [
            {
                category: "Respiratory Diseases",
                diseases: [
                    {
                        disease: "Cold & Flu",
                        symptoms: ["Cough", "Sneezing", "Sore throat", "Runny nose", "Fever"],
                        nutrients_needed: ["Vitamin C", "Zinc", "Antioxidants", "Hydration"],
                        exercises_fitness: ["Light cardio", "Walking", "Breathing exercises"],
                        meditation_yoga_asanas: ["Bhramari Pranayama", "Shavasana"]
                    },
                    {
                        disease: "Asthma",
                        symptoms: ["Shortness of breath", "Wheezing", "Chest tightness", "Coughing"],
                        nutrients_needed: ["Magnesium", "Vitamin D", "Omega-3", "Antioxidants"],
                        exercises_fitness: ["Breathing exercises", "Walking", "Swimming", "Cycling"],
                        meditation_yoga_asanas: ["Bhastrika Pranayama", "Sukhasana", "Matsyasana"]
                    },
                    {
                        disease: "Pneumonia",
                        symptoms: ["Cough", "Fever", "Difficulty breathing", "Chest pain"],
                        nutrients_needed: ["Vitamin C", "Zinc", "Hydration", "Protein"],
                        exercises_fitness: ["Breathing exercises", "Walking"],
                        meditation_yoga_asanas: ["Bhramari Pranayama", "Savasana", "Ujjayi Pranayama"]
                    },
                    {
                        disease: "Tuberculosis",
                        symptoms: ["Cough", "Weight loss", "Night sweats", "Fever"],
                        nutrients_needed: ["Protein", "Vitamin D", "Zinc", "Iron"],
                        exercises_fitness: ["Gentle walking", "Breathing exercises"],
                        meditation_yoga_asanas: ["Savasana", "Bhramari Pranayama", "Anulom Vilom"]
                    },
                    {
                        disease: "Chronic Obstructive Pulmonary Disease",
                        symptoms: ["Breathlessness", "Chronic cough", "Fatigue", "Wheezing"],
                        nutrients_needed: ["Vitamin C", "Omega-3", "Antioxidants"],
                        exercises_fitness: ["Breathing exercises", "Walking", "Swimming"],
                        meditation_yoga_asanas: ["Savasana", "Anulom Vilom", "Bhastrika"]
                    }
                ]
            },
            {
                category: "Endocrine and Metabolic Disorders",
                diseases: [
                    {
                        disease: "Diabetes",
                        symptoms: ["Increased thirst", "Frequent urination", "Fatigue", "Blurry vision"],
                        nutrients_needed: ["Chromium", "Magnesium", "Fiber", "Omega-3", "Low-Glycemic Foods"],
                        exercises_fitness: ["Strength training", "Aerobics", "Cycling", "Yoga"],
                        meditation_yoga_asanas: ["Kapalbhati Pranayama", "Dhanurasana", "Bhujangasana"]
                    },
                    {
                        disease: "Obesity",
                        symptoms: ["Excess body weight", "Joint pain", "Fatigue", "Shortness of breath"],
                        nutrients_needed: ["Fiber", "Protein", "Omega-3", "Whole grains", "Low-Glycemic Foods"],
                        exercises_fitness: ["Cardio", "Strength training", "Swimming", "HIIT"],
                        meditation_yoga_asanas: ["Surya Namaskar", "Bhujangasana", "Trikonasana"]
                    },
                    {
                        disease: "Thyroid Disorders",
                        symptoms: ["Fatigue", "Weight changes", "Hair loss", "Dry skin", "Mood changes"],
                        nutrients_needed: ["Iodine", "Selenium", "Zinc", "Vitamin D", "Omega-3"],
                        exercises_fitness: ["Yoga", "Walking", "Strength training"],
                        meditation_yoga_asanas: ["Setu Bandhasana", "Trikonasana", "Savasana"]
                    }
                ]
            },
            {
                category: "Cardiovascular Diseases",
                diseases: [
                    {
                        disease: "Hypertension",
                        symptoms: ["Headaches", "Fatigue", "Dizziness", "Shortness of breath", "Chest pain"],
                        nutrients_needed: ["Potassium", "Magnesium", "Omega-3", "Reduced sodium", "Fiber"],
                        exercises_fitness: ["Walking", "Low-impact cardio", "Swimming"],
                        meditation_yoga_asanas: ["Anulom Vilom", "Sukhasana", "Vrikshasana"]
                    },
                    {
                        disease: "Heart Disease",
                        symptoms: ["Chest pain", "Shortness of breath", "Fatigue", "Swelling in legs"],
                        nutrients_needed: ["Omega-3", "Fiber", "Antioxidants", "Magnesium", "Potassium"],
                        exercises_fitness: ["Cardio", "Strength training", "Walking", "Swimming"],
                        meditation_yoga_asanas: ["Anulom Vilom", "Tadasana", "Bhujangasana"]
                    }
                ]
            },
            {
                category: "Mental Health Disorders",
                diseases: [
                    {
                        disease: "Depression",
                        symptoms: ["Sadness", "Fatigue", "Sleep disturbance", "Loss of interest", "Anxiety"],
                        nutrients_needed: ["Omega-3", "Vitamin D", "Folate", "Antioxidants", "Tryptophan"],
                        exercises_fitness: ["Walking", "Yoga", "Aerobic exercises", "Dancing"],
                        meditation_yoga_asanas: ["Meditation", "Balasana", "Savasana", "Viparita Karani"]
                    },
                    {
                        disease: "Insomnia",
                        symptoms: ["Difficulty sleeping", "Restlessness", "Daytime fatigue", "Irritability"],
                        nutrients_needed: ["Magnesium", "Melatonin-rich foods", "B6", "Calcium"],
                        exercises_fitness: ["Stretching", "Light yoga", "Breathing exercises"],
                        meditation_yoga_asanas: ["Savasana", "Yoga Nidra", "Viparita Karani"]
                    }
                ]
            },
            {
                category: "Musculoskeletal and Autoimmune Disorders",
                diseases: [
                    {
                        disease: "Arthritis",
                        symptoms: ["Joint pain", "Stiffness", "Swelling", "Reduced range of motion"],
                        nutrients_needed: ["Omega-3", "Vitamin D", "Calcium", "Antioxidants", "Collagen"],
                        exercises_fitness: ["Swimming", "Low-impact strength exercises", "Stretching"],
                        meditation_yoga_asanas: ["Virabhadrasana", "Trikonasana", "Tadasana"]
                    },
                    {
                        disease: "Osteoporosis",
                        symptoms: ["Bone weakness", "Back pain", "Height loss", "Fracture risk"],
                        nutrients_needed: ["Calcium", "Vitamin D", "Magnesium", "Protein", "Vitamin K"],
                        exercises_fitness: ["Weight-bearing exercises", "Strength training", "Walking"],
                        meditation_yoga_asanas: ["Tadasana", "Vrikshasana", "Setu Bandhasana"]
                    }
                ]
            }
        ]
    },
    {
        "main_category": "Mental Health",
        "categories": [
            {
                "category": "Anxiety Disorders",
                "diseases": [
                    {
                        "disease": "Anxiety Disorders",
                        "symptoms": ["Excessive worry", "Restlessness", "Fatigue", "Difficulty concentrating"],
                        "nutrients_needed": ["Omega-3", "Magnesium", "Vitamin D", "B vitamins"],
                        "exercises_fitness": ["Yoga", "Walking", "Aerobics"],
                        "meditation_yoga_asanas": ["Savasana", "Anulom Vilom", "Bhramari Pranayama"]
                    },
                    {
                        "disease": "Generalized Anxiety Disorder",
                        "symptoms": ["Chronic worry", "Fatigue", "Difficulty concentrating", "Sleep disturbances"],
                        "nutrients_needed": ["Omega-3", "Magnesium", "Vitamin D"],
                        "exercises_fitness": ["Yoga", "Walking", "Meditation"],
                        "meditation_yoga_asanas": ["Savasana", "Anulom Vilom", "Bhramari Pranayama"]
                    },
                    {
                        "disease": "Social Anxiety Disorder",
                        "symptoms": ["Intense fear of social situations", "Avoidance", "Sweating", "Rapid heartbeat"],
                        "nutrients_needed": ["Vitamin B6", "Magnesium", "Omega-3"],
                        "exercises_fitness": ["Yoga", "Walking", "Swimming"],
                        "meditation_yoga_asanas": ["Savasana", "Anulom Vilom", "Bhramari Pranayama"]
                    }
                ]
            },
            {
                "category": "Mood Disorders",
                "diseases": [
                    {
                        "disease": "Depression",
                        "symptoms": ["Persistent sadness", "Loss of interest", "Fatigue", "Sleep disturbances"],
                        "nutrients_needed": ["Omega-3", "Vitamin D", "Folate", "Antioxidants"],
                        "exercises_fitness": ["Walking", "Yoga", "Strength training"],
                        "meditation_yoga_asanas": ["Meditation", "Balasana", "Savasana"]
                    },
                    {
                        "disease": "Bipolar Disorder",
                        "symptoms": ["Mood swings", "Mania", "Depression", "Sleep disturbances"],
                        "nutrients_needed": ["Omega-3", "Folate", "Vitamin D", "Magnesium"],
                        "exercises_fitness": ["Yoga", "Aerobics", "Walking"],
                        "meditation_yoga_asanas": ["Balasana", "Savasana", "Anulom Vilom"]
                    },
                    {
                        "disease": "Seasonal Affective Disorder",
                        "symptoms": ["Depression during winter months", "Fatigue", "Social withdrawal", "Weight gain"],
                        "nutrients_needed": ["Vitamin D", "Omega-3", "Folate"],
                        "exercises_fitness": ["Walking", "Light cardio", "Yoga"],
                        "meditation_yoga_asanas": ["Savasana", "Viparita Karani", "Meditation"]
                    }
                ]
            },
            {
                "category": "Personality Disorders",
                "diseases": [
                    {
                        "disease": "Personality Disorders",
                        "symptoms": ["Extreme emotional responses", "Distorted thinking", "Relationship problems"],
                        "nutrients_needed": ["Omega-3", "Magnesium", "Zinc"],
                        "exercises_fitness": ["Yoga", "Walking", "Strength training"],
                        "meditation_yoga_asanas": ["Savasana", "Anulom Vilom", "Meditation"]
                    },
                    {
                        "disease": "Borderline Personality Disorder",
                        "symptoms": ["Instability in relationships", "Self-image issues", "Impulsivity"],
                        "nutrients_needed": ["Omega-3", "Vitamin D", "Folate"],
                        "exercises_fitness": ["Walking", "Yoga", "Aerobics"],
                        "meditation_yoga_asanas": ["Savasana", "Balasana", "Anulom Vilom"]
                    },
                    {
                        "disease": "Narcissistic Personality Disorder",
                        "symptoms": ["Grandiosity", "Need for admiration", "Lack of empathy"],
                        "nutrients_needed": ["Omega-3", "Magnesium", "Vitamin D"],
                        "exercises_fitness": ["Yoga", "Walking"],
                        "meditation_yoga_asanas": ["Savasana", "Viparita Karani", "Matsyasana"]
                    }
                ]
            },
            {
                "category": "Compulsive and Impulsive Disorders",
                "diseases": [
                    {
                        "disease": "Compulsive Hoarding Disorder",
                        "symptoms": ["Difficulty discarding items", "Cluttered living spaces", "Distress"],
                        "nutrients_needed": ["Vitamin B complex", "Omega-3", "Magnesium"],
                        "exercises_fitness": ["Gentle yoga", "Walking"],
                        "meditation_yoga_asanas": ["Savasana", "Balasana", "Meditation"]
                    },
                    {
                        "disease": "Impulsive Control Disorders",
                        "symptoms": ["Failure to resist a temptation", "Engaging in harmful behaviors", "Disruptive behavior"],
                        "nutrients_needed": ["Omega-3", "Vitamin D", "Magnesium"],
                        "exercises_fitness": ["Walking", "Yoga", "Strength training"],
                        "meditation_yoga_asanas": ["Savasana", "Anulom Vilom", "Meditation"]
                    },
                    {
                        "disease": "Kleptomania",
                        "symptoms": ["Compulsive stealing", "Tension before stealing", "Guilt after stealing"],
                        "nutrients_needed": ["Omega-3", "Vitamin D", "B vitamins"],
                        "exercises_fitness": ["Walking", "Yoga"],
                        "meditation_yoga_asanas": ["Savasana", "Meditation", "Anulom Vilom"]
                    }
                ]
            },
            {
                "category": "Anxiety and Stress Disorders",
                "diseases": [
                    {
                        "disease": "Panic Disorder",
                        "symptoms": ["Recurring panic attacks", "Intense fear", "Physical symptoms"],
                        "nutrients_needed": ["Vitamin B complex", "Omega-3", "Magnesium"],
                        "exercises_fitness": ["Walking", "Yoga", "Breathing exercises"],
                        "meditation_yoga_asanas": ["Savasana", "Anulom Vilom", "Bhramari Pranayama"]
                    },
                    {
                        "disease": "Adjustment Disorders",
                        "symptoms": ["Difficulty adjusting to significant life changes", "Anxiety", "Depression"],
                        "nutrients_needed": ["Omega-3", "Vitamin D", "B vitamins"],
                        "exercises_fitness": ["Walking", "Yoga", "Meditation"],
                        "meditation_yoga_asanas": ["Savasana", "Balasana", "Anulom Vilom"]
                    },
                    {
                        "disease": "Trauma",
                        "symptoms": ["Flashbacks", "Avoidance", "Anxiety", "Mood swings"],
                        "nutrients_needed": ["Vitamin D", "Omega-3", "Magnesium"],
                        "exercises_fitness": ["Yoga", "Walking"],
                        "meditation_yoga_asanas": ["Savasana", "Meditation", "Anulom Vilom"]
                    }
                ]
            },
            {
                "category": "Developmental and Cognitive Disorders",
                "diseases": [
                    {
                        "disease": "Learning Disorders",
                        "symptoms": ["Difficulty with reading, writing, or math", "Struggles in school"],
                        "nutrients_needed": ["Omega-3", "B vitamins", "Iron"],
                        "exercises_fitness": ["Yoga", "Walking"],
                        "meditation_yoga_asanas": ["Savasana", "Anulom Vilom", "Bhramari Pranayama"]
                    },
                    {
                        "disease": "Tic Disorders",
                        "symptoms": ["Sudden, rapid movements or sounds", "Tics"],
                        "nutrients_needed": ["Magnesium", "Omega-3", "Zinc"],
                        "exercises_fitness": ["Yoga", "Walking"],
                        "meditation_yoga_asanas": ["Savasana", "Balasana", "Meditation"]
                    },
                    {
                        "disease": "Pervasive Developmental Disorders",
                        "symptoms": ["Impairments in social interaction", "Communication challenges"],
                        "nutrients_needed": ["Omega-3", "Antioxidants", "Zinc"],
                        "exercises_fitness": ["Yoga", "Walking"],
                        "meditation_yoga_asanas": ["Savasana", "Balasana", "Meditation"]
                    }
                ]
            },
            {
                "category": "Psychotic and Mood Disorders",
                "diseases": [
                    {
                        "disease": "Psychosis",
                        "symptoms": ["Loss of contact with reality", "Hallucinations", "Delusions"],
                        "nutrients_needed": ["Omega-3", "Folate", "Zinc"],
                        "exercises_fitness": ["Walking", "Gentle yoga"],
                        "meditation_yoga_asanas": ["Savasana", "Meditation", "Viparita Karani"]
                    },
                    {
                        "disease": "Paranoia",
                        "symptoms": ["Intense fear or suspicion", "Distrust of others", "Social withdrawal"],
                        "nutrients_needed": ["Omega-3", "Magnesium", "Vitamin D"],
                        "exercises_fitness": ["Walking", "Yoga"],
                        "meditation_yoga_asanas": ["Savasana", "Balasana", "Meditation"]
                    }
                ]
            }
        ]
    }
    
];

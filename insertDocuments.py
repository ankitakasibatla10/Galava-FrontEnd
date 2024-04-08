import random
import os
from faker import Faker
import datetime

fake = Faker()

universities = {
    "KIM904": "Pune University",
    "BGC265": "Vadodara University",
    "HGP015": "Ahmedabad University",
    "NTC522" : "Bangalore University",
    "DGM130" : "Imphal University",
    "BPF119" : "Amritsar University",
    "WVK566": "Kozhikode University",
    "ZRG667": "Banglore University",
    "BDT117": "Itanagar University",
    "SGX178": "Varanasi University",
    "YTF596": "Ahmedabad University",
    "PSR664": "Shillong University",
    "PTT802": "Guwahati University",
    "CZC946": "Jaipur University",
    "MJT518": "Hyderabad University",
    "USA481": "Ghaziabad University",
    "XPH170": "Mangalore University",
    "QZW658": "Jodhpur University",
    "DIK773": "Faridabad University",
    "KGV285": "Chandigarh University",
    "MDN216": "Mumbai University",
    "EUE815": "Guwahati University",
    "WMT549": "Visakhapatnam University",
    "PWG506": "Jodhpur University",
    "PAJ290": "Kota University",
    "MMN595": "Dehradun University",
    "OBS376": "Faridabad University",
    "MEH867": "Coimbatore University",
    "DTB247": "Noida University",
    "FNC577": "Kozhikode University",
    "MMN175": "Ahmedabad University",
    "MDD555": "Surat University",
    "KRE410": "Shillong University",
    "DPF912": "Lucknow University",
    "SIU737": "Coimbatore University",
    "VRK972": "Pune University",
    "MBH709": "Coimbatore University",
    "SEK078": "Kolkata University",
    "QXP683": "Patna University",
    "RIC865": "Imphal University",
    "YQE641": "Jodhpur University",
    "XGK397": "Kota University",
    "BFH596": "Tiruchirappalli University",
    "XOL395": "Allahabad University",
    "WVC119": "Pune University",
    "RLJ360": "Srinagar University",
    "DPL068": "Jamshedpur University",
    "GCR973": "Gandhinagar University",
    "KZK430": "Itanagar University",
    "FKP350": "Mangalore University"
}

field_of_study = ["Computer Science", "Finance", "Psychology", "Business", "Engineering",
                   "Biology", "Chemistry", "Mathematics", "Physics", "History"]


def generateData(field_of_study):
    instituition_id = random.choice(list(universities.keys()))
    university_name = universities[instituition_id]

    return{
         "_id": fake.uuid4(),
        "name": fake.sentence(nb_words=3),
        "university": university_name,
        "department": fake.word(),
        "degreeType": random.choice(["Bachelor's", "Master's", "PhD", "Certificate"]),
        "fieldOfStudy": field_of_study,
        "description": fake.text(max_nb_chars=200),
        "duration": random.choice([2, 4]) * 12,  # Assuming 2 or 4 years for simplicity
        "creditHours": random.randint(120, 200),
        "curriculum": [{"courseCode": fake.bothify(text='???###'), "courseName": fake.sentence(nb_words=3), "credits": random.randint(2, 4)} for _ in range(10)],
        "admissionRequirements": ["Bachelor's degree", "GRE scores"] if field_of_study != "Bachelor's" else ["High School Diploma"],
        "tuition": {"domestic": random.randint(10000, 50000), "international": random.randint(20000, 70000)},
        "ranking": {"nationalRanking": random.randint(1, 100), "internationalRanking": random.randint(1, 500)},
        "accreditation": [fake.company() for _ in range(random.randint(1, 3))],
    }
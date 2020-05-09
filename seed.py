import os
import datetime
from collections import OrderedDict

from faker import Faker
import numpy as np
import sqlite3

if os.path.exists("ladder.db"):
    os.remove("ladder.db")

conn = sqlite3.connect("ladder.db")
cur = conn.cursor()

# Seed pets ==================================
cur.execute("""
CREATE TABLE IF NOT EXISTS pets (
    name text,
    sex text,
    species text,
    age integer
);
""")

def add_into_pets(data):
    cur.execute("""
    INSERT INTO pets (name, sex, species, age)
    VALUES (?, ?, ?, ?);
    """, data)

pets = [
    ("Chloe", "F", "dog", 9),
    ("Paddinton", "M", "dog", 10),
    ("Petey", "M", "dog", 7),
    ("Bella", "F", "dog", 1),
    ("Glenn Coco", "M", "cat", 6),
    ("Alanna", "F", "cat", 3),
    ("Mimi", "F", "dog", 4),
    ("Midge", "F", "cat", 7),
    ("Eli", "M", "dog", 8),
    ("Shuri", "F", "cat", 2),
    ("Oliver", "M", "cat", 5),
    ("Dottie", "F", "cat", 3),
    ("Pinchy", "M", "lobster", 3)
]

for pet in pets:
    add_into_pets(pet)

# Seed employees ==================================
cur.execute("""
CREATE TABLE IF NOT EXISTS employees (
    ID integer primary key,
    firstname text,
    lastname text,
    job text,
    salary numeric,
    startdate text
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS pets (
    name text,
    sex text,
    species text,
    age integer
);
""")

def gen_fake_person(fake, i):
    return (
        i,
        fake.first_name(),
        fake.last_name(),
        fake.random_element(OrderedDict([
            ("Administrator", 0.1),
            ("Sales", 0.7),
            ("Operations", 0.1),
            ("IT", 0.1)
        ])),
        np.round(np.random.uniform(30000, 125000, 1)[0]),
        fake.date_between_dates(
            date_start=datetime.date(year=1990, month=1, day=1),
            date_end=datetime.date(year=2020, month=1, day=1)
        ).strftime("%Y-%m-%d")
    )

def add_into_employees(emp):
    cur.execute("""
    INSERT INTO employees (ID, firstname, lastname, job, salary, startdate)
    VALUES (?, ?, ?, ?, ?, ?);
    """, emp) 

fake = Faker()
Faker.seed(2020)
np.random.seed(2020)
for i in range(1000):
    employee = gen_fake_person(fake, i)
    add_into_employees(employee)

conn.commit()

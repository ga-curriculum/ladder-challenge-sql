import os
import sqlite3

if os.path.exists("ladder.db"):
    os.remove("ladder.db")

conn = sqlite3.connect("ladder.db")
cur = conn.cursor()

# Seed pets
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

conn.commit()

# The Basics

## Simple SELECTs
1) Query all the data in the `pets` table.
```sql
SELECT * FROM pets;
```

2) Query only the first 5 rows of the `pets` table.
```sql
SELECT * FROM pets LIMIT 5;
```

3) Query only the names and ages of the pets in the `pets` table.
```sql
SELECT name, age FROM pets;
```

4) Query the pets in the `pets` table, sorted youngest to oldest.
```sql
SELECT * FROM pets ORDER BY age;
```

5) Query the pets in the `pets` table alphabetically.
```sql
SELECT * FROM pets ORDER BY name;
```

6) Query all the male pets in the `pets` table.
```sql
SELECT * 
FROM pets
WHERE sex = "M";
```

7) Query all the cats in the `pets` table.
```sql
SELECT *
FROM pets
WHERE species = "cat";
```

8) Query all the pets in the `pets` table that are at least 5 years old.
```sql
SELECT *
FROM pets
WHERE age >= 5;
```

9) Query all the male dogs in the `pets` table. Do not include the sex or species column, since you already know them.
```sql
SELECT name, age
FROM pets
WHERE sex = "M" AND species = "dog";
```

10) Get all the names of the dogs in the `pets` table that are younger than 5 years old.
```sql
SELECT name
FROM pets
WHERE species = "dog" AND age < 5;
```

11) Query all the pets in the `pets` table that are either male dogs or female cats.
```sql
SELECT *
FROM pets
WHERE
    (sex = "M" AND species = "dog")
    OR (sex = "F" and species = "cat");
```

12) Query the five oldest pets in the `pets` table.
```sql
SELECT *
FROM pets
ORDER BY age DESC
LIMIT 5;
```

13) Get the names and ages of all the female cats in the `pets` table sorted by age, descending.
```sql
SELECT name, age
FROM pets
WHERE sex = "F" and species = "cat"
ORDER BY age DESC;
```

14) Get all pets from `pets` whose names start with P.
```sql
SELECT * FROM pets WHERE name LIKE "P%;"
```








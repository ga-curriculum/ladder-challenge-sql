# Summarizing Data with SQL

## Summary Statistics
25) How many rows are in the `pets` table?
26) How many female pets are in the `pets` table?
27) How many female cats are in the `pets` table?
28) What's the mean age of pets in the `pets` table?
29) What's the mean age of dogs in the `pets` table?
30) What's the mean age of male dogs in the `pets` table?
31) What's the count, mean, minimum, and maximum of pet ages in the `pets` table?
    * _NOTE:_ SQLite doesn't have built-in formulas for standard deviation or median!
32) Repeat the previous problem with the following stipulations:
    * Round the average to one decimal place.
    * Give each column a human-readable column name (for example, "Average Age")
XX) How many rows in `employees_null` have missing salaries?
XX) How many salespeople in `employees_null` having _nonmissing_ salaries?
XX) What's the mean salary of employees who joined the company after 2010?
XX) What's the mean salary of employees in Swiss Francs? Go back to the usual `employees` table for this one.
    * _Hint:_ Swiss Francs are abbreviated "CHF" and 1 USD = 0.97 CHF.
XX) Create a query that computes the mean salary in USD as well as CHF. Give the columns human-readable names (for example "Mean Salary in USD"). Also, format them with comma delimiters and currency symbols.
    * _NOTE:_ Comma-delimiting numbers is only available for integers in SQLite, so rounding (down) to the nearest dollar or franc will be done for us.
    * _NOTE2:_ The symbols for francs is simply `Fr.` or `fr.`. So an example output will look like `100,000 Fr.`.

## Aggregating Statistics with GROUP BY
XX) What is the average age of `pets` by species?
XX) Repeat the previous problem but make sure the species label is also displayed! Assume this behavior is always being asked of you throughout this section.
XX) What is the count, mean, minimum, and maximum age by species? Make sure the species is also outputted.

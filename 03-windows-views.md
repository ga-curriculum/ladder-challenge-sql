# Views, CTEs, and Window Functions

This file contains several exercises on views, common table expressions (CTEs), and window functions. These topics are a step more involved and confusing than in the previous two files. Before attempting these problems, you'll probably need to do some research into these topics. Here are a few tutorials:

* [Tutorial on Views](https://www.sqlitetutorial.net/sqlite-create-view/)
* [Tutorial on CTEs](https://www.essentialsql.com/introduction-common-table-expressions-ctes/)
* Tutorial on Window Functions

Here are a few other important notes I'd like you read before beginning:
* Some of these problems can get pretty involved. Queries with adequate spacing can go longer than 15 lines in some problems.
* Make sure you read each question thoroughly.
* Don't skip problems, as some problems may rely on previous problems being done correctly.
* Make sure you are saving your answers as you go, as some answers will simply be reworkings of previous answers.
* Some problems in the `Views` section involve you making persistent changes to the database itself. Specifically, if you create a view, you cannot create another view with the same name if it already exists. You may want to learn the `DROP VIEW` command. Or maybe a little easier,  you can recreate the entire database by simply running the `seed.py` script provided in this repo. If you're unsure, you can see your list of tables and views using the `.tables` dot-command from the `sqlite3` interface.

## Views
XX) Look at the `yum` table. It is the stock data for Yum! Brands, Inc. from 2015 through 2019. Yum! is the company that owns Taco Bell, the best restaurant.

```sql
SELECT * FROM yum LIMIT 10;
```

XX) Query the `yum` table, aggregating by **both** month and year, with the following resulting columns:

* Year (4 digits)
* Month
* Average open, high, low, and close
* Total volume

Finally, sort this data so it's in proper chronological order.

```sql
SELECT
    STRFTIME("%Y", date) AS year,
    STRFTIME("%m", date) AS month,
    AVG(open) AS avg_open,
    AVG(high) AS avg_high,
    AVG(low) AS avg_low,
    AVG(close) AS avg_close,
    SUM(volume) AS tot_volume
FROM yum
GROUP BY month, year
ORDER BY year, month;
```

XX) Save the results of the previous query as a view named `yum_by_month`.

```sql
CREATE VIEW yum_by_month AS
SELECT
    STRFTIME("%Y", date) AS year,
    STRFTIME("%m", date) AS month,
    AVG(open) AS avg_open,
    AVG(high) AS avg_high,
    AVG(low) AS avg_low,
    AVG(close) AS avg_close,
    SUM(volume) AS tot_volume
FROM yum
GROUP BY month, year
ORDER BY year, month;
```

XX) Create a view of `transactions` consisting of only three columns: year, month, and total sales in that month. Call this view `trans_by_month`.

```sql
CREATE VIEW trans_by_month AS
SELECT
    STRFTIME("%Y", orderdate) AS year,
    STRFTIME("%m", orderdate) AS month,
    SUM(unit_price*quantity) AS total_cost
FROM transactions
GROUP BY year, month
ORDER BY year, month;
```

XX) Create a view of `transactions` consisting of only two columns: `employee_id` and the total sales corresponding to that employee. Call this view `trans_by_employee`.

```sql
CREATE VIEW trans_by_employee AS
SELECT
    employee_id,
    SUM(unit_price*quantity) AS total_cost
FROM transactions
GROUP BY employee_id
ORDER BY employee_id;
```

XX) 

# Window Functions, Subqueries

The only new topics in this file are that of window functions and subqueries. By themselves, these topics are not difficult, and so we will start out slow. However, these topics are very useful in more complex queries. Solutions to some of these problems will be even longer and more involved than in the previous file.

## Window Functions

XX) Create a daily cumulative sum of the trading volume of the Yum! stock in `yum`.

```sql
SELECT
    *,
    SUM(volume) OVER (ORDER BY date) AS cum_volume
FROM yum;
```

XX) Create a cumulative sum of the trading volume of Yum! across months. That is, the final row of this query should be the cumulative sum of all months from 2015 through 2019.

```sql
SELECT
    *,
    STRFTIME("%Y", date) AS year,
    STRFTIME("%m", date) AS month,
    SUM(volume) OVER (ORDER BY date) AS cum_volume
FROM yum
GROUP BY year, month
ORDER BY year, month;
```

XX) For March 2017, create a table from `yum` with the following columns:
* Day of the month
* Row number (ie, the nth trading day of the month)
* Cumulative low (ie, lowest low so far this month)
* Cumulative high (ie, highest high so far this month)
* Cumulative total volume

```sql
SELECT
    STRFTIME("%d", date) AS day,
    ROW_NUMBER() OVER (ORDER BY date) AS row_number,
    MIN(low) OVER (ORDER BY date) AS cum_low,
    MAX(high) OVER (ORDER BY date) AS cum_high,
    SUM(volume) OVER (ORDER BY date) AS cum_volume
FROM yum
WHERE 
    STRFTIME("%Y", date) = "2017"
    AND STRFTIME("%m", date) = "03";
```

XX) From `yum`, create a column that represents the 7-day moving average of the closing price. This syntax is very confusing. You can read more about it [here](https://www.sqlitetutorial.net/sqlite-window-functions/sqlite-window-frame/).

```sql
SELECT
    *,
    AVG(close) OVER (
        ORDER BY date
        ROWS BETWEEN 7 PRECEDING AND 1 PRECEDING
    ) AS moving_avg
FROM yum;
```

XX) Repeat the March 2017 problem but instead of cumulative highs, lows, and totals, show the 5-day moving highs and lows. (No need for volume here.)

```sql
SELECT
    STRFTIME("%d", date) AS day,
    ROW_NUMBER() OVER (ORDER BY date) AS row_number,
    MIN(low) OVER (
        ORDER BY date
        ROWS BETWEEN 5 PRECEDING AND 1 PRECEDING
    ) AS cum_low,
    MAX(high) OVER (
        ORDER BY date
        ROWS BETWEEN 5 PRECEDING AND 1 PRECEDING
    ) AS cum_high
FROM yum
WHERE 
    STRFTIME("%Y", date) = "2017"
    AND STRFTIME("%m", date) = "03";
```



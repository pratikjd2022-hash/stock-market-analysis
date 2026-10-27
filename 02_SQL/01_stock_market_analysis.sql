
CREATE DATABASE IF NOT EXISTS stock_market_db;
USE stock_market_db;

SHOW TABLES;

USE stock_market_db;

SELECT COUNT(*) AS total_rows
FROM stock_market_data;

SELECT *
FROM stock_market_data
LIMIT 10;



SELECT
    Company,
    COUNT(*) AS total_records
FROM stock_market_data
GROUP BY Company;


SELECT
    Company,
    MIN(Date) AS first_date,
    MAX(Date) AS last_date,
    COUNT(*) AS total_records
FROM stock_market_data
GROUP BY Company;


SELECT
    Company,
    MAX(Close) AS highest_close
FROM stock_market_data
GROUP BY Company
ORDER BY highest_close DESC;


SELECT
    Company,
    ROUND(AVG(Close), 2) AS average_close
FROM stock_market_data
GROUP BY Company
ORDER BY average_close DESC;

SELECT 
	company,
    ROUND(MIN(close), 2) As lowest_close
FROM stock_market_data
group by Company
order by lowest_close DESC ;


SELECT
    Company,
    MAX(Volume) AS highest_volume
FROM stock_market_data
GROUP BY Company
ORDER BY highest_volume DESC;


SELECT
    Company,
    DATE_FORMAT(STR_TO_DATE(Date, '%Y-%m-%d'), '%Y-%m') AS month,
    ROUND(AVG(Close), 2) AS monthly_avg_close
FROM stock_market_data
GROUP BY
    Company,
    DATE_FORMAT(STR_TO_DATE(Date, '%Y-%m-%d'), '%Y-%m')
ORDER BY
    month,
    Company;


SELECT
    Company,
    Date,
    Close,
    LAG(Close) OVER (
        PARTITION BY Company
        ORDER BY STR_TO_DATE(Date, '%Y-%m-%d')
    ) AS previous_close
FROM stock_market_data
ORDER BY Company, STR_TO_DATE(Date, '%Y-%m-%d');


WITH daily_prices AS (
    SELECT
        Company,
        Date,
        Close,
        LAG(Close) OVER (
            PARTITION BY Company
            ORDER BY STR_TO_DATE(Date, '%Y-%m-%d')
        ) AS previous_close
    FROM stock_market_data
)
SELECT
    Company,
    Date,
    ROUND(Close - previous_close, 2) AS price_change
FROM daily_prices
ORDER BY Company, STR_TO_DATE(Date, '%Y-%m-%d')
LIMIT 10;



SELECT
    Company,
    ROUND(AVG(Close), 2) AS avg_close,
    ROUND(MIN(Close), 2) AS lowest_close,
    ROUND(MAX(Close), 2) AS highest_close,
    MAX(Volume) AS highest_volume
FROM stock_market_data
GROUP BY Company
ORDER BY avg_close DESC;


-- PHASE 3: SQL Database

-- STEP 2: Create Database
CREATE DATABASE phonepe;
USE phonepe;

-- STEP 3: Create Tables
-- 1. aggregated_transaction
CREATE TABLE aggregated_transaction (
    state VARCHAR(100),
    year INT,
    quarter INT,
    type VARCHAR(100),
    count BIGINT,
    amount DOUBLE
);

-- 2. aggregated_user
CREATE TABLE aggregated_user (
    state VARCHAR(100),
    year INT,
    quarter INT,
    registeredUsers BIGINT,
    appOpens BIGINT
);
-- 3. map_transaction
CREATE TABLE map_transaction (
    state VARCHAR(100),
    year INT,
    quarter INT,
    district VARCHAR(100),
    count BIGINT,
    amount DOUBLE
);

-- 4. top_transaction 
CREATE TABLE top_transaction (
    state VARCHAR(100),
    year INT,
    quarter INT,
    district VARCHAR(100),
    count BIGINT,
    amount DOUBLE
);
-- STEP 4: Import CSV into MySQL
-- STEP 5: Verify Data
SELECT * FROM aggregated_transaction LIMIT 10;
SELECT * FROM aggregated_user LIMIT 10;
SELECT * FROM map_transaction LIMIT 10;
SELECT * FROM top_transaction LIMIT 10;


-- STEP 6: SQL ANALYSIS QUERIES
-- 1. aggregated_transaction
-- Top 10 States by Transaction Amount
SELECT state, SUM(amount) AS total_amount
FROM aggregated_transaction
GROUP BY state
ORDER BY total_amount DESC
LIMIT 10;

-- Payment Category Performance
SELECT type, SUM(amount) AS total_amount
FROM aggregated_transaction
GROUP BY type
ORDER BY total_amount DESC;

-- Year-wise Growth
SELECT year, SUM(amount) AS total_amount
FROM aggregated_transaction
GROUP BY year
ORDER BY year;

-- Quarterly Trend
SELECT year, quarter, SUM(amount) AS total_amount
FROM aggregated_transaction
GROUP BY year, quarter
ORDER BY year, quarter;

-- Fraud Detection (High spikes)
SELECT state, year, quarter, SUM(amount) AS total
FROM aggregated_transaction
GROUP BY state, year, quarter
HAVING total > 1000000000
ORDER BY total DESC;

-- 2. aggregated_user
-- Top States by Users
SELECT state, SUM(registeredUsers) AS users
FROM aggregated_user
GROUP BY state
ORDER BY users DESC
LIMIT 10;

-- App Engagement (App Opens)
SELECT state, SUM(appOpens) AS opens
FROM aggregated_user
GROUP BY state
ORDER BY opens DESC;

-- Growth of Users Over Years
SELECT year, SUM(registeredUsers) AS users
FROM aggregated_user
GROUP BY year
ORDER BY year;

-- User Engagement Ratio
SELECT state,
       SUM(appOpens)/SUM(registeredUsers) AS engagement_ratio
FROM aggregated_user
GROUP BY state
ORDER BY engagement_ratio DESC;

-- 3. map_transaction
-- Top Districts
SELECT district, SUM(amount) AS total
FROM map_transaction
GROUP BY district
ORDER BY total DESC
LIMIT 10;

-- State-wise District Contribution
SELECT state, SUM(amount) AS total
FROM map_transaction
GROUP BY state
ORDER BY total DESC;

-- District-wise Count Analysis
SELECT district, SUM(count) AS total_count
FROM map_transaction
GROUP BY district
ORDER BY total_count DESC;

-- 4. top_transaction
-- Top Districts by Amount
SELECT district, SUM(amount) AS total
FROM top_transaction
GROUP BY district
ORDER BY total DESC
LIMIT 10;

-- Top States by Count
SELECT state, SUM(count) AS total_count
FROM top_transaction
GROUP BY state
ORDER BY total_count DESC;

-- High Performing Regions
SELECT state, district, SUM(amount) AS total
FROM top_transaction
GROUP BY state, district
ORDER BY total DESC
LIMIT 10;

-- Compare Transactions vs Users
SELECT t.state,
       SUM(t.amount) AS total_transaction,
       SUM(u.registeredUsers) AS total_users
FROM aggregated_transaction t
JOIN aggregated_user u
ON t.state = u.state AND t.year = u.year AND t.quarter = u.quarter
GROUP BY t.state
ORDER BY total_transaction DESC;

-- Growth Rate
SELECT year,
       SUM(amount) AS total,
       LAG(SUM(amount)) OVER (ORDER BY year) AS prev_year,
       (SUM(amount) - LAG(SUM(amount)) OVER (ORDER BY year)) AS growth
FROM aggregated_transaction
GROUP BY year;


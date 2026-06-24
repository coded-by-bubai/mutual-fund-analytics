-- 1 Top 5 Funds by AUM

SELECT fund_house,aum_lakh_crore
FROM aum_by_fund_house 
ORDER BY aum_lakh_crore DESC
LIMIT 5;

-- 2 Average NAV per Month

SELECT month,
AVG(nav)
FROM fact_nav n
JOIN dim_date d
ON n.date=d.date
GROUP BY month;

-- 3 SIP YoY Growth

SELECT year,
SUM(amount_inr)
FROM fact_transactions t
JOIN dim_date d
ON t.transaction_date=d.date
WHERE transaction_type='SIP'
GROUP BY year;

-- 4 Transactions by State

SELECT state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

-- 5 Funds with Expense Ratio <1%

SELECT fund_house,
expense_ratio_pct
FROM fact_performance 
WHERE expense_ratio_pct<1;

-- 6 Highest 1Y Return

SELECT fund_house,return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;

-- 7 Lowest Expense Ratio

SELECT fund_house,expense_ratio_pct
FROM fact_performance
ORDER BY expense_ratio_pct;

-- 8 Monthly Transaction Volume

SELECT month,
SUM(amount_inr)
FROM fact_transactions t
JOIN dim_date d
ON t.transaction_date=d.date
GROUP BY month;

-- 9 Average AUM by Category

SELECT category,
AVG(aum_lakh_crore)
FROM aum_by_fund_house a
JOIN fund_master f
ON a.fund_house=f.fund_house
GROUP BY category;

-- 10 Redemption Analysis

SELECT year,
SUM(amount_inr)
FROM fact_transactions t
JOIN dim_date d
ON t.transaction_date=d.date
WHERE transaction_type='Redemption'
GROUP BY year;

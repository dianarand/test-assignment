SELECT 
    customer_id, 
    value_date, 
    amount,
    SUM(amount) OVER (PARTITION BY customer_id, value_date ORDER BY value_date, amount RANGE UNBOUNDED PRECEDING) cumulative_amount,
    SUM(amount) OVER (PARTITION BY customer_id) total_amount
FROM customers;

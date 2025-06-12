-- Find total money made by each toy
SELECT ToyName, SUM(Quantity * Price) as TotalMoney
FROM toy_sales
GROUP BY ToyName
ORDER BY TotalMoney DESC;

-- Count how many toys each customer bought
SELECT CustomerID, SUM(Quantity) as TotalToys
FROM toy_sales
GROUP BY CustomerID
ORDER BY TotalToys DESC;

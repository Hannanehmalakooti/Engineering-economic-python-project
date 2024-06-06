#Company Financial Forecasting Project
<li>
 You can look through "گزارش کار.pdf" for more information and some visualization of this project.
</li>
Teammates
<ul>
  <li>Fatemeh Iraji 99103677</li>
  <li>Mohammad Mehdi Mehri 99109993</li>
  <li>Hannaneh Malakooti 99100903</li>
  <li>Matin Kharazi 99103858</li>
  <li>Alireza Azadi 400103119</li>
  <li>Sara Yedegari 401104565</li>
</ul>

This project involves analyzing and forecasting the financial data for a company based in Philadelphia. The data is provided in the data.xlsx file, which includes the following columns:
Year
Employee Salaries (per year)
Price of Raw Material 1 (per unit, per year)
Price of Raw Material 2 (per unit, per year)
Product Demand (per year)
Price of Final Product (per unit, per year)
The main goal of this project is to determine the year until which it is economically viable to maintain the company. This requires predicting prices and costs for the upcoming years until 2050. The following tasks outline the steps to be taken to achieve this goal.

Project Tasks
Data Preprocessing
Handle Missing Values: Manage null values in the dataset. This can be done using techniques such as mean imputation, forward fill, or backward fill.
Employee Salaries
Predict Future Salaries: Implement a simple linear regression model to predict employee salaries for future years.
Plot Salaries: Plot the existing employee salary data along with the regression line. Report the accuracy of the regression model.
Raw Material 1 Price
Predict Raw Material 1 Price: Assume the price of Raw Material 1 increases by 1% annually due to inflation. For future years, forecast its price considering an additional 5% interest rate on top of the inflation rate.
Raw Material 2 Price
Predict Raw Material 2 Price: Since the demand for this material is decreasing annually, its value (not price) also decreases linearly. This decrease is relative to the base year 1990, with a 5% interest rate affecting its price. To predict future prices, first multiply the existing prices by the corresponding factors, then apply a linear regression model on the new values.
Plot Raw Material 2 Price: Plot the adjusted prices of Raw Material 2 along with the regression line. Report the accuracy of the regression model.
Product Demand
Calculate Demand Function: Create a new column in the dataset to calculate the output of the function 
𝑒
−
𝑛
50
e 
− 
50
n
​
 
  for each year, where 
𝑛
=
year
−
1990
n=year−1990.
Predict Future Demand: Implement a linear regression model to predict future product demand using the values obtained from the demand function. Use the function outputs as the independent variable (x) in the regression model.
Plot Product Demand: Plot the existing product demand data along with the regression line. Report the accuracy of the regression model. Ensure the x-axis represents the years.
Final Product Price
Predict Final Product Price: Implement a simple linear regression model to predict the price of the final product for future years.
Plot Final Product Price: Plot the existing price data for the final product along with the regression line. Report the accuracy of the regression model.
Objectives
Determine Company Viability: Predict until what year it will be profitable to maintain the company. Consider that the total cost includes the adjusted price of Raw Material 2 based on demand. Discount rates are applied as follows:

18% if demand > 60
10% if demand is between 40 and 60
5% if demand is between 20 and 40
No discount if demand ≤ 20
Investment Planning: One of the stakeholders, who receives 25% of the annual profit, wants to save 20% of his profit from 2022 to 2032. Calculate a fixed annual investment amount for him based on your predictions.

Company Valuation: Determine the purchase price of the company in 2022 to ensure an annual profit of at least $250,000 (in base year dollars).

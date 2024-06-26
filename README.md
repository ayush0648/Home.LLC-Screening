# Home.LLC Screening Task

The task is to find publicly available data for the national factors that impact the pricing of houses in the US, and build a model to study the effect of these variables.
The **S&P CASE-SHILLER Index** is used, as mentioned in the task.

**Factors**

The factors used are:
- Federal Funds Rate
- Unemployment Rate
- Average price of Housing Inventory
- CPI

There could be several other factors, but these have been chosen as they show a direct correlation in change to the Case-Shiller Index.

The datasets have been taken from [https://fred.stlouisfed.org/].

**Approach:**
1. Gathering datasets showing the value of factors across the last 20 years.
2. Clean and process the data: Ensure all factors align in dates, use mean to fill initial empty values and then use linear interpolation to fill the remaining empty ones.
3. Use Power BI to graph the factors and show the correlation between the CASE-SHILLER Index and the other variables.
4. Use linear regression to show the coefficient by which the factors affect the CASE-SHILLER Index.

**File Directory:**
1. The datasets folder contains all the datasets used and created throughout the model.
2. Report.pdf contains this model's step-by-step working and the end result.
3. data_processing.py, extra_dates.py are the ones used for data processing.
4. dashboard.pbix is a Power BI file which contains the dashboard showing the correlation of the Home Price Index against other factors.
5. coefficient_finder.py is the Python code that runs linear regression to determine the coefficients of the Home Price index against the variables.

**References:**
1. https://fred.stlouisfed.org/series/CSUSHPISA
2. https://www.westernasset.com/us/en/research/blog/deciphering-factors-that-impact-the-us-housing-market-2024-03-13.cfm
3. https://point.com/blog/factors-that-affect-home-prices
4. https://helenpainter.com/what-influences-home-value/

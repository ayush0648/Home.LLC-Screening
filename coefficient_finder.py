import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the filtered data
filtered_data = pd.read_csv('combined_data_last_20_years_filtered.csv', parse_dates=['DATE'], index_col='DATE')

# Define the target variable
y = filtered_data['Home_Price_Index']

# Initialize the dictionary to store coefficients
coefficients = {}

# Perform linear regression separately for each factor
for factor in ['CPI', 'Federal_Funds_Rate', 'Housing_Inventory', 'Unemployment_Rate']:
    X = filtered_data[[factor]]
    model = LinearRegression()
    model.fit(X, y)
    coefficients[factor] = model.coef_[0]

# Display the coefficients
for factor, coef in coefficients.items():
    print(f"Coefficient for {factor}: {coef}")
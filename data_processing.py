import pandas as pd

cpi = pd.read_csv('CPIAUCSL.csv', parse_dates=['DATE'], index_col='DATE')
home_price_index = pd.read_csv('CSUSHPISA.csv', parse_dates=['DATE'], index_col='DATE')
federal_funds_rate = pd.read_csv('DFF.csv', parse_dates=['DATE'], index_col='DATE')
housing_inventory = pd.read_csv('ETOTALUSQ176N.csv', parse_dates=['DATE'], index_col='DATE')
unemployment_rate = pd.read_csv('UNRATE.csv', parse_dates=['DATE'], index_col='DATE')

# Aligning all dates to Home Index dates
start_date = '2004-01-01'
end_date = '2024-01-01'

cpi_aligned = cpi[start_date:end_date]
federal_funds_rate_aligned = federal_funds_rate[start_date:end_date]
housing_inventory_aligned = housing_inventory[start_date:end_date]
unemployment_rate_aligned = unemployment_rate[start_date:end_date]

# Resample CPI to monthly data (forward filling the values)
cpi_monthly = cpi_aligned.resample('M').ffill()

# Resample Federal Funds Effective Rate to monthly data (taking the average for each month)
federal_funds_rate_monthly = federal_funds_rate_aligned.resample('M').mean()

# Resample Housing Inventory Estimate to monthly data (forward filling the values)
housing_inventory_monthly = housing_inventory_aligned.resample('M').ffill()

# Combine all datasets into a single DataFrame
combined_data = pd.concat([
    home_price_index,
    cpi_monthly,
    federal_funds_rate_monthly,
    housing_inventory_monthly,
    unemployment_rate_aligned
], axis=1)

# Rename columns for clarity
combined_data.columns = [
    'Home_Price_Index', 
    'CPI', 
    'Federal_Funds_Rate', 
    'Housing_Inventory', 
    'Unemployment_Rate'
]

# Fill initial NaN values by taking the mean for the month across all years
combined_data = combined_data.apply(lambda x: x.fillna(x.groupby(x.index.month).transform('mean')))

# Interpolate missing values using linear interpolation after the first non-NaN value in each column
combined_data = combined_data.apply(lambda x: x.interpolate(method='linear', limit_area='inside'))

# Save the combined data to a CSV file
combined_data.to_csv('combined_data_last_20_years.csv')

# Display the first few rows of the combined data to verify
print(combined_data.head())

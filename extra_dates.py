import pandas as pd

combined_data = pd.read_csv('combined_data_last_20_years.csv', parse_dates=['DATE'], index_col='DATE')

# Filter the DataFrame to keep only data from the last 20 years
start_date = '2004-01-01'
end_date = '2024-01-01'
filtered_data = combined_data.loc[start_date:end_date]

# Save the filtered data to a new CSV file
filtered_data.to_csv('combined_data_last_20_years_filtered.csv')

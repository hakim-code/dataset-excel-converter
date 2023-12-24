# Import the pandas library for data manipulation
import pandas as pd

# This line assumes that 'loaded_data' is a pre-existing DataFrame containing your main data
# It also assumes 'frequency', 'forecast_horizon', 'contain_missing_values',
# and 'contain_equal_length' are predefined variables

# Create a new DataFrame for summary information
# This DataFrame consists of a single row with the summary variables
summary_data = pd.DataFrame({
    'frequency': [frequency],                      # Add 'frequency' as a column with its value
    'forecast_horizon': [forecast_horizon],        # Add 'forecast_horizon' as a column
    'contain_missing_values': [contain_missing_values],  # Add 'contain_missing_values'
    'contain_equal_length': [contain_equal_length] # Add 'contain_equal_length'
})

# Combine the 'loaded_data' DataFrame with the 'summary_data' DataFrame
# The concat function is used for concatenation along a particular axis
# axis=1 denotes concatenation along the columns (side-by-side)
combined_data = pd.concat([loaded_data, summary_data], axis=1)

# Export the combined DataFrame to an Excel file
# 'forecasting_data.xlsx' is the filename for the exported Excel file
# index=False means that the index of the DataFrame (row numbers) will not be written to the Excel file
combined_data.to_excel('forecasting_data.xlsx', index=False)

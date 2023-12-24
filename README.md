# dataset-excel-converter
This converter enables the conversion of tsf formatted dataset into excel format.  Credits are given to Huggingsface/glutonTS for the tsf dataset. 

In this work we use Pandas library to interact with tsf data.

import pandas as pd: Imports the pandas library for data manipulation.
summary_data = pd.DataFrame({...}): Creates a new DataFrame named summary_data with specified summary variables as columns.

pd.concat([loaded_data, summary_data], axis=1): Merges the loaded_data DataFrame with summary_data, aligning them column-wise.

combined_data.to_excel('forecasting_data.xlsx', index=False): Saves the merged DataFrame to an Excel file without including the row indices.

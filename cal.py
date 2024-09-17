# import pandas as pd

# # Creating a dataframe for the data
# data = {
#     'State': ['Johor', 'Kedah', 'Kelantan', 'Melaka', 'Negeri Sembilan', 'Pahang', 'Pulau Pinang', 'Perak', 
#               'Perlis', 'Selangor', 'Terengganu', 'Sabah', 'Sarawak', 'WP K Lumpur', 'WP Labuan', 'WP Putrajaya'],
#     'Establishments_2022': [15727, 6603, 7181, 4838, 6362, 6841, 11432, 11551, 1475, 24625, 6825, 7875, 10654, 11692, 369, 246],
#     'Establishments_2015': [16259, 12181, 11434, 7298, 8471, 8397, 12272, 15072, 1886, 28793, 8319, 7447, 10804, 18143, 379, 335],
#     'CAGR_Percentage': [-0.47, -8.38, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
# }

# df = pd.DataFrame(data)

# # Defining a function to calculate CAGR
# def calculate_cagr(final_value, initial_value, years):
#     if initial_value == 0:
#         return None
#     return ((final_value / initial_value) ** (1 / years) - 1) * 100

# # Number of years between 2022 and 2015
# years = 7

# # Calculating missing CAGRs
# df['CAGR_Percentage'] = df.apply(lambda x: calculate_cagr(x['Establishments_2022'], x['Establishments_2015'], years), axis=1)

# # export as csv file in current directory
# df.to_csv('data.csv', index=False)

import pandas as pd

# Read the CSV file
df = pd.read_csv("js/data.csv")

# Check the data types of each column
print(df.dtypes)
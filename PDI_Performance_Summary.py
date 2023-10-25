# Importing required libraries
import pandas as pd
import os

# Define the path to the CSV file
# Note: You'll need to specify the correct path where your file is located.
csv_file_path = 'your/file/path.csv'

# Read the CSV file into a DataFrame
wcn_df = pd.read_csv(csv_file_path)

# Display the first few rows to understand its structure
wcn_df.head()

# Group the DataFrame by 'About' and calculate the mean for each group, setting numeric_only=True
grouped_wcn_df = wcn_df.groupby('About').mean(numeric_only=True).reset_index()

# Display the first few rows of the aggregated DataFrame
grouped_wcn_df.head()

# Sort the DataFrame by 'Overall Pass %' in descending order
sorted_wcn_df = grouped_wcn_df.sort_values(by='Overall Pass %', ascending=False).reset_index(drop=True)

# Assign rankings in a new column 'Class Ranking'
sorted_wcn_df['Class Ranking'] = sorted_wcn_df.index + 1

# Create a new column 'T5B5' and populate it with 'Top 5' and 'Bottom 5' based on 'Class Ranking'
top_5 = sorted_wcn_df.nlargest(5, 'Overall Pass %').index
bottom_5 = sorted_wcn_df.nsmallest(5, 'Overall Pass %').index

sorted_wcn_df['T5B5'] = ''
sorted_wcn_df.loc[top_5, 'T5B5'] = 'Top 5'
sorted_wcn_df.loc[bottom_5, 'T5B5'] = 'Bottom 5'

# Display the first few rows of the DataFrame with rankings and labels
print(sorted_wcn_df.head())
print(sorted_wcn_df.tail())

# Calculate the team average for each WCN event and 'Overall Pass %', excluding the 'About' column
team_averages = grouped_wcn_df.drop(columns=['About']).mean()

# Create new columns in the DataFrame for team averages
for column in team_averages.index:
    team_column = f'Team {column}'
    sorted_wcn_df[team_column] = team_averages.loc[column]

# Display the first few rows of the DataFrame with team averages
sorted_wcn_df.head()

# Create a new DataFrame with the columns needed for the GPSDSU Performance Report
gpsdsu_columns = ['UW %', 'M&S %', 'BB %', 'KTS %', 'ER %', 'TW %', 'DP %', 'Total Average %', 'T5B5', 'Class Ranking',
                  'Team UW %', 'Team M&S %', 'Team BB %', 'Team KTS %', 'Team ER %', 'Team TW %', 'Team DP %']

gpsdsu_df = pd.DataFrame(columns=gpsdsu_columns)

# Include the 'About' column from the sorted_wcn_df
gpsdsu_df['About'] = sorted_wcn_df['About']

# Populate the new DataFrame with data from sorted_wcn_df
gpsdsu_df['UW %'] = sorted_wcn_df['UW Pass %']
gpsdsu_df['M&S %'] = sorted_wcn_df['MS Pass %']
gpsdsu_df['BB %'] = sorted_wcn_df['BB Pass %']
gpsdsu_df['KTS %'] = sorted_wcn_df['KTS Pass %']
gpsdsu_df['ER %'] = sorted_wcn_df['ER Pass %']
gpsdsu_df['TW %'] = sorted_wcn_df['TW Pass %']
gpsdsu_df['DP %'] = sorted_wcn_df['DP Pass %']
gpsdsu_df['Total Average %'] = sorted_wcn_df['Overall Pass %']
gpsdsu_df['T5B5'] = sorted_wcn_df['T5B5']
gpsdsu_df['Class Ranking'] = sorted_wcn_df['Class Ranking']
gpsdsu_df['Team UW %'] = sorted_wcn_df['Team UW Pass %']
gpsdsu_df['Team M&S %'] = sorted_wcn_df['Team MS Pass %']
gpsdsu_df['Team BB %'] = sorted_wcn_df['Team BB Pass %']
gpsdsu_df['Team KTS %'] = sorted_wcn_df['Team KTS Pass %']
gpsdsu_df['Team ER %'] = sorted_wcn_df['Team ER Pass %']
gpsdsu_df['Team TW %'] = sorted_wcn_df['Team TW Pass %']
gpsdsu_df['Team DP %'] = sorted_wcn_df['Team DP Pass %']

# Reorder the columns to have 'About' as the first column
final_columns_order = ['About'] + gpsdsu_columns
gpsdsu_df = gpsdsu_df[final_columns_order]

# Extract last names and create a temporary column for sorting
gpsdsu_df['Last_Name'] = gpsdsu_df['About'].apply(lambda x: x.split(' ')[1] if ' ' in x else x)

# Sort the DataFrame by 'Last_Name' in alphabetical order
gpsdsu_df.sort_values(by='Last_Name', ascending=True, inplace=True)

# Drop the temporary 'Last_Name' column as it is no longer needed
gpsdsu_df.drop(columns=['Last_Name'], inplace=True)

# Display the first few rows of the GPSDSU Performance Report DataFrame
gpsdsu_df.head()

# Define the path where you want to save the CSV file
save_path = '/file/path.csv'

# Export the DataFrame to a CSV file
gpsdsu_df.to_csv(save_path, index=False)

print(f"GPSDSU Performance Report has been saved to {save_path}")


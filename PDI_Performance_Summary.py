# Import required libraries
import pandas as pd

# Step 1: Load Data
# -----------------
# Define the path to the CSV file (change this to your actual file path)
csv_file_path = '/filepath/pdi_wcn_progress_check_wk.csv'

# Read the CSV file into a DataFrame
wcn_df = pd.read_csv(csv_file_path)

# Step 2: Data Aggregation
# -------------------------
# Group by 'About' and calculate the mean for numerical columns
grouped_wcn_df = wcn_df.groupby('About').mean(numeric_only=True).reset_index()

# Step 3: Ranking and Labeling
# -----------------------------
# Sort by 'Overall Pass %' in descending order and reset index
sorted_wcn_df = grouped_wcn_df.sort_values(by='Overall Pass %', ascending=False).reset_index(drop=True)

# Add class ranking based on the sorted order
sorted_wcn_df['Class Ranking'] = sorted_wcn_df.index + 1

# Add labels for Top 5 and Bottom 5
top_5 = sorted_wcn_df.nlargest(5, 'Overall Pass %').index
bottom_5 = sorted_wcn_df.nsmallest(5, 'Overall Pass %').index

sorted_wcn_df['T5B5'] = ''
sorted_wcn_df.loc[top_5, 'T5B5'] = 'Top 5'
sorted_wcn_df.loc[bottom_5, 'T5B5'] = 'Bottom 5'

# Step 4: Calculate Team Averages
# --------------------------------
# Calculate the team average for each event and 'Overall Pass %'
team_averages = grouped_wcn_df.drop(columns=['About']).mean()

# Add team averages to DataFrame
for column in team_averages.index:
    team_column = f'Team {column}'
    sorted_wcn_df[team_column] = team_averages.loc[column]

# Step 5: Assemble Data for GPSDSU Report
# ----------------------------------------
# Define the columns required for the GPSDSU report
gpsdsu_columns = [ ... ]  # As previously defined

# Create a new DataFrame for the GPSDSU report
gpsdsu_df = sorted_wcn_df[['About'] + gpsdsu_columns]

# Step 6: Export to CSV
# -----------------------
# Define the save path (change this to your desired directory)
save_path = '/pathname/pdi_performance_report.csv'

# Save the DataFrame to a CSV file
gpsdsu_df.to_csv(save_path, index=False)

# Print a confirmation message
print(f"PDI Performance Report has been saved to {save_path}")

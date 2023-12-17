import pandas as pd
from datetime import datetime

sheet_name = 'Session - Race'

# Load the Excel file into a pandas DataFrame
excel_file_path = r'C:\Users\jakob\software\sim_racing\garage61 data\Garage 61 - IMSA Vintage Series - Race - Export - 2023-12-16-19-41-03.xlsx'
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

# Function to convert lap time to total seconds
def lap_time_to_seconds(lap_time):
    # Use lap_time instead of 'Lap time' as a string
    lap_time_obj = datetime.strptime(str(lap_time), "%H:%M:%S.%f")
    total_seconds = lap_time_obj.hour * 3600 + lap_time_obj.minute * 60 + lap_time_obj.second + lap_time_obj.microsecond / 1e6
    return total_seconds

# Apply the function to the 'Lap time' column and create a new column 'total_seconds'
df['total_seconds'] = df['Lap time'].apply(lap_time_to_seconds)

# Save the modified DataFrame back to Excel
output_file_path = r'C:\Users\jakob\software\sim_racing\garage61 data\Garage 61 - IMSA Vintage Series - Race - Export - 2023-12-16-19-41-03 (adjusted).xlsx'
df.to_excel(output_file_path, index=False)

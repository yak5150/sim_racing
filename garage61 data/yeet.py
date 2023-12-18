import pandas as pd
from datetime import datetime

sheet_name = 'Session - Race'
excel_file_path = r'C:\Users\jakob\software\sim_racing\garage61 data\Garage 61 - IMSA Vintage Series - Race - Export - 2023-12-16-19-41-03.xlsx'
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

def lap_time_to_seconds(lap_time):
    try:
        lap_obj = datetime.strptime(str(lap_time), "%H:%M:%S.%f")
        total_seconds = lap_obj.hour * 3600 + lap_obj.minute * 60 + lap_obj.second + lap_obj.microsecond / 1e6
        return total_seconds
    except ValueError:
        return None

df['total_seconds'] = df['Lap time'].apply(lap_time_to_seconds)

print(df)
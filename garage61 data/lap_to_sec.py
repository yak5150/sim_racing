import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


excel_file_path = input("Enter Garage 61 excel file path:").strip('"')
sheet_name = 'Session - Race'
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

def lap_time_to_seconds(lap_time):
    try:
        lap_obj = datetime.strptime(str(lap_time), "%H:%M:%S.%f")
        total_seconds = lap_obj.hour * 3600 + lap_obj.minute * 60 + lap_obj.second + lap_obj.microsecond / 1e6
        return total_seconds
    except ValueError:
        return None

df['total_seconds'] = df['Lap time'].apply(lap_time_to_seconds)

plt.plot('Lap', 'total_seconds', data=df)
plt.xlabel('Lap Number')
plt.ylabel('Total Seconds')
plt.grid(True)
plt.show()
import random
from enum import Enum

class track(Enum):
    with open('track_list.txt', 'r') as file:
        for line in file:
            track_name = line.strip()
            globals()[track_name] = track_name

class car(Enum):
    with open('car_list.txt', 'r') as file:
        for line in file:
            car_name = line.strip()
            globals()[car_name] = car_name

random_track = random.choice(list(track))
random_car = random.choice(list(car))

print(f"Your car & track combo is: {random_car} at {random_track}")
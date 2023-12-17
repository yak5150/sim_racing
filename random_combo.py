import random
from enum import Enum

with open('track_list.txt', 'r') as file:
    track_names = [line.strip() for line in file]

track_list = Enum('track', track_names)

with open('car_list.txt', 'r') as file:
    car_names = [line.strip() for line in file]

car_list = Enum('car', car_names)

random_track = random.choice(list(track_list)).name
random_car = random.choice(list(car_list)).name

print(f"Your car & track combo is: {random_car} at {random_track}")
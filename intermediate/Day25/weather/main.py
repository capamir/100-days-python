# import csv

# with open("weather_data.csv") as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperature = int(row[1])
#             temperatures.append(temperature)

#     print(temperatures)

import pandas as pd


data = pd.read_csv("weather_data.csv")

# temperatures = data["temp"].to_list()
# avg = sum(temperatures) / len(temperatures)
# print(round(avg, 2))
# print(data["temp"].mean())

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32

print(monday_temp_F)
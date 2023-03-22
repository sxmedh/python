import pandas
# import csv
# with open("data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# for item in temperatures:
#     print(item)


data = pandas.read_csv("data.csv")
print(data)
print("")
print(type(data))
print()
print(type(data["temp"]))
print("")
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# x = 0
# for temp in temp_list:
#     x += temp

# avg_temp = x/len(temp)
# print(f"average temperature {avg_temp}")
print(f"average temperature {data['temp'].mean()}")
print(f"average temperature {data['temp'].max()}")

print(data["condition"])
print(data.condition)

print(data[data.day == 'monday'])

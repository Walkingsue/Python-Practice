import csv

highest_selling = 0

with open("Sheet1.csv", "r", encoding="utf-8") as file:
  csv_reader = csv.reader(file)
  header = next(csv_reader)

  list_of_sales = [float(val[4]) for val in csv_reader]

  for val in list_of_sales:
    if val > highest_selling:
      highest_selling = val

print(highest_selling)
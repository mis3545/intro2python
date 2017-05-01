import csv
with open('date.csv', mode='r') as fp:
    reader = csv.reader(fp)
    dates = {row[0]: int(row[1]) for row in reader}
    print(dates)


date_list = list(dates.keys())
print(date_list[0])
print(date_list[1])

import csv
def count_records():
    with open("judedata/car_prices.csv") as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        r = 0
        for row in csvreader:
            r =  r+1
        print(f"There are {r} records in total")

count_records()
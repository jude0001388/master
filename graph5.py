import csv

def create_lists():
 makes_list = []
 num_solid_list = []
 avg_price_list = []

 with open("judedata/car_sales.csv") as csvfile:
     reader = csv.reader(csvfile)
     header = next(reader)
     for row in reader:
         makes_list.append(row[0])
         num_solid_list.append(row[1])
         avg_price_list.append(row[2])
     return makes_list, num_solid_list, avg_price_list
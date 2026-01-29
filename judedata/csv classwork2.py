import csv
def display_make(car_make):
    print(f"{'year':<6}{'Make':<10}{'model':<20}{'sellingprice':<6}")
    with open('car_prices.csv',mode='r',newline='') as file:
        csvreader = csv.reader(file)
        header_csvreader = csv.reader= next(file)

        for row in csvreader:
            year = row[0]
            make = row[1]
            model = row[2]
            sellingprice = row[6]
            if make == car_make:
                print(f"{year:<6}{make:<10}{model:<20}{sellingprice:<6}")


display_make("VW")


def display():
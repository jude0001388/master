import csv
def create_brands_list():
    phones_data = []

 with open("mobile_phones.csv") as csvfile:
     reader = csv.reader(csvfile)
     for row in reader:
         brands_list = []
         row[0] = row[0].strip()
         row[1] = row[1].strip()

        phones_data.append(row)
     return phones_data



import csv
def read_csv_file():
 phones_data = []

 with open("mobile_phones.csv") as csvfile:
     reader = csv.reader(csvfile)
     header = next(reader)
     for row in reader:

         phones_data.append(row)
     return phones_data

def create_brands_list(phones_data):
    brands_list = []
    for row in phones_data:
        if row[0] not in brands_list:
            brands_list.append(row[0])
    return sorted( brands_list)

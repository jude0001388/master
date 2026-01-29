import csv
def list_all_makes():
    all_list=[]
    with open("cars.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:
             make = row[1]
             if make not in all_makes:
                 all_makes.append(make)
    return all_makes

#---------------Main program---------------
makes=list_all_makes()

print("list of all makes in the file:")
for m in makes:
    print(m)
    print("/n there are",len(makes),"cars in total")
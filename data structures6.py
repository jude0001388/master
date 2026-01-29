#set up the list of tuples
german_cars =[('Audi',5064), ('Bmw',6350), ('Ford',10954),('Mercedes',4390),('Porsche',755)]
#append vw to the list
german_cars.append(('VW',8745))
#remove ford from the list
german_cars.remove(('Ford',10954))
#print the list
print("The list contains the following vehicles")

for brand, sales in german_cars:
    print(f"{brand} has {sales} sales")

#second list of japanese cars
japanese_cars =[('Honda',9200),('Lexus',2665),('Mazda',3450),('Suzuki')]

#list of german car brands
german_cars = ('Audi','bmw','Mercedes','Porsche','Vw')

while True:
    car = input("Enter a car name")
    if car == 'end':
        print("program ended")
        break
    if car in german_cars:
        index_position = german_cars.index(car)
        print(f"{car} is at position {index_position}")
    else:
        print(f"{car} is not in the list")
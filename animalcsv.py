import csv

def create_animal_dict(file):
    animal_dict = {}
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headings = next(csv_reader)
        key1 = headings[0]
        key2 = headings[1]
        count = 1
        for row in csv_reader:
            key = "animal" + str(count)
            animal_dict[key]={key1:row[0],key2:row[1]}
            count +=1
            return animal_dict
animal_dict = create_animal_dict("judedata/longleat_zoo.csv")
print(animal_dict)
animal_dict = create_animal_dict("judedata/marwell_zoo.csv")
print(animal_dict)

def print_inventory(zoo_name,dictionary_name):
    print(f"the animals in{zoo_name} are:")
    for animal, count in dictionary_name.items():
        print(f"{animal}: {count}")
        print()

if __name__ == "__main__":
    zoo_name = "longleat_zoo"

marwell_zoo={
    "Rabbit": 4,
    "Elephant": 2,
    "Panda": 2,
    "Lion": 3
}
longleat_zoo={
    "Tiger": 4,
    "Giraffe": 2,
    "Zebra": 7,
    "Penguin": 10
}
print_inventory(zoo_name,longleat_zoo)


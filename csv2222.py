import csv
def create_animal_set(file):
    animal_set = set()
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            animal_set.add(row[0])
            animal_set.add(animal_set)
        return animal_set
zoo1_animals = create_animal_set("judedata/longleat_zoo.csv")
zoo2_animals = create_animal_set("judedata/marwell_zoo.csv")

zoo_union = zoo1_animals.union(zoo2_animals)
zoo_diff = zoo1_animals.intersection(zoo2_animals)
zoo_longleat =zoo1_animals.difference(zoo2_animals)
zoo_marwell = zoo1_animals.difference(zoo2_animals)

print(f"longleat zoo animals: {zoo_longleat}")
print(f"marwell zoo animals: {zoo_marwell}")
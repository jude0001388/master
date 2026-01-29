#display menu and return user choice
def display_menu():
    print("Menu:")
    print("add a fruit")
    print("remove a fruit")
    print("display a menu")
    print("exit the program")
    choice = input("choice: ")
    return choice
def option1():
    fruit = input("Enter a fruit to add").lower()
    if fruit in fruits:
        print("the fruit is already added to the list")
    else:
        fruits.append(fruit)
        print(f"the {fruit} is added to the list")

# function 3: removing a fruit
def option2():
    fruit = input("Enter a fruit to remove").lower()
    if fruit not in fruits:
        print("the fruit is already removed from the list")
    else:
        fruits.remove(fruit)
        print(f"the {fruit} is removed from the list")

#set up the list
fruits = ["apple", "banana", "lemon", "orange"]

#main program
while True:
    choice = display_menu()
    if choice == "add":
        option1()
    elif choice == "remove":
        option2()
    elif choice == "display":
        print("current list of the fruits, ",fruits)
    elif choice == "exit":
        break

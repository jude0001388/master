import csv

def main_menu():
    while True:
        print("1.all phones of given brand")
        print("2.display the average price for each brand")
        print("3.display a bar chart showing the 10 most expensive phones")
        print("4. display a bar chart showing the cheapest phones")
        try:
            choice = int(input("Enter your choice:"))
            if choice == [1,2,3,4]:
                return choice
            else:
                print("Invalid choice")
              except ValueError:
             print("Invalid choice")

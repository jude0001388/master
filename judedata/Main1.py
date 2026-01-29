from Process1 import load_reviews, write_summary
from Tui1 import main_menu, view_data_menu
from Visual1 import visualise_data_menu

def print_title():
    title = "Disneyland Review"
    print(title)
    print("-" * len(title))

def main():
    print_title()

    reviews = load_reviews("disneyland_reviews.csv")
    print(f"loaded successfully. Rows: {len(reviews)}")

    while True:
        choice = main_menu()

        if choice == "A":
            view_data_menu(reviews)

        elif choice == "B":
            visualise_data_menu(reviews)

        elif choice == "C":
            write_summary(reviews)

        elif choice == "X":
            print("Exiting program...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

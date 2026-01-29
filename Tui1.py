from Process1 import (
    get_reviews_by_park,
    count_reviews_by_location,
    average_score_by_year,
    average_score_by_location
)

def main_menu():
    print("\nPlease enter the letter which corresponds with your desired menu choice:\n")
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[C] Export Summary")
    print("[X] Exit\n")

    return input(">> ").strip().upper()


def view_data_menu(reviews):
    print("\nPlease enter one of the following options:\n")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Park and Reviewer Location")
    print("[C] Average Score per Year by Park")
    print("[D] Average Score per Park by Reviewer Location\n")

    choice = input(">> ").strip().upper()

    if choice == "A":
        park = input("Enter park: ")
        results = get_reviews_by_park(reviews, park)
        for r in results:
            print(f"{r['Reviewer_Location']} | {r['Rating']} | {r['Review']}")

    elif choice == "B":
        park = input("Enter park: ")
        location = input("Enter reviewer location: ")
        count = count_reviews_by_location(reviews, park, location)
        print(f"{park} has {count} reviews from {location}.")

    elif choice == "C":
        park = input("Enter park: ")
        year = input("Enter year: ")
        avg = average_score_by_year(reviews, park, year)
        print(f"Average rating: {avg:.2f}" if avg else "No data found.")

    elif choice == "D":
        data = average_score_by_location(reviews)
        for park, locs in data.items():
            print(f"\n--- {park} ---")
            for loc, avg in locs.items():
                print(f"{loc}: {avg:.2f}")

    else:
        print("choice invalid.")

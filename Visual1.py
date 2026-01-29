import matplotlib.pyplot as plt
from collections import Counter

def visualise_data_menu(reviews):
    print("\nPlease enter one of the following options:\n")
    print("[A] Most Reviewed Park")
    print("[B] Average Scores")
    print("[C] Most Popular Month by Park\n")

    choice = input(">> ").strip().upper()

    if choice == "A":
        pie_reviews_per_park(reviews)

    elif choice == "B":
        bottom_10_locations(reviews)

    elif choice == "C":
        avg_rating_by_month(reviews)

    else:
        print("choice invalid.")
def pie_reviews_per_park(reviews):
    counts = Counter(r["Park"] for r in reviews)

    plt.pie(counts.values(), labels=counts.keys(), autopct="%1.1f%%")
    plt.title("Reviews per Park")
    plt.show()
def bottom_10_locations(reviews):
    park = input("Enter Park: ").strip()

    scores = {}
    for r in reviews:
        if r["Park"] == park:
            loc = r["Reviewer_Location"]
            scores.setdefault(loc, []).append(float(r["Rating"]))

    averages = {loc: sum(vals)/len(vals) for loc, vals in scores.items()}
    bottom = sorted(averages.items(), key=lambda x: x[1])[:10]

    locations, values = zip(*bottom)

    plt.bar(locations, values)
    plt.xticks(rotation=45)
    plt.title(f"Lowest Avg Ratings for {park}")
    plt.show()
def avg_rating_by_month(reviews):
    park = input("Enter Park: ").strip()

    month_map = {
        "January": 1, "February": 2, "March": 3, "April": 4,
        "May": 5, "June": 6, "July": 7, "August": 8,
        "September": 9, "October": 10, "November": 11, "December": 12
    }

    monthly = {m: [] for m in month_map}

    for r in reviews:
        if r["Park"] == park:
            monthly[r["Month"]].append(float(r["Rating"]))

    months = list(month_map.keys())
    averages = [
        (sum(monthly[m]) / len(monthly[m])) if monthly[m] else 0
        for m in months
    ]

    plt.bar(months, averages)
    plt.xticks(rotation=45)
    plt.title(f"Average Rating per Month — {park}")
    plt.show()

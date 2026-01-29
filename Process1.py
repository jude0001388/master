import csv
from collections import Counter

def load_reviews(filename):
    data = []
    with open(filename, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def get_reviews_by_park(reviews, park):
    return [r for r in reviews if r["Park"] == park]


def count_reviews_by_location(reviews, park, location):
    return sum(
        1 for r in reviews
        if r["Park"] == park and r["Reviewer_Location"] == location
    )


def average_score_by_year(reviews, park, year):
    ratings = [
        float(r["Rating"])
        for r in reviews
        if r["Park"] == park and r["Year"] == year
    ]
    return sum(ratings)/len(ratings) if ratings else None


def average_score_by_location(reviews):
    parks = {}

    for r in reviews:
        park = r["Park"]
        loc = r["Reviewer_Location"]
        rating = float(r["Rating"])

        parks.setdefault(park, {})
        parks[park].setdefault(loc, []).append(rating)

    return {
        park: {loc: sum(vals)/len(vals) for loc, vals in locs.items()}
        for park, locs in parks.items()
    }


def write_summary(reviews):
    parks = {}

    for r in reviews:
        park = r["Park"]
        rating = float(r["Rating"])

        parks.setdefault(park, {"count": 0, "positive": 0, "ratings": []})
        parks[park]["count"] += 1
        parks[park]["ratings"].append(rating)
        if rating >= 4:
            parks[park]["positive"] += 1

    with open("review_summary.txt", "w") as f:
        for park, data in parks.items():
            avg = sum(data["ratings"]) / len(data["ratings"])
            f.write(
                f"{park}\n"
                f"Total Reviews: {data['count']}\n"
                f"Positive Reviews: {data['positive']}\n"
                f"Average Score: {avg:.2f}\n\n"
            )

    print("Summary written to review_summary.txt")


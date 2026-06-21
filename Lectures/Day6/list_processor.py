"""
Idea 3: The "List-Processor" Web Scraper (Mock)
Focus: List Comprehensions, Lambda Functions, and map/filter/reduce
Team: 5 People | Time: 60 Minutes
"""

import csv
from functools import reduce


# ============================================================
# PERSON 1 — Load CSV & parse into list of dicts
# ============================================================

def load_csv(filepath: str) -> list[dict]:
    """
    Reads the CSV file and returns a list of dictionaries.
    Each dict has keys: Name, Email, Age (int), City, Purchase_Amount (float).
    """
    users = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            users.append({
                "Name":            row["Name"],
                "Email":           row["Email"],
                "Age":             int(row["Age"]),
                "City":            row["City"],
                "Purchase_Amount": float(row["Purchase_Amount"]),
            })
    return users


# ============================================================
# PERSON 2 — filter() + map() for "Over 30 & spent > $100"
# ============================================================

def filter_high_value_users(users: list[dict]) -> list[dict]:
    """
    Uses filter() + lambda to keep users who are:
      - Age > 30  AND
      - Purchase_Amount > 100
    """
    return list(
        filter(lambda u: u["Age"] > 30 and u["Purchase_Amount"] > 100, users)
    )


def extract_emails(filtered_users: list[dict]) -> list[str]:
    """
    Uses map() + lambda to pull just the email from each filtered user.
    """
    return list(map(lambda u: u["Email"], filtered_users))


# ============================================================
# PERSON 3 — List comprehension for New York users
# ============================================================

def new_york_name_age(users: list[dict]) -> list[str]:
    """
    Returns a list of "Name: Age" strings for every user based in New York,
    built entirely with a list comprehension.
    """
    return [
        f"{u['Name']}: {u['Age']}"
        for u in users
        if u["City"] == "New York"
    ]


# ============================================================
# PERSON 4 — reduce() for total sum  +  top-5 oldest sorting
# ============================================================

def total_purchase_amount(users: list[dict]) -> float:
    """
    Uses functools.reduce to sum every user's Purchase_Amount.
    No built-in sum() allowed — pure reduce.
    """
    return reduce(lambda acc, u: acc + u["Purchase_Amount"], users, 0.0)


def top5_oldest_names(users: list[dict]) -> list[str]:
    """
    Sorts ALL users by Age (descending), takes the top 5, returns their names.
    Uses a lambda as the sort key.
    """
    sorted_users = sorted(users, key=lambda u: u["Age"], reverse=True)
    return [u["Name"] for u in sorted_users[:5]]


# ============================================================
# PERSON 5 — Integrator: main() glues everything together
# ============================================================

def print_section(title: str) -> None:
    print(f"\n{'=' * 55}")
    print(f"  {title}")
    print('=' * 55)


def main():
    CSV_PATH = "users.csv"   # judges will place their file here

    # --- Person 1: Load data ---
    print_section("Loading Data")
    users = load_csv(CSV_PATH)
    print(f"  Total records loaded : {len(users)}")

    # --- Person 2: Filter + Map ---
    print_section("REQUIREMENT 1 & 2 — High-Value Users (Age>30 & Spent>$100)")
    high_value = filter_high_value_users(users)
    emails     = extract_emails(high_value)
    print(f"  Users matching filter : {len(high_value)}")
    print(f"  Sample emails (first 5):")
    for email in emails[:5]:
        print(f"    • {email}")

    # --- Person 3: List comprehension ---
    print_section("REQUIREMENT 3 — New York Users  (Name: Age)")
    ny_list = new_york_name_age(users)
    print(f"  New York user count : {len(ny_list)}")
    print(f"  Sample (first 5):")
    for entry in ny_list[:5]:
        print(f"    • {entry}")

    # --- Person 4: reduce + sorting ---
    print_section("REQUIREMENT 4 — Total Purchase Amount (via reduce)")
    total = total_purchase_amount(users)
    print(f"  Total spend across all users : ${total:,.2f}")

    print_section("REQUIREMENT 5 — Top 5 Oldest Users")
    oldest = top5_oldest_names(users)
    for rank, name in enumerate(oldest, 1):
        print(f"  #{rank}  {name}")

    print(f"\n{'=' * 55}")
    print("  All requirements complete!")
    print('=' * 55)


if __name__ == "__main__":
    main()

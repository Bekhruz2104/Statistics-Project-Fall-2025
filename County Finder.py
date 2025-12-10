import math

# === ACS 2023 median household income ===
median_income = {
    "Hunterdon": 131846, "Morris": 131825, "Somerset": 128774, "Bergen": 121273,
    "Monmouth": 112308, "Sussex": 111256, "Middlesex": 108088, "Burlington": 103754,
    "Mercer": 101980, "Warren": 97910, "Union": 91817, "Gloucester": 88626,
    "Ocean": 80089, "Cape May": 78434, "Hudson": 76298, "Passaic": 72420,
    "Camden": 71395, "Essex": 63490, "Atlantic": 62043, "Salem": 67500,
    "Cumberland": 52667,
}

# === NJ county populations (2023 estimates) ===
population = {
    "Bergen": 955000, "Middlesex": 871000, "Essex": 862000, "Hudson": 702000,
    "Ocean": 655000, "Monmouth": 643000, "Union": 575000, "Camden": 523000,
    "Passaic": 513000, "Morris": 510000, "Burlington": 462000, "Mercer": 387000,
    "Somerset": 345000, "Gloucester": 303000, "Atlantic": 274000, "Cumberland": 154000,
    "Sussex": 145000, "Hunterdon": 129000, "Warren": 110000, "Cape May": 95000,
    "Salem": 66000,
}

def county_probabilities(salary, sigma=25000):
    raw = {}

    for county, median in median_income.items():
        # Gaussian likelihood of salary vs median
        diff = salary - median
        likelihood = math.exp(-(diff**2) / (2 * sigma**2))

        # Population weighting (Bayesian prior)
        weighted = likelihood * population[county]

        raw[county] = weighted

    # Normalize to probabilities
    total = sum(raw.values())
    probs = {c: raw[c] / total for c in raw}

    # Sort high → low
    return dict(sorted(probs.items(), key=lambda x: x[1], reverse=True))


# ==== Example ====
salary = int(input("Enter annual salary: $"))
probs = county_probabilities(salary)

print("\nNJ County Probabilities")
for county, p in probs.items():
    print(f"{county}: {p*100:.2f}%")

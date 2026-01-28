"""
Route, distance, duration, fare & interchange logic
Assumptions documented as official data is not published yet
"""

METRO_LINES = {
    "Blue Line": [
        "Patna Junction",
        "Akashvani",
        "Gandhi Maidan",
        "PMCH",
        "Moin-ul-Haq Stadium",
        "Khemni Chak"
    ],
    "Red Line": [
        "Danapur Cantonment",
        "Saguna Mor",
        "RPS Mor",
        "Patliputra",
        "Khemni Chak"
    ]
}

# Assumptions (clearly documented)
FARE_PER_STATION = 10        # ₹
DISTANCE_PER_STATION = 1.2  # km
TIME_PER_STATION = 3        # minutes

FIRST_TRAIN_TIME = "06:00 AM"
LAST_TRAIN_TIME = "10:30 PM"

def find_route(start, end):
    for line, stations in METRO_LINES.items():
        if start in stations and end in stations:
            s, e = stations.index(start), stations.index(end)
            route = stations[s:e+1] if s <= e else stations[e:s+1][::-1]
            return route, [line]

    # Interchange case (via Khemni Chak)
    if start != end:
        common = "Khemni Chak"
        for l1, s1 in METRO_LINES.items():
            if start in s1:
                for l2, s2 in METRO_LINES.items():
                    if end in s2 and common in s1 and common in s2:
                        r1 = s1[s1.index(start):s1.index(common)+1]
                        r2 = s2[s2.index(common)+1:s2.index(end)+1]
                        return r1 + r2, [l1, l2]

    return [], []

def calculate_summary(route, lines):
    stations_between = route[1:-1]
    distance = (len(route) - 1) * DISTANCE_PER_STATION
    duration = (len(route) - 1) * TIME_PER_STATION
    fare = (len(route) - 1) * FARE_PER_STATION
    interchanges = max(0, len(lines) - 1)

    return {
        "stations_between": stations_between,
        "distance_km": distance,
        "duration_min": duration,
        "fare": fare,
        "first_train": FIRST_TRAIN_TIME,
        "last_train": LAST_TRAIN_TIME,
        "interchanges": interchanges
    }

if __name__ == "__main__":
    start = "Patna Junction"
    end = "Patliputra"

    route, lines = find_route(start, end)
    summary = calculate_summary(route, lines)

    print(f"\nRoute from {start} to {end}")
    print("Stations:", " → ".join(route))
    print("Stations in between:", summary["stations_between"])
    print("Distance:", summary["distance_km"], "km")
    print("Duration:", summary["duration_min"], "minutes")
    print("Interchanges:", summary["interchanges"])
    print("Fare: ₹", summary["fare"])
    print("First Train:", summary["first_train"])
    print("Last Train:", summary["last_train"])

from logic.route_fare import find_route, calculate_summary, METRO_LINES
from database.db import create_tables, insert_summary

def main():
    create_tables()

    all_stations = set()
    for stations in METRO_LINES.values():
        all_stations.update(stations)

    all_stations = list(all_stations)

    for start in all_stations:
        for end in all_stations:
            if start == end:
                continue

            route, lines = find_route(start, end)
            if not route:
                continue

            summary = calculate_summary(route, lines)

            data = {
                "start": start,
                "end": end,
                "stations_between": summary["stations_between"],
                "distance": summary["distance_km"],
                "duration": summary["duration_min"],
                "interchanges": summary["interchanges"],
                "fare": summary["fare"],
                "first_train": summary["first_train"],
                "last_train": summary["last_train"]
            }

            insert_summary(data)

    print("ALL routes inserted into database")

if __name__ == "__main__":
    main()

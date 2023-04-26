# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open(
    "/workspaces/advanced-python-working-with-data-4312001/30DayQuakes.json", "r"
) as datafile:
    data = json.load(datafile)


# 1: How many quakes are there in total?
total_quakes = len(data["features"])
print(f"Total quakes: {total_quakes}")


# 2: How many quakes were felt by at least 100 people?
total_quakes_felt_by_100_people = sum(
    quake["properties"]["felt"] is not None and quake["properties"]["felt"] >= 100
    for quake in data["features"]
)
print(f"Total quakes felt by at least 100 poeple: {total_quakes_felt_by_100_people}")


# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
most_felt_reposrts = max(
    [
        quake["properties"]["felt"]
        for quake in data["features"]
        if quake["properties"]["felt"] is not None
    ]
)
print(f"Most felt reposrts: {most_felt_reposrts}")


# 4: Print the top 10 most significant events, with the significance value of each
def sorting_by_significance(events):
    significant = events["properties"]["sig"]
    if events["properties"]["sig"] is None:
        significant = 0
    return float(significant)


data["features"].sort(key=sorting_by_significance, reverse=True)


print(f"Top 10 most significant events were:\n")

for event in data["features"][:10]:
    print(
        f"Event: {event['properties']['mag']} - {event['properties']['place']}, Significance: {event['properties']['sig']}"
    )

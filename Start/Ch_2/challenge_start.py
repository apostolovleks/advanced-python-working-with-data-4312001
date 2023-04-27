# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import Counter


# open the data file and load the JSON
with open(
    "/workspaces/advanced-python-working-with-data-4312001/30DayQuakes.json", "r"
) as datafile:
    data = json.load(datafile)
all_vent_type = Counter(
    [
        quake["properties"]["type"]
        for quake in data["features"]
        if quake["properties"]["type"] is not None
    ]
)

for event_type, quantity in all_vent_type.items():
    print(f"{event_type:<15} : {quantity}")

# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime


# open the data file and load the JSON
with open(
    "/workspaces/advanced-python-working-with-data-4312001/30DayQuakes.json",
    "r",
) as datafile:
    data = json.load(datafile)


def sort_signifivant(dataitem):
    sig = dataitem["properties"]["sig"]
    if sig is None:
        sig = 0
    return float(sig)


data["features"].sort(key=sort_signifivant, reverse=True)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD

header = ["Magnitude", "Place", "Felt Reports", "Date", "Link"]
rows = []

for quake in data["features"][:40]:
    thedate = datetime.datetime.fromtimestamp(
        int(quake["properties"]["time"] / 1000)
    ).date()

    longitude, latitude, *other = quake["geometry"]["coordinates"]

    google_link = f"https://www.google.com/maps/search/?api=1&query={latitude}%2C{longitude}"
    rows.append(
        [
            quake["properties"]["mag"],
            quake["properties"]["place"],
            quake["properties"]["felt"],
            thedate,
            google_link,
        ]
    )

rows.sort(key=lambda x: x[3], reverse=True)

with open(
    "/workspaces/advanced-python-working-with-data-4312001/Start/Ch_3/significantevents.csv",
    "w",
) as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(rows)

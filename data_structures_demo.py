"""Read car_fleet.csv and print each vehicle's details."""

import csv

# Template showing the fields every vehicle record has.
vehicle_template = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0,
}

print("Vehicle fields:")
for key, value in vehicle_template.items():
    print(f"{key}: {value}")

inventory = []

try:
    with open("car_fleet.csv", newline="") as csv_file:
        reader = csv.DictReader(csv_file)  # uses the header row as column names
        print(f"Column names are: {', '.join(reader.fieldnames)}")

        for row in reader:
            inventory.append(row)
            print(
                f"vin: {row['vin']}, make: {row['make']}, model: {row['model']}, "
                f"year: {row['year']}, range: {row['range']}, "
                f"topSpeed: {row['topSpeed']}, zeroSixty: {row['zeroSixty']}, "
                f"mileage: {row['mileage']}"
            )
except FileNotFoundError:
    print("car_fleet.csv was not found. Run this script from the folder that contains it.")

print(f"Loaded {len(inventory)} vehicles.")

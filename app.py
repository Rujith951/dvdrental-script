import csv

with open("csv/actor.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(", ".join(row))

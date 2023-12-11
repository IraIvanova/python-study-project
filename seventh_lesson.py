iso_country = "UA"
iso_index = 5
airport_name_index = 2

with open("data/airport-codes_csv.csv", mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        airport_data = line.split(";")
        if airport_data[iso_index] == iso_country:
            print(airport_data[airport_name_index])

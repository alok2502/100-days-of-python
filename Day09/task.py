capitals = {
    "France" : "Paris", 
    "Germany" : "Berlin",
}

travel_log = {
    "France" : ["Paris", "Dijon", "Lille"],
    "Germany" : ["Berlin", "Stuttgart"]
}

for Key in travel_log:
    print(travel_log[Key][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

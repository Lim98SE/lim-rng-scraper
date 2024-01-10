import json

with open("websites.json") as jsonfile:
    websites = json.load(jsonfile)

print(len(websites.keys()))


while True:
    query = input("? ").lower()
    type_query = "data"

    found = 0
        
    for i in websites:
        if query in websites[i][type_query].lower():
            print(i)
            found += 1

    print("Found", found, "results")

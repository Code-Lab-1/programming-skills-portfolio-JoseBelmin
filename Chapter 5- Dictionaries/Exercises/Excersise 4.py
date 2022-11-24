#Make a dictionary containing three major rivers and the country each river runs through.

rivers = {
    "The Rio Grande de Mindanao": "Philippines",
    "The Yangtze River": "China",
    "The Euphrates River": "Iraq"
    }

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nThe data set includes the following rivers. :")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe data set includes the following rivers. :")
for country in rivers.values():
    print("- " + country.title())

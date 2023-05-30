#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about each pet.

pets = []
pet = {
    "animal type": "parrot",
    "name": "Blu",
    "owner": "Jose",
    "weight": "3kg",
}
pets.append(pet)
pet = {
    "animal type": "dog",
    "name": "Spots",
    "owner": "Jack",
    "weight": "14kg",
}
pets.append(pet)
pet = {
    "animal type": "cat",
    "name": "Whiskers",
    "owner": "Anny",
    "weight": "7kg",
}
pets.append(pet)

for pet in pets:
    print("\nSo far, here's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))

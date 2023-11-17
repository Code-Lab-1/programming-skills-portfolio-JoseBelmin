#Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.


orders = ["Meat ball", "Smoked ham", "Chicken Teriyaki", "Tuna"]
finished_sandwiches = []

while orders:
    current = orders.pop()
    print("Please wait a minute, your " + current + " is on the way.")
    finished_sandwiches.append(current)

print("\n")
for sandwich in finished_sandwiches:
    print("I finished the " + sandwich + " sandwich.")

#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times.


sandwich_orders = [
    "Meat ball", "Pastrami", "Smoked ham", 
    "Pastrami", "Chicken Teriyaki", "Pastrami", 
    "Tuna"]
finished_sandwiches = []

print("We're all out of pastrami today, I apologize.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("Please wait a minute, your  " + current_sandwich + " is on the way.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I finished the " + sandwich + " sandwich.")

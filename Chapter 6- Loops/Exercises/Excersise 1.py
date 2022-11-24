#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.


ask = "\nWhat type of topping do you want on your pizza? "
ask += "\nWhen you are done, type 'quit': "

while True:
    toppings = input(ask)
    if toppings != 'quit':
        print("  Noted, I'll place " + toppings + " to your pizza pie.")
    else:
        break

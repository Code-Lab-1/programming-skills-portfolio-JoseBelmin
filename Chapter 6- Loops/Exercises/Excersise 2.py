#A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free


ask = "May I know your age?"
ask += "\nWhen you are done, type 'quit':  "

while True:
    age = input(ask)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  Congratulations, you're free of charge!")
    elif age < 13:
        print("  That'll be 15dhs.")
    else:
        print("  That'll be 20dhs.")

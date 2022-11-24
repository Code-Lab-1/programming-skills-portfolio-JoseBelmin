#Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age.

print("Please type in your age.")
age = int(input())

if age >= 2 and age <= 3:
    print("You're a baby!")
elif age >= 4 and age <= 12:
    print("You're a kid!")
elif age >= 13 and age <= 19:
    print("You're a teenager!")
elif age >= 20 and age <= 64:
    print("You're an adult!")
else:
    print("You're an elder!")
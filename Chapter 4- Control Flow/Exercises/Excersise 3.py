#Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

print("Please give your alien a color.")
alien_color = str(input())

if alien_color == "Green":
    print("Congratulations! You just earned 5 points!")
elif alien_color == "Yellow":
    print("Congratulations! You just earned 10 points!")
elif alien_color == "Red":
    print("Congratulations! You just earned 15 points!")
else:
    print("")
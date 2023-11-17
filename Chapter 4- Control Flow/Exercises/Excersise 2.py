#If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
#If the alien’s color isn’t green, print a statement that the player just earned 10 points.
#Write one version of this program that runs the if block and another that runs the else block.

print("Please give your alien a color.")
alien_color = str(input())

if alien_color == "Green":
    print("Congratulations! You just earned 5 points!")
else:
    print("Congratulations! You just earned 10 points!")

#Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
#Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

print("Please give your alien a color.")
alien_color = str(input())

if alien_color == "Green":
    print("Congratulations! You just earned 5 points!")
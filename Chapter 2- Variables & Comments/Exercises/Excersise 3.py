#Tidy up the code to make it easier to understand.

print("----------normal----------")
name = "777\n   \tJose Belmin\t888\n"
print(name)

#lstrip
print("----------lstrip----------")
name = name.lstrip("   ,777,\n,\t")
print(name)

#rstrip
print("----------rstrip----------")
name = name.rstrip("\t,888,\n")
print(name)

#strip
print("----------strip----------")
name = name.strip("   ,777,888,\n,\t")
print(name)
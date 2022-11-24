#Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
#Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#Print a second set of invitation messages, one for each person who is still in your list.

invite = ["paternal grandfather", "maternal father", "my crush"]

print("Hello! I've never met you once in my life since you died before I was born, so it'd be nice to talk with you", invite[0])
print("Hello! I've never met you once in my life since you died before I was born, so it'd be nice to talk with you", invite[1])
print("Hey, want to go out for food? I'd like to get to know you", invite[2])

print("I guess", invite[1], "is not going to make it...")

invite.append("maternal grandmother")
print("Instead, My", invite[3], "will replace him.")
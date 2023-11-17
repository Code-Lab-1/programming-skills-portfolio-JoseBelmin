#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.


def make_shirt(size = "large", message="Python is easily digestable."):
    """Briefly describe the t-shirt that will be produced. """
    print("\nI'm going to sew a " + size + " t-shirt.")
    print('It will print, "' + message + '"')

make_shirt()
make_shirt(size = "small")
make_shirt("medium", "Sleep? never heard of such a thing!")

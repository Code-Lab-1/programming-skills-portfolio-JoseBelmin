#clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

glossary = {
    "string": "A collection of characters.",

    "integer": "A collection of numbers.",

    "list": "A collection of variables in a planned order.",

    "loop": "Go through a group of things one at a time. ",

    "dictionary": "A collection of key-value pairs.",
    
    "key": "The first entry in a dictionary's key-value pair. ",

    "value": "A thing connected to a dictionary key. ",

    "variable": "An interchangeable data holder.",

    "float": "A decimal part of a numerical value. ",
    
    "boolean expression": "A statement that can either be True or False. ",
    }

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)

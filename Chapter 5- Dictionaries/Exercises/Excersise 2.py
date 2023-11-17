#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

glossary = {
    "string": "A collection of characters.",
    "integer": "A collection of numbers.",
    "variable": "An interchangeable data holder.",
    "list": "A collection of variables in a planned order.",
    "dictionary": "A collection of key-value pairs.",
    }

word = 'string'
print("\n" + word.title() + ": " + glossary[word])

word = 'integer'
print("\n" + word.title() + ": " + glossary[word])

word = 'variable'
print("\n" + word.title() + ": " + glossary[word])

word = 'list'
print("\n" + word.title() + ": " + glossary[word])

word = 'dictionary'
print("\n" + word.title() + ": " + glossary[word])

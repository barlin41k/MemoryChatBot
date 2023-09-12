from barladb import db
from random import randint, choice
import functions
import os

barladb = db.BarlaDB()

data = barladb.get("words")
words = data["words"]

question = input("You: ")

if question not in words:
    if randint(1, 4) >= 2:
        words.append(question)
        barladb.save("words", data)
        if len(words) < 5:
            functions.GetTheMessage(0, words, len(words), question)
        else:
            functions.GetTheMessage(1, words, len(words), question)
    else:
        if len(words) < 5:
            functions.GetTheMessage(2, words, len(words))
        else:
            functions.GetTheMessage(3, words, len(words))
else:
    if len(words) < 5:
        functions.GetTheMessage(3, words, len(words))
    else:
        functions.GetTheMessage(2, words, len(words))
try:
    os.remove("__pycache__")
except PermissionError:
    print("Error with removing __pycache__ directory")
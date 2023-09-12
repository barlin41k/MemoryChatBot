from random import randint, choice

def GetTheMessage(mode: int, words: list, len_words: int, question=""):
    if len(words) >= 10:
        len_words = len(words) / 4
    if mode == 0:
        message = ""
        for i in range(randint(1, int(len_words))):
            message += choice(words) + ", "
        message = message.rstrip(", ")
        new_message = question + ", " + message
        print(new_message)
    elif mode == 1:
        message = ""
        for i in range(randint(1, 5)):
            message += choice(words) + ", "
        message = message.rstrip(", ")
        new_message = question + ", " + message
        print(new_message)
    elif mode == 2:
        message = ""
        for i in range(randint(1, int(len_words))):
            message += choice(words) + ", "
        message = message.rstrip(", ")
        print(message)
    elif mode == 3:
        message = ""
        for i in range(randint(1, 5)):
            message += choice(words) + ", "
        message = message.rstrip(", ")
        print(message)
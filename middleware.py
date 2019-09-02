
def correct_message(message):
    if len(message) == 14 and message.isdigit():
        return True
    elif len(message) == 13 and message[:2].isalpha() and message[-2:].isalpha():
        return True
    else:
        return False

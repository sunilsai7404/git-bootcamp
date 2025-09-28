def word_count(text):
    return len(text.split())

def to_upper(text):
    return text.upper()

def add_exclaim(text, strong=False):
    if strong:
        return f"{text}!!!"
    return text + "!"


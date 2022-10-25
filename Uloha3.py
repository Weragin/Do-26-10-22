def vowels_only(text) -> bool:
    for symbol in text:
        if symbol not in "aeiouy":
            return False
    return True

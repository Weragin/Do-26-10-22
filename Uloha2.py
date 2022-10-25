def count_digits(text: str) -> int:
    res = 0
    for symbol in text:
        if symbol in "0123456789":
            res += 1
    return res

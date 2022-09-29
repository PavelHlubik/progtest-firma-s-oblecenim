def expand_wildcards(s: str) -> str:
    """aa5bb12cc3 -> aa?????bb????????????cc???"""
    buffer = ""
    number_buffer = ""
    reading_number = False
    for c in s:
        if c.isnumeric():
            reading_number = True
            number_buffer += c
        elif not c.isnumeric() and reading_number:
            reading_number = False
            buffer += "?" * int(number_buffer) + c
            number_buffer = ""
        else:
            buffer += c
    if reading_number:
        buffer += "?" * int(number_buffer)

    return buffer


def char_compare(char_tuple):
    a, b = char_tuple
    if a == "?" or b == "?":
        return True

    return a == b


def solution(s1: str, s2: str) -> bool:
    s1 = expand_wildcards(s1)
    s2 = expand_wildcards(s2)

    if len(s1) != len(s2):
        return False

    return all(map(char_compare, zip(s1, s2)))


print(solution("aa5bb12cc3", "aa6b12cc3"))
print(solution("A2Le", "2pL1"))
print(solution("a10", "10a"))
print(solution("ba1", "1Ad"))
print(solution("3x2x", "8"))

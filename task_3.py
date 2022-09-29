def solution(s: str) -> int:
    for i in range(len(s) - 1, 0, -1):
        # print(s[:i], s[-i:])
        if s[:i] == s[-i:]:
            return i


print(solution("abbabba"))

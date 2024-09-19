def permute(s):
    def backtrack(start):
        if start == len(s):
            result.append(''.join(s))
        seen = set()
        for i in range(start, len(s)):
            if s[i] in seen:
                continue
            seen.add(s[i])
            s[start], s[i] = s[i], s[start]
            backtrack(start + 1)
            s[start], s[i] = s[i], s[start]

    result = []
    s = list(s)
    backtrack(0)
    return result

print(permute("abc"))

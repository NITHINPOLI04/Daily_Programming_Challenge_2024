def groupAnagrams(strs):
    anagram_groups = {}
    for word in strs:
        char_count = [0] * 26
        for char in word:
            char_count[ord(char) - ord('a')] += 1
        key = tuple(char_count)
        if key in anagram_groups:
            anagram_groups[key].append(word)
        else:
            anagram_groups[key] = [word]

    return list(anagram_groups.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
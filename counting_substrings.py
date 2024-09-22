def count_substrings_with_at_most_k_distinct(s, k):
    n = len(s)
    freq = {}
    left = 0
    result = 0
    
    for right in range(n):

        if s[right] not in freq:
            freq[s[right]] = 0
        freq[s[right]] += 1

        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        result += (right - left + 1)
    
    return result

def count_substrings_with_exactly_k_distinct(s, k):

    return count_substrings_with_at_most_k_distinct(s, k) - count_substrings_with_at_most_k_distinct(s, k - 1)

print(count_substrings_with_exactly_k_distinct("pqpqs", 2))
print(count_substrings_with_exactly_k_distinct("aabacbebebe", 3)) 
print(count_substrings_with_exactly_k_distinct("a", 1))
print(count_substrings_with_exactly_k_distinct("abc", 3))
print(count_substrings_with_exactly_k_distinct("abc", 2))  

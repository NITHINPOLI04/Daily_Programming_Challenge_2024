def first_element_to_repeat_k_times(arr, k):
    occurrences = {}
    
    for num in arr:
        occurrences[num] = occurrences.get(num, 0) + 1
    
    for num in arr:
        if occurrences[num] == k:
            return num

    return -1

print(first_element_to_repeat_k_times([2, 3, 4, 2, 2, 5, 5], 2))
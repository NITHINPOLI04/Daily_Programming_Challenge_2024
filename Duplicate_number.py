def find_duplicate(a, n):
    new_a = set()
    for num in a:
        if num in new_a:
            return num
        new_a.add(num)
    return -1

a = [1, 4, 4, 2, 3]  
n = len(a) - 1  
print(find_duplicate(a, n))  
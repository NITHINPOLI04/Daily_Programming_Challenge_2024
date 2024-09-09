def sort_012(a,n):
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            low = low + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        elif a[mid] == 2:
            a[mid], a[high] = a[high], a[mid]
            high = high - 1

a = [0, 1, 2, 1, 0, 2, 1, 0]
n = len(a)
sort_012(a,n)
print(a)
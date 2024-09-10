def missing_num(arr,n):
    sum1 = (n * (n + 1)) // 2
    sum2 = sum(arr)

    missing_number = sum1 - sum2
    return missing_number

arr = [1, 2, 4, 5]
n = len(arr) + 1
print(missing_num(arr,n))


def k_largest_element(arr,k):
    n = len(arr)
    for i in range(n):
        max = i
        for j in range(i+1,n):
            if(arr[j] > arr[max]):
                max = j
        arr[i],arr[max] = arr[max],arr[i]

    return arr[k-1]    

arr = [3, 2, 1, 5, 6, 4]
k = 2
result = k_largest_element(arr,k)
print(result)
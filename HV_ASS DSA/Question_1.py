# Recursive Function 


def dup_ele(arr, i, n, count):
    if i == n:
        return
    if arr[i] == arr[i + 1]:
        count[0] += 1
        dup_ele(arr, i + 1, n, count)
    else:
        if count[0] != 0:
            print(arr[i], "appears", count[0] + 1, "times")
        count[0] = 0
        dup_ele(arr, i + 1, n, count)

def find_duplicate(arr):
    arr.sort()
    n = len(arr) - 1
    count = [0]
    dup_ele(arr, 0, n, count)

arr = [1, 2, 3, 1, 2, 5, 6, 5]
print("Duplicate elements in the array: ")
find_duplicate(arr)





# Iterative Method 



def find_duplicate(arr):
    arr.sort()
    n = len(arr)
    for i in range(n):
        count = 1
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                count += 1
                j += 1
            else:
                break
        if count > 1:
            print(arr[i], "appears", count, "times")

arr = [1, 2, 3, 1, 2, 5, 6, 5]
print("Duplicate elements in the array: ")
find_duplicate(arr)



# User-defined function


def check_ele(arr):
    dict = {}
    for i in arr:
        dict[i] = dict.get(i, 0) + 1
    for key, value in dict.items():
        if value > 1:
            print(key, "appears", value, "times")

arr = [1, 2, 3, 1, 2, 5, 6, 5]
print("Duplicate elements in the array: ")
check_ele(arr)
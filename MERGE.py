def merge(arr1, arr2, m, n):
    i = m - 1
    j = 0

    while i >= 0 and j < n:
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
        i -= 1
        j += 1

    arr1.sort()
    arr2.sort()

m = int(input("Enter the size of arr1: "))
arr1 = list(map(int, input(f"Enter {m} sorted elements for arr1: ").split()))

n = int(input("Enter the size of arr2: "))
arr2 = list(map(int, input(f"Enter {n} sorted elements for arr2: ").split()))

merge(arr1, arr2, m, n)

print("Merged arr1:", arr1)
print("Merged arr2:", arr2)
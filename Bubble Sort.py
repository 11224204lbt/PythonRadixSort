def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  
        swapped = False   # 標記這一輪有沒有交換
        for j in range(n - 1 - i):  # 每一輪把最大值冒到最後
            if arr[j] > arr[j + 1]:  # 如果前面比後面大，就交換
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # 如果這一輪完全沒交換，代表已經排好
            break
    return arr

# 測試
nums = [5, 1, 4, 2, 8, 3]
print("排序前:", nums)
print("排序後:", bubble_sort(nums))

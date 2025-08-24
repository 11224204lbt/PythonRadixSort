def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # 只需排到倒數第二個
        min_index = i
        # 找出剩餘元素中最小值的位置
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # 將最小值和目前起始位置交換
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# 測試
nums = [64, 25, 12, 22, 11]
print("排序前:", nums)
print("排序後:", selection_sort(nums))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # 選第一個元素作為基準
        left = [x for x in arr[1:] if x <= pivot]  # 小於等於基準
        right = [x for x in arr[1:] if x > pivot]  # 大於基準
        return quick_sort(left) + [pivot] + quick_sort(right)

# 測試
nums = [10, 7, 8, 9, 1, 5]
print("排序前:", nums)
print("排序後:", quick_sort(nums))

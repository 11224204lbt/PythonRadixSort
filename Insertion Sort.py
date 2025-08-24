def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]   # 要插入的元素
        j = i - 1
        # 往前比較，若比 key 大就往後移
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # 插入 key 到正確位置
        arr[j + 1] = key
    return arr

# 測試
nums = [12, 11, 13, 5, 6]
print("排序前:", nums)
print("排序後:", insertion_sort(nums))

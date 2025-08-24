def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 分割
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 合併
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # 比較左右子序列，將小的依序放入結果
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 剩下的元素直接加入
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# 測試
nums = [38, 27, 43, 3, 9, 82, 10]
print("排序前:", nums)
print("排序後:", merge_sort(nums))

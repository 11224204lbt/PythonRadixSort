def counting_sort(arr):
    if not arr:
        return arr

    # 找最大和最小值
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # 計數陣列 (初始化為 0)
    count = [0] * range_of_elements

    # 輸出陣列
    output = [0] * len(arr)

    # 計數每個元素出現次數
    for num in arr:
        count[num - min_val] += 1

    # 累加計數，讓 count[i] 表示 <= i 的數字數量
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # 反向填充輸出陣列 (確保穩定性)
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output

# 測試
nums = [4, 2, 2, 8, 3, 3, 1]
print("排序前:", nums)
print("排序後:", counting_sort(nums))

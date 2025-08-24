def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # 找最大值和最小值
    max_val = max(arr)
    min_val = min(arr)
    
    # 建立桶
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]
    
    # 分配元素到桶
    for num in arr:
        # 計算桶索引，確保是整數
        index = int((num - min_val) / (max_val - min_val + 1e-9) * (bucket_count - 1))
        buckets[index].append(num)
    
    # 桶內排序
    for i in range(bucket_count):
        buckets[i].sort()
    
    # 合併結果
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr

# 測試
nums = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47]
print("排序前:", nums)
print("排序後:", bucket_sort(nums))

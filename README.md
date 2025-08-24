# 期末題目五: 【Python 算法零基礎 4.排序 ⑧ 基數排序】
## 11224204 林柏廷

### 基数排序簡述
基數排序是一種非比較型整數排序演算法，其原理是將整數按位元數切割成不同的數字，然後按每個位數分別比較。由於整數也可以表達字串（比如名字或日期）和特定格式的浮點數，所以基數排序也不是只能使用於整數。

它是這樣實現的：將所有待比較數值（正整數）統一為同樣的數位長度，數位較短的數前面補零。然後，從最低位開始，依次進行一次排序。這樣從最低位排序一直到最高位排序完成以後，數列就變成一個有序序列。

基數排序的方式可以採用LSD（Least significant digital）或MSD（Most significant digital），LSD的排序方式由鍵值的最右邊開始，而MSD則相反，由鍵值的最左邊開始。

## 圖例說明
![01](https://github.com/11224204lbt/PythonRadixSort/blob/main/pic1.jpg)

### 選擇排序（Selection Sort）原理

從未排序的序列中，找到最小值（或最大值）
把這個最小值和「目前起始位置」的元素交換
然後縮小範圍，對剩下的序列重複步驟 1、2
持續進行，直到整個序列排序完成

<pre>
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
</pre>
![01](https://github.com/11224204lbt/PythonRadixSort/blob/main/Selection%20Sort.png)
## 冒泡排序（Bubble Sort）原理

比較 相鄰的兩個元素，如果順序錯誤就交換
每一輪比較之後，最大（或最小）的元素會被“冒泡”到最後面
下一輪就少比較一次（因為最後的元素已經就定位）
重複進行，直到整個序列完成排序
每輪從頭開始相鄰比較，大元素逐步“冒泡”至末端

<pre>
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

</pre>
![01](https://github.com/11224204lbt/PythonRadixSort/blob/main/Bubble%20Sort.png)
## 插入排序（Insertion Sort）原理

插入排序的想法就像「整理撲克牌」：
從第二個元素開始，拿起來，往前跟已排序好的部分比較
如果比前面的元素小，就把前面的元素往後移
直到找到正確位置，把該元素插入
重複這個過程，直到所有元素都放到正確位置

<pre>
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
  
</pre>
![01](https://github.com/11224204lbt/PythonRadixSort/blob/main/Insertion%20Sort.png)
## 計數排序（Counting Sort）原理

計數排序是一種 非比較型排序演算法，特別適合 整數、範圍有限 的資料。
核心想法：
找出陣列中的最大值與最小值，確定數字範圍
建立一個「計數陣列 (count array)」，用來記錄每個數字出現的次數
累加計數陣列，讓它能表示「小於或等於某數字的元素個數」
建立結果陣列，根據計數陣列把元素放到正確位置

<pre>
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

</pre>
![01](https://github.com/11224204lbt/PythonRadixSort/blob/main/Counting%20Sort.png)
## 歸併排序（Merge Sort）原理

歸併排序是一種 分治法 (Divide and Conquer) 排序演算法
主要步驟：
分割 (Divide)：不斷將序列一分為二，直到每個子序列只剩一個元素（自然有序）
合併 (Merge)：兩個已排序的子序列合併成一個有序序列
持續合併，直到所有子序列合成一個完整排序好的序列

<pre>
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

</pre>
![01](https://github.com/11224204lbt/PythonRadixSort/blob/main/Merge%20Sort.png)
## 快速排序（Quick Sort）原理

快速排序是一種 分治法 (Divide and Conquer) 排序演算法
主要概念：
選擇基準 (Pivot)：從序列中選一個元素作為基準
分割 (Partition)：將序列分成兩部分：
左邊元素 ≤ 基準
右邊元素 > 基準
遞迴排序：對左、右子序列重複以上步驟，直到子序列長度 ≤ 1
最終得到排序好的序列

<pre>
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

</pre>
![01](https://github.com/11224204lbt/PythonRadixSort/blob/main/Quick%20Sort.png)
## 桶排序（Bucket Sort）原理

桶排序是一種 分配到不同桶、再個別排序 的排序演算法，特別適合 均勻分布的數值
步驟如下：
建立桶：根據數值範圍，建立多個空桶
分配元素：把每個元素放入對應桶中（通常依照大小比例決定桶位置）
桶內排序：對每個桶使用其他排序演算法（例如插入排序或內建排序）排序
合併結果：將所有桶依順序合併，得到最終排序序列

<pre>
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

</pre>
![01](https://github.com/11224204lbt/PythonRadixSort/blob/main/Bucket%20Sort.png)
# 基數排序（Radix Sort）分析
1️⃣ 算法原理

基數排序是一種 非比較型排序算法，主要用於 整數或固定長度字串 的排序。
核心思想：
將所有元素按照 位數（digit）分組排序
從 最低有效位（LSD） 或 最高有效位（MSD） 開始排序
每次排序必須使用 穩定排序（如計數排序）
遍歷完所有位數後，得到完整排序的序列

範例：
排序 [170, 45, 75, 90, 802, 24, 2, 66]：
按「個位數」排序 → [170, 90, 2, 802, 24, 45, 75, 66]
按「十位數」排序 → [2, 802, 24, 45, 66, 170, 75, 90]
按「百位數」排序 → [2, 24, 45, 66, 75, 90, 170, 802]

2️⃣
| 特性        | 說明                                                |
| --------- | ------------------------------------------------- |
| **時間複雜度** | O(d × (n + k)) <br>n = 元素數量，d = 位數長度，k = 每位可能的值範圍 |
| **空間複雜度** | O(n + k)                                          |
| **是否穩定**  | ✅ 穩定排序（取決於子排序算法）                                  |
| **適用場景**  | 整數排序、固定長度字串排序，尤其適合「範圍大但位數小」的數據                    |

3️⃣ 算法分析重點

非比較型排序：不像快排或歸併排序，需要比較元素大小。

穩定性重要：每一位的排序必須保持穩定，否則結果會錯誤。

時間效率：當元素很多但位數少時，比 O(n log n) 的比較型排序更快。

空間消耗：需要額外空間存桶或計數陣列。

# 基數排序（Radix Sort）優缺點
✅ 優點

1.高效率:當元素很多且位數少時，時間複雜度為 O(d × (n + k))，比比較型排序（O(n log n)）更快。

2.穩定排序:如果使用穩定的子排序算法（如計數排序），可以保持相同元素的相對順序。

3.適合特定資料類型:特別適合整數、長度固定的字串或資料範圍大但位數少的情況。

4.非比較型排序:不需要元素之間直接比較大小，可以處理大範圍數據。

❌ 缺點

1.額外空間消耗:需要額外空間來存放桶或計數陣列，空間複雜度 O(n + k)。

2.限制資料類型:主要適用於整數或固定長度字串，對浮點數或自定義對象不方便。

3.位數過多影響效率:如果位數 d 很大，排序效率可能下降，不適合位數長的資料。

4.依賴穩定排序子算法:若子排序不穩定，最終結果可能錯誤。

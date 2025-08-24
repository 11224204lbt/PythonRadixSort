# 期末題目五: 【Python 算法零基础 4.排序 ⑧ 基数排序】
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
## 快速排序（Quick Sort）

選擇基準值進行分區，使得左側小於基準，右側大於基準，再對兩側遞迴排序。
<pre>
arr = [9, 3, 7, 6, 2]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([9, 3, 7, 6, 2])) 

</pre>
![01](https://github.com/XUPOWEN/Radix-Sort/blob/main/RS6.png)
## 桶排序（Bucket Sort）

將元素分配到不同桶中，分別排序後合併。
<pre>
arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]

def bucket_sort(arr):
    n = len(arr)
    if n == 0:
        return arr


    buckets = [[] for _ in range(n)]


    for num in arr:
        index = int(num * n)
        buckets[index].append(num)


    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr

print(bucket_sort([0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]))
</pre>
![01](https://github.com/XUPOWEN/Radix-Sort/blob/main/RS7.png)
# 基數排序（Radix Sort）算法分析
## 1. 時間複雜度

時間複雜度為 O(d × (n + r))

d：最大位數（digits）

n：元素個數

r：基數（radix，如十進制為 10）

基數排序的效率取決於元素的位數和數量。
當位數較少時，基數排序效率非常高，且無需元素間比較；但若位數過多，需重複多輪「分配」與「收集」操作，效率會降低。

## 2. 空間複雜度

需要額外空間存放「桶」，空間複雜度取決於：

桶的數量（通常為基數 r）

每個桶中元素的存儲方式

小提醒：在某種程度上，基數排序可視為特殊的桶排序（Bucket Sort）。

## 3. 優點

效率高：不進行元素間比較，對於特定情境（如排序範圍有限）非常高效。

適合定長數據：特別適合排序固定長度的數字序列，例如：電話號碼、身份證號等。

## 4. 缺點

需額外空間：使用桶結構需要較大的內存空間，對大型數據集不夠友好。

適用範圍有限：對於非整數或複雜類型資料，需要進行額外轉換或處理才能應用。

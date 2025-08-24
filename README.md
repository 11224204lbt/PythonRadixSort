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
持續進行，直到整個序列排序完成。

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
![01](https://github.com/XUPOWEN/Radix-Sort/blob/main/RS2.png)
## 冒泡排序（Bubble Sort）

每輪從頭開始相鄰比較，大元素逐步“冒泡”至末端。
<pre>
arr = [5, 3, 8, 4, 2]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([5, 3, 8, 4, 2])) 
</pre>
![01](https://github.com/XUPOWEN/Radix-Sort/blob/main/RS2.png)
## 插入排序（Insertion Sort）

將未排序元素插入已排序序列中正確的位置。
<pre>
arr = [7, 4, 5, 2]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current
    return arr

print(insertion_sort([7, 4, 5, 2]))  
</pre>
![01](https://github.com/XUPOWEN/Radix-Sort/blob/main/RS3.png)
## 計數排序（Counting Sort）

適用於範圍固定的整數。透過統計每個數字出現的次數，重建有序數列。
<pre>
arr = [4, 2, 2, 8, 3, 3, 1]

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr

print(counting_sort([4, 2, 2, 8, 3, 3, 1])) 
</pre>
![01](https://github.com/XUPOWEN/Radix-Sort/blob/main/RS4.png)
## 歸併排序（Merge Sort）

遞迴分割序列，再將兩個有序序列合併為一個。
<pre>
arr = [6, 3, 8, 5]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(merge_sort([6, 3, 8, 5])) 
</pre>
![01](https://github.com/XUPOWEN/Radix-Sort/blob/main/RS5.png)
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

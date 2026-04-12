import time
import random
import sys

# 增加遞迴深度限制以防快速排序報錯
sys.setrecursionlimit(20000)

# 1. 氣泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# 2. 選擇排序
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 3. 插入排序
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 4. 合併排序
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# 5. 快速排序
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# ---- 實驗設計與時間測試 ----
def run_experiments():
    sizes = [1000, 5000, 10000] # 可以自己修改資料量
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    print(f"{'資料規模':<10} | {'演算法':<15} | {'花費時間 (秒)'}")
    print("-" * 45)

    for size in sizes:
        # 生成隨機陣列
        test_data = [random.randint(1, 100000) for _ in range(size)]
        
        for name, func in algorithms.items():
            data_copy = test_data.copy() # 確保每次排序都是用一樣的亂數
            
            start_time = time.time()
            if name == "Quick Sort": # Quick sort 返回新陣列，用法稍有不同
                data_copy = func(data_copy)
            else:
                func(data_copy)
            end_time = time.time()
            
            elapsed_time = end_time - start_time
            print(f"{size:<10} | {name:<15} | {elapsed_time:.4f}")
        print("-" * 45)

if __name__ == "__main__":
    run_experiments()

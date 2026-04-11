import time
import random
import matplotlib.pyplot as plt

def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def test(func, n):
    arr = [random.randint(0,10000) for _ in range(n)]
    start = time.time()
    func(arr)
    return time.time() - start

sizes = [100, 1000, 3000]
bubble_t = []
insertion_t = []

for n in sizes:
    bubble_t.append(test(bubble, n))
    insertion_t.append(test(insertion, n))

plt.plot(sizes, bubble_t, label="Bubble")
plt.plot(sizes, insertion_t, label="Insertion")

plt.xlabel("n")
plt.ylabel("time")
plt.legend()
plt.savefig("../images/chart.png")

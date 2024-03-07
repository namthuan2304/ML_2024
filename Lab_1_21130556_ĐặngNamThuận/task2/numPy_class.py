import numpy as np


# Task 2. NumPy API
def numPy_func():
    # task2.1
    x = np.arange(10, 26)
    reversed_arr = x[::-1]
    print('Mảng nghịch đảo của mảng có giá trị chạy từ 10 đến 25: ', reversed_arr)
    print('-------------------------------------')
    # task2.2
    n = int(input("Nhập n: "))
    L = []
    repeated_arr = []
    for i in range(n):
        L.append(int(input(f"Nhập N{i + 1}: ")))
    print('Original array: ', L)
    re = int(input("Số lần lặp: "))
    for _ in range(re):
        repeated_arr.extend(L)
    print(f'Repeating {re} times: ', repeated_arr)
    print('-------------------------------------')
    # task2.3
    rows = int(input("Nhập số hàng: "))
    cols = int(input("Nhập số cột: "))
    arr = np.empty((rows, cols), dtype=float)
    for i in range(rows):
        for j in range(cols):
            arr[i, j] = float(input(f"Nhập phần tử tại hàng {i + 1}, cột {j + 1}: "))
    print("Original array:")
    print(arr)
    arr[arr > 0.5] = 0.5
    print("Replace all elements of the original array with .5 for values which are greater than .5")
    print(arr)
    print('-------------------------------------')


def main():
    print(numPy_func())


if __name__ == "__main__":
    main()


#task 1.1 thuộc task 1: Python Programming

def func():
    n = int(input("Nhập n: "))
    L = []
    count_positive = 0
    count_negative = 0
    for i in range(n):
        L.append(int(input(f"Nhập số thứ {i + 1}: ")))
        if L[i] > 0:
            count_positive += 1
        elif L[i] < 0:
            count_negative += 1
    print('Số lớn nhất trong L là: ', max(L))
    print('Số nhỏ nhất trong L là: ', min(L))
    print('Tổng các phần tử của L: ', sum(L))
    L.sort()
    print('L được sắp xếp tăng dần', L)
    print('Sô phần tử dương', count_positive)
    print('Sô phần tử âm', count_negative)


def main():
    print(func())


if __name__ == "__main__":
    main()

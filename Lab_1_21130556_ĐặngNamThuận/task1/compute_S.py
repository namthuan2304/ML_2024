
#task 1.2 thuộc task 1: Python Programming

def total(n):
    if n <= 0:
        return 'Tham số không phù hợp'
    x = 1
    value = 0
    for i in range(n):
        x *= i + 1
        value += x
    return value


def main():
    n = int(input("Nhập n: "))
    if n <= 0:
        print(total(n))
    else:
        print(f'Tổng của 1 + 1.2 + 1.2.3 + ... + 1.2.3...{n} bằng: ', total(n))


if __name__ == "__main__":
    main()

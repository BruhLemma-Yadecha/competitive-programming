binary_decimals = []


def generate(n, ls):
    if n == 0:
        binary_decimals.append(int("".join(map(str, ls))))
        return
    generate(n - 1, ls + [0])
    generate(n - 1, ls + [1])


generate(4, [])
binary_decimals.remove(1)
binary_decimals.remove(0)

t = int(input())
for _ in range(t):
    n = int(input())

    # find a combination of numbers in binary_decimals whose product is n
    def find_combination(n):
        if n == 1:
            return True
        res = False
        for option in binary_decimals:
            if n % option == 0:
                res |= find_combination(n / option)
        return res

    if find_combination(n):
        print("YES")
    else:
        print("NO")



# 1부터 n까지의 합 구하기
def print_sum_n(n):
    s = 0
    for i in range(1, n+1):
        log = "1"
        s += i
        for j in range(2, i+1):
            log = f"{log} + {j}"

        print(f"{log} = {s}")
    print(f"1부터 {n}까지의 합은 {s} 입니다.")


# print_sum_n(10)

def print_f_sum(n):
    print(n * (n + 1) // 2)


print_f_sum(10)


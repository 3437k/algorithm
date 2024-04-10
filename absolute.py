import math


# 절대값 구하기
def print_absolute_value(n):
    # 입력받은 n 제곱처리 , 다른방법 n * n
    sqaure = n ** 2
    print(f"{n}의 제곱은 {sqaure}")

    # 제곱근(square root) 구하기
    abs = math.sqrt(sqaure)
    print(f"결과:{abs}")


print_absolute_value(10)

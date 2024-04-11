fruits = ["딸기", "바나나", "카카오", "체리", "딸기", "카카오", "망고", "딸기"]


# 중복된 이름 찾기
# set
# dictionary
def find_name_dictionary(arr):
    d = {}
    for i in range(0, len(arr)):
        t = arr[i]
        if t in d:
            d[t] = d[t]+1
        else:
            d.setdefault(t, 0)
    # {'딸기': 1, '바나나': 0, '카카오': 1, '체리': 0, '망고': 0}
    print(d)

    # 중복값 찾기
    result1 = {k: v for k, v in d.items() if v >= 1}
    # {'딸기': 1, '카카오': 1}
    print(result1)


find_name_dictionary(fruits)

def find_name_set(arr):
    length = len(arr)
    result_set = set()

    # 비교기준
    # 마지막은 자기자신이므로 기준에서 제외합니다.
    for i in range(0, length-1):
        print("---시작---")
        print(f"비교기준:{arr[i]}")

        # 비교대상
        # i 사용시 기준과 중복 따라서 i+1 처리
        # 비교 기준에 맞춰 끝(n)까지 비교를 합니다.
        for j in range(i+1, length):
            if arr[i] == arr[j]:
                print(f"{arr[i]} == {arr[j]}")
                result_set.add(arr[i])
            else:
                print(f"{arr[i]} != {arr[j]}")
        print("---종료---")
    print(f"결과: {result_set}")


# find_name_set(fruits)

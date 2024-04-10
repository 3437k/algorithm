def find_max_num(nums):
    length = len(nums)

    maxNum = nums[0]
    maxIdx = 0

    minNum = nums[0]
    minIdx = 0

    for i in range(0, length):
        if maxNum < nums[i]:
            maxNum = nums[i]
            maxIdx = i

        if minNum > nums[i]:
            minNum = nums[i]
            minIdx = i

    print(f"[최대값: {maxNum}, 최대값 index: {maxIdx}], [최소값:{minNum}, 최소값 index: {minIdx}] 입니다.")


nums = [4, 8, 9, 3, 2, 6, 7]

find_max_num(nums)

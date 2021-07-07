'''
is_stack_sequence 함수를 작성하세요.
'''


def is_stack_sequence(nums):
    # 1을 push하는 것 : 가장 먼저해야하는 작업(무조건)
    stack = [1]  # 리스트로 스택 대신

    current = 0

    for i in range(2, len(nums) + 1):
        while len(stack) > 0 and stack[-1] == nums[current]:
            stack.pop()
            current += 1

        if len(stack) == 0 or stack[-1] < nums[current]:
            stack.append(i)
        else:
            return "No"

    return "Yes"

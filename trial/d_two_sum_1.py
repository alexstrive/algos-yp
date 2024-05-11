from typing import List


def get_two_sum(values: List[int], target_sum: int) -> (int, int):
    sorted_values = sorted(values)

    left = 0
    right = len(values) - 1

    while left < right:
        current_sum = sorted_values[left] + sorted_values[right]
        if current_sum == target_sum:
            return sorted_values[left], sorted_values[right]
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1

    return None, None


if __name__ == '__main__':
    n = int(input())
    values = list(map(int, input().split(' ')))
    target_sum = int(input())
    result = get_two_sum(values, target_sum)

    print(" ".join(map(str, result)) if result[0] is not None and result[1] is not None else None)

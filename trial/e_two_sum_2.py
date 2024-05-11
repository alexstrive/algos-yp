from typing import List


def get_two_sum(values: List[int], target_sum: int) -> (int, int):
    prev = set()

    for val in values:
        diff = target_sum - val
        if val in prev:
            return val, diff
        else:
            prev.add(diff)

    return None, None


if __name__ == '__main__':
    n = int(input())
    values = list(map(int, input().split(' ')))
    target_sum = int(input())
    result = get_two_sum(values, target_sum)

    print(" ".join(map(str, result)) if result[0] is not None and result[1] is not None else None)

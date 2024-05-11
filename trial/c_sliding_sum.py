from typing import List


def sliding(ts: List[int], k: int) -> List[float]:
    result = []
    current_sum = sum(ts[0:k])
    result.append(current_sum / k)

    for i in range(len(ts) - k):
        current_sum -= ts[i]
        current_sum += ts[i + k]
        current_avg = current_sum / k
        result.append(current_avg)

    return result


if __name__ == "__main__":
    n = int(input())
    ts = list(map(int, input().split(' ')))
    k = int(input())

    slided = sliding(ts, k)
    print(" ".join(map(str, slided)))

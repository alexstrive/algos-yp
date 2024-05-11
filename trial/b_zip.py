from typing import List


def make_zip(seq_a: List[int], seq_b: List[int]) -> List[int]:
    seq_c = list()
    c = 0
    for i in range(len(seq_a) + len(seq_b)):
        if i % 2 == 0:
            seq_c.append(seq_a[c])
        else:
            seq_c.append(seq_b[c])
            c += 1

    return seq_c


if __name__ == "__main__":
    n = int(input())
    seq_a = list(map(int, input().split(' ')))
    seq_b = list(map(int, input().split(' ')))
    zipped = make_zip(seq_a, seq_b)
    print(" ".join(map(str, zipped)))

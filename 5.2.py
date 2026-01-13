from collections.abc import Iterable
from utils import read_data

EXPECTED = 14
LEVEL = 5


def get_sorted_ranges(data: list[str]) -> Iterable[tuple[int, int]]:
    return sorted(
        map(
            lambda line: (int(line.split("-")[0]), int(line.split("-")[1])),
            data[0].split(),
        ),
        key=lambda x: x[0],
    )


def merge_ranges(ranges: Iterable[tuple[int, int]]) -> list[tuple[int, int]]:
    merged: list[tuple[int, int]] = []
    iterator = iter(ranges)
    range_a = next(iterator)
    while True:
        try:
            range_b = next(iterator)
        except StopIteration:
            merged.append(range_a)
            break

        if range_a[1] >= range_b[0]:
            range_a = (range_a[0], max(range_a[1], range_b[1]))
        else:
            merged.append(range_a)
            range_a = range_b
    return merged


def resolve(data: list[str]) -> int:
    return sum(map(lambda r: 1 + r[1] - r[0], merge_ranges(get_sorted_ranges(data))))


def main() -> None:
    assert resolve(read_data(f"./input/{LEVEL}/test.txt", delimiter="\n\n")) == EXPECTED

    print(resolve(read_data(f"./input/{LEVEL}/input.txt", delimiter="\n\n")))


if __name__ == "__main__":
    main()

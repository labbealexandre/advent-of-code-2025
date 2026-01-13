from functools import reduce
from operator import mul
from collections.abc import Iterator
from utils import read_data

EXPECTED = 4277556
LEVEL = 6


def columns_number(data: list[str]) -> int:
    return len(data[0].split())


def column_operation(data: list[str], i: int) -> str:
    return data[-1].split()[i]


def column_numbers(data: list[str], i: int) -> Iterator[int]:
    return map(lambda row: int(row[i]), map(lambda row: row.split(), data[:-1]))


def rotate_data(data: list[str]) -> Iterator[tuple[Iterator[int], str]]:
    return map(
        lambda i: (
            column_numbers(data, i),
            column_operation(data, i),
        ),
        range(columns_number(data)),
    )


def resolve(data: list[str]) -> int:
    return sum(
        map(
            lambda col: sum(col[0]) if col[1] == "+" else reduce(mul, col[0], 1),
            rotate_data(data),
        )
    )


def main() -> None:
    assert resolve(read_data(f"./input/{LEVEL}/test.txt", delimiter="\n")) == EXPECTED

    print(resolve(read_data(f"./input/{LEVEL}/input.txt", delimiter="\n")))


if __name__ == "__main__":
    main()

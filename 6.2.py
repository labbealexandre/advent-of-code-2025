from functools import reduce
from operator import mul
from collections.abc import Iterator
from utils import read_data

EXPECTED = 3263827
LEVEL = 6


def get_raw_numbers(data: list[str]) -> Iterator[str]:
    return map(
        lambda col: "".join(col).strip(),
        map(lambda i: map(lambda row: row[i], data[:-1]), range(len(data[0]))),
    )


def get_operations(data: list[str]) -> list[str]:
    return data[-1].split()


def resolve(data: list[str]) -> int:
    raw_numbers_it = iter(get_raw_numbers(data))
    raw_operations_it = iter(get_operations(data))

    res: int = 0
    operator: str = next(raw_operations_it)
    while True:
        numbers: list[int] = []
        while True:
            try:
                n = next(raw_numbers_it)

                if n == "":
                    break
                numbers.append(int(n))
            except StopIteration:
                break

        res += sum(numbers) if operator == "+" else reduce(mul, numbers, 1)
        try:
            operator = next(raw_operations_it)
        except StopIteration:
            return res


def main() -> None:
    assert resolve(read_data(f"./input/{LEVEL}/test.txt", delimiter="\n")) == EXPECTED

    print(resolve(read_data(f"./input/{LEVEL}/input.txt", delimiter="\n")))


if __name__ == "__main__":
    main()

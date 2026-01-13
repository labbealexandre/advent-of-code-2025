from collections.abc import Iterable
from utils import read_data

EXPECTED = 3
LEVEL = 5


def is_fresh(ingredient: int, start: int, end: int) -> bool:
    return ingredient in range(start, end + 1)


def get_ranges(data: list[str]) -> Iterable[tuple[int, int]]:
    return map(
        lambda line: (int(line.split("-")[0]), int(line.split("-")[1])),
        data[0].split(),
    )


def get_ingredients(data: list[str]) -> Iterable[int]:
    return map(int, data[1].split())


def resolve(data: list[str]) -> int:
    return sum(
        map(
            lambda ingredient: any(
                map(
                    lambda range: is_fresh(ingredient, *range),
                    get_ranges(data),
                )
            ),
            get_ingredients(data),
        )
    )


def main() -> None:
    assert resolve(read_data(f"./input/{LEVEL}/test.txt", delimiter="\n\n")) == EXPECTED

    print(resolve(read_data(f"./input/{LEVEL}/input.txt", delimiter="\n\n")))


if __name__ == "__main__":
    main()

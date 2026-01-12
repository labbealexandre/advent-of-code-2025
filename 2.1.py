from utils import read_data

EXPECTED = 1227775554
LEVEL = 2


def is_invalid(n: str) -> bool:
    return len(n) % 2 == 0 and n[: len(n) // 2] == n[len(n) // 2 :]


def count_invalid(start: int, end: int) -> int:
    return sum(filter(lambda n: is_invalid(str(n)), range(start, end + 1)))


def resolve(data: list[str]) -> int:
    return sum(
        map(
            lambda numbers: count_invalid(*numbers),
            map(lambda line: map(lambda n: int(n), line.split("-")), data),
        )
    )


def main() -> None:
    assert resolve(read_data(f"./input/{LEVEL}/test.txt")) == EXPECTED

    print(resolve(read_data(f"./input/{LEVEL}/input.txt")))


if __name__ == "__main__":
    main()

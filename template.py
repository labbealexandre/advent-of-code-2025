from utils import read_data

EXPECTED = 0
LEVEL = -1


def resolve(data: list[str]) -> int:
    return EXPECTED


def main() -> None:
    assert resolve(read_data(f"./input/{LEVEL}/test.txt")) == EXPECTED

    print(resolve(read_data(f"./input/{LEVEL}/input.txt")))


if __name__ == "__main__":
    main()

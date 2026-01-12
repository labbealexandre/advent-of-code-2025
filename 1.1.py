from utils import read_data

EXPECTED = 3
LEVEL = 1


def resolve(data: list[str]) -> int:
    rotations = map(lambda line: int(line[1:]) * (-1 if line[0] == "L" else 1), data)

    pointer, counter = 50, 0
    for rotation in rotations:
        pointer += rotation

        if pointer % 100 == 0:
            counter += 1

    return counter


def main() -> None:
    assert resolve(read_data(f"./input/{LEVEL}/test.txt")) == EXPECTED

    print(resolve(read_data(f"./input/{LEVEL}/input.txt")))


if __name__ == "__main__":
    main()

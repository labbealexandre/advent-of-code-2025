from utils import read_data

EXPECTED = 6
LEVEL = 1


def mirror_pointer(pointer: int) -> int:
    return (100 - pointer) % 100


def resolve(data: list[str]) -> int:
    pointer, counter = 50, 0
    for line in data:
        rotation = int(line[1:])
        if line[0] == "R":
            pointer = pointer + rotation
            counter += pointer // 100
            pointer %= 100
        else:
            lpointer = mirror_pointer(pointer) + rotation
            counter += lpointer // 100
            pointer = mirror_pointer(lpointer)

    return counter


def main() -> None:
    assert resolve(read_data(f"./input/{LEVEL}/test.txt")) == EXPECTED

    print(resolve(read_data(f"./input/{LEVEL}/input.txt")))


if __name__ == "__main__":
    main()

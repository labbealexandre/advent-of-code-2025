from utils import read_data

EXPECTED = 4174379265
LEVEL = 2


def is_k_invalid(n: str, k: int) -> bool:
    return len(n) % k == 0 and n == "".join([n[:k]] * (len(n) // k))


def is_invalid(n: str) -> bool:
    return any([is_k_invalid(n, k) for k in range(1, int(1 + (len(n) // 2)))])


def count_invalid(start: int, end: int) -> int:
    a = sum(filter(lambda n: is_invalid(str(n)), range(start, end + 1)))
    return a


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

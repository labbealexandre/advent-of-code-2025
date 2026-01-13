from utils import read_data

EXPECTED = 21
LEVEL = 7


def propagate(raw_a: str, raw_b: str) -> str:
    return "".join(
        map(
            lambda i: (
                "^"
                if raw_b[i] == "^"
                else (
                    "|"
                    if (
                        raw_a[i] in ["|", "S"]
                        or (
                            i < len(raw_a) - 1
                            and raw_a[i + 1] == "|"
                            and raw_b[i + 1] == "^"
                        )
                        or (i > 0 and raw_a[i - 1] == "|" and raw_b[i - 1] == "^")
                    )
                    else raw_b[i]
                )
            ),
            range(len(raw_a)),
        )
    )


def count_split(raw_a: str, raw_b: str) -> int:
    return sum(map(lambda i: raw_b[i] == "^" and raw_a[i] == "|", range(len(raw_a))))


def resolve(data: list[str]) -> int:
    data_it = iter(data)

    raw_a = next(data_it)
    count: int = 0
    while True:
        try:
            raw_b = next(data_it)
        except StopIteration:
            break

        raw_b = propagate(raw_a, raw_b)
        count += count_split(raw_a, raw_b)

        raw_a = raw_b

    return count


def main() -> None:
    assert resolve(read_data(f"./input/{LEVEL}/test.txt")) == EXPECTED

    print(resolve(read_data(f"./input/{LEVEL}/input.txt")))


if __name__ == "__main__":
    main()

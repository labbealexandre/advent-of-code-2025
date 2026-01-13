from utils import read_data

EXPECTED = 40
LEVEL = 7


def propagate(raw_a: list[int], raw_b: list[int]) -> list[int]:
    return list(
        map(
            lambda i: (
                -1
                if raw_b[i] == -1
                else (
                    0
                    if raw_a[i] == -1
                    else (
                        raw_a[i - 1] + raw_a[i] + raw_a[i + 1]
                        if 0 < i < len(raw_a) - 1
                        and raw_b[i + 1] == -1
                        and raw_b[i - 1] == -1
                        else (
                            raw_a[i] + raw_a[i + 1]
                            if i < len(raw_a) - 1 and raw_b[i + 1] == -1
                            else (
                                raw_a[i - 1] + raw_a[i]
                                if i > 0 and raw_b[i - 1] == -1
                                else raw_a[i]
                            )
                        )
                    )
                )
            ),
            range(len(raw_a)),
        )
    )


def resolve(data: list[str]) -> int:
    data_it = iter(
        map(
            lambda row: list(
                map(lambda x: -1 if x == "^" else (1 if x == "S" else 0), row)
            ),
            data,
        )
    )

    raw_a = next(data_it)
    while True:
        try:
            raw_b = next(data_it)
        except StopIteration:
            break

        raw_a = propagate(raw_a, raw_b)

    return sum(raw_a)


def main() -> None:
    assert resolve(read_data(f"./input/{LEVEL}/test.txt")) == EXPECTED

    print(resolve(read_data(f"./input/{LEVEL}/input.txt")))


if __name__ == "__main__":
    main()

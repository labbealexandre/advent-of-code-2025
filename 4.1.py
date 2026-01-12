from utils import read_data

EXPECTED = 13
LEVEL = 4


def is_accessible(rolls: list[str], x: int, y: int) -> bool:
    return rolls[x][y] == "@" and (
        sum(
            [
                sum(
                    [
                        (i != x or j != y) and rolls[i][j] == "@"
                        for j in range(y - 1, y + 2)
                    ]
                )
                for i in range(x - 1, x + 2)
            ]
        )
        < 4
    )


def resolve(data: list[str]) -> int:
    return sum(
        [
            sum(
                [
                    is_accessible(
                        (
                            ["." * (len(data[0]) + 2)]
                            + list(map(lambda line: "." + line + ".", data))
                            + ["." * (len(data[0]) + 2)]
                        ),
                        x,
                        y,
                    )
                    for y in range(1, len(data[0]) + 1)
                ]
            )
            for x in range(1, len(data) + 1)
        ]
    )


def main() -> None:
    assert resolve(read_data(f"./input/{LEVEL}/test.txt")) == EXPECTED

    print(resolve(read_data(f"./input/{LEVEL}/input.txt")))


if __name__ == "__main__":
    main()

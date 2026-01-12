from utils import read_data

EXPECTED = 43
LEVEL = 4


def extend_rolls(rolls: list[str]) -> list[str]:
    return (
        ["." * (len(rolls[0]) + 2)]
        + list(map(lambda line: "." + line + ".", rolls))
        + ["." * (len(rolls[0]) + 2)]
    )


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


def update_roll(rolls, x, y):
    if rolls[x][y] != "@":
        return "."

    if is_accessible(rolls, x, y):
        return "x"

    return rolls[x][y]


def count_rolls(rolls: list[str], start=True):
    count = sum([row.count("x") for row in rolls])

    return (
        0
        if count == 0 and not start
        else count
        + count_rolls(
            extend_rolls(
                [
                    "".join(
                        [update_roll(rolls, x, y) for y in range(1, len(rolls[0]) - 1)]
                    )
                    for x in range(1, len(rolls) - 1)
                ]
            ),
            start=False,
        )
    )


def resolve(data: list[str]) -> int:
    return count_rolls(extend_rolls(data))


def main() -> None:
    assert resolve(read_data(f"./input/{LEVEL}/test.txt")) == EXPECTED

    print(resolve(read_data(f"./input/{LEVEL}/input.txt")))


if __name__ == "__main__":
    main()

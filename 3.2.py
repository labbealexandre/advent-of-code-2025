from utils import read_data

EXPECTED = 3121910778619
LEVEL = 3


def max_bank_voltage(bank: list[int], k=12) -> int:
    return (
        max(bank)
        if k == 1
        else ((10 ** (k - 1)) * max(bank[: 1 - k]))
        + max_bank_voltage(bank[bank.index(max(bank[: 1 - k])) + 1 :], k=k - 1)
    )


def resolve(data: list[str]) -> int:
    return sum(map(lambda line: max_bank_voltage(list(map(int, line))), data))


def main() -> None:
    assert resolve(read_data(f"./input/{LEVEL}/test.txt")) == EXPECTED

    print(resolve(read_data(f"./input/{LEVEL}/input.txt")))


if __name__ == "__main__":
    main()

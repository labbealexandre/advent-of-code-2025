from utils import read_data

EXPECTED = 357
LEVEL = 3


def max_bank_voltage(bank: list[int]) -> int:
    return (max(bank[:-1]) * 10) + max(bank[bank.index(max(bank[:-1])) + 1 :])


def resolve(data: list[str]) -> int:
    return sum(map(lambda line: max_bank_voltage(list(map(int, line))), data))


def main() -> None:
    assert resolve(read_data(f"./input/{LEVEL}/test.txt")) == EXPECTED

    print(resolve(read_data(f"./input/{LEVEL}/input.txt")))


if __name__ == "__main__":
    main()

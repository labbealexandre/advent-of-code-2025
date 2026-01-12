def read_data(file_path: str, delimiter: str = "\n") -> list[str]:
    with open(file_path) as file:
        data = file.read().strip().split(delimiter)

    return data

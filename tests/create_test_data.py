import random


def create_test_data(num_rows, num_cols):
    state = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
    for i in range(num_rows):
        for j in range(num_cols):
            state[i][j] = random.randint(0, 1)
    return state


def create_test_file_data(num_rows, num_cols, filename):
    state = create_test_data(num_rows, num_cols)
    with open(filename, "a") as f:
        for line in state:
            f.write(" ".join(map(str, line)))
            f.write("\n")


if __name__ == "__main__":
    num_rows = 10
    num_cols = 10
    filename = f"test_data-{random.randint(0,1000)}.txt"
    create_test_file_data(num_rows, num_cols, filename)

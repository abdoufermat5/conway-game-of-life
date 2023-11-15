def display_state(matrices):
    print("================================CURRENT STATE")
    for i in range(len(matrices)):
        print(matrices[i], sep="\n")


def game_of_life(matrices):
    n_c = len(matrices[0])
    n_r = len(matrices)
    nex_M = [[0 for _ in range(n_c)] for _ in range(n_r)]
    for i in range(n_r):
        for j in range(n_c):
            num_neighbors = 0
            print("ij: ", i, j, "mat:", matrices[i][j], end="\t")
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x < len(matrices) and 0 <= y < len(matrices[0]):
                        if matrices[x][y] == 1:
                            num_neighbors += 1

            num_neighbors = num_neighbors - matrices[i][j]
            print("neighbors: ",num_neighbors, end="\t")
            if num_neighbors in [0, 1] or num_neighbors > 3:
                    print("die")
                    nex_M[i][j] = 0
            else:

                if matrices[i][j] == 0:
                    if num_neighbors == 3:
                        print("survival")
                        nex_M[i][j] = 1
                    else:
                        print("died")
                if matrices[i][j] == 1:
                    nex_M[i][j] = 1
                    print("survival")

    return nex_M


def total_live_cells(matrices):
    N = sum([sum(x) for x in matrices])
    print("Total live cells", N)
    return N


def get_stable_state(matrices, n):
    i = 0
    while i < n:
        print(f"iteration {i}:")
        matrices = game_of_life(matrices)
        display_state(matrices)
        total_live_cells(matrices)
        i += 1


if __name__ == '__main__':
    M = [[0, 1, 0, 1, 0],
         [1, 0, 1, 0, 0],
         [0, 1, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0]
         ]
    N_iter = 20
    print(get_stable_state(M, N_iter))

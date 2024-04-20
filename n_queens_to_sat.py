# nQueens to SAT converter ♕
# Rok Nikolič 2024

from write_helpers import cnf_writer


def at_least_one(item_list):
    return [item_list]


def at_most_one(item_list):
    clauses = []
    for i in range(len(item_list)-1):
        for j in range(i + 1, len(item_list)):
            clauses.append([f"-{item_list[i]}", f"-{item_list[j]}"])
    return clauses


def exactly_one(item_list):
    final_list = at_least_one(item_list)
    final_list.extend(at_most_one(item_list))
    return final_list


# The code for diagonals in not pretty and could be made better
def find_negative_diagonals(i, size):
    primary = i
    secondary = 1
    left_diagonals = []
    top_diagonals = []
    while primary < size + 1:
        left_diagonals.append(f"{primary}{secondary}")
        top_diagonals.append(f"{secondary}{primary}")
        primary += 1
        secondary += 1

    return [left_diagonals, top_diagonals]


def find_positive_diagonals(i, size):
    primary = 5 - i
    bottom_primary = 4
    secondary = 1
    bottom_secondary = i
    left_diagonals = []
    bottom_diagonals = []
    while bottom_secondary < size + 1:
        left_diagonals.append(f"{primary}{secondary}")
        bottom_diagonals.append(f"{bottom_primary}{bottom_secondary}")
        primary -= 1
        bottom_primary -= 1
        secondary += 1
        bottom_secondary += 1

    return [left_diagonals, bottom_diagonals]


def convert_nqueens_to_sat(size):
    # Generate lists of rows, columns and diagonals
    main_lists = []
    diagonal_lists = []
    for i in range(1, size + 1):
        # Rows
        main_lists.append([f"{i}{j}" for j in range(1, size + 1)])
        # Columns
        main_lists.append([f"{j}{i}" for j in range(1, size + 1)])
        # Negative diagonals
        diagonal_lists.extend(find_negative_diagonals(i, size))
        # Positive diagonals
        diagonal_lists.extend(find_positive_diagonals(i, size))

    # Convert lists to sat clauses
    sat_list = []
    for item_list in main_lists:
        sat_list.extend(exactly_one(item_list))

    for item_list in diagonal_lists:
        sat_list.extend(at_most_one(item_list))

    return sat_list


sat_array = convert_nqueens_to_sat(4)
print(cnf_writer(sat_array, "n_queens_sat"))

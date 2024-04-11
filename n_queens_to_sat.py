# nQueens to SAT converter ♕
# Rok Nikolič 2024

def cnf_writer(size, sat_array):
    comment_line = f"c nQueens to sat converter, RN 2024\n"
    file_format = "CNF"
    variables = size**2
    clauses = len(sat_array)
    problem_line = f"p {file_format} {variables} {clauses}\n"
    preamble = f"{comment_line}c\n{problem_line}"


def at_least_one_multi(size):
    clauses = []
    for i in range(1, size + 1):
        # Rows
        clauses.append([f"{i}{j}" for j in range(1, size + 1)])
        # Columns
        clauses.append([f"{j}{i}" for j in range(1, size + 1)])
    return clauses


def at_most_one_multi(size):
    clauses = []
    for i in range(1, size + 1):
        for j in range(1, size):
            for k in range(j + 1, size + 1):
                # Row
                clauses.append([f"-{i}{j}", f"-{i}{k}"])
                # Column
                clauses.append([f"-{j}{i}", f"-{k}{i}"])
    return clauses


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


def convert_queens_to_sat(size):
    sat_array1 = []
    sat_array1.extend(at_least_one_multi(size))
    sat_array1.extend(at_most_one_multi(size))
    print(sat_array1)

    lists = []
    for i in range(size):
        # Rows
        lists.append([f"{i}{j}" for j in range(size)])
        # Columns
        lists.append([f"{j}{i}" for j in range(size)])
        # Diagonals
        primary_num = i
        secondary_num = 0
        while primary_num < size:
            print(f"{primary_num}{secondary_num}")
            print(f"{secondary_num}{primary_num}")
            secondary_num += 1
            primary_num += 1

    sat_array = []
    for item_list in lists:
        sat_array.extend(exactly_one(item_list))

    return sat_array


print(convert_queens_to_sat(4))

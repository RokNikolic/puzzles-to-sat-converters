# nQueens to SAT converter ♕
# Rok Nikolič 2024

def cnf_writer(sat_list):
    comment_line = f"c nQueens to sat converter, Rok N 2024\n"
    file_format = "cnf"
    variables = len(sat_list[0])**2
    clauses = len(sat_list)
    problem_line = f"p {file_format} {variables} {clauses}\n"
    preamble = f"{comment_line}{problem_line}"
    clauses = ""
    for clause in sat_list:
        clause_string = ""
        for variable in clause:
            clause_string += f"{variable} "
        clause_string += "0\n"
        clauses += clause_string
    return f"{preamble}{clauses}"


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
        primary = i
        secondary = 1
        left_diagonals = []
        top_diagonals = []
        while primary < size + 1:
            left_diagonals.append(f"{primary}{secondary}")
            top_diagonals.append(f"{secondary}{primary}")
            primary += 1
            secondary += 1
        diagonal_lists.append(left_diagonals)
        diagonal_lists.append(top_diagonals)

        # Positive diagonals
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
        diagonal_lists.append(left_diagonals)
        diagonal_lists.append(bottom_diagonals)

    # Convert lists to sat clauses
    sat_list = []
    for item_list in main_lists:
        sat_list.extend(exactly_one(item_list))

    for item_list in diagonal_lists:
        sat_list.extend(at_most_one(item_list))

    return sat_list


def write_to_cnf_file(cnf_file):
    with open("n_queens_sat.cnf", 'w') as file:
        file.write(cnf_file)


sat_array = convert_nqueens_to_sat(4)
cnf = cnf_writer(sat_array)
write_to_cnf_file(cnf)

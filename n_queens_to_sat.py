# nQueens to SAT reducer

def cnf_writer(comment, size, sat_array):
    empty_line = "c\n"
    comment_line = f"c {comment}\n"
    file_format = "CNF"
    variables = size**2
    clauses = len(sat_array)
    problem_line = f"p {file_format} {variables} {clauses}\n"
    preamble = f"{comment_line}{empty_line}{problem_line}"


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
    for i in range(1, size+1):
        # Rows
        lists.append([f"{i}{j}" for j in range(1, size + 1)])
        # Columns
        lists.append([f"{j}{i}" for j in range(1, size + 1)])
        # Diagonals
        for j in range(1, size+1):
            pass

    sat_array = []
    for item_list in lists:
        sat_array.extend(exactly_one(item_list))

    return sat_array


print(convert_queens_to_sat(3))

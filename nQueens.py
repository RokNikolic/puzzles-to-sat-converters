# nQueens to SAT reducer

def cnf_writer(comment, size, sat_array):
    empty_line = "c\n"
    comment_line = f"c {comment}\n"
    file_format = "CNF"
    variables = size**2
    clauses = len(sat_array)
    problem_line = f"p {file_format} {variables} {clauses}\n"
    preamble = f"{comment_line}{empty_line}{problem_line}"


def at_least_one_per_rows(size):
    temp_array = []
    for i in range(1, size + 1):
        temp_array.append([f"{i}{j}" for j in range(1, size + 1)])
    return temp_array


def at_least_one_per_columns(size):
    temp_array = []
    for i in range(1, size + 1):
        temp_array.append([f"{j}{i}" for j in range(1, size + 1)])
    return temp_array


def at_most_one_per_rows(size):
    temp_array = []
    for i in range(1, size + 1):
        for j in range(1, size):
            for k in range(j + 1, size + 1):
                temp_array.append([f"-{i}{j}", f"-{i}{k}"])
    return temp_array


def at_most_one_per_columns(size):
    temp_array = []
    for i in range(1, size + 1):
        for j in range(1, size):
            for k in range(j + 1, size + 1):
                temp_array.append([f"-{j}{i}", f"-{k}{i}"])
    return temp_array


def convert_queens_to_sat(size):
    sat_array = []
    sat_array.extend(at_least_one_per_rows(size))
    sat_array.extend(at_least_one_per_columns(size))
    sat_array.extend(at_most_one_per_rows(size))
    sat_array.extend(at_most_one_per_columns(size))

    print(sat_array)


convert_queens_to_sat(2)

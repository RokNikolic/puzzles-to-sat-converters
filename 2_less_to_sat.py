# 2-Less to SAT converter
# Rok Nikolič 2024


def cnf_writer(sat_list, variables):
    comment_line = f"c 2less to sat converter, Rok N 2024\n"
    file_format = "cnf"
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


def at_most_one(item_list):
    clauses = []
    for i in range(len(item_list)-1):
        for j in range(i + 1, len(item_list)):
            clauses.append([f"-{item_list[i]}", f"-{item_list[j]}"])
    return clauses


def convert_2less_to_sat(n, sequence_length):
    size_of_cube = n**3
    # Some node is the rth node of the sequence
    lists = []
    for r in range(1, sequence_length + 1):
        sat_list = [f"{i}{r}" for i in range(1, size_of_cube + 1)]
        lists.append(sat_list)

    # No node is in the sequence twice
    for i in range(1, size_of_cube + 1):
        node_list = []
        for r in range(1, sequence_length + 1):
            node_list.append(f"{i}{r}")
        lists.extend(at_most_one(node_list))

    print(lists)
    # Nodes with no connections can't both be in a sequence
    for i in range(1, size_of_cube + 1):
        pass

    return lists


def write_to_cnf_file(cnf_file):
    with open("2less_sat.cnf", 'w') as file:
        file.write(cnf_file)


convert_2less_to_sat(3, 2)

# clique to SAT converter
# Rok Nikolič 2024


def cnf_writer(sat_list, variables):
    comment_line = f"c clique to sat converter, Rok N 2024\n"
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


def convert_clique_to_sat(num_of_vertices, clique_size, graph_edges):
    # Some node is the rth node of the clique
    lists = []
    for r in range(1, clique_size + 1):
        sat_list = [f"{i}{r}" for i in range(1, num_of_vertices + 1)]
        lists.append(sat_list)

    # No node is in the clique twice
    for i in range(1, num_of_vertices + 1):
        node_list = []
        for r in range(1, clique_size + 1):
            node_list.append(f"{i}{r}")
        lists.extend(at_most_one(node_list))

    # Nodes with no connections can't both be in a clique
    for i in range(1, num_of_vertices + 1):
        for j in range(i + 1, num_of_vertices + 1):
            edge = f"{i}{j}"
            edge_list = []
            if edge not in graph_edges:
                for r in range(1, clique_size + 1):
                    edge_list.append(f"{i}{r}")
                    edge_list.append(f"{j}{r}")
            if edge_list:
                lists.extend(at_most_one(edge_list))

    return lists


def write_to_cnf_file(cnf_file):
    with open("clique_sat.cnf", 'w') as file:
        file.write(cnf_file)


graph_edges1 = ["13", "23", "34", "35", "45"]
sat_array = convert_clique_to_sat(5, 3, graph_edges1)
cnf = cnf_writer(sat_array, 5*3)
write_to_cnf_file(cnf)

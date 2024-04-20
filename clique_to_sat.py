# clique to SAT converter
# Rok Nikolič 2024

from write_helpers import cnf_writer


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
        lists.append([f"{i}{r}" for i in range(1, num_of_vertices + 1)])

    # No node is in the clique twice
    for i in range(1, num_of_vertices + 1):
        node_list = [f"{i}{r}" for r in range(1, clique_size + 1)]
        lists.extend(at_most_one(node_list))

    # Nodes with no connections can't both be in a clique
    for i in range(1, num_of_vertices + 1):
        for j in range(i + 1, num_of_vertices + 1):
            if f"{i}{j}" not in graph_edges:
                for r in range(1, clique_size + 1):
                    for s in range(1, clique_size + 1):
                        if r == s:
                            continue
                        edge_list = [f"{i}{r}", f"{j}{s}"]
                        print(edge_list)
                        lists.extend(at_most_one(edge_list))

    return lists


def write_to_cnf_file(cnf_file):
    with open("clique_sat.cnf", 'w') as file:
        file.write(cnf_file)


graph_edges1 = ["13", "23", "34", "35", "45"]
sat_list = convert_clique_to_sat(5, 3, graph_edges1)
print(cnf_writer(sat_list, "clique_to_sat"))

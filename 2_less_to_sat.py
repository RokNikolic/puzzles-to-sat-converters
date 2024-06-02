# 2-Less to SAT converter 2024, github.com/RokNikolic

from write_helpers import cnf_writer


def at_most_one(item_list):
    clauses = []
    for i in range(len(item_list)-1):
        for j in range(i + 1, len(item_list)):
            clauses.append([f"-{item_list[i]}", f"-{item_list[j]}"])
    return clauses


def two_less(coordinate1, coordinate2):
    x, y, z = coordinate1
    u, v, w = coordinate2
    return x < u and y < v or x < u and z < w or y < v and z < w


def make_list_of_not_connected(coordinate, size):
    list_of_not_connected = []
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            for k in range(1, size + 1):
                if not two_less(coordinate, (i, j, k)):
                    list_of_not_connected.append((i, j, k))
    return list_of_not_connected


def convert_2less_to_sat(n, sequence_length):
    # Some node is the rth node of the sequence
    lists = []
    for r in range(1, sequence_length + 1):
        sat_list = []
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                for k in range(1, n + 1):
                    sat_list.append(f"{i}{j}{k}{r}")
        lists.append(sat_list)

    # No node is in the sequence twice
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                node_list = []
                for r in range(1, sequence_length + 1):
                    node_list.append(f"{i}{j}{k}{r}")
                lists.extend(at_most_one(node_list))

    # Nodes with no connections can't both be in a sequence
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                not_connected = make_list_of_not_connected((i, j, k), n)
                for non_conn in not_connected:
                    if non_conn == (i, j, k):
                        continue
                    for r in range(1, sequence_length + 1):
                        for s in range(1, r):
                            sat_list = [f"{i}{j}{k}{s}", f"{non_conn[0]}{non_conn[1]}{non_conn[2]}{r}"]
                            lists.extend(at_most_one(sat_list))

    return lists


if __name__ == "__main__":
    sat_array = convert_2less_to_sat(4, 9)
    print(cnf_writer(sat_array, "2_less_sat"))

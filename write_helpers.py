def cnf_writer(sat_list, comment):
    comment_line = f"c {comment}\n"
    file_format = "cnf"
    num_of_variables = len(sat_list)
    num_of_clauses = len(sat_list)
    problem_line = f"p {file_format} {num_of_variables} {num_of_clauses}\n"
    preamble = f"{comment_line}{problem_line}"
    clauses = ""
    for clause in sat_list:
        clause_string = ""
        for variable in clause:
            clause_string += f"{variable} "
        clause_string += "0\n"
        clauses += clause_string
    final_sat = f"{preamble}{clauses}"
    write_cnf_to_disc(final_sat, comment)
    return final_sat


def write_cnf_to_disc(cnf_file, name):
    with open(f"{name}.cnf", 'w') as file:
        file.write(cnf_file)

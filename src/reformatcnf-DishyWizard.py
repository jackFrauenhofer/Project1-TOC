#This script was used to reformat 2SAT.cnf into the proper format

input_file = "/Users/jackfrauenhofer/Theory Project 1/Project1-TOC/input/2SAT.cnf"
output_file = "/Users/jackfrauenhofer/Theory Project 1/Project1-TOC/input/2SAT2.cnf"

with open(input_file, "r") as input, open(output_file, "w") as output:
    for line in input:
        if line.startswith(('c', 'p')):  # lines that start with 'c' or 'p' need commas to be replaced with spaces
            line = line.replace(',', ' ')
        output.write(line)
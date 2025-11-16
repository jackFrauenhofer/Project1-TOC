"""
SAT Solver - DIMACS-like Multi-instance Format
----------------------------------------------------------
Project 1: Tough Problems & The Wonderful World of NP

INPUT FORMAT (multi-instance file):
-----------------------------------
Each instance starts with a comment and a problem definition:

c <instance_id> <k> <status?>
p cnf <n_vertices> <n_edges>
u,v
x,y
...

Example:
c 1 3 ?
p cnf 4 5
1,2
1,3
2,3
2,4
3,4
c 2 2 ?
p cnf 3 3
1,2
2,3
1,3

OUTPUT:
-------
A CSV file named 'resultsfile.csv' with columns:
instance_id,n_vars,n_clauses,method,satisfiable,time_seconds,solution


EXAMPLE OUTPUT
------------
instance_id,n_vars,n_clauses,method,satisfiable,time_seconds,solution
3,4,10,U,0.00024808302987366915,BruteForce,{}
4,4,10,S,0.00013304100139066577,BruteForce,"{1: True, 2: False, 3: False, 4: False}"
"""

from typing import List, Tuple, Dict
from src.helpers.sat_solver_helper import SatSolverAbstractClass
import itertools


class SatSolver(SatSolverAbstractClass):

    """
        NOTE: The output of the CSV file should be same as EXAMPLE OUTPUT above otherwise you will loose marks
        For this you dont need to save anything just make sure to return exact related output.
        
        For ease look at the Abstract Solver class and basically we are having the run method which does the saving
        of the CSV file just focus on the logic
    """


    def sat_backtracking(self, n_vars:int, clauses:List[List[int]]) -> Tuple[bool, Dict[int, bool]]:
        pass

    def sat_bruteforce(self, n_vars:int, clauses:List[List[int]]) -> Tuple[bool, Dict[int, bool]]:

        def generate_solutions(n_vars: int, max_assignments):
            """
            This is a generator to yield one assignment at a time in order to reduce time complexity.
            Each assignment is a list of variablles, where the index correlates to a variable, and its value is either 0/1.
            For example:
                assignment[0] correlates to variable 1
                assignment[1] correlates to variable 2
            """

            # Error Check: if n_vars is 0 or negative, do not assign anything and return
            if n_vars <= 0:
                yield []
                return
            
            # First assignment generated is all 0s
            assignment = [ 0 for _ in range(n_vars)]

            assignments_generated = 0 #Count how many assignments were generated

            for i in range(max_assignments):
                
                yield assignment
                assignments_generated += 1

                # This algorithm loops over list and generates a new assignment
                curr = 0
                while curr < n_vars:
                    if assignment[curr] == 0:
                        assignment[curr] = 1
                        break
                    else:
                        assignment[curr] = 0
                        curr += 1
                    
                # All assignments have been generated
                if curr >= n_vars:
                    return

        def satisfiable_verifier(assignment: List[int], clauses:List[List[int]]) -> bool:
            
            for clause in clauses:

                clause_satisfiable = False

                for literal in clause:
                
                    # Need to absolute value because literal could be negative
                    # and have to subtract 1 to shift to correlate to list indexing
                    var_idx = abs(literal) - 1

                    value = assignment[var_idx]
                    
                    # Check if literal would be True or False
                    if value == 1 and literal > 0 or value == 0 and literal < 0:
                        clause_satisfiable = True
                        break

                # If clause is not satisfiable, return false (which will cause a new assignment to be generated below)    
                if not clause_satisfiable:
                    return False

            # If all clauses were not false, then the assignment is a solution  
            return True

        max_assignments = 1 << n_vars #Bit shift to calculate (2^n_vars)

        for assignment in generate_solutions(n_vars, max_assignments):
            if satisfiable_verifier(assignment, clauses):
                solution = {}
                for i in range(n_vars):
                    solution[i+1] = assignment[i]
                return True, solution
            
        # If no solution found, will return False with no variables assigned
        return False, {}


    def sat_bestcase(self, n_vars:int, clauses:List[List[int]]) -> Tuple[bool, Dict[int, bool]]:
        pass

    def sat_simple(self, n_vars:int, clauses:List[List[int]]) -> Tuple[bool, Dict[int, bool]]:
        pass
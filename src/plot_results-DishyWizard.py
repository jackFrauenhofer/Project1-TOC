import matplotlib.pyplot as plt
import numpy as np
import csv

# Initialize axes and color list
x = []
y = []
colors = []

# To read different input files, copy and paste the absolute path here:
with open("/Users/jackfrauenhofer/Theory Project 1/Project1-TOC/results/brute_force_2SAT_sat_solver_results.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        x.append(int(row["n_vars"])) # Adds the n_vars rule to x-axis
        y.append(float(row["time_seconds"])) # Adds the time (in seconds) to the y-axis

        # This section classifies the color for the point. Green if satisfiable, red if not.
        if row["satisfiable"].strip() == "S":
            colors.append("green")
        else:
            colors.append("red")

plt.figure(figsize=(12,8))
plt.scatter(x, y, c=colors, marker="o")

# Labels the graph's axes and title
plt.title("SAT Instances: Time Solved with Bruteforce v. k-complexity")
plt.xlabel("Number of Variables (ie. k-complexity)")
plt.ylabel("Time (seconds)")
plt.ticklabel_format(style='plain', axis='y')

# This saves the plot to the 'figures' folder to a specified name
plt.savefig(f"../figures/brute_force_2SAT_plot")
plt.show()

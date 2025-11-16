Project TeamworkTemplate
Version 1 9/11/24
A separate copy of this template should be filled out and submitted by each student, regardless of the number of students on the team. Also change the title of this template to “Project x Teamwork <team> - <netid>”
1
	Team Name: Dishy Wizard
	2
	Individual name: Jack Frauenhofer
	3
	Individual netid: jfrauenh
	4
	Other team members names and netids: N/A
	5
	Link to github repository: 
	6
	Overall project attempted, with sub-projects: Brute-Force SAT Solver
	7
	List of included files (if you have many files of a certain type, such as test files of different sizes, list just the folder): (Add more rows as necessary)


File/folder Name
	File Contents and Use
	Code Files
	plot_results-DishyWizard.py
	Used to plot the results from the brute force SAT solver
	sat.py
	Updated the ‘sat_bruteforce’ function.
	reformatcnf-DishyWizard.py
	

	Test Files
	cnffile.cnf
	Basic CNF file input to test Brute Force SAT solver on few instances. This file was included in the original github clone as a basic test. I used this file to mainly test that the output of my solver was working before running the CNF’s with much more instances.
	check-kSAT.cnf-DishyWizard
	CNF file that contains instances of various k-complexities to test Brute Force SAT solver. This file was sourced from the canvas resource page.
	check-2SAT.cnf-DishyWizard
	CNF file that contains instances of only k=2 complexity SATs to test Brute Force SAT solver. This file was sourced from the canvas resource page.
	Output Files
	brute_force_cnffile_sat_solver_results-DishyWizard.csv
	CSV file that includes the output from running Brute Force on input file ‘cnffile.cnf’
	brute_force_kSAT_sat_solver_results-DishyWizard.csv
	CSV file that includes the output from running Brute Force on input file ‘check-kSAT.cnf-DishyWizard’.
	brute_force_2SAT_sat_solver_results-DishyWizard.csv
	CSV file that includes the output from running Brute Force on input file ‘check-kSAT.cnf-DishyWizard’.
	Plots (as needed)
	plots-brute_force_cnffile-DishyWizard.png
	Simple plot analyzing various execution times compared to different instances. This plot is not materially helpful in analyzing different complexities and their time executions - it was more to test if the output of my ‘plot_results.py’ was working.
	plots-brute_force_kSAT-DishyWizard.png
	Plot analyzing various execution times compared to different instances with various k-complexities
	plots-brute_force_2SAT-DishyWizard.png
	Plot analyzing various execution times compared to different instances, all with k=2 complexities.
	

	8
	Individual Student time (in hours) to complete: 10 hours
	9
	Your specific activities and responsibilities:
* I built the ‘sat_bruteforce’ function
* I built the ‘plot_results-DishyWizard.py’ script to plot the results of the SAT solver
* I built the ‘reformatcnf-DishyWizard.py’
	10
	What was personally learned (topic, programming, algorithms)
* I learned how to build a brute force algorithm to actually solve an SAT
* Because 2SAT.cnf had commas instead of spaces when lines started with a ‘c’ or a ‘p’, I learned how to parse a csv using the script that I built named ‘reformatcnf-DishyWizard.py’
* Overall, it was helpful to learn the layout of the github folder. In order to build ‘sat_bruteforce’, I had to effectively understand all of the helper functions. This was a great learning exercise to practice my python programming as a result.
	11
	How the team was organized, and what might be improved.
* I was a one man team, hence why I only completed ‘sat_bruteforce’. Thus, all responsibilities and progress with this project was from my individual work.
* In general, the program could be improved by implementing the ‘plot_results.py’ script to be run after each input when ‘uv run main.py’ is run. In the github, we were warned not to interfere with this script, so I thought it was best to manually create the plots. However, I think automating this process of updating the input_file for the plot into the direct function when the output CSV file is created would help automate the process.
* Although I signed up to build the ‘sat_bruteforce’ function, there are clearly better, more time-effective ways to solve SAT problems. Brute force is a relatively basic, less time-efficient solver than backtracking or other solvers. Thus, I would want to improve my solver by implementing the other more effective solvers.
	12
	Any additional material: None
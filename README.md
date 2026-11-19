# Week 1 Assessment - Analysis


## Setup steps
1. Clone the repository and open the folder in VS Code
2. Create a virtual environment: python -m venv venv
3. Activate it: venv\Scripts\activate
4. Install packages: pip install -r requirements.txt
5. Create a .env file with API_KEY=your_key (this file is not committed)
6. Run each file from the main folder, for example: python src\task1\task1.py

## Notes
- Tasks are split into small files, one per job, inside src/task1, src/task2 and src/task3.
- Task 1 is split into two parts task1.py and task1_part2.py.
- Task 2 is split into five parts task2_files.py ,task2_env.py , task2_api.py , task2_nest.py ,  task2_errors.py
- Task 3 is split into five parts 
- In the terminal I used mkdir, cp, mv and Select-String (the Windows version of grep).

## Findings summary
1. Headcount: Sales 2, HR 2, IT 3, Finance 1; the Legal department has no employees.
2. Finance has the highest average salary (90000) and Sales the lowest (41000).
3. Two missing salaries were filled with the median (56000) and one duplicate row was removed.
4. The median salary is 56000, and the highest paid employee is Karthik in Finance.
5. Chennai has the most employees (4 of 8).
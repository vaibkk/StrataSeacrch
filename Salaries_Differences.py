# Import your libraries
import pandas as pd

# Start writing code
employee = db_employee
dept = db_dept

merged_data = pd.merge(employee,dept,how="left",left_on=["department_id"],right_on=["id"])

eng = merged_data[merged_data["department"]=="engineering"].reset_index()
marketing = merged_data[merged_data["department"]=="marketing"].reset_index()

max_eng = eng.salary.max()
max_mar = marketing.salary.max()

diff = max_mar - max_eng
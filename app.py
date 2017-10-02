
def add_employee():
		import re
		import datetime
		import csv
		f = open('employees.csv','rt')
		str_of_file = f.read()
		indexes = re.findall(r'\n(\d{2,4})',str_of_file)
		last_index = int(indexes[-1])
		list_of_employees=[]
		while True:
			start = input('Hit enter to add a new employee [q to exit] ')
			if start == 'q':
				break
			employee_info = []
			last_index+=1
			em_fname = input('first name ')
			em_lname = input('last name ')
			em_hire_date = str(datetime.date.today())
			em_salary = input('salary ')
			employee_info.extend([last_index,em_fname,em_lname,em_hire_date,em_salary])
			list_of_employees.append(employee_info)
		f = open('employees.csv','at')
		cout = csv.writer(f)
		cout.writerows(list_of_employees)
		
add_employee()

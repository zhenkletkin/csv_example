import datetime
import csv

def add_employee():
    with open('employees.csv','r+') as f:
        cin = csv.reader(f)
        list_of_employees = [row for row in cin if row]
        new_employees=[]
        last_id = int(list_of_employees[-1][0])
        today = str(datetime.date.today())
        while True:
            start = input('Press enter to add a new employee [q to exit] ')
            if start.lower() == 'q':
                print('')
                print('list of new employees:')
                print('')
                for each in new_employees:
                    print('{first_name} {last_name}'.format(**each))
                break
            
            employee = {}
            employee['employee_id'] = last_id + 1
            employee['first_name'] = input('first name ')
            employee['last_name'] = input('last name ')
            employee['salary'] = input('salary ')
            employee['hire_date'] = today
            
            new_employees.append(employee)
            last_id+=1
        cout = csv.DictWriter(f, ['employee_id','first_name','last_name','hire_date','salary'])
        cout.writerows(new_employees)

add_employee()
        

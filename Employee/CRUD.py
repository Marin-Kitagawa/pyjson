from uuid import *
from collections import defaultdict
from pprint import *
from json import *
from Validators import *


class Employee:
    database = defaultdict(dict)

    def __init__(self, name, salary, dob, doj, department, position, email, phone):
        self.name = name
        self.id = str(uuid4())
        self.salary = salary
        self.dob = dob
        self.doj = doj
        self.department = department
        self.position = position
        self.email = email
        self.phone = phone
        temp = {}
        for i in ['name', 'salary', 'dob', 'doj', 'department', 'position', 'email', 'phone']:
            temp[i] = eval(f'self.{i}')
        self.database[self.id] = temp

    @classmethod
    def get_employee_by_id(self, id):
        if id in self.database:
            pprint(self.database[id])
        else:
            pprint("Employee with the given id doesn't exists\n")

    @classmethod
    def get_employee_id_by_phone(self, phone):
        for i in self.database:
            if self.database[i]['phone'] == phone:
                pprint(i)

    @classmethod
    def get_employee_id_by_email(self, email):
        for i in self.database:
            if self.database[i]['email'] == email:
                pprint(i)

    @classmethod
    def get_employees_by_name(self, name):
        found = []
        for i in self.database:
            if self.database[i]['name'].lower() == name.lower():
                found.append(self.database[i])
        if len(found) == 0:
            pprint("No employee with the given name exists\n")
        else:
            for i in found:
                pprint(i)

    @classmethod
    def get_employee_by_phone(self, phone):
        found = None
        for i in self.database:
            if self.database[i]['phone'] == phone:
                found = self.database[i]
        if not found:
            pprint("No employees with the given phone number exists\n")
        else:
            pprint(found)

    @classmethod
    def get_employees_by_department(self, department):
        found = []
        for i in self.database:
            if self.database[i]['department'].lower() == department.lower():
                found.append(self.database[i])
        if len(found) == 0:
            pprint("Department not found\n")
        else:
            for i in found:
                pprint(i)

    @classmethod
    def get_employees_by_position(self, position):
        found = []
        for i in self.database:
            if self.database[i]['position'].lower() == position.lower():
                found.append(self.database[i])
        if len(found) == 0:
            pprint("Position not found\n")
        else:
            for i in found:
                pprint(i)

    @classmethod
    def get_employees_by_doj(self, doj):
        found = []
        for i in self.database:
            if self.database[i]['doj'].lower() == doj.lower():
                found.append(self.database[i])
        if len(found) == 0:
            pprint("There are no employers who joined on the given date\n")
        else:
            for i in found:
                pprint(i)

    @classmethod
    def get_employee_by_email(self, email):
        for i in self.database:
            if self.database[i]['email'].lower() == email.lower():
                pprint(self.database[i])
        else:
            pprint("There are no users with the given email\n")

    @classmethod
    def update_employee_name(self, name, new_name):
        found = []
        for i in self.database:
            if self.database[i]['name'] == name:
                found += [i]
        if len(found) == 0:
            pprint("No employee found with the given name")
        elif len(found) == 1:
            self.database[found[0]]['name'] = new_name
        else:
            it = 0
            pprint("Choose the employee id of the employee whose name must be changed")
            for i in found:
                it += 1
                pprint(f"{it}. {i}")
            choice = int(input())
            while choice not in range(1, len(found)+1):
                pprint("Enter a valid choice")
                choice = int(input())
            self.database[choice-1]['name'] = new_name

    @classmethod
    def update_employee_phone(self, phone, new_phone):
        found = False
        for i in self.database:
            if self.database[i]['phone'] == phone:
                self.database[i]['phone'] = new_phone
                found = True
                pprint(f'Phone number has been successfully changed from {phone} to {new_phone} for user wih id: {i}')
        if not found:
            pprint("No employee with the given phone number exists")

    @classmethod
    def update_employee_salary_by_email(self, email, salary):
        found = False
        for i in self.database:
            if self.database[i]['email'] == email:
                self.database[i]['salary'] = salary
                found = True
                pprint(f"Salary information has been updated for user with id: {i}")
        if not found:
            pprint("No employee with the given email exists")

    @classmethod
    def update_employee_salary_by_phone(self, phone, salary):
        found = False
        for i in self.database:
            if self.database[i]['phone'] == phone:
                self.database[i]['salary'] = salary
                found = True
                pprint(f"Salary information for user with id: {i} has ben updated")
        if not found:
            pprint("No employee with the given phone number exists")


    @classmethod
    def update_employee_department_by_email(self, email, new_department):
        found = False
        for i in self.database:
            if self.database[i]['email'] == email:
                self.database[i]['department'] = new_department
                found = True
                pprint(f"Department has been changed for user with ID: {i}")
        if not found:
            pprint("No employee with the given email exists")

    @classmethod
    def update_employee_department_by_phone(self, phone, new_department):
        found = False
        for i in self.database:
            if self.database[i]['phone'] == phone:
                self.database[i]['department'] = new_department
                found = True
                pprint(f"Department has been changed for user with ID: {i}")
        if not found:
            pprint("No employee with the given phone number exists")

    @classmethod
    def update_employee_position_by_email(self, email, new_position):
        found = False
        for i in self.database:
            if self.database[i]['email'] == email:
                self.database[i]['position'] = new_position
                found = True
                pprint(f"Position has been changed for user with ID: {i}")
        if not found:
            pprint("No employee with the given email exists")

    @classmethod
    def update_employee_position_by_phone(self, phone, new_position):
        found = False
        for i in self.database:
            if self.database[i]['phone'] == phone:
                self.database[i]['position'] = new_position
                found = True
                pprint(f"Position has been changed for user with ID: {i}")
        if not found:
            pprint("No employee with the given phone exists")

    @classmethod
    def update_employee_email(self, email, new_email):
        found = False
        for i in self.database:
            if self.database[i]['email'] == email:
                self.database[i]['email'] = new_email
                found = True
                pprint(f"Email changed for employee with ID: {i}")
        if not found:
            pprint("No employee with the given email exists")

    @classmethod
    def delete_employee_by_id(self, id):
        if id in self.database:
            del self.database[id]
        else:
            pprint("ID NOT FOUND\n")

    @classmethod
    def delete_employees_by_department(self, department):
        employees = []
        for i in self.database:
            if self.database[i]['department'] == department:
                employees.append(i)
        if len(employees) == 0:
            pprint("There are currently no employees in the department\n")
        elif len(employees) == 1:
            del self.database[employees[0]]
        else:
            pprint("There are more than one employee in the department. Do you want to delete all of them?\n")
            choice = input("Type yes or no\n")
            if choice.lower() == 'yes':
                for i in employees:
                    del self.database[i]
            else:
                ids = input("Enter the ids of the employees to be deleted separated by space\n\n").split()
                for i in ids:
                    if i in self.database:
                        del self.database[i]
                        pprint(f'Employee with ID: {i} has been deleted')
                    else:
                        pprint(f'Employee with ID: {i} NOT FOUND')

    @classmethod
    def delete_employees_by_position(self, position):
        employees = []
        for i in self.database:
            if self.database[i]['position'] == position:
                employees.append(i)
        if len(employees) == 0:
            pprint("There are currently no employees in the position\n")
        elif len(employees) == 1:
            del self.database[employees[0]]
        else:
            pprint("There are more than one employee in the position. Do you want to delete all of them?\n")
            choice = input("Type yes or no\n")
            if choice.lower() == 'yes':
                for i in employees:
                    del self.database[i]
            else:
                ids = input("Enter the ids of the employees to be deleted separated by space\n\n").split()
                for i in ids:
                    if i in self.database:
                        del self.database[i]
                        pprint(f'Employee with ID: {i} has been deleted')
                    else:
                        pprint(f'Employee with ID: {i} NOT FOUND')

    @classmethod
    def delete_employee_by_email(self, email):
        found = None
        for i in self.database:
            if self.database[i]['email'] == email:
                del self.database[i]
                found = i
                break
        if not found:
            pprint("There are no employees with the given email\n")
        else:
            pprint(f'User with ID: {found} has been deleted')

    @classmethod
    def delete_employee_by_phone(self, phone):
        found = None
        for i in self.database:
            if self.database[i]['phone'] == phone:
                del self.database[i]
                found = i
                break
        if not found:
            pprint("There are no employees with the given phone number\n")
        else:
            pprint(f'User with ID: {found} has been deleted')


def create_employee(name, salary, dob, doj, department, position, email):
    return Employee(name, salary, dob, doj, department, position, email)


if __name__ == '__main__':
    while True:
        employee_count = len(Employee.database)
        employee = None
        choice = int(input(
            """
            What do you want to do?
            1. Create a new employee
            2. Update employee details
            3. Delete an employee record
            4. View details of a specific employee
            5. View details of all the employees
            6. Get employee id from email or phone
            """
        ))
        while choice not in range(1, 7):
            pprint("Enter a valid choice\n")
            choice = int(input(
                """
                What do you want to do?
                1. Create a new employee
                2. Update employee details
                3. Delete an employee record
                4. View details of a specific employee
                5. View details of all the employees
                6. Get employee id from email or phone
                """
            ))

        if choice == 1:
            name = input("Enter name of the employee\n")
            while not name_validator(name):
                pprint("Enter a valid name\n")
                name = input("Enter name of the employee\n")
            salary = input("Enter salary of the employee\n")
            while not salary_validator(salary):
                pprint("Enter a valid salary in compliance with labor laws in India\n")
                salary = input("Enter salary of the employee\n")
            dob = input("Enter dob of the employee\n")
            while not date_validator(dob):
                pprint("Enter a valid date\n")
                dob = input("Enter dob of the employee\n")
            doj = input("Enter doj of the employee\n")
            while not date_validator(doj):
                pprint("Enter a valid date\n")
                doj = input("Enter doj of the employee\n")
            while not age_validator(dob, doj):
                pprint("Enter a valid DOJ. Minimum age for working is 14 years in India\n")
                doj = input("Enter doj of the employee\n")
            department = input("Enter department of the employee\n")
            position = input("Enter position of the employee\n")
            email = input("Enter email of the employee\n")
            while not email_validator(email):
                pprint("Enter a valid Email\n")
                email = input("Enter email of the employee\n")
            while temp_email_validator(email):
                pprint("This email service provider is not trusted. Enter a non-disposable email\n")
                email = input("Enter email of the employee\n")
            phone = input("Enter the phone number of the employee\n")
            while not phone_validator(phone):
                pprint("Enter a valid phone number in this format `+CountryCode (AreaCode) XXX-XXXX\n")
                phone = input("Enter the phone number of the employee\n")
            employee_count += 1
            employee = Employee(name, salary, dob, doj, department, position, email, phone)

        elif choice == 2:
            update = int(input(
                """
                What do you want to update?
                1. Name
                2. Salary
                3. Department
                4. Position
                5. Email
                6. Phone Number
                """
            ))
            if not employee_count:
                pprint("Create an employee first\n")
                exit(1)
            while update not in range(1, 7):
                pprint("Enter a valid choice\n")
                update = int(input(
                    """
                    What do you want to update?
                    1. Name
                    2. Salary
                    3. Department
                    4. Position
                    5. Email
                    6. Phone Number
                    """
                ))

            param = 0
            if update in range(2, 5):
                change = ['salary', 'department', 'position'][update-2]
                param = int(input(
                    f"""
                    How do you want to update the {change}?
                    1. By email
                    2. By phone
                    """
                ))
                while param not in range(1, 3):
                    pprint("Enter a valid choice")
                    param = int(input(
                        f"""
                        How do you want to update the {change}?
                        1. By email
                        2. By phone
                        """
                    ))
            global_email = ''
            global_phone = ''
            if param == 1 or update == 5:
                global_email = input("Enter the email of the employee\n")
                while not email_validator(global_email):
                    pprint("Enter a valid email")
                    global_email = input("Enter the email of the employee\n")
                while temp_email_validator(global_email):
                    pprint("Enter an email from a trusted provider")
                    global_email = input("Enter the email of the employee\n")
            elif param == 2 or update == 6:
                global_phone = input("Enter the phone number of the employee\n")
                while not phone_validator(global_phone):
                    pprint("Enter a valid phone_number")
                    global_phone = input("Enter the phone number of the employee\n")
            if update == 1:
                name = input("Enter the old name for the employee\n")
                while not name_validator(name):
                    pprint("Enter a valid name\n")
                    name = input("Enter the old name for the employee\n")
                new_name = input("Enter the new name for the employee\n")
                while not name_validator(name):
                    pprint("Enter a valid name\n")
                    new_name = input("Enter the new name for the employee\n")
                Employee.update_employee_name(name, new_name)
            elif update == 2:
                salary = float(input("Enter the new salary for the employee\n"))
                while not salary_validator(salary):
                    pprint("Enter a valid salary in compliance with labor laws in India\n")
                    salary = float(input("Enter the new salary for the employee\n"))
                if len(global_email) > 0:
                    Employee.update_employee_salary_by_email(global_email, salary)
                else:
                    Employee.update_employee_salary_by_phone(global_phone, salary)
            elif update == 3:
                department = input("Enter the new department for the employee\n")
                if len(global_email) > 0:
                    Employee.update_employee_department_by_email(global_email, department)
                else:
                    Employee.update_employee_department_by_phone(global_phone, department)
            elif update == 4:
                position = input("Enter the new position for the employee\n\n")
                if len(global_email) > 0:
                    Employee.update_employee_position_by_email(global_email, position)
                else:
                    Employee.update_employee_position_by_phone(global_phone, position)
            elif update == 5:
                new_email = input("Enter the new email of the employee\n")
                while not email_validator(new_email):
                    pprint("Enter a valid email address")
                    new_email = input("Enter the new email of the employee\n")
                while temp_email_validator(new_email):
                    pprint("Enter an email id from a trusted provider")
                    new_email = input("Enter the new email of the employee\n")
                Employee.update_employee_email(global_email, new_email)
            elif update == 6:
                new_phone = input("Enter the new phone for the employee\n")
                while not phone_validator(new_phone):
                    pprint("Enter a valid phone number in the format +CountryCode (AreaCode) XXX-XXXX\n")
                    new_phone = input("Enter the new phone for the employee\n")
                Employee.update_employee_phone(global_phone, new_phone)

        elif choice == 3:
            if not employee_count:
                pprint("Create an employee first\n")
                exit(1)
            delete = int(input(
                """
                What do you want to delete by?
                1. ID
                2. Department
                3. Position
                4. Email
                5. Phone Number
                """
            ))
            while delete not in range(1, 6):
                pprint("Enter a valid choice\n")
                delete = int(input(
                    """
                    What do you want to delete by?
                    1. ID
                    2. Department
                    3. Position
                    4. Email
                    5. Phone Number
                    """
                ))

            if delete == 1:
                id = input("Enter the id of the employee to be deleted\n")
                while not id_validator(id):
                    pprint("Enter a valid UUID4 ID\n")
                    id = input("Enter the id of the employee to be deleted\n")
                Employee.delete_employee_by_id(id)

            elif delete == 2:
                Employee.delete_employees_by_department(input("Enter the department of the employee to be deleted\n"))

            elif delete == 3:
                Employee.delete_employees_by_position(input("Enter the position of the employee to be deleted\n"))

            elif delete == 4:
                email = input("Enter the email of the employee to be deleted\n")
                while not email_validator(email):
                    pprint("Enter a valid email id\n")
                    email = input("Enter the email of the employee to be deleted\n")
                while temp_email_validator(email):
                    pprint("Enter an email id from a trusted provider (non-disposable)\n")
                    email = input("Enter the email of the employee to be deleted\n")
                Employee.delete_employee_by_email(email)

            elif delete == 5:
                phone = input("Enter the phone of the employee to be deleted\n\n")
                while not phone_validator(phone):
                    pprint("Enter a valid phone number in the format +CountryCode (AreaCode) XXX-XXXX\n")
                    phone = input("Enter the phone of the employee to be deleted\n\n")
                Employee.delete_employee_by_phone(phone)

        elif choice == 4:
            if not employee_count:
                pprint("Create an employee first\n")
                exit(1)
            details = int(input(
                """
                What do you want to search the employee by?
                1. ID
                2. Phone
                3. Email
                """
            ))

            while details not in range(1, 4):
                pprint("Enter a valid choice\n")
                details = int(input(
                    """
                    What do you want to search the employee by?
                    1. ID
                    2. Phone
                    3. Email
                    """
                ))

            if details == 1:
                id = input("Enter the ID of the employee\n")
                while not id_validator(id):
                    pprint("Enter a valid UUIDv4 ID\n")
                    id = input("Enter the ID of the employee\n")
                Employee.get_employee_by_id(id)
            elif details == 2:
                phone = input("Enter the phone of the employee\n")
                while not phone_validator(phone):
                    pprint("Enter a valid phone number in the format +CountryCode (AreaCode) XXX-XXXX\n")
                    phone = input("Enter the phone of the employee\n")
                Employee.get_employee_by_phone(phone)
            elif details == 3:
                email = input("Enter the email of the employee\n")
                while not email_validator(email):
                    pprint("Enter a valid email\n")
                    email = input("Enter the email of the employee\n")
                while temp_email_validator(email):
                    pprint("Enter a non-disposable email\n")
                    email = input("Enter the email of the employee\n")
                Employee.get_employee_by_email(email)
        elif choice == 5:
            if not employee_count:
                pprint("Create an employee first\n")
                exit(1)
            details = int(input(
                """
                Do you want to view the details of 
                1. All the employees 
                or
                2. with specific name, doj, department, position 
                """
            ))

            while details not in range(1, 3):
                pprint("Enter a valid choice\n")
                details = int(input(
                    """
                    Do you want to view the details of 
                    1. All the employees 
                    or
                    2. with specific name, doj, department, position 
                    """
                ))

            if details == 1:
                for i in Employee.database:
                    pprint(Employee.database[i])
            elif details == 2:
                param = int(input(
                    """
                    What do you want to search by?
                    1. Name
                    2. DOJ
                    3. Department
                    4. Position
                    """
                ))

                while param not in range(1, 5):
                    pprint("Enter a valid choice\n")
                    param = int(input(
                        """
                        What do you want to search by?
                        1. Name
                        2. DOJ
                        3. Department
                        4. Position
                        """
                    ))

                if param == 1:
                    name = input("Enter the name of the employee(s)\n")
                    while not name_validator(name):
                        pprint("Enter a valid name\n")
                        name = input("Enter the name of the employee(s)\n")
                    Employee.get_employees_by_name(name)
                elif param == 2:
                    doj = input("Enter the doj of the employee(s)\n")
                    while not date_validator(doj):
                        pprint("Enter a valid date\n")
                        doj = input("Enter the doj of the employee(s)\n")
                    while not joining_validator(doj):
                        pprint("Enter a valid DOJ\n")
                        doj = input("Enter the doj of the employee(s)\n")
                    Employee.get_employees_by_doj(doj)
                elif param == 3:
                    Employee.get_employees_by_department(input("Enter the department of the employee(s)\n"))
                elif param == 4:
                    Employee.get_employees_by_position(input("Enter the position of the employee(s)\n"))

        elif choice == 6:
            search = int(input(
                """
                How to you want to get the ID?
                1. Using email
                2. Using phone
                """
            ))
            while not search in range(1, 3):
                pprint("Enter a valid choice\n")
                search = int(input(
                    """
                    How to you want to get the ID?
                    1. Using email
                    2. Using phone
                    """
                ))

            if search == 1:
                email = input("Enter the email of the employee\n")
                while not email_validator(email):
                    pprint("Enter a valid email")
                    email = input("Enter the email of the employee\n")
                while temp_email_validator(email):
                    pprint("Enter an email from a trusted provider")
                    email = input("Enter the email of the employee\n")
                Employee.get_employee_id_by_email(email)
            elif search == 2:
                phone = input("Enter the phone number of the employee")
                while not phone_validator(phone):
                    pprint("Enter a valid phone number")
                    phone = input("Enter the phone number of the employee")
                Employee.get_employee_id_by_phone(phone)

        with open('../db.json', 'w') as f:
            f.write(dumps(Employee.database))
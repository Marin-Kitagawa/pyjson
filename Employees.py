from collections import defaultdict
from pprint import *
from json import *
from random import choice
from uuid import *

if __name__ == '__main__':
    n = int(input('Enter the number of employees:\n'))
    d = defaultdict(list)
    for i in range(n):
        id = input("Enter the id of the employee\n")
        name = input('Enter the name of the employee\n')
        salary = input('Enter the salary of the employee\n')
        phone = ''
        for i in range(10):
            phone += choice('0123456789')
        phone = f'+1 ({phone[:3]}) {phone[3:6]}-{phone[6:]}'
        email = '_'.join(name.lower().split())+'@gmail.com'
        department = input('Enter the department of the employee\n')
        position = input('Enter the position of the employee\n')
        unique_key = uuid4()
        d[str(unique_key)] += [id, name, salary, phone, email, department, position]
    pprint(d)
    with open('db.json', 'w') as f:
        f.write(dumps(d))

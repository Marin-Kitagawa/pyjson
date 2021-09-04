import re
from datetime import datetime
from pprint import pprint
from uuid import *


def name_validator(name):
    return len(name) > 0


def email_validator(email):
    return re.fullmatch(r"\b[\w\.\+\-]+@[\w-]+\.[A-Z|a-z]{2,}\b", email)


def phone_validator(phone):
    return re.fullmatch(r"\+\d+ \(\d+\) \d+-\d+", phone) and len(''.join(re.findall(r'\d+', ''.join(phone.split()[1:])))) == 10


def age_validator(dob, doj):
    return int(doj.split()[0]) - int(dob.split()[0]) >= 14


def joining_validator(doj):
    return datetime(*map(int, doj.split()), ) < datetime.now()


def date_validator(date):
    try:
        return bool(datetime(*map(int, date.split()), ))
    except:
        return False


def salary_validator(salary):
    return float(salary) > 4576 * 12


def temp_email_validator(email):
    banned = [
        'temp-mail.org',
        'mailinator.com',
        'guerrillamail.com',
        'sharklasers.com',
        '10minutesmail.net',
    ]
    return any(x[1:] in banned or 'guerrillamail' in x for x in re.findall(r'@[\w\-]+\.\w+$', email))


def id_validator(id):
    try:
        return re.fullmatch(r'^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$', id, re.I)
    except:
        return False

if __name__ == '__main__':
    phone = "+91 (994) 346-8997"
    print(phone_validator(phone))
    print(temp_email_validator('something@temp-mail.org'))
    print(email_validator('somename@gmail.com'))
    print(age_validator('2021 01 01', '2021 07 19'))
    print(id_validator(str(uuid4())))
    print(id_validator('nonsense'))
    print(salary_validator(1234))
    print(name_validator('F'))
    print(joining_validator('2047 11 11'))
    print(date_validator('sjcnc'))
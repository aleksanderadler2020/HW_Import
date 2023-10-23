from datetime import *
from salary import *
from db.people import *


if __name__ == '__main__':
    print(date.today().strftime("%d.%m.%y"))
    print(calculate_salary())
    print(get_employees())


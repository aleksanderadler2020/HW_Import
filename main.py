from datetime import date
import salary
from db import people
import numpy as np
import pandas as pd


if __name__ == '__main__':
    print(date.today().strftime("%d.%m.%y"))
    print(salary.calculate_salary())
    print(people.get_employees())
    print(np.array([[1, 2, 3], [4, 5, 6]]))
    print(pd.DataFrame([[1, 2, 3]]))

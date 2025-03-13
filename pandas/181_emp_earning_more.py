import pandas as pd


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee = pd.merge(employee, employee, left_on='managerId', right_on='id', suffixes=('_emp', '_man'))
    employee = employee[employee['salary_emp'] > employee['salary_man']]
    return pd.DataFrame({'Employee': employee['name_emp']})


if __name__ == '__main__':
    data = [[1, 'Joe', 70000, 3],
            [2, 'Henry', 80000, 4],
            [3, 'Sam', 60000, None],
            [4, 'Max', 90000, None]]
    employee_df = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype(
        {'id': 'Int64', 'name': 'object', 'salary': 'Int64', 'managerId': 'Int64'})
    print(find_employees(employee_df))

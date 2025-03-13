import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee['salary'].drop_duplicates()
    if len(employee) == 1:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    return pd.DataFrame({'SecondHighestSalary': [employee.nlargest(2).iloc[-1]]})


if __name__ == '__main__':
    # data = [[1, 100], [2, 200], [3, 300], [4, 400]]
    data = [[1, 100], [2, 100]]
    employee_df = pd.DataFrame(data, columns=['id', 'salary']).astype({'id': 'int64', 'salary': 'int64'})
    print(second_highest_salary(employee_df))

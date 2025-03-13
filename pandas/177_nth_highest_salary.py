import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, n: int) -> pd.DataFrame:
    if n < 1:
        return pd.DataFrame({f'getNthHighestSalary({n})': [None]})
    employee = employee['salary'].drop_duplicates()
    if n > len(employee):
        return pd.DataFrame({f'getNthHighestSalary({n})': [None]})
    return pd.DataFrame({f'getNthHighestSalary({n})': [employee.nlargest(n).iloc[-1]]})


if __name__ == '__main__':
    data = [[1, 100], [2, 200], [3, 300], [4, 400]]
    employee_df = pd.DataFrame(data, columns=['id', 'salary']).astype({'id': 'int64', 'salary': 'int64'})
    n = 3
    print(nth_highest_salary(employee_df, n))

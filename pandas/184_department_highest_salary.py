import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(employee, department, how='left',
                         left_on='departmentId', right_on='id', suffixes=('_emp', '_dep'))

    if len(merged_df.index) == 0:
        return pd.DataFrame({'Department': [], 'Employee': [], 'Salary': []})

    dep_max_salaries = merged_df.groupby('name_dep').apply(
        func=lambda group: group['salary'].max(axis=0)).reset_index(drop=False)
    dep_max_salaries.columns = ['name_dep', 'salary']

    merged_df = merged_df.merge(dep_max_salaries, on=['name_dep', 'salary'])

    merged_df = merged_df[['name_dep', 'name_emp', 'salary']]
    merged_df.columns = ['Department', 'Employee', 'Salary']

    return merged_df


if __name__ == '__main__':
    data = [[1, 'Joe', 70000, 1],
            [2, 'Jim', 90000, 1],
            [3, 'Henry', 80000, 2],
            [4, 'Sam', 60000, 2],
            [5, 'Max', 90000, 1]]
    employee_df = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype(
        {'id': 'Int64', 'name': 'object', 'salary': 'Int64', 'departmentId': 'Int64'})
    data = [[1, 'IT'],
            [2, 'Sales']]
    department_df = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
    print(department_highest_salary(employee_df, department_df))

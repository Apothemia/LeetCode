import pandas as pd


# There might be a cleaner solution using DataFrame.rolling()
def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    if len(logs.index) < 3:
        return pd.DataFrame({'ConsecutiveNums': []})

    logs.sort_values(by='id', inplace=True)

    consecutive_nums = set()
    last_id = logs.iloc[0, 0] - 1
    last_num = logs.iloc[0, 1]
    count = 0

    for i, row in logs.iterrows():
        if row['num'] == last_num and row['id'] == last_id + 1:
            count += 1
        else:
            count = 1

        if count == 3:
            consecutive_nums.add(row['num'])

        last_num = row['num']
        last_id = row['id']

    return pd.DataFrame({'ConsecutiveNums': list(consecutive_nums)})


if __name__ == '__main__':
    data = [[1, 1], [2, 0], [3, 0], [4, 0], [5, 1], [6, 1]]
    logs_df = pd.DataFrame(data, columns=['id', 'num']).astype({'id': 'Int64', 'num': 'Int64'})
    print(consecutive_numbers(logs_df))

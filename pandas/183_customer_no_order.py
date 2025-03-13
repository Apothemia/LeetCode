import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(customers, orders, how='left',
                         left_on='id', right_on='customerId', suffixes=('_cus', '_ord'))
    return pd.DataFrame({'Customers': merged_df[merged_df['id_ord'].isna()]['name']})


if __name__ == '__main__':
    data = [[1, 'Joe'],
            [2, 'Henry'],
            [3, 'Sam'],
            [4, 'Max']]
    customers_df = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
    data = [[1, 3],
            [2, 1]]
    orders_df = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id': 'Int64', 'customerId': 'Int64'})
    print(find_customers(customers_df, orders_df))

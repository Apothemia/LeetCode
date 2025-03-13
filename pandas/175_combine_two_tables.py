import pandas as pd


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(person, address, on='personId', how='left')[['firstName', 'lastName', 'city', 'state']]


if __name__ == '__main__':
    person_df = pd.DataFrame([
        [1, 'Wang', 'Allen'],
        [2, 'Alice', 'Bob']],
        columns=['personId', 'firstName', 'lastName']).astype(
        {'personId': 'Int64', 'firstName': 'object', 'lastName': 'object'})
    address_df = pd.DataFrame([
        [1, 2, 'New York City', 'New York'],
        [2, 3, 'Leetcode', 'California']],
        columns=['addressId', 'personId', 'city', 'state']).astype(
        {'addressId': 'Int64', 'personId': 'Int64', 'city': 'object', 'state': 'object'})
    print(combine_two_tables(person_df, address_df))

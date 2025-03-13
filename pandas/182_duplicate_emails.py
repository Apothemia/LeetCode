import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    res_df = person['email']
    return pd.DataFrame({'Email': res_df[res_df.duplicated()].unique()})


if __name__ == '__main__':
    data = [[1, 'a@yahoo.com'], [2, 'jacky@yahoo.com'], [3, 'jacky@yahoo.com']]
    person_df = pd.DataFrame(data, columns=['id', 'email']).astype({'id': 'Int64', 'email': 'object'})
    print(duplicate_emails(person_df))

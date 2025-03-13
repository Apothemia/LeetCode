import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores_sorted = scores['score'].sort_values(ascending=False)
    return pd.DataFrame({'score': scores_sorted, 'rank': scores_sorted.rank(method='dense', ascending=False)})


if __name__ == '__main__':
    data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
    scores_df = pd.DataFrame(data, columns=['id', 'score']).astype({'id': 'Int64', 'score': 'Float64'})
    print(order_scores(scores_df))

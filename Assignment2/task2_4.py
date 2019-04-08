import pandas as pd

CSV_FILE = '../The-Movies-Dataset/ratings_small.csv'


def main(file):
    print("Task 2.4: Analyzing a rating dataset")

    # Read a CSV file into DataFrame
    df = pd.read_csv(file)

    # Group data by movieId
    df_grouped = df.groupby(df['movieId'])

    # Display count of items per movieId
    # print(df_grouped.size())

    for index, row in df_grouped:
        # Create per movieId a dictionary /w aggregated data
        item = {
            'id': index,
            'rating_mean': row['rating'].mean(),
            'rating_median': row['rating'].median()
        }

        # Print its details
        print(item)

    # Similar approach /wo iterating
    # # Get mean rating by movieId
    # df_grouped_mean = df['rating'].groupby(df['movieId']).mean()
    # print(type(df_grouped_mean))
    #
    # # Get median rating by movieId
    # df_grouped_median = df['rating'].groupby(df['movieId']).median()
    # print(type(df_grouped_median))


if __name__ == '__main__':
    main(CSV_FILE)

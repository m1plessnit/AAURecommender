import pandas as pd
import numpy as np

FILE_RATINGS_CSV = '../The-Movies-Dataset/movies_metadata.csv'


def main(file):

    print("Task 2.3: Analyzing a movie dataset")

    # Read a CSV file into DataFrame
    df = pd.read_csv(file)

    print("\n--- Inspect output ---")
    print(type(df))     # Return: DtypeWarning: Columns (10) have mixed types

    print("\n--- Print details of first movie ---")
    print(df.iloc[0])

    print("\n--- Print details of last movie ---")
    print(df.iloc[-1])

    print("\n--- Print details of 'Jumanji' movie ---")
    # TODO print(df['title'] == 'Jumanji')

    print("\n--- Create a subset from existing /w few columns ---")
    small_df = df[['title', 'release_date', 'popularity', 'revenue', 'runtime', 'genres']].copy()
    print(small_df)

    print("\n--- Make familiar /w lambda ---")
    small_df = df[['title', 'release_date', 'popularity', 'revenue', 'runtime', 'genres']].copy()
    small_df.loc['release_date'] = pd.to_datetime(small_df['release_date'], errors='coerce')

    small_df['release_year'] = small_df['release_date'].apply(lambda x: str(x).split('-')[0] if x != np.nan else np.nan)
    small_df['release_year'] = small_df['release_year'].apply(to_float)
    small_df['release_year'] = small_df['release_year'].astype('float')
    small_df = small_df.drop(columns="release_date")
    print(small_df)

    print("\n--- Pint details of all movies with 2010 release-year ---")
    print(small_df['release_year'] == 2010)


def to_float(x):
    try:
        x = float(x)
    except:
        x = np.nan
    return x


if __name__ == '__main__':
    main(FILE_RATINGS_CSV)

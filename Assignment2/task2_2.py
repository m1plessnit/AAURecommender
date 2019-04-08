import pandas as pd


def main():
    print("Task 2.2: Getting used to DataFrames")

    # Create a table-like structure
    data = [
        ['Toy Story', 21.946943],
        ['Jumanji', 17.015539],
        ['Grumpier Old Men', 11.7129]
    ]

    # Create a DataFrame-instance /w headings
    result = pd.DataFrame(data, columns=['Title', 'Popularity'])

    # Sort DataFrame's values
    result_sorted = result.sort_values(by='Popularity', ascending=True)

    print("\n--- Print the popularity values ---")
    print(result_sorted['Popularity'])


if __name__ == '__main__':
    main()
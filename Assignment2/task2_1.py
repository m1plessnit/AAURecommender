# Task 2.1: Getting used to Series
import pandas as pd
import numpy as np


def main():
    print("Task 2.1: Getting used to Series")

    # Create Panda's Series-instance based on an array
    data = np.array(['Toy Story', 'Jumanji', 'Grumpier Old Men'])
    series = pd.Series(data)

    print("\n--- Print first element ---")
    print(series[0])
    print("\n--- Print first two elements ---")
    print(series[:2])
    print("\n--- Print last two elements ---")
    print(series[-2:])

    # Create a new series /w defined indexes
    series = pd.Series(data, index=['a', 'b', 'c'])

    print("\n--- Print element at index position 'b' ---")
    print(series['b'])


if __name__ == '__main__':
    main()
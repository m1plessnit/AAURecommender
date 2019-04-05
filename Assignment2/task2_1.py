# Task 2.1: Getting used to Series
import pandas as pd
import numpy as np


def main():
    # Create a Panda's Series based on an array
    data = np.array(['Toy Story', 'Jumanji', 'Grumpier Old Men'])
    series = pd.Series(data)

    print("Task 2.1")
    print("\n")
    print("Print first element:")
    print(series[0])
    print("\n")
    print("Print first two elements:")
    print(series[:2])
    print("\n")
    print("Print last two elements:")
    print(series[-2:])
    print("\n")

    series = pd.Series(data, index=['a', 'b', 'c'])

    print("Print element at index position 'b':")
    print(series['b'])
    print("\n")


if __name__ == '__main__':
    main()
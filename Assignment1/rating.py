FILE_RATINGS_CSV = '../MovieLens/ratings.csv'


def compute_mean_rating(file_name):
    ratings = []

    try:
        input_file = open(file_name, 'r')
    except FileNotFoundError:
        print("ERROR: File could not be found")
        exit()

    # Skip first line (if any)
    next(input_file, None)

    # Read one line at a time
    for row in input_file:
        # Get rid of the \n character
        row = row.strip()
        # Split to columns
        columns = row.split(',')
        # Display whole row, including invisible chars
        #    print(repr(columns))

        # Map single columns to temporary data-types
        userId = columns[0]  # ATM not used
        movieId = columns[1]  # ATM not used
        rating = float(columns[2])
        timestamp = columns[3]  # ATM not used

        # Finally, build up ratings
        ratings.append(rating)

    input_file.close()

    print('--- Calculation ---')

    cnt = len(ratings)
    print('Number of ratings: ', cnt)

    total = sum(ratings)
    print('Sum: ', total)

    avg = total / cnt
    print('Average: ', avg)

    return avg


def main():

    print('--- Process ratings.csv ---')

    print('Read: ', FILE_RATINGS_CSV)
    print()

    mean_value = compute_mean_rating(FILE_RATINGS_CSV)
    print()

    print('--- Output ---')

    print('Mean value: ', mean_value)
    print()


main()

import operator

FILE_RATINGS_CSV = '../MovieLens/ratings.csv'

def calc_mean(ratings):
    cnt = len(ratings)
    total = sum(ratings)
    return total / cnt


def calc_mode(ratings):
    result = {}

    for i in ratings:
        if i not in result:
            result[i] = ratings.count(i)

    sorted_result = sorted(result.items(), key=operator.itemgetter(1))
    # print(sorted_result)

    return sorted_result[len(sorted_result)-1][0]


def calc_median(ratings):
    cnt = len(ratings)
    return ratings[int(cnt/2)]


def compute_mean_rating(file_name):
    ratings = []

    try:
        input_file = open(file_name, 'r')
    except FileNotFoundError:
        print("ERROR: given file - ' + file_name + ' could not be found")
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
        userId = columns[0]         # ATM not used
        movieId = columns[1]        # ATM not used
        rating = float(columns[2])
        timestamp = columns[3]      # ATM not used

        # Finally, build up ratings
        ratings.append(rating)

    input_file.close()

    # Sort ratings ascending
    ratings.sort()

    # Mean: the average value
    mean = calc_mean(ratings)

    # Mode: value that occurs most often
    mode = calc_mode(ratings)

    # Median: is the "middle" value in an ordered list of numbers
    median = calc_median(ratings)

    result_string = 'Mean: ' + str(mean) + '\nMode: ' + str(mode) + '\nMedian: ' + str(median)


    return result_string


def main():

    print('\n--- Process ratings.csv ---')
    print('Read: ', FILE_RATINGS_CSV)

    print('\n--- Output ---')
    print(compute_mean_rating(FILE_RATINGS_CSV))


main()

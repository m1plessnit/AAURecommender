ratings = []

inputFile = open('../MovieLens/ratings.csv', 'r')

# Skip first line (if any)
next(inputFile, None)

# Read one line at a time
for row in inputFile:
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

inputFile.close()


def compute_mean_rating(rating_list):
    cnt = len(rating_list)
    print('Number of ratings: ', cnt)

    total = sum(rating_list)
    print('Sum: ', total)

    avg = total / cnt
    print('Average: ', avg)


print('--- Ratings Snapshot ---')
compute_mean_rating(ratings)

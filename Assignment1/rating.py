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

print('--- Ratings Snapshot ---')

cnt = len(ratings)
print('Number of ratings: ', cnt)

sum = sum(ratings)
print('Sum: ', sum)

avg = sum / cnt
print('Average: ', avg)
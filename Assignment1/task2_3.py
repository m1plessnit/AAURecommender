def computeMeanRating(file):
    try:
        f = open(file,'r')
    except:
        print('Something went wrong reading the file "' + file + '"')
        exit()

    ratingsCount = 0
    sum = 0.0
    ratings = []

    #loop to get numeric rating values; proceed them as needed
    for x in f:
        ratingValue = x.split(',')[2]
        if isFloat(ratingValue):
            sum += float(ratingValue)
            ratingsCount += 1
            ratings.append(float(ratingValue))

    MeanValue = sum / ratingsCount





    #MODE
    ratings.sort()
    refValue = -1
    actValue = -1
    refCount = -1 #to determine if actual counting element appears more often as the one before
    count = 1
    modes = {}

    for x in ratings:
        actValue = x
        if actValue == refValue:
            count += 1

        elif refValue == -1: #first iteration over ratings[]
            refValue = actValue
            continue

        else: #one sequence of same numbers ends
            if count == refCount:
                modes[refValue] = count
                count = 1

            if count > refCount:
                modes.clear()
                modes[refValue] = count
                refCount = count
                count = 1

            refValue = actValue

    modeString = ''
    for x in modes:
        modeString += str(x) + "  "



    #MEDIAN
    length = len(ratings)
    middleIndex = int(length / 2)

    if length%2==0:   #if length is even
        median= (ratings[middleIndex - 1] + ratings[middleIndex]) / 2
    else:
        median = ratings[middleIndex]



    resultString = 'Statistics:\n\n' \
                   'number of ratings: ' + str(ratingsCount) + '\n \n' \
                                                          'mean rating: ' + str(MeanValue) +'\n' \
                                                                                            'mode(s): ' + modeString + '\n' \
                    'median: ' + str(median)


    return resultString



#helping method to determine if string is convertable to float
def isFloat(str):
    try:
        x = float(str)
        return True
    except ValueError:
        return False


#call of main method
print(computeMeanRating("../MovieLens/ratings.csv"))
class Statistic:
    def computeMeanRating(self, file):
        try:
            f = open(file, 'r')
        except:
            print('Something went wrong reading the file "' + file + '"')
            exit()

        count = 0
        sum = 0.0

        for x in f:
            toCheck = x.split(',')[2]
            if isFloat(toCheck):
                sum += float(toCheck)
                count += 1

        meanValue = sum / count
        print('number of ratings: ' + str(count))
        return meanValue

    # helping method to determine if string is convertable to float

def isFloat(str):
    try:
        x = float(str)
        return True
    except ValueError:
        return False
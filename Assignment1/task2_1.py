print('Script Start')

#create a list of float
ratings = []

#open file
f = open("../MovieLens/ratings.csv", "r")

#store ratings in the list

print(f.readline())
for x in f:
    ratings.append(x)

#close the file
f.close()

#calculate avg
ratingSum = 0.0
nrOfRatings = 0

for x in ratings:
    rating = x.split(',')[2]
    ratingSum += float(rating)
    nrOfRatings += 1

avgRating = ratingSum/nrOfRatings
print('number of ratings: ' + str(nrOfRatings))
print('average rating: ' + str(avgRating))
print('\n'+'script end ')
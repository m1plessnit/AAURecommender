import utilityModule

statObject = utilityModule.Statistic()
x = statObject.computeMeanRating('../MovieLens/ratings.csv')
print(x)
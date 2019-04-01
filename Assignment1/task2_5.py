import utilityModule

statObject = utilityModule.Statistic()
x = statObject.computeMeanRating('ratings.csv')
print(x)
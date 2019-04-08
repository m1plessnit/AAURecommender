import pandas as pd

CSV_FILE = 'ratings_small.csv'



def main(file):

    print('Task 2.5: Find similar users \n')

    df = pd.read_csv('ratings_small.csv')

    #Group the DataFrame by the attribut "UserId
    grouped = df.groupby('userId')

    #get the first group
    first_group = grouped.get_group(1)

    #create a set of the first group
    firstUserMovies = set(first_group['movieId'])

    #print the set of rated movies for user A (= for the first group)
    print('set of rated movies for first user: ')
    print(firstUserMovies)
    print('-----')



    #iterate over the grouped DataFrame & make an intersection operation to determine users that
    #ratet at least three movies that the first user has rated

    #create a list for similar users (=users with at least three ratings)
    similarUsers = []

    for user, user_df in grouped:
        currentSet = set(user_df['movieId'])
        sameMovies = currentSet.intersection(firstUserMovies)
        if len(sameMovies) > 2:
            similarUsers.append(user)

    #print the determined users
    print('users with an intersection of at least three movies:')
    print(similarUsers)

if __name__ == '__main__':
    main(CSV_FILE)
import csv
import operator

FILE_RATINGS_CSV = '../MovieLens/movies.csv'

def analyze(file_name):
    with open(file_name, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        result = {}

        for row in csv_reader:
            # print(row)

            movie_id = row[0]       # ATM not used
            title = row[1]          # ATM not used
            genres = row[2]

            genre_list = genres.split('|')

            for item in genre_list:
                if item in result:
                    result[item] = result[item]+1
                else:
                    result[item] = 1

        print(result)

        sorted_result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)

        print(sorted_result)


def main():

    print('\n--- Process movies.csv ---')
    print('Read: ', FILE_RATINGS_CSV)

    print('\n--- Output ---')
    print(analyze(FILE_RATINGS_CSV))


main()
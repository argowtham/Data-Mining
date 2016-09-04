import numpy as np
import operator
import sys
from scipy import spatial


def create_movie_user_dictionary(movie_data):
    movie_user_data = {}
    for i in range(0, 1682):
        for j in range(0, 943):
            user_list = []
            if not movie_data[j][i] == 0.0:
                user_list.append(j+1)
            movie_user_data[i+1] = user_list
    return movie_user_data
    # sys.stdout = open("movie_user_dict.txt", 'w')
    # print(movie_user_data)


if __name__ == '__main__':
    print("Program to predict the user rating for a movie he/she did not see")
    in_file = open("D:\OneDrive\IU\DataMining\Home works\HW1\ml-100k\/u.data", "r")
    next(in_file)
    np.set_printoptions(threshold=np.inf)
    mv_lens = np.zeros(943*1682).reshape(943, 1682)
    for line in in_file:
        line = list(line.split())
        user_id, item_id, rating = int(line[0]), int(line[1]), int(line[2])
        mv_lens[user_id-1][item_id-1] = rating

    movie_user_dict = create_movie_user_dictionary(mv_lens)
    for i in range(0, 943):
        for j in range(0, 1682):
            distance = {}
            if mv_lens[i][j] == 0.0:
                tot_rating = 0
                for user in movie_user_dict[j+1]:
                    distance[user] = (np.linalg.norm(mv_lens[user-1] - mv_lens[i]))  # Euclidean distance
                    distance[user] = (spatial.distance.cityblock(mv_lens[user-1] - mv_lens[i]))  # Manhattan distance
                sorted_distance = sorted(distance.items(), key=operator.itemgetter(1))
                if len(sorted_distance) > 10:
                    n = 20
                else:
                    n = len(sorted_distance)
                for user_distance_set in sorted_distance[:n]:
                    tot_rating += mv_lens[user_distance_set[0]-1][j]
                if n == 0:
                    predicted_rating = -1
                else:
                    predicted_rating = tot_rating/n
                mv_lens[i][j] = predicted_rating
    sys.stdout = open("final_output.txt", 'w')
    print(mv_lens)
    # in_file.close()

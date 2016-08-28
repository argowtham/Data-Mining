import pandas
import numpy
import operator

if __name__ == '__main__':
    mv_lens_data = pandas.read_table(open("u.data", 'r'))
    mv_lens_mod = pandas.DataFrame(data=list(set(mv_lens_data['user id'])), columns=['user id'])

    for item_id in range(1, 1683):
        mv_lens_mod[item_id] = 0
    for row in mv_lens_data.iterrows():
        mv_lens_mod[row[1][1]][row[1][0]] = row[1][2]
    # print(mv_lens_mod)

    for u_id in range(0, 943):
        for item_id in range(1, 1683):
            if mv_lens_mod.loc[u_id][item_id] == 0:
                user_list, distance, tot_rating = [], {}, 0
                for j in range(0, 943):
                    if not mv_lens_mod.loc[j][item_id] == 0:
                        user_list.append(mv_lens_mod.loc[j]['user id'])
                for user in user_list:
                    distance[user] = (numpy.linalg.norm(mv_lens_mod.loc[u_id] - mv_lens_mod.loc[user-1]))

                sorted_distance = sorted(distance.items(), key=operator.itemgetter(1))
                if len(sorted_distance) > 10:
                    for user in range(0, 10):
                        user_id = sorted_distance[user][0]
                        tot_rating += mv_lens_mod.loc[user_id-1][item_id]
                    predicted_rating = tot_rating // 10
                elif not len(sorted_distance) == 0:
                    for user in range(0, len(sorted_distance)):
                        user_id = sorted_distance[user][0]
                        tot_rating += mv_lens_mod.loc[user_id-1][item_id]
                    predicted_rating = tot_rating // len(sorted_distance)
                else:
                    predicted_rating = -1
                mv_lens_mod.loc[u_id][item_id] = predicted_rating
                # print(predicted_rating)
    out_file = open("out.txt", 'w')
    print(mv_lens_mod) >> out_file
    out_file.close()


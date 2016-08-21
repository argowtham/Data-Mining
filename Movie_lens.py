import pandas

if __name__ == '__main__':
    mv_lens_data = pandas.read_table(open("ml-100k/u.data", 'r'))
    # mv_user_data = pandas.read_csv("ml-100k/u.user", sep='|', header=None, index_col=0)
    # for i in range(0, len(mv_user_data)):
    #     print(mv_user_data.loc[i])
    for i in range(0, 1):
        row = mv_lens_data.loc[i]
        seen_movies, unseen_movies, compare_data = [row[1]], [], []
        for j in range(0, len(mv_lens_data)):
            if row[0] == mv_lens_data.loc[j][0]:
                seen_movies.append(mv_lens_data.loc[j][1])
        seen_movies = list(set(seen_movies))

        for k in range(1, 1683):
            if k not in seen_movies:
                unseen_movies.append(k)

        for l in range(0, len(mv_lens_data)):
            if unseen_movies[0] == mv_lens_data.loc[l][1]:
                compare_data.append(mv_lens_data.loc[l])
        compare_data = pandas.DataFrame(compare_data)

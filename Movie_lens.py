import pandas

if __name__ == '__main__':
    mv_lens_data = pandas.read_table(open("ml-100k/u.data", 'r'))
    i = 0
    for row in mv_lens_data.iterrows():
        print(row[1])
        i += 1
        if i > 10:
            break

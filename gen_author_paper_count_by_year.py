import pandas as pd
import cPickle as cpk
from collections import defaultdict


def preprocess(indata):
    data = []
    for i in range(len(indata)):
        data.append(indata[i].split("_"))
    return data


infile = "./data/papers.csv"
outfile = "./output/"
data = pd.read_csv(infile)
paper_author = data['author'].values
transactions = preprocess(paper_author)
name_dict = {}
for i in range(len(transactions)):
    for name in transactions[i]:
        if name not in name_dict.keys():
            name_dict[name] = defaultdict(lambda: 0)
        name_dict[name][data.iloc[i]['year']] += 1

with open(outfile + "author_year_paper_count.csv", "w") as sfh:
    sfh.write("author,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,total\n")
    for key in name_dict.keys():
        ss_arr = [key]
        total = 0
        for i in range(2007,2018):
            ss_arr.append(str(name_dict[key][i]))
            total += name_dict[key][i]
        ss_arr.append(str(total))
        ss = ",".join(ss_arr)
        sfh.write(ss + "\n")

import pandas as pd
import cPickle as cpk


def preprocess(indata):
    data = []
    for i in range(len(indata)):
        data.append(indata[i].split("_"))
    return data


min_sup = 5
conf_arr = ["IJCAI", "AAAI", "COLT", "CVPR", "NIPS", "KR", "SIGIR", "KDD"]
infile = "./data/papers.csv"
outfile = "./output/"
data = pd.read_csv(infile)

for conf in conf_arr:
    conf_paper_author = data[data['conference'] == conf]['author'].values
    transactions = preprocess(conf_paper_author)
    name_dict = {}
    with open(outfile + conf +"_author.cpk", "w") as sfh:
        for i in range(len(transactions)):
            for name in transactions[i]:
                if name not in name_dict.keys():
                    name_dict[name] = 0
                name_dict[name] += 1
        cpk.dump(name_dict, sfh)

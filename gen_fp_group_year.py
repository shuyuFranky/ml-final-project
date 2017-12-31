from fp_growth import find_frequent_itemsets as find_fp
import pandas as pd


def preprocess(indata):
    data = []
    for i in range(len(indata)):
        data.append(indata[i].split("_"))
    return data


min_sup = 5
conf_arr = ["IJCAI", "AAAI", "COLT", "CVPR", "NIPS", "KR", "SIGIR", "KDD"]
infile = "./data/papers.csv"
outfile = "./output_group_by_year/"
data = pd.read_csv(infile)

for conf in conf_arr:
    conf_paper = data[data['conference'] == conf]
    paper_year_authors = conf_paper[conf_paper['year'] >= 2012]['author'].values
    transactions = preprocess(paper_year_authors)
    with open(outfile + conf + "_msup_after_2012_" + str(min_sup), "w") as sfh:
        sfh.write(str(len(paper_year_authors)) + "\n")
        for itemset in find_fp(transactions, min_sup, include_support=True):
            if len(itemset[0]) < 3:
                continue
            names = ",".join(itemset[0])
            sfh.write(names + ", " + str(itemset[1]) + "\n")

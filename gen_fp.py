from fp_growth import find_frequent_itemsets as find_fp
import pandas as pd


min_sup = 5
conf_arr = ["IJCAI", "AAAI", "COLT", "CVPR", "NIPS", "KR", "SIGIR", "KDD"]
infile = "./data/papers.csv"
outfile = "./output_group_by_year/"
data = pd.read_csv(infile)


def preprocess(indata):
    data = []
    for i in range(len(indata)):
        data.append(indata[i].split("_"))
    return data


def pf_for_each_conf():
    for conf in conf_arr:
        conf_paper_author = data[data['conference'] == conf]['author'].values
        transactions = preprocess(conf_paper_author)
        with open(outfile + conf + "_msup_" + str(min_sup), "w") as sfh:
            sfh.write(str(len(conf_paper_author)) + "\n")
            for itemset in find_fp(transactions, min_sup, include_support=True):
                if len(itemset[0]) < 3:
                    continue
                names = ",".join(itemset[0])
                sfh.write(names + "," + str(itemset[1]) + "\n")


def pf_all_conf():
    paper_before = data[data['year'] < 2012]
    # paper_after = data[data['year'] > 2011]
    paper_author = paper_before['author'].values
    # paper_author = paper_after['author'].values
    transactions = preprocess(paper_author)
    with open(outfile + "all_msup_before_" + str(min_sup), "w") as sfh:
    # with open(outfile + "all_msup_after_" + str(min_sup), "w") as sfh:
        for itemset in find_fp(transactions, min_sup, include_support=True):
            if len(itemset[0]) < 3:
                continue
            names = ",".join(itemset[0])
            sfh.write(names + "," + str(itemset[1]) + "\n")


if __name__ == '__main__':
    # pf_for_each_conf()
    pf_all_conf()
    print ("Done!")

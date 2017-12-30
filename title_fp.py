import sys
import re
import pandas as pd
from gen_fp import preprocess
from fp_growth import find_frequent_itemsets as find_fp


paper_data = "./data/papers.csv"
data = pd.read_csv(paper_data)
authors = preprocess(data['author'].values)
title = data['title'].values
min_sup = 10

infile = "./output/all_msup_8"
if len(sys.argv) == 2:
    infile = sys.argv[1]
outfile = infile + "_title_fp"
outfile = infile + "_title_fp"


def fliter_stopwords(indata):
    stop_words = ["the", "of", "is", "and", "to", "in", "that", "we", "for", "an", "are", "by", "be", "as", "on", "with", "can", "if", "from", "which", "you", "it", "this", "then", "at", "have", "all", "not", "one", "has", "or", "that", "a", "two", "what", "via"]
    data = indata.split(" ")
    rdata = [p for p in data if p.lower() not in stop_words]
    return rdata


def gen_title_data_team():
    outfile = infile + "_title_fp_team"
    with open(infile, "r") as fh:
        with open(outfile, "w") as sfh:
            for ln in fh:
                ln = ln.strip()
                sfh.write("# " + ln + "\n")
                names = ln.split(",")[:-1]
                ss = []
                for i in range(len(authors)):
                    if set(names).issubset(set(authors[i])):
                        tdata = re.sub("[:\?\.\!\/_,$%^*(+)\"\']", "", title[i])
                        tfdata = fliter_stopwords(tdata)
                        ss.append(tfdata)
                for itemset in find_fp(ss, min_sup, include_support=True):
                    words = ",".join(itemset[0])
                    sfh.write(words + "," + str(itemset[1]) + "\n")


def gen_title_data_person():
    outfile = infile + "_title_fp_person"
    with open(infile, "r") as fh:
        with open(outfile, "w") as sfh:
            for ln in fh:
                ln = ln.strip()
                sfh.write("# " + ln + "\n")
                names = ln.split(",")[:-1]
                ss = []
                for i in range(len(authors)):
                    for name in names:
                        if name in authors[i]:
                            tdata = re.sub("[:\?\.\!\/_,$%^*(+)\"\']", "", title[i])
                            tfdata = fliter_stopwords(tdata)
                            ss.append(tfdata)
                for itemset in find_fp(ss, min_sup, include_support=True):
                    words = ",".join(itemset[0])
                    sfh.write(words + "," + str(itemset[1]) + "\n")


if __name__ == '__main__':
    # gen_title_data_team()
    gen_title_data_person()
    print ("Done!")

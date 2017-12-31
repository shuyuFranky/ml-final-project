import sys
import re
import pandas as pd
from gen_fp import preprocess


paper_data = "./data/papers.csv"
data = pd.read_csv(paper_data)
authors = preprocess(data['author'].values)
title = data['title'].values

infile = "./output/all_msup_8"
if len(sys.argv) == 2:
    infile = sys.argv[1]
# outfile = infile + "_title_data_team"
# outfile = infile + "_title_data_person"


def gen_title_data_team():
    outfile = infile + "_title_data_team"
    with open(infile, "r") as fh:
        with open(outfile, "w") as sfh:
            for ln in fh:
                ln = ln.strip()
                names = ln.split(",")[:-1]
                ss = []
                for i in range(len(authors)):
                    if set(names).issubset(set(authors[i])):
                        ss.append(title[i])
                title_data = " ".join(ss)
                # fliter punctuation
                tdata = re.sub("[:\?\.\!\/_,$%^*(+)\"\']", "", title_data)
                sfh.write(tdata + "\n")


def gen_title_data_person():
    outfile = infile + "_title_data_person"
    with open(infile, "r") as fh:
        with open(outfile, "w") as sfh:
            for ln in fh:
                ln = ln.strip()
                names = ln.split(",")[:-1]
                sfh.write(ln + "\n")
                ss = []
                for i in range(len(authors)):
                    for name in names:
                        if name in authors[i]:
                            ss.append(title[i])
                title_data = " ".join(ss)
                # fliter punctuation
                tdata = re.sub("[:\?\.\!\/_,$%^*(+)\"\']", "", title_data)
                sfh.write(tdata + "\n")


if __name__ == '__main__':
    # gen_title_data_team()
    gen_title_data_person()
    print ("Done!")

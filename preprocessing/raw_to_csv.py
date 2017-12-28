import re


def preprocess_lns(lns):
    conference_arr = ["IJCAI", "AAAI", "COLT", "CVPR", "NIPS", "KR", "SIGIR", "KDD"]
    author = []
    title = ''
    year = ''
    conference = ''
    for ln in lns:
        content = ln.split("\t")[1]
        if ln.startswith("author"):
            author.append(content)
        elif ln.startswith("title"):
            title = re.sub(",", "", content)
        elif ln.startswith("year"):
            year = content
        elif ln.startswith("Conference"):
            conference = content
        else:
            raise ValueError('The current ln %s is invalid.' % ln)
    if len(author):
        author = "_".join(author)
    else:
        return False, "Error Data"
    if title == '':
        return False, "Error Data"
    if year == '':
        return False, "Error Data"
    if conference == '' or conference not in conference_arr:
        return False, "Error Data"
    return True, author + ',' + title + ',' + year + ',' + conference


fname = "../rawdata/FilteredDBLP.txt"
savefile = "../data/papers.csv"

with open(fname, "r") as fh:
    with open(savefile, "w") as sfh:
        lns = []
        isFirstLn = True
        if isFirstLn:
            sfh.write("author,title,year,conference\n")
        for ln in fh:
            ln = ln.strip()
            if ln.startswith("#") and not isFirstLn:
                isadd, res = preprocess_lns(lns)
                if isadd:
                    sfh.write(res + "\n")
                res = ''
                lns = []
            else:
                if ln.startswith("#"):
                    continue
                lns.append(ln)
            isFirstLn = False

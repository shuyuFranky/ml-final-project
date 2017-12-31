fname = "./draw/author_paper.txt"

res = []
names = []
with open(fname, "r") as fh:
    cnt = 0
    for ln in fh:
        ln = ln.strip()
        info = ln.split(",")
        name = info[0]
        names.append(name)
        total = info[-1]
        data = info[1:-1]
        tcnt = 0
        for p in data:
            tmp_arr = [cnt, tcnt, int(p)]
            tcnt += 1
            res.append(tmp_arr)
        cnt += 1
print(res)
print(names)

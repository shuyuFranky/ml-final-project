import jieba.analyse

infile = "./output/all_msup_8_title_data_person"

with open(infile, "r") as fh:
    cnt = 0
    for ln in fh:
        cnt += 1
        print ("Group %d" % cnt)
        ln = ln.strip()
        kwords = jieba.analyse.extract_tags(ln, withWeight=True)
        for word, weight in kwords:
            print (word, weight)

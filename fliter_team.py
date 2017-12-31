
data_path = "./output/"
conf_arr = ["IJCAI", "AAAI", "COLT", "CVPR", "NIPS", "KR", "SIGIR", "KDD"]
config = {"IJCAI":4, "AAAI":5, "COLT":3, "CVPR":5, "NIPS":5, "KR":3, "SIGIR":5, "KDD":5}

data_path_year = "./output_group_by_year/"
config_before = {"IJCAI":3, "AAAI":3, "COLT":3, "CVPR":4, "NIPS":3, "KR":2, "SIGIR":3, "KDD":3}
config_after = {"IJCAI":4, "AAAI":5, "COLT":3, "CVPR":5, "NIPS":5, "KR":2, "SIGIR":5, "KDD":4}

for conf in conf_arr:
    # fname = data_path + conf + "_msup_" + str(config[conf])
    # fname = data_path_year + conf + "_msup_before_2012_" + str(config_before[conf])
    fname = data_path_year + conf + "_msup_after_2012_" + str(config_after[conf])
    sfh = open(fname + "_fliter", "w")
    with open(fname, "r") as fh:
        cnt  = 0
        start = "shuyu"
        cur_names = ["shuyu"]
        for ln in fh:
            cnt += 1
            if cnt == 1:
                continue
            names = ln.strip().split(",")[:-1]
            if names[0] in cur_names:
                # try merge
                if set(names).issubset(set(cur_names)):
                    continue
                else:
                    sfh.write(",".join(cur_names) + ",1\n")
                    cur_names = names
            else:
                sfh.write(",".join(cur_names) + ",1\n")
                cur_names = names
    sfh.close()

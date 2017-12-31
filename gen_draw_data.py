import json
import os
import cPickle as cpk


data_path = "./output/"
conf_arr = ["IJCAI", "AAAI", "COLT", "CVPR", "NIPS", "KR", "SIGIR", "KDD"]
config = {"IJCAI":4, "AAAI":5, "COLT":3, "CVPR":5, "NIPS":5, "KR":3, "SIGIR":5, "KDD":5}

data_path_year = "./output_group_by_year/"
config_before = {"IJCAI":3, "AAAI":3, "COLT":3, "CVPR":4, "NIPS":3, "KR":2, "SIGIR":3, "KDD":3}
config_after = {"IJCAI":4, "AAAI":5, "COLT":3, "CVPR":5, "NIPS":5, "KR":2, "SIGIR":5, "KDD":4}

def pre_name_paper(conf):
    fname = os.path.join("./output", conf + "_author.cpk")
    fh = open(fname, "r")
    data = cpk.load(fh)
    fh.close()
    return data


flare = {"name": "flare", "group": 0, "children": []}
data = []
cnt = 0
for conf in conf_arr:
    cnt += 1
    conf_data = {"name": conf, "group": cnt, "children": []}
    conf_children = []
    # fpath = os.path.join(data_path, conf + "_msup_" + str(config[conf]) + "_fliter")
    # fpath = os.path.join(data_path_year, conf + "_msup_before_2012_" + str(config_before[conf]) + "_fliter")
    fpath = os.path.join(data_path_year, conf + "_msup_after_2012_" + str(config_after[conf]) + "_fliter")
    name_paper_count = pre_name_paper(conf)
    with open(fpath, "r") as fh:
        tcnt = -1
        for ln in fh:
            tcnt += 1
            if tcnt == 0:
                continue
            ln = ln.strip()
            team_data = {"name": conf + "team_" + str(tcnt), "group": cnt, "children": []}
            team_children = []
            names = ln.split(",")[:-1]
            for name in names:
                p_data = {"name": name, "group": cnt, "size": name_paper_count[name] * 1007}
                team_children.append(p_data)
            team_data["children"] = team_children
            conf_children.append(team_data)
    conf_data["children"] = conf_children
    data.append(conf_data)
flare["children"] = data

ss = "var flare = " + json.dumps(flare) + ";"
with open("./draw/flareData_after.js", "w") as sfh:
    sfh.write(ss + "\n")
    sfh.write("module.exports = flare;\n")

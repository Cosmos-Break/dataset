# coding=utf-8
import json


def to_src_tgt_format(srcfile, tgtfile, outputfile):
    with open(srcfile, "r", encoding='utf-8') as src:
        src_list = src.readlines()
    with open(tgtfile, "r", encoding='utf-8') as tgt:
        tgt_list = tgt.readlines()
    assert len(src_list) == len(tgt_list)
    f = open(outputfile, "a+", encoding='utf-8')
    for i in range(len(src_list)):
        dic = {}
        dic["src"] = src_list[i][0:-1]
        dic["tgt"] = tgt_list[i][0:-1]
        js = json.dumps(dic, ensure_ascii=False)
        f.write(js + "\n")
    f.close()


to_src_tgt_format("data/task1/tok/train.lc.norm.tok.en", "data/task1/tok/train.lc.norm.tok.de",
                  "data/task1/src_tgt/train.en_de")
to_src_tgt_format("data/task1/tok/val.lc.norm.tok.en", "data/task1/tok/val.lc.norm.tok.de",
                  "data/task1/src_tgt/val.en_de")
to_src_tgt_format("data/task1/tok/test_2016_flickr.lc.norm.tok.en", "data/task1/tok/test_2016_flickr.lc.norm.tok.de",
                  "data/task1/src_tgt/test2016.en_de")

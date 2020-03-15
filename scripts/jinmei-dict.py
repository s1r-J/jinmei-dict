# coding:utf-8
# 人名辞書をjson形式に変換
import sys
import csv
import json
import re
from tqdm import tqdm
import chardet

def append_dict(row, jinmei_dict):
    yomi = row[11]
    kaki = row[0]
    if re.match(u'^[\u30a1-\u30fa\u30fcぁ-ん]+$', kaki) or re.match(u'^[a-zA-Z]+$', kaki):
        return
    if yomi in jinmei_dict:
        if kaki not in jinmei_dict[yomi]:
            jinmei_dict[yomi].append(kaki)
    else:
        jinmei_dict[yomi] = [kaki]

def detect_encoding(filename):
    with open(filename, 'rb') as rawdata:
        result = chardet.detect(rawdata.read(10000))
    print(f'{filename}: {result["encoding"]}')
    return result['encoding']

def count_vocabulary(jinmei_dict):
    kaki_count = len(jinmei_dict)
    yomi_count = 0
    for k in jinmei_dict.keys():
        yomi_count = yomi_count + len(jinmei_dict[k])
    return kaki_count, yomi_count

def main(filepaths):
    sei_dict = dict()
    mei_dict = dict()
    for filename in filepaths:
        with open(filename, mode='r', encoding=detect_encoding(filename)) as f:
            csv_file = csv.reader(f, delimiter=",")
            for row in tqdm(csv_file):
                if row[6] == '人名' and row[7] == '姓':
                    append_dict(row, sei_dict)
                elif row[6] == '人名' and row[7] == '名':
                    append_dict(row, mei_dict)

    seipath = './sei.json'
    with open(seipath, mode='w', encoding='utf_8') as s:
        s.write(json.dumps(sei_dict, ensure_ascii=False))
    sei_counts = count_vocabulary(sei_dict)
    print('姓の読み仮名数:', sei_counts[0], '姓の漢字候補数:', sei_counts[1])

    meipath = './mei.json'
    with open(meipath, mode='w', encoding='utf_8') as m:
        m.write(json.dumps(mei_dict, ensure_ascii=False))
    mei_counts = count_vocabulary(mei_dict)
    print('名の読み仮名数:', mei_counts[0], '名の漢字候補数:', mei_counts[1])

if __name__ == '__main__':
    args = sys.argv
    filepaths = args[1:]
    main(filepaths)

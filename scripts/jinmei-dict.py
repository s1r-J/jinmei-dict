# coding:utf-8
# 人名辞書をjson形式に変換
import sys
import csv
import json
import re
from tqdm import tqdm
import chardet
import itertools

def append_dict(row, jinmei_dict, itaiji):
    yomi = row[11]
    kaki = row[0]
    if re.match(u'^[\u30a1-\u30fa\u30fcぁ-ん]+$', kaki) or re.match(u'^[a-zA-Z]+$', kaki):
        return
    if yomi in jinmei_dict:
        for k in create_itaiji_name(kaki, itaiji):
            if k not in jinmei_dict[yomi]:
                jinmei_dict[yomi].append(k)
    else:
        jinmei_dict[yomi] = create_itaiji_name(kaki, itaiji)

def create_itaiji_name(kaki, itaiji):
    moji_list = []
    for k in kaki:
        l = [k]
        if k in itaiji:
            l.extend(itaiji[k])
        moji_list.append(l)
    kari_list = list(itertools.product(*moji_list))
    all_kaki = [kaki]
    for kari in kari_list:
        all_kaki.append(''.join(kari))
    return all_kaki

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
    with open('./itaiji.json', mode='r', encoding='utf_8') as f:
        itaiji = json.load(f)

    sei_dict = dict()
    mei_dict = dict()
    for filename in filepaths:
        with open(filename, mode='r', encoding=detect_encoding(filename)) as f:
            csv_file = csv.reader(f, delimiter=",")
            for row in tqdm(csv_file):
                if row[6] == '人名' and row[7] == '姓':
                    append_dict(row, sei_dict, itaiji)
                elif row[6] == '人名' and row[7] == '名':
                    append_dict(row, mei_dict, itaiji)

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

import sys
import os
import csv

key_dic = {}
bad_duplicates = []
bad_singles = []
good_duplicates = []
normal_singles = []

# add check if one hanzi has sevel keywords

with open('tradHanziToDe.tsv', mode='r', encoding='utf-8', newline='') as txt_file:
    reader = csv.reader(txt_file, delimiter='\t', quotechar='"')
    for line in reader:
        keyword = line[1].lower()
        if not keyword in key_dic:
            key_dic[keyword] = [line]
        else:
            key_dic[keyword].append(line)

def add(v, a_list):
    for item in v:
        a_list.append(item)

for k, v in key_dic.items():
    if len(v) == 1:
        if v[0][3] != '':
            add(v, bad_singles)
        else:
            add(v, normal_singles)
    else:
        bad = False
        for item in v:
            if item[3] == '' or item[4] == '':
                bad = True
        if bad:
            add(v, bad_duplicates)
        else:
            add(v, good_duplicates)

bad_good = (bad_singles +
           bad_duplicates +
           good_duplicates +
           normal_singles)
bad_duplicates.insert(0,('possible duplicate keywords or missing tags', '', '', '', ''))
bad_singles.insert(0, ('second keyword not necessary, no problem', '', '', '', ''))
print(str(len(bad_duplicates)) + ' possible problems...')

for l in (bad_good, bad_duplicates, bad_singles):
    l.sort(key=lambda i: i[1].lower())
problems = bad_duplicates + bad_singles

with open('possibleProblems.tsv', mode='w', encoding='utf-8', newline='') as txt_file:
    writer = csv.writer(txt_file, delimiter='\t', quotechar='"', lineterminator='\n')
    writer.writerows(problems)

with open('tradHanziToDe.tsv', mode='w', encoding='utf-8', newline='') as txt_file:
    writer = csv.writer(txt_file, delimiter='\t', quotechar='"', lineterminator='\n')
    writer.writerows(bad_good)

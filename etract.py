#coding=utf-8
import csv
import re

csv_lists = ['abroad.csv','china.csv']

def FullToHalf(s):
        n = []
        for char in s:
                num = ord(char)
                if num == 0x3000:
                        num = 32
                elif 0xFF01 <= num <= 0xFF5E:
                        num -= 0xfee0
                num = unichr(num)
                n.append(num)
        return ''.join(n)

def clean_seq(sentence):
    sentence = sentence.strip().decode('utf-8')
    sentence = FullToHalf(sentence)
    sentence = sentence.replace(' ','_')
    sentence = re.sub(ur"[^\u4e00-\u9fffA-Za-z0-9\-_\xb7]","",sentence)
    sentence = sentence.lower()
    return sentence

def write2file(file_name,list_):
	with open(file_name,'w') as w_f:
		w_f.write('\n'.join(list_).encode('utf-8'))

place = []
scenic = []
for file_item in csv_lists:
	for inx,item in enumerate(csv.reader(open(file_item))):
		if inx == 0:
			continue
		scenic_item = clean_seq(item[1].strip())
		place_item = clean_seq(item[2].strip())
		if u'\xb7' in scenic_item:
			scenic_item = scenic_item.replace(u'\xb7','')
		if u'\xb7' in place_item:
			place_item = place_item.split(u'\xb7')
		else:
			place_item = [place_item]
		for inx,item in enumerate(place_item):
			if (item.endswith(u'\u53bf') or item.endswith(u'\u5e02') or item.endswith(u'\u7701')) and len(item) > 2:
				item = item[:-1]
			place_item[inx] = item
		place = place + place_item
		scenic.append(scenic_item)

place = list(set(place))
scenic = list(set(scenic))

write2file('scenic_place.txt',place)
write2file('scenic_spot.txt',scenic)
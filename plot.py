import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json

# 알파벳 출현 빈도 데이터 읽어오기
with open('./data/freq.json', 'r', encoding='utf-8') as f:
    freq = json.load(f)

# 언어마다 계산하기
lang_dic = {}
for i, lbl in enumerate(freq[0]['labels']):
    fq = freq[0]['freqs'][i]
    if not (lbl in lang_dic):
        lang_dic[lbl] = fq
        continue
    for idx, v in enumerate(fq):
        lang_dic[lbl][idx] = (lang_dic[lbl][idx] + v) / 2

# pandas의 DataFrame에 데이터 넣기
asc_list = [[chr(n) for n in range(97, 97+26)]] # ['a', 'b', 'c', 'd', .... , 'x', 'y', 'z']
df = pd.DataFrame(lang_dic, index=asc_list)

# 그래프 그리기
plt.style.use('ggplot')
df.plot(kind='bar', subplots=True, ylim=(0, 0.15))
plt.show()


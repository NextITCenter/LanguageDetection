from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import re, json, glob, os


# 텍스트를 읽고 각 알파벳의 출현 빈도 조사하기
def check_freq(fname):
    name = os.path.basename(fname)
    lang = re.match(r'^[a-z]{2,}', name).group()
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    text = text.lower()
    # 숫자 변수(cnt) 초기화
    cnt = [0 for n in range(0, 26)]
    code_a = ord('a') # 97
    code_z = ord('z') # 97 + 26
    # 알파벳 출현 횟수 구하기
    for ch in text:
        n = ord(ch)
        if code_a <= n <= code_z: # a ~ z 사이에 있을 때
            cnt[n - code_a] += 1
    # 정규화하기
    total = sum(cnt)
    freq = list(map(lambda n: n / total, cnt))
    return freq, lang


# 각 파일 처리하기
def load_files(path):
    freqs = []
    labels = []
    file_list = glob.glob(path)
    for fname in file_list:
        freq, lang = check_freq(fname)
        freqs.append(freq)
        labels.append(lang)
    return {'freqs': freqs, 'labels': labels}


data = load_files('./data/train/*.txt')
test = load_files('./data/test/*.txt')

# 이후를 대비하기 위해 JSON으로 결과 저장하기
with open('./data/freq.json', 'w', encoding='utf-8') as f:
    json.dump([data, test], f)

# 학습하기
model = SVC()
model.fit(data['freqs'], data['labels'])

# 평가하기
predict = model.predict(test['freqs'])

# 결과 확인
ac_score = accuracy_score(test['labels'], predict)
cl_report = classification_report(test['labels'], predict)
print(f'정답률: {ac_score}')
print(f'리포트: {cl_report}')


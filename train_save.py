from sklearn import svm
import joblib
import json

with open('./data/freq.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
    data = d[0]

# 학습하기
model = svm.SVC()
model.fit(data['freqs'], data['labels'])

# 학습 데이터 저장하기
joblib.dump(model, './data/freq.pkl')
print('file is saved!!')
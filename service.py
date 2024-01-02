import joblib


def detect_language(text):
    # 알파벳 출현빈도 구하기
    text = text.lower()

    code_a, code_z = ord('a'), ord('z')
    cnt = [0 for i in range(26)]
    for c in text:
        n = ord(c) - code_a
        if 0 <= n < 26:
            cnt[n] += 1
    total = sum(cnt)
    if total == 0:
        return "입력이 없습니다."
    freq = list(map(lambda x: x / total, cnt))

    # 학습 데이터 읽어오기
    model = joblib.load('./data/freq.pkl')
    # 언어 예측하기
    result = model.predict([freq])

    lang_dic = {'en':'영어', 'fr': '프랑스어', 'id': '인도네시아어', 'tl': '타갈로그어'}
    return lang_dic[result[0]]

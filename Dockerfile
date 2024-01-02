FROM python:3.10
LABEL authors="nextit"

# 현재 디렉토리의 모든 파일들을 도커 컨테이너의 /root/LanguageDetection 디렉토리로 복사
# 자신이 원하는 디렉토리로 설정할 수도 있음
ADD . /root/LanguageDetection

# 작업 디렉토리로 이동
WORKDIR /root/LanguageDetection

# 작업 디렉토리에 있는 requirements.txt를 사용하여 패키지 설치
RUN pip3 install -r requirements.txt

# 8000번 포트 개방
EXPOSE 8000

ENTRYPOINT ["python3", "main.py"]
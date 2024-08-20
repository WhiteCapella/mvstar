import pandas as pd
import os
import requests
import json
import time
from tqdm import tqdm
# API_KEY 
key = os.getenv('MOVIE_API_KEY')

# URL
def gen_url(pg = 1):
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyList.json'
    url = f'{base_url}?key={key}&curPage={pg}'
    return url

# Load JSON
def req(pg = 1):
    url = gen_url(pg)
    res = requests.get(url)
    data = json.loads(res.text)
    return data

# SAVE_JSON
def save_movies(data, file_path):
    # 디렉토리 생성
    os.makedirs(os.path.dirname(file_path), exist_ok=True) # exist_ok : 폴더가 있으면 스킵, 없으면 생성
    with open(file_path, 'w', encoding = "utf-8") as f: # Json 형태로 저장
        json.dump(data, f, indent = 4, ensure_ascii=False)

# MAKE JSON
def cpjson(pg = 1, sleep_time = 1):
    file_path = '/home/whitecapella/data/movies/movie_company/data.json'
    if os.path.isfile(file_path):
        print(f"!!!데이터가 이미 존재합니다!!!: {file_path}")
        return True
    dic = req(pg) # 첫번째 10개 데이터 저장
    cpli = dic['companyListResult']['companyList']
    result = [] # 결과 저장될 곳
    # 첫페이지 저장
    result.extend(cpli)
    cnt = (dic['companyListResult']['totCnt'] // 10) + 1 # 몇번 돌아야 하는가
    # 첫번째는 저장했으니 두번째부터
    for i in tqdm(range(2,cnt+1)):
        time.sleep(sleep_time) # 쉬었다가~
        data = req(pg=i) # 2번째 페이지부터 쭉쭉
        cplist = data['companyListResult']['companyList'] # 영화 목록
        result.extend(cplist) # 이미 있던 곳에 extend로 추가
    save_movies(result, file_path)
    return True

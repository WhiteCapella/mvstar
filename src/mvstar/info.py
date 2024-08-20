import pandas as pd
import os
import requests
import json
import math
import time
from tqdm import tqdm
# API_KEY
key = os.getenv('MOVIE_API_KEY')
# URL
def gen_url(moviecd='20158561'):
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
    url = f'{base_url}?key={key}&movieCd={moviecd}'
    return url

# Load JSON
def req(moviecd='20158561'):
    url = gen_url(moviecd)
    res = requests.get(url)
    data = res.json()
    return data

# SAVE_JSON
def save_movies(data, file_path):
    # 디렉토리 생성
    os.makedirs(os.path.dirname(file_path), exist_ok=True) # exist_ok : 폴더가 있으면 스킵, 없으면 생성
    with open(file_path, 'w', encoding = "utf-8") as f: # Json 형태로 저장
        json.dump(data, f, indent = 4, ensure_ascii=False)

def read_data(dt = 2015, sleep_time = 1):
    file_path = f'/home/kimpass189/data/movies/movieinfo/year={dt}/data.json'
    read_path = f'/home/kimpass189/data/movies/year={dt}/data.json'
    # 파일이 있다면?
    if os.path.isfile(file_path):
        print(f"!!!데이터가 이미 존재합니다!!! : {file_path}")
        return True
    # 결과 저장 장소
    result = []
    # 파일 읽기
    with open(read_path, "r") as st_json:
        data_js = json.load(st_json)
    for dic in tqdm(data_js):
        time.sleep(sleep_time)
        mvcd = dic['movieCd']
        data = req(mvcd)
        ap_dt = data['movieInfoResult']['movieInfo']
        result.append(ap_dt)
    save_movies(data = result, file_path = file_path)
    return True

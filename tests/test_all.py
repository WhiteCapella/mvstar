from mvstar.main import mkjson
from mvstar.info import read_data
from mvstar.copylist import cpjson
from mvstar.dynamic import mkdynamic
import requests
import json

def test_json():
    print("==============영화목록==============")
#    for i in range(2015 ,2016):
#        r = mkjson(dt=i, sleep_time=0.1)
#        assert r
    r = mkjson(dt = 2015, sleep_time = 0.1)
    assert r
    print("================================")

def test_info():
    print("==============영화상세정보==============")
#    for i in range(2015 ,2016):
#        r = read_data(dt = i, sleep_time = 0.1)
#        assert r
    r = read_data(dt = 2015, sleep_time = 0.1)
    assert r
    print("================================")

def test_cplist():
    print("==============영화사목록==============")
    try:
        r = cpjson(pg = 1, sleep_time = 0.1)
        assert r
    except json.JSONDecodeError:
        print('알 수 없는 JsonDecodeError')
    except KeyError:
        print("이상한 key error")
    print("================================")
def test_dy():
    r = mkdynamic(sleep_time = 0.1)
    assert r

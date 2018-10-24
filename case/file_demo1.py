# _*_ coding:utf-8 _*_
import requests
import json

URL='https://api.github.com'

def build_url(endpoint):
    return  '/'.join([URL,endpoint])

def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_mesthod():
    response = requests.get(build_url('user/haotest'))
    print(better_output(response.text))


if __name__ == '__main__':
    request_mesthod()





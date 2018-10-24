import requests
import json


URL='https://api.github.com'

#构建一个url进行拼接
def build_url(endpoint):
    return '/'.join([URL,endpoint])

#把传过来的字符串转成json格式
def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_method():
    response=requests.get(build_url('users/haotest123'))
    # print(response.text)
    print('状态码：',response.status_code)

if __name__=='__main__':
    request_method()

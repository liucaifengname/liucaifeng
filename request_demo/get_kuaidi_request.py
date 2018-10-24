import requests
import json


URL='http://www.kuaidi100.com/'

#构建一个url进行拼接
def build_url(endpoint):
    return '/'.join([URL,endpoint])

#把传过来的字符串转成json格式
def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_method():
    response=requests.get(build_url('/query?type=jd&postid=80384626272&temp=0.21928820090364365'))
    print(better_output(response.text))
    print('状态码：',response.status_code)

if __name__=='__main__':
    request_method()

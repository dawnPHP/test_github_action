import re
import requests

#发出请求
url= 'https://www.163.com/'

respose=requests.get(url)
#print(respose.status_code)# 响应的状态码 200
#print(respose.content)  #返回字节信息
#print(respose.text)  #返回文本内容

# write to file
with open("zhihu/index.html",'w') as f:
    f.write(respose.text)

print("end")

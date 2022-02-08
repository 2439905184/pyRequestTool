from urllib import response
import requests
import json
#测试工具
domain = "";
def read_config():
    file = open("config.json")
    json_data = json.load(file)
    return json_data['domain']
    pass
#请用phpstudy把域名修改为student 端口:1234 方便大家测试
print("请选择是否使用config.json中的配置信息,  y/n")
use_config = input()
if use_config == "y":
    domain = read_config()
else:
    print("请输入临时域名参数如: http://test:1234/")
    domain = input()
print("是否启用附加参数, y/n")
enable_param = input()
if enable_param == "y":
    print("请输入附加参数。格式：@p 参数名 参数值 每个命令直接一个空格")
    print("输入完成输入 @finish   来结束设置")
    result_params = []
    while(True):
        param = input()
        if param != "@finish":
            split_param = param.split(" ")
            print(split_param)
            params = {}
            params['param'] = split_param[1]
            params['value'] = split_param[2]
            result_params.append(params)
        if param == "@finish":
            break
    params_data = {}
    print("每一个参数")
    for item in result_params:
        print(item)
        key   = item['param']#获取参数名 参数值
        value = item['value']
        #赋值最终参数
        params_data[key]   = item['value']
    print("附加参数为：")
    print(params_data)
    response = requests.post(domain,data=params_data)
    print("结果")
    print(response.text)
else:
    response = requests.post(domain)
    print(response.text)

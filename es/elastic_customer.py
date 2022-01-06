#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse


def customer_search(url):
    request = """
        {'kw':'苹果',}
    """
    request = urllib.parse.urlencode(request)
    request = request.encode()
    response = urllib.request.urlopen(url=url, data=request)
    data = response.read()
    print(data)



    # 发起POST请求之前，要处理POST请求携带的参数 流程:
    # 一、将POST请求封装到字典
    data = {
        # 将POST请求所有携带参数放到字典中
        'kw': '苹果',
    }

    # 二、使用parse模块中的urlencode(返回值类型是字符串类型)进行编码处理
    data = urllib.parse.urlencode(data)

    # 三、将步骤二的编码结果转换成byte类型
    data = data.encode()

    '''2. 发起POST请求:urlopen函数的data参数表示的就是经过处理之后的
    POST请求携带的参数
    '''
    response = urllib.request.urlopen(url=url, data=data)

    data = response.read()
    print(data)


if __name__ == '__main__':
    url = 'https://fanyi.baidu.com/sug'
    customer_search(url)

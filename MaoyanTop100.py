import requests
import re
import json
import time
from requests.exceptions import RequestException


# 抓取网页源码
def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(response.status_code)
            return response.text
        return None
    except RequestException:
        return None


# 正则提取
def parse_one_page(html):
    # compile()将正则字符串编译为正则表达式对象pattern
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        re.S)
    items = re.findall(pattern, html)
    # for item in items:
        # yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后开始
        # yield {
        #     'index': item[0],
        #     'image': item[1],
        #     'title': item[2],
        #     'actor': item[3].strip()[3:],
        #     'time': item[4].strip()[5:],
        #     'score': item[5] + item[6]
        # }
    print(items)


# 结果写入文件
def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        # 使用json库的dumps()方法实现字典的序列化，ensure——ascii指定为False可以保证输出结果为中文形式。
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    parse_one_page(html)
    # for循环遍历字典写入文件
    # for item in parse_one_page(html):
    #     print(item)
    #     write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)

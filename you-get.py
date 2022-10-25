import sys
from you_get import common as you_get

# 读取txt文本内容
data = []
for line in open("url.txt", "r"):  # 设置文件对象并读取每一行文件
    data = data + line.splitlines()

# for 循环数组下载视频
for url in data:
    print(url)
    directory = r'D:\1\monye'  # 设置下载目录
    sys.argv = ['you-get', '-o', directory, url,"-l"]  # sys传递参数执行下载，就像在命令行一样
    you_get.main()

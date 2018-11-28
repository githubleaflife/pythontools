# -*- coding: utf-8 -*-

'''
Created on 2018-11-28

@author: zhanglu
'''


import os
import sys

import math
import xlwt
from moviepy.editor import VideoFileClip





reload(sys)
sys.setdefaultencoding('utf8')

# 定义文件目录
file_dir = u"G:/视频目录/"

class FileCheck():
    def __init__(self):
        self.file_dir = file_dir

    def get_filesize(self, filename):
        u"""
        获取文件大小（M: 兆）
        """
        file_byte = os.path.getsize(filename)
        return self.sizeConvert(file_byte)

    def get_file_times(self, filename):
        u"""
        获取视频时长（s:秒）
        """
        clip = VideoFileClip(filename)
        file_time,money = self.timeConvert(clip.duration)

        return file_time,money

    def sizeConvert(self, size):  # 单位换算
        K, M, G = 1024, 1024 ** 2, 1024 ** 3
        if size >= G:
            return str(size / G) + 'G Bytes'
        elif size >= M:
            return str(size / M) + 'M Bytes'
        elif size >= K:
            return str(size / K) + 'K Bytes'
        else:
            return str(size) + 'Bytes'

    def timeConvert(self, size):  # 单位换算
        if size >0 and size <= 60*10:
            money = 100
        elif size <= 60*20:
            money = 200
        else:
            s = int(math.ceil((size-60*20)/60.0))
            money = 200+s*10


        M, H = 60, 60 ** 2
        if size < M:
            return str(size) + u'秒',money
        if size < H:
            return u'%s分钟%s秒' % (int(size / M), int(size % M)),money
        else:
            hour = int(size / H)
            mine = int(size % H / M)
            second = int(size % H % M)
            tim_srt = u'%s小时%s分钟%s秒' % (hour, mine, second)
            return tim_srt,money

    def get_all_file(self):
        u"""
        获取视频下所有的文件
        """
        for root, dirs, files in os.walk(file_dir):
            return files  # 当前路径下所有非目录子文件


print(u"=============开始,文件较多，请耐心等待...")
fc = FileCheck()
files = fc.get_all_file()
datas = [[u'文件名称', u'文件大小', u'视频时长',u'费用']]  # 二维数组
for f in files:

    cell = []
    file_path = os.path.join(file_dir, f)
    file_size = fc.get_filesize(file_path)
    file_times,money = fc.get_file_times(file_path.encode("gbk"))

    print(u"文件名字：{filename},大小：{filesize},时长：{filetimes},费用：{m}".format(filename=f, filesize=file_size, filetimes=file_times,m=money))
    cell.append(f)
    cell.append(file_size)
    cell.append(file_times)
    cell.append(money)
    datas.append(cell)

wb = xlwt.Workbook()  # 创建工作簿
sheet = wb.add_sheet('data')  # sheet的名称为test

# 单元格的格式
style = 'pattern: pattern solid, fore_colour yellow; '  # 背景颜色为黄色
style += 'font: bold on; '  # 粗体字
style += 'align: horz centre, vert center; '  # 居中
header_style = xlwt.easyxf(style)

row_count = len(datas)
col_count = len(datas[0])
for row in range(0, row_count):
    col_count = len(datas[row])
    for col in range(0, col_count):
        if row == 0:  # 设置表头单元格的格式
            sheet.write(row, col, datas[row][col], header_style)
        else:
            sheet.write(row, col, datas[row][col])

wb.save(file_dir + "video.xlsx")


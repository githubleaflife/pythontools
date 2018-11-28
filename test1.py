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

# �����ļ�Ŀ¼
file_dir = u"G:/��ƵĿ¼/"

class FileCheck():
    def __init__(self):
        self.file_dir = file_dir

    def get_filesize(self, filename):
        u"""
        ��ȡ�ļ���С��M: �ף�
        """
        file_byte = os.path.getsize(filename)
        return self.sizeConvert(file_byte)

    def get_file_times(self, filename):
        u"""
        ��ȡ��Ƶʱ����s:�룩
        """
        clip = VideoFileClip(filename)
        file_time,money = self.timeConvert(clip.duration)

        return file_time,money

    def sizeConvert(self, size):  # ��λ����
        K, M, G = 1024, 1024 ** 2, 1024 ** 3
        if size >= G:
            return str(size / G) + 'G Bytes'
        elif size >= M:
            return str(size / M) + 'M Bytes'
        elif size >= K:
            return str(size / K) + 'K Bytes'
        else:
            return str(size) + 'Bytes'

    def timeConvert(self, size):  # ��λ����
        if size >0 and size <= 60*10:
            money = 100
        elif size <= 60*20:
            money = 200
        else:
            s = int(math.ceil((size-60*20)/60.0))
            money = 200+s*10


        M, H = 60, 60 ** 2
        if size < M:
            return str(size) + u'��',money
        if size < H:
            return u'%s����%s��' % (int(size / M), int(size % M)),money
        else:
            hour = int(size / H)
            mine = int(size % H / M)
            second = int(size % H % M)
            tim_srt = u'%sСʱ%s����%s��' % (hour, mine, second)
            return tim_srt,money

    def get_all_file(self):
        u"""
        ��ȡ��Ƶ�����е��ļ�
        """
        for root, dirs, files in os.walk(file_dir):
            return files  # ��ǰ·�������з�Ŀ¼���ļ�


print(u"=============��ʼ,�ļ��϶࣬�����ĵȴ�...")
fc = FileCheck()
files = fc.get_all_file()
datas = [[u'�ļ�����', u'�ļ���С', u'��Ƶʱ��',u'����']]  # ��ά����
for f in files:

    cell = []
    file_path = os.path.join(file_dir, f)
    file_size = fc.get_filesize(file_path)
    file_times,money = fc.get_file_times(file_path.encode("gbk"))

    print(u"�ļ����֣�{filename},��С��{filesize},ʱ����{filetimes},���ã�{m}".format(filename=f, filesize=file_size, filetimes=file_times,m=money))
    cell.append(f)
    cell.append(file_size)
    cell.append(file_times)
    cell.append(money)
    datas.append(cell)

wb = xlwt.Workbook()  # ����������
sheet = wb.add_sheet('data')  # sheet������Ϊtest

# ��Ԫ��ĸ�ʽ
style = 'pattern: pattern solid, fore_colour yellow; '  # ������ɫΪ��ɫ
style += 'font: bold on; '  # ������
style += 'align: horz centre, vert center; '  # ����
header_style = xlwt.easyxf(style)

row_count = len(datas)
col_count = len(datas[0])
for row in range(0, row_count):
    col_count = len(datas[row])
    for col in range(0, col_count):
        if row == 0:  # ���ñ�ͷ��Ԫ��ĸ�ʽ
            sheet.write(row, col, datas[row][col], header_style)
        else:
            sheet.write(row, col, datas[row][col])

wb.save(file_dir + "video.xlsx")


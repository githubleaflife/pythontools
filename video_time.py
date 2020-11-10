import os
import sys
import re
import xlwt
import csv
from moviepy.editor import *
#from moviepy.editor import VideoFileClip
import openpyxl
 
file_dir = "/Users/lucy/Desktop/hello/" #定义文件目录
book_name_xlsx = '录制视频统计工作簿.xlsx'
sheet_name_xlsx = '录制视频统计表'
count = 0




 
class FileCheck():


    def __init__(self):
        self.file_dir = file_dir
 
    def get_filesize(self,filename):
        u"""
        获取文件大小（M: 兆）
        """
        file_byte = os.path.getsize(filename)
        return self.sizeConvert(file_byte)


    def get_counter(self,size):
        """记录总时长"""
        global count
        count += size
 
    def get_file_times(self,filename):
        u"""
        获取视频时长（s:秒）
        """
        clip = VideoFileClip(filename)
        self.get_counter(clip.duration)
        file_time = self.timeConvert(clip.duration)
        return file_time
 
    def sizeConvert(self,size):# 单位换算
        K, M, G = 1024, 1024**2, 1024**3
        if size >= G:
            a = str(size/G)
            a = str(int(a.split('.')[0]))
 
            return a +'G Bytes'
            #return str(size/G)+'G Bytes'
        elif size >= M:
            a = str(size/M)
            a = str((int(a.split('.')[0])+1))
 
            return a +'M Bytes'
        elif size >= K:
            return str(size/K)+'K Bytes'
        else:
            return str(size)+'Bytes'
 
    def timeConvert(self,size):# 单位换算
        print(size)

        M, H = 60, 60**2
        if size < M:
            return str(size)+u'秒'
        if size < H:
            return u'%s分钟%s秒'%(int(size/M),int(size%M))
        else:
            hour = int(size/H)
            mine = int(size%H/M)
            second = int(size%H%M)
            tim_srt = u'%s小时%s分钟%s秒'%(hour,mine,second)
            return tim_srt
 
    def get_all_file(self):
        u"""
        获取视频下所有的文件
        """

        ds = list(os.walk(file_dir))

        list_a = [["文件名", "时长"]]

        for root,dirs,files in ds:
            for file in files:
                file_path = '{}/{}'.format(root,file)

                if re.match('/Users/lucy/Desktop/hello/(.*?\.mp4)',file_path):
                    file_times = self.get_file_times(file_path)
                    list_a.append([file,file_times])
        print(list_a)


        #写入excel中
        # self.write_excel_xlsx(book_name_xlsx, sheet_name_xlsx, list_a)




    def write_excel_xlsx(self,path, sheet_name, value):
        index = len(value)
        workbook = openpyxl.Workbook()  # 新建工作簿（默认有一个sheet？）
        sheet = workbook.active  # 获得当前活跃的工作页，默认为第一个工作页
        sheet.title = sheet_name  # 给sheet页的title赋值
        for i in range(0, index):
            for j in range(0, len(value[i])):
                sheet.cell(row=i + 1, column=j + 1, value=str(value[i][j]))  # 行，列，值 这里是从1开始计数的
        workbook.save(path)  # 一定要保存
        print("xlsx格式表格写入数据成功！")
 
if __name__ == '__main__':

    obj = FileCheck()
    obj.get_all_file()
    print(obj.timeConvert(count))

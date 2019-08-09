# -*- coding: utf-8 -*-
"""
time :  2019-08-08
author: luqian
"""
import sys
import csv


def dic_sec(file1):
    """
    :param file1:
    :return: 字典dd,存储二级类目名称
    """
    #file1 = "C:/Users/dell/Desktop/sec_idname.csv"
    file = open(file1, "r", encoding="utf-8")
    dd = {}
    while True:
        line = file.readline()
        if not line:
            break
        try:
            # print(line)
            line = line.strip()
            parts = line.split(",")
            # print(parts)
            # print(len(parts))
            if len(parts) < 2:
                continue
            # print(parts[1])
            if parts[0] not in dd:
                dd[int(parts[0])] = parts[1]
                # print(dd)
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()  ##sys.exc_info自己捕获异常详细信息
            sys.stderr.write("line:%s\n" % str(exc_traceback.tb_lineno))
            sys.stderr.write("%s\n" % str(e))
            sys.stderr.write("%s\n" % line)
    return dd

def product_data(filer,filew, dd, fileless):
    key_list = list(dd.keys())
    file = open(filer, "r", encoding="utf-8")
    filew=open(filew, "w", encoding="gbk")
    fileless = open(fileless, "w", encoding="gbk")
    count=0
    while True:
        line = file.readline()
        if not line:
            break
        try:
            #print(line)
            line = line.strip()
            parts = line.split("\t")
            # if len(parts) < 8:
            #     continue
            if len(parts) < 8:
                fileless.write(line + '\n')
            count = count + 1
            idname_text_int = int(parts[6].split(':')[0])
            # print(type(idname_text_int))
            # print(idname_text_int)

            if idname_text_int in key_list:
                idname_text = str(idname_text_int)
                # print(type(idname_text))
                # print(idname_text)
                idname_text = idname_text + dd[idname_text_int]
                # print(22)
                # print(idname_text)
                idname_text = idname_text+'||,'+parts[0]
                print(idname_text)
                filew.write(idname_text + '\n')

            print(count)  #数据总数

        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()  ##sys.exc_info自己捕获异常详细信息
            sys.stderr.write("line:%s\n" % str(exc_traceback.tb_lineno))
            sys.stderr.write("%s\n" % str(e))
            sys.stderr.write("%s\n" % line)


if __name__ == '__main__':
    file1 = "C:/Users/dell/Desktop/sec_idname.csv"
    dd = dic_sec(file1)   #返回字典，键为二级id，值为二级name
    #print(dd)

    res = "C:/Users/dell/Desktop/result"
    test = "E:/mia_cate_classification/click_score_file"
    res_less = "C:/Users/dell/Desktop/res_less"
    product_data(test, res, dd, res_less)  #生成CNN模型所需要的数据
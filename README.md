# -Intern-mia_click_newfile
#2019-08-09     测试蜜芽的用户点击数据所召回的商品类目的准确度。
# 数据说明:
click_score_file: 用户点击数据， 第一列为query，倒数第二列 冒号前面的为二级类目id。
# 流程说明：
1.首先用sql语句从蜜芽数据库中提取二级类目id及name，导出文件到 sec_idname.txt
2.然后根据文件sec_idname.txt去匹配click_score_file中二级类目id所对应的name，生成整个数据集result.csv 。见 new_click.py。
3.将数据集result.csv 划分成训练集、验证集、测试集，带入CNN模型进行训练，观测误差。

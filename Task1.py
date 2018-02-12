"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records.""""
list_1 = []#短信，电话号码收集
for each_num in texts:
    a = list_1.append(each_num[0])
    b = list_1.append(each_num[1])
for each_num in calls:
    a = list_1.append(each_num[0])
    b = list_1.append(each_num[1])
list_2 = set(list_1)#去重
n=len(list_2)
print("There are %s different telephone numbers in the records." % (n))
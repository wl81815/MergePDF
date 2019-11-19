# -*- coding:utf-8 -*-
# author:WL
# place:RZ
# time:2019-11-19

import PyPDF2, os
path = r'D:\公司\1111'
pdfFiles = []
#遍历文件夹下所有pdf文件，存储在列表中，并按小写字母升序进行排列
for filename in os.listdir(path):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWrite = PyPDF2.PdfFileWriter() # 创建pdfWrite对象

#遍历pdf列表，创建pdfFileObj打开pdf文件，创建pdfReader对象读取pdf，pageObj对象获取每一页pdf,写入pdfWrite对象
for file in pdfFiles:
    filename = os.path.join(path,file)
    pdfFileObj = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(0,pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWrite.addPage(pageObj)
#新建一个PdfOutput 以wb方式打开，写入pdfWrite，关闭pdf
pdfOutput = open('allminutes.pdf','wb')
pdfWrite.write(pdfOutput)
pdfOutput.close()

print('Done!')
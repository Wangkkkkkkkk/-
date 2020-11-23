from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from tkinter import filedialog, dialog
import os
from io import StringIO
from io import open
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from googletrans import Translator

Easter_eggs = 0
char_data = ''
trans_data = ''

def fileopen():
    file_YuD = askopenfilename()
    if file_YuD:
        v1.set(file_YuD)

def match():
    global Easter_eggs
    global char_data
    global trans_data
    translator = Translator(service_urls=['translate.google.cn'])
    if (not v1.get() and Easter_eggs <10):
        text1.delete(0.0, END)
        text2.delete(0.0, END)
        text1.insert(INSERT, "Please select a PDF file!")
        Easter_eggs += 1
    elif( Easter_eggs == 10):
        text1.delete(0.0, END)
        text2.delete(0.0, END)
        text1.insert(INSERT, "恭喜你发现彩蛋！")
        text1.insert(INSERT, "\n")
        text1.insert(INSERT, "***     ***      *     *            *                *")
        text1.insert(INSERT, "\n")
        text1.insert(INSERT, " *      *                *  *         *           *         *")
        text1.insert(INSERT, "\n")
        text1.insert(INSERT, " *    *            *     *   *        *        *              *")
        text1.insert(INSERT, "\n")
        text1.insert(INSERT, " *  *              *     *     *      *       *                ")
        text1.insert(INSERT, "\n")
        text1.insert(INSERT, " *    *            *     *       *    *        *         * * *")
        text1.insert(INSERT, "\n")
        text1.insert(INSERT, " *       *         *     *         *  *           *          *")
        text1.insert(INSERT, "\n")
        text1.insert(INSERT, "***      ***     *     *            *                 *")
        text1.insert(INSERT, "\n")
        text1.insert(INSERT, "制作者：王凯")
        text1.insert(INSERT, "\n")
        text1.insert(INSERT, "制作时间：2020/8/26")
        text1.insert(INSERT, "\n")
        Easter_eggs = 0
    else:
        text1.delete(0.0, END)
        text2.delete(0.0, END)
        pdf = open(v1.get(), "rb")
        # resource manager
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        laparams = LAParams()
        # device
        device = TextConverter(rsrcmgr, retstr, laparams=laparams)
        process_pdf(rsrcmgr, device, pdf)
        device.close()
        content = retstr.getvalue()
        retstr.close()
        # 获取所有行
        lines = str(content).split("\n")
        text1.insert(INSERT, '    ')
        for ip in lines:
            # 去除无用字符
            str_num = 0
            lenth = len(ip) - 1
            for each in ip:
                if (each.isalpha()):
                    str_num += 1
            if (str_num == 1 or str_num == 0):
                pass
            elif (ip[lenth] != '.'):
                char_data = '{} {}'.format(char_data, ip)
                text1.insert(INSERT, ip)
            else:
                char_data = '{} {}'.format(char_data, ip)
                trans_data = translator.translate(char_data, src='en', dest='zh-CN').text
                text2.insert(INSERT, '        ')
                text2.insert(INSERT, trans_data)
                text2.insert(INSERT, '\n')
                char_data = ''
                text1.insert(INSERT, ip)
                text1.insert(INSERT, '\n')
                text1.insert(INSERT, '    ')

'''
def fileopen_1():
    file_YuD = askopenfilename()
    if file_YuD:
        v2.set(file_YuD)
'''

frameT = Tk()

frameT.geometry('500x500+400+100')
frameT.resizable(width=False, height=False)
frameT.title('Please select the PDF to be translated:')
v1 = StringVar()

file_path = ''
file_text = ''

 # 设置部件参数
frame = Frame(frameT)
frame.pack(padx=10, pady=10)  # 设置外边距

frame1 = Frame(frameT)
frame1.pack(padx=5, pady=5)

frame2 = Frame(frameT)
frame2.pack(padx=5, pady=5)

frame3 = Frame(frameT)
frame3.pack(padx=5, pady=5)

# 加入载入文件框
v1 = StringVar()
ent = Entry(frame, width=50, textvariable=v1).pack(fill=X, side=LEFT)  # x方向填充,靠左

text1 = Text(frame2, width=50, height=10, bg='white', font=('Arial', 12))
text1.pack(side=LEFT)

scrollbar1 = Scrollbar(frame2)
scrollbar1.pack(side=RIGHT, fill=Y)
text1.config(yscrollcommand=scrollbar1.set)
scrollbar1.config(command=text1.yview)

text2 = Text(frame3, width=50, height=10, bg='white', font=('Arial', 12))
text2.pack(side=LEFT)

scrollbar2 = Scrollbar(frame3)
scrollbar2.pack(side=RIGHT, fill=Y)
text1.config(yscrollcommand=scrollbar2.set)
scrollbar2.config(command=text2.yview)

# v2 = StringVar()
# ent = Entry(frame_1, width=50, textvariable=v2).pack(fill=X, side=LEFT)  # x方向填充,靠左

btn = Button(frame, width=20, text='open file', font=("宋体", 14), command=fileopen).pack(fill=X, padx=10)
# btn_1 = Button(frame_1, width=20, text='匹配文件', font=("宋体", 14), command=fileopen_1).pack(fil=X, padx=10)
ext = Button(frame1, width=10, text='run', font=("宋体", 14), command=match).pack(fill=X, side=LEFT)
etb = Button(frame1, width=10, text='quit', font=("宋体", 14), command=frameT.quit).pack(fill=Y, padx=10)

frameT.mainloop()

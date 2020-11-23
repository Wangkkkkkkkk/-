from io import StringIO
from io import open
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf

import GUI
import Get_picture

def read_pdf(pdf):
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
    return lines

if __name__ == '__main__':
    '''
    # 显示pdf列表
    with open('1.pdf', "rb") as my_pdf:
        Lists = read_pdf(my_pdf)
        print(Lists)

'''
    my_pdf = open('1.pdf', "rb")
    Lists = read_pdf(my_pdf)

    # 写入txt
    ipTable = Lists
    fileObject = open('4.txt', 'a', encoding='utf-8')
    for ip in ipTable:
        # 去除无用字符
        str_num = 0
        lenth = len(ip) - 1
        for each in ip:
            if( each.isalpha() ):
                str_num += 1
        if( str_num == 1 or str_num == 0):
            pass
        elif( ip[lenth] != '.'):
            fileObject.write(str(ip))
        else:
            fileObject.write(str(ip))
            fileObject.write('\n')

    GUI.Create_GUI( my_pdf )


    fileObject.close()

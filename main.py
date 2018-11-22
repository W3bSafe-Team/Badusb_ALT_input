#coding: utf-8
print "BadUSB ALT输入转换工具 By:W3bSafe Angel"


def convert(text):
    print "\033[0;32m [+]Source: \033[0m" + text
    ToGBK = text.encode('gb2312')
    ToHEX = ToGBK.encode('hex')
    print str("\033[0;36m [+]HEX: \033[0m") + ToHEX
    ToDEC = int(ToHEX,16)
    print str("\033[1;35m [+]DEC: \033[0m ") + str(ToDEC) + "\n"
    return ToDEC


if __name__ == '__main__':
   list=[]
   text=raw_input("请输入要转换的汉字：")
   for i in unicode(text, 'utf-8'):
       answer=convert(i)
       list.append(answer)

   print "转换后的结果："

   for j in list:
print str(j),

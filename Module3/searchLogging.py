import logging
import re
class Filelog:
    def __init__(self):
        logging.basicConfig(filename="filelog2.txt",level=logging.INFO)
    def search_log(self,filename):
        file=open("filelog2.txt","r")
        # str="zzz.txt"
        # data=re.compile(str)
        # res=data.search(str)
        # line=file.readline()
        # print(res)
    # def operation(self):
    #     try:
    #         self.x=int(input("num1"))
    #         self.y=int(input("num2"))
    #         print(self.x/self.y)
    #     except ZeroDivisionError as msg:
    #         logging.exception(msg)
    #     except ValueError as msg:
    #         logging.exception(msg)
# if _name=='main_':
#     obj=Filelog()
#     obj.operatio()
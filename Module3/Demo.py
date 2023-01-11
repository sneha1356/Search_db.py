from Exception_Class import File
import win32api
# class Example:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def cal(self):
#         try:
#             if(self.b<=0):
#                 raise File("error")
#             else:
#                 c=self.a//self.b
#         except File as f:
#             print(f)
# ex=Example(2,0)
# ex.cal()
def locate_Alldrives():
    d = win32api.GetLogicalDriveStrings()
    #d = d.split('\000')[:-1]
    print(d)

locate_Alldrives()
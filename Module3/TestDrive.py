import pytest
from searchfile import SearchFile
from locatedrives import SearchEngine
from Search_db import SearchDB
class Test_Search:
    def testdrive(self):
        obj=SearchEngine()
        result=obj.locate_Activedrives()
        self.expected=['C']
        if result==self.expected:
            assert True
        else:
            assert False
    def test_searchfile(self):
        obj=SearchFile("C","zzz.txt")
        result=obj.search_file1()
        if result[0]=='C:\Hcl_folder\zzz.txt':
            assert True
        else:
            assert False
    def test_serachindb(self):
        obj=SearchDB()
        re=obj.searchDB('zzz.txt')
        assert re==1
    def test_insertindb(self):
        obj=SearchDB()
        re=obj.insertDB('C:\Hcl_folder\sneha1.txt')
        assert re=="added successfully"
    def test_updateindb(self):
        obj=SearchDB()
        re=obj.updateDb('C:\Hcl_folder\sneha1.txt')
        assert re=="updated"
    def test_deleteindb(self):
        obj=SearchDB()
        re=obj.deleteDb(3)
        assert re=="record deleted"



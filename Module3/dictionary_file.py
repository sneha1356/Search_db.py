import os,string
from searchfile import SearchFile
from threading import Thread
class SearchManager:
    def search(self):
        s_threads=[]
        f_searchers=[]
        f_search=SearchFile("c://","hcl_program3.txt")
        f_search.search_file1()
        s_thread=Thread()
        s_thread.start(f_search)
        f_searchers.append(f_search)
        s_threads.append(s_thread)
        for searcher in s_threads:
                searcher.join()
        search_results=[]
        for f_searcher in f_searchers:
            search_results.append(f_searcher.file_paths)
        print(search_results)
if __name__=='__main__':

    s_m=SearchManager()
    s_m.search()
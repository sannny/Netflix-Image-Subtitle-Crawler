import os
from creds import *

class renaming:

    def __init__(self):
        self.os = os

    def switch_to_ss_dir(self):
        self.os.chdir(ss_dir_path)

    def list_all_files(self):
        return self.os.listdir()

    def rename(self, oldname, newname):
        on = ''.join([ss_dir_path,'\\',oldname])
        nn = ''.join([ss_dir_path,'\\',newname,'.png'])
        self.os.rename(on,nn)
    
    def clean_dir(self):
        self.switch_to_ss_dir()
        files = self.list_all_files()
        for file in files:
            on = ''.join([ss_dir_path,'\\',file])
            self.os.remove(on)

    def filtering_for_required_pic(self, newname):
        files = self.list_all_files()
        for file in files:
            if 'Screenshot' in file:
                self.rename(file,newname)
    
    def __main__(self,newname):
        self.switch_to_ss_dir()
        self.filtering_for_required_pic(newname.getNewName())
    


        








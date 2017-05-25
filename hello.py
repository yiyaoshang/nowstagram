# -*- encoding=utf-8 -*-
import os
def rename():
    path='H://nowstagram/nowstagram/static/touxiang'
    filelist=os.listdir(path)
    for i,files in enumerate(filelist):
        Olddir=os.path.join(path,files)
        filename=os.path.splitext(files)[0]
        filetype=os.path.splitext(files)[1]
        Newdir=os.path.join(path,str(i)+filetype)
        os.rename(Olddir,Newdir)
rename()
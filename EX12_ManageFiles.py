import os
import shutil
dir2='C:/Users/Yasser B/Desktop/txt Files/'  
dir_1='C:/Users/Yasser B/Dropbox/Python tutorials/'
fileformat='.py'
formatfile=len(fileformat)
for files in os.listdir(dir_1):
    try:
        dir1=dir_1+files+'/'
        for f in os.listdir(dir1):
            if f[-formatfile:]==fileformat:
                shutil.copy2(dir1+f, dir2+f)
    except:
        pass

# for files in os.listdir(dir1): 
#     if files[-4:]=='.txt':
#         shutil.copy2(dir1+files, dir2+files) 
#         # shutil.move(dir1+files, dir2+files)  
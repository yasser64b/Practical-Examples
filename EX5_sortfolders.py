import os 
Directory=input('Directory to be read=')
os.chdir(Directory)
DirectoryFiles=os.listdir(Directory)


for i in range (len(DirectoryFiles)):
    try:
        os.renames(DirectoryFiles[i],str(i)+'-' + DirectoryFiles[i])
    except:
        pass
        print('Please change manually', DirectoryFiles[i])


import os 
directory='C:/Users/Yasser Bigdeli/Dropbox/Python tutorials/05-Rename and sort folders/1'
os.chdir(directory)
filesDir=os.listdir(directory)
for i in range (len(directory)):
    os.rename(filesDir[i], str(i)+'-Test') 
Simple one , make folders inside folders

import os 
path= 'C:/Users/Yasser B/Dropbox/Python tutorials/02-creat folders'
os.chdir(path)
for i in range (1,11):
    Newfolder='Tutorial-'+str(i)
    os.makedirs(Newfolder)
    



import os 
path='C:/Users/Yasser B/Dropbox/Python tutorials/02-creat folders/Tutorial' # Directory to make folders inside
os.chdir(path) # make it current directory
# How to make 10 new folders in a directory 
for i in range(1,11):
    os.chdir(path) # make it current directory
    NewFolder= 'Tutorial-' +str(i)
    os.makedirs(NewFolder)
    # to make folders inside the other folders  
    path2=path +'/'+ NewFolder
    os.chdir(path2)
    for j in range (1,3):
        Newfolder1='Test'+ str(j)
        os.makedirs(Newfolder1)


function of making folders 
import os
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        

# # Example
# createFolder('C:/Users/Yasser B/Dropbox/Python tutorials/02-creat folders/AAA')
# # Creates a folder in the current directory called data

# help(os)
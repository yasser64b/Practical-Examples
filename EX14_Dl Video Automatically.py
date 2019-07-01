import os
from urllib import request # pip install urllib  : See my video for pip install (Example 1)

def download_file_information(url):
    fileOpen=request.urlopen(url)
    file_info=fileOpen.read()
    file_info_str=str(file_info)
    file_lines=file_info_str.split('\\n')
    newfile=open('file.txt','w')
    for info in file_lines:
        newfile.write(info +'\n')
    newfile.close()
    start='"'
    end='"'
    for i in file_lines:
        if '.mp4' in i:
            Vurl=(i.split(start))[1].split(end)[0]
    return Vurl 

for i in range (194526, 194531+1):
    file_url=r'https://video.varzesh3.com/video/'+str(i)
    try: 
        Vurl=download_file_information(file_url)
        url=Vurl
        # print('Video-'+str(i) +'=', file_url)
        name = 'Video-'+str(i)
        full_name = name + ".MP4" 
        request.urlretrieve(url, full_name)
    except:
        pass


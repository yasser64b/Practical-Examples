import os 
import urllib.request # pip install urllib  # Example 1 

# url ='http://img.kiosko.net/2019/06/26/us/latimes.750.jpg'
# url='http://img.kiosko.net/2019/06/26/us/sf_chronicle.750.jpg'

news=['latimes', 'sf_chronicle']
days=['20', '21', '22', '23', '24']

for newspaper in news: 
    for day in days:
        name=newspaper + day +'.jpg'
        url='http://img.kiosko.net/2019/06/' + day + '/us/'+ newspaper+'.750.jpg'
        urllib.request.urlretrieve(url, name)
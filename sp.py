import os

listdir = os.listdir('audio')

f = open('listdata.txt', 'a')
i = 0
for file in listdir:
    name = file.split('-')[0].strip()
    # 1.jpg,mp3_1.mp3,Sao anh chưa về,Thanh Hà    
    text = str(i) +'.jpg|'+file+'|'+name+'|Thanh Hà\n'
    print(text)
    f.write(text)
    i = i+1
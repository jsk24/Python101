# ชื่อโปรแกรม writefile.py
# homework ep4

import csv
#import มักจะไว้ด้านบน

def writedata ():
    with open('data.txt','w', encoding='utf-8') as file:
          file.write('สบายดีไหม?')
# แบบข้างบนนี้เปลี่ยนข้อมูลไม่ได้
          

def adddata(text):
    with open('add-data.txt','a',encoding='utf-8') as file:
        file.writelines(text+'\n')

def readdata ():
    with open ('add-data.txt',encoding='utf-8') as file:
        data = file.readlines() # export to list
        print(data)

#file.readlines ข้อมูลจะรวมอยู่ในบรรทัดเดียวกันหมด
#file.read ข้อมูลแยกทีละบรรทัด ต่อให้มี \n ก็ไม่ขึ้นบรรทัดใหม่
    
readdata ()  
#adddata('น้ำมันมวย 25 บาท')
#adddata('ผ้าเช็ดหน้า 376 บาท')
#adddata('กระสอบ 7 บาท')
#adddata('ผ้าดิบ 94 บาท')

#box คือการเก็บข้อมูลในตัวแปร



Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

====== RESTART: /Users/manop/Documents/Python 101 by ลุงวิศว/write file.py =====
['น้ำเต้าหู้ป้าเล็กปากซอย 8 บาทลูกอม 12 บาทลูกอม 12 บาทปลาทู 25 บาทปลาทู 25 บาทปลาทู 25 บาท\n', 'น้ำมันมวย 25 บาท\n', 'น้ำมันมวย 25 บาท\n', 'ผ้าเช็ดหน้า 376 บาท\n', 'กระสอบ 7 บาท\n', 'ผ้าดิบ 94 บาท\n']

box = []
box.append ('น้ำมันมวย')
box.append ('ผ้าเช็ดหน้า')
box.append ('กระสอบ')
box.append ('ผ้าดิบ')
print(box)
['น้ำมันมวย', 'ผ้าเช็ดหน้า', 'กระสอบ', 'ผ้าดิบ']
print(box[2])
กระสอบ
print(box[0])
น้ำมันมวย
print(box(3)]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
print(box[3])
ผ้าดิบ
print(box[-2])
กระสอบ
brand={'Pen':['Lamy','Pental','Fiber-Castel']'pencil':['Hourse','Steadler'],'Eraser':['Thai Eraser'}
       
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
       
SyntaxError: invalid syntax
brand={'Pen':['Lamy','Pental','Fiber-Castel']'pencil':['Hourse','Steadler'],'Eraser':['Thai Eraser']}
       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
brand={'Pen':['Lamy','Pental','Fiber-Castel']'pencil':['Hourse','Steadler'],'Eraser':['Thai-Eraser']}
       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
brand = {'pen':['Lamy','Pentel','Fiber-Castel'], 'pencil':['hourse','steadler'], 'eraser':'thai-two-tone'}
       
print(brand['pen'])
       
['Lamy', 'Pentel', 'Fiber-Castel']

print(brand['pen'][1])
       
Pentel
print(brand['pencil'][0])
       
hourse
print(brand[eraser][0])
       
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(brand[eraser][0])
NameError: name 'eraser' is not defined
print(brand[eraser][0])
       
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(brand[eraser][0])
NameError: name 'eraser' is not defined
print(brand['eraser'])
       
thai-two-tone
print(len(box))
       
4
print(brand.keys())
       
dict_keys(['pen', 'pencil', 'eraser'])
dict_keys(['pen', 'pencil', 'eraser'])
       
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dict_keys(['pen', 'pencil', 'eraser'])
NameError: name 'dict_keys' is not defined
print(brand.values())
       
dict_values([['Lamy', 'Pentel', 'Fiber-Castel'], ['hourse', 'steadler'], 'thai-two-tone'])
for b in box:
       print(b)

       
น้ำมันมวย
ผ้าเช็ดหน้า
กระสอบ
ผ้าดิบ
for br in brand.keys():
       print(br)

       
pen
pencil
eraser
for br in brand::
       
SyntaxError: incomplete input
>>> for br in brand:
...        print(br)
... 
...        
pen
pencil
eraser
>>> for br in brand.items():
...        print(br)
... 
...        
('pen', ['Lamy', 'Pentel', 'Fiber-Castel'])
('pencil', ['hourse', 'steadler'])
('eraser', 'thai-two-tone')
>>> len(brand)
...        
3

from tkinter import *
from tkinter import ttk #Theme of tk
from tkinter import messagebox


GUI = Tk()
GUI.title('วันนี้กินอะไรดี')
GUI.geometry('400x600')

import random
import tkinter as tk


# รายการอาหาร
food_list = ["ส้มตำ", "ข้าวผัดหมู", "ผัดไทย", "ก๋วยเตี๋ยวต้มยำ", "ข้าวมันไก่", "คะน้าหมูกรอบ", "บะหมี่หมูแดง", "กะเพราหมูสับ", "ยำวุ้นเส้น"]

# ฟังก์ชันสุ่มอาหาร
def choose_food():
    chosen_food = random.choice(food_list)
    result_label.config(text=chosen_food)



# สร้างปุ่มสุ่ม
choose_button = tk.Button(text="สุ่ม", command=choose_food, width=10, height=2)
choose_button.pack()


# สร้างป้ายแสดงผล
result_label = tk.Label(text="")
result_label.pack()

# เริ่มลูป GUI
GUI.mainloop()


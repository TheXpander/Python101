from tkinter import *
from tkinter import ttk #theme of Tk
from tkinter import messagebox
import tkinter.messagebox

GUI = Tk()
GUI.title('ตารางงาน')#ชื่อโปรแกรม
GUI.geometry('1050x300')#ขนาดหน้าจอโปรแกรม
GUI.config(bg='White')#สีพื้นหลัง
L1=Label(GUI,text='ตารางงาน',font=('Angsana New',30),fg='blue',bg='White')
L1.place(x=500,y=20)
### 1 ###
def display_text1():
    tkinter.messagebox.showinfo("วันจันทร์", "พบลูกค้า A 10:00น.")
button = Button(GUI, text="วันจันทร์\n13",command=display_text1)
button.config(bg="yellow", fg="black",font=('Angsana New',30,), width=10, height=1)
button.place(x=0,y=100)
########
### 2 ###
def display_text2():
    tkinter.messagebox.showinfo("วันอังคาร", "พบลูกค้า B 10:00น.\nพบลูกค้า C 14:00น.")
    
button = Button(GUI, text="วันอังคาร\n14",command=display_text2)
button.config(bg="magenta", fg="black",font=('Angsana New',30,), width=10, height=1)
button.place(x=150,y=100)
########
### 3 ###
def display_text3():
    tkinter.messagebox.showinfo("วันพุธ", "Office")
    
button = Button(GUI, text="วันพุธ\n15",command=display_text3)
button.config(bg="lime", fg="black",font=('Angsana New',30,), width=10, height=1)
button.place(x=300,y=100)
########
### 4 ###
def display_text4():
    tkinter.messagebox.showinfo("วันพฤหัสบดี", "ประชุม แผนก 10:00น.\nประชุม บริษัท 14:00น.")
    
button = Button(GUI, text="วันพฤหัสบดี\n16",command=display_text4)
button.config(bg="orange", fg="black",font=('Angsana New',30,), width=10, height=1)
button.place(x=450,y=100)
########
### 5 ###
def display_text5():
    tkinter.messagebox.showinfo("วันศุกร์", "อบรม\n9:30-16:30น.")
    
button = Button(GUI, text="วันศุกร์\n17",command=display_text5)
button.config(bg="cyan", fg="black",font=('Angsana New',30), width=10, height=1)
button.place(x=600,y=100)
########
### 6 ###
def display_text6():
    tkinter.messagebox.showinfo("วันเสาร์", "Activity Day\n8:30-12:00น.")
    
button = Button(GUI, text="วันเสาร์\n18",command=display_text6)
button.config(bg="purple", fg="black",font=('Angsana New',30,), width=10, height=1)
button.place(x=750,y=100)
########
### 7 ###
def display_text7():
    tkinter.messagebox.showinfo("วันอาทิตย์", "Holiday")
    
button = Button(GUI, text="วันอาทิตย์\n19",command=display_text7)
button.config(bg="red", fg="black",font=('Angsana New',30), width=10, height=1)
button.place(x=900,y=100)
########

GUI.mainloop()

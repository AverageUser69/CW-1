from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Number System Converter')
root.geometry('1280x720')
#====================variable====================
num=IntVar()
lblbinary=StringVar()
lbldecimal=StringVar()
lblhexa=StringVar()
lbloctal=StringVar()

#===================functions=====================
def convert():
    if num.get()<0:
        messagebox.showerror('Error','You must enter a positive number.')
    elif num.get()==0:
        messagebox.showerror('Error','You must enter a number.')
    else:
        
        lblbinary.set(str(bin(num.get()).replace("0b", "")))
        lbldecimal.set(str(num.get()))
        lblhexa.set(str.upper(hex(num.get()).replace("0x", "")))
        lbloctal.set(str(oct(num.get()).replace("0o", "")))

def clear():
    num.set(0)
    lblhexa.set('')
    lblbinary.set('')
    lbldecimal.set('')
    lbloctal.set('')

def exit():
    if messagebox.askyesno('Exit','Do you want to Exit'):
        root.destroy()


Label(root,text='Number System Converter',font=('times new rommon',40,'bold'),fg='black').pack(pady=10)


n=Label(root,text='Enter Number',font=('arial 20 bold'),fg='#7D9EC0')
n.place(x=300,y=150)
n_txt=Entry(root,font=('times new rommon',20,'bold'),fg='#20B2AA',justify=CENTER,relief=GROOVE,textvariable=num)
n_txt.place(x=650,y=160)

b=Label(root,text='Binary',font=('arial 20 bold'),fg='#7D9EC0')
b.place(x=300,y=230)
b_txt=Entry(root,font=('times new rommon',20,'bold'),fg='#20B2AA',justify=CENTER,relief=GROOVE,textvariable=lblbinary)
b_txt.place(x=650,y=230)

d=Label(root,text='decimal',font=('arial 20 bold'),fg='#7D9EC0')
d.place(x=300,y=310)
d_txt=Entry(root,font=('times new rommon',20,'bold'),fg='#20B2AA',justify=CENTER,relief=GROOVE,textvariable=lbldecimal)
d_txt.place(x=650,y=300)

h=Label(root,text='Hexa Decimal',font=('arial 20 bold'),fg='#7D9EC0')
h.place(x=300,y=390)
h_txt=Entry(root,font=('times new rommon',20,'bold'),fg='#20B2AA',justify=CENTER,relief=GROOVE,textvariable=lblhexa)
h_txt.place(x=650,y=380)


o=Label(root,text='Octal',font=('arial 20 bold'),fg='#7D9EC0')
o.place(x=300,y=470)
o_txt=Entry(root,font=('times new rommon',20,'bold'),fg='#20B2AA',justify=CENTER,relief=GROOVE,textvariable=lbloctal)
o_txt.place(x=650,y=460)

btn1=Button(root,text='Convert',font='arial 17 bold',fg='#5C5C5C',bg='#97FFFF',width=10,relief=GROOVE,bd=10,command=convert)
btn1.place(x=300,y=600)

btn2=Button(root,text='Clear',font='arial 17 bold',fg='#5C5C5C',bg='#97FFFF',width=10,relief=GROOVE,bd=10,command=clear)
btn2.place(x=550,y=600)

btn3=Button(root,text='Exit',font='arial 17 bold',fg='#5C5C5C',bg='#97FFFF',width=10,relief=GROOVE,bd=10,command=exit)
btn3.place(x=800,y=600)

root.mainloop()
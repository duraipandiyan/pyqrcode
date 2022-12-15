from tkinter import*
from tkinter import messagebox as mb
import pyqrcode as qr

window: Tk=Tk()
window.title("qrcode generation")
window.geometry("500x500")
window.config(background="gray")
title=Label(window,text="QRCODE GENRATION",font=("times",20,"bold"),bg="black",fg="white",pady="10")
title.pack(fill=X)
#frame for widject


myframe=Frame(window,bg="gray")
myframe.pack(fill=X)

#WINDOW IN THE FRAME

lbl_stid=Label(myframe,text="STD_ID",font=("times",20),fg="blue",bg="gray")
lbl_stid.grid(row=0,column=0,pady=10)

lbl_stNAME=Label(myframe,text="STD_NAME",font=("times",20),fg="blue",bg="gray")
lbl_stNAME.grid(row=1,column=0,padx=6,pady=10)

lbl_stcourse=Label(myframe,text="COURSE",font=("times",20),fg="blue",bg="gray")
lbl_stcourse.grid(row=2,column=0,padx=6,pady=10)

#variables
std_id=StringVar()
name=StringVar()
course=StringVar()

def get():
    data=stdi_entry.get()
    data1=stdn_entry.get()
    data2=stdc_entry.get()

    file=open("d:\\durai.txt",'w')
    info=file.write(data+"\n"+data1+"\n"+data2)
    print(info)
    file.close()
    code=qr.create(info)
    code.svg("image.svg",scale=5)
    mb.showinfo("Message","qrcode created successfully")




#entry box
stdi_entry=Entry(myframe,textvariable=std_id,font=("times",20),fg="blue",bg="gray")
stdi_entry.grid(row=0,column=1)

stdn_entry=Entry(myframe,textvariable=name,font=("times",20),fg="blue",bg="gray")
stdn_entry.grid(row=1,column=1)

stdc_entry=Entry(myframe,textvariable=course,font=("times",20),fg="blue",bg="gray")
stdc_entry.grid(row=2,column=1)

sub_button=Button(myframe,text="submit",width=6,bd=0,font=("times",20,"bold"),fg="yellow",bg="green",command=get)
sub_button.grid(row=3,column=1)
window.mainloop()
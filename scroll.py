from tkinter import *
window=Tk()
window.geometry("300x300")
window.title("scroll")
window.resizable(width="false",height="false")
title=Label(window,text="Scroll bar",font=("times",20,"bold"),bg="black",fg="white",pady="10")
title.pack(pady=10,fill=X)

frame1=Frame(window)
frame1.pack(pady=10)


yscrollbar=Scrollbar(frame1,orient=VERTICAL)
yscrollbar.pack(side=RIGHT,fill=Y)
xscrollbar=Scrollbar(frame1,orient=HORIZONTAL)
xscrollbar.pack(side=BOTTOM,fill=X)

textbox=Text(frame1,width=40,height=40,yscrollcommand=yscrollbar.set,xscrollcommand=xscrollbar.set,wrap="none")
textbox.pack()
yscrollbar.config(command=textbox.yview)
xscrollbar.config(command=textbox.xview)

for i in range(40):
        print(textbox.insert(END,"\npython is  a easyest language and easy to understand and it is a platform independent we can use diffrent platform"))
window.mainloop()
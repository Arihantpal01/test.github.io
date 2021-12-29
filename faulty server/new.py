
from tkinter import *


r=Tk()

r.geometry('250x250')


def Start_Server():
    import os
   
    
    a="python -m http.server --bind=localhost"
    os.system(f"cmd /k {a}")
    f_t = LabelFrame(r,bg="white").grid(row=1,column=0)
    L=Label(r,text="Enter localhost:8000 on your browser",bg='white')
    L.grid(row=2,column=0)
    f_t.grid(row=3,column=0)

f=LabelFrame(r)

l=Label(f,text="MPS")
l.grid(row=0,column=1)
b=Button(f,text="Start",command=Start_Server)
b.grid(row=0,column=2,padx=10)



f.grid()

r.mainloop()

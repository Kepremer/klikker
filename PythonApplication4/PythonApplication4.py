from tkinter import *
klik=0
def klikker(event):
    global klik
    klik+=1
    lbl.configure(text=klik)
def klikker_minus(event):
    global klik
    klik-=1
    lbl.configure(text=klik)
def txt_to_lbl(event):
    #pass
    text=txt.get()#From Entry to text
    lbl.configure(text=text)
    txt.delete(0, END)
def valik():
    valik_=var.get()
    lbl.configure(text=valik_)
    txt.insert(0,valik_)
okno=Tk()
okno.title("Imja okna")
okno.geometry("500x1000")
knopka=Button(okno,text="TLN420", font="Arial 30", fg="purple", bg="green", height=5, width=10, relief=GROOVE)#RAISED, SUNKEN
knopka.bind("<Button-1>", klikker)
knopka.bind("<Button-3>", klikker_minus)
knopka1=Button(okno, text"X2", font="Arial 30", fg="purple", bg="green", height=5, width=10, relief=GROOVE)
knopka1.bind("<Button-1>")
lbl=Label(okno, text="Joint", font="Arial 30", height=5, width=10, fg="red", bg="brown",)
txt=Entry(okno, font="Arial 20", width=20, fg="red", bg="brown", justify=CENTER)
txt.bind("<Return>") #Enter
i1=PhotoImage(file="Bong.png")
i2=PhotoImage(file="Kes.png")
i3=PhotoImage(file="Vedro.png")
var=StringVar()
var.set(1)
r1=Radiobutton(okno, image=i1, variable=var, value="Üks", command=valik)
r2=Radiobutton(okno, image=i2, variable=var, value="Kaks", command=valik)
r3=Radiobutton(okno, image=i3, variable=var, value="Kolm", command=valik)



r1.pack()
r2.pack()
r3.pack()
lbl.pack()
knopka.pack()#side=LEFT,TOP, RIGHT
txt.pack()
okno.mainloop()
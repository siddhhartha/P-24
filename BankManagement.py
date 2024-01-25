from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector as connector
import webbrowser

mydb=connector.connect(host="localhost",user='root',database="bank",password="")
mycursor=mydb.cursor()

win = Tk()

win.attributes("-fullscreen",True)

a="1"

def change():

    frame_c=Frame(win,width=10000,height=10000,bg='white')
    frame_c.place(x=0,y=0)

    def ok():
        global a
        if acc.get()!=a:
            messagebox.showinfo("ALERT BOX","INCORRECT INFORMATION")
            return
        d="update new set password='{}' where email='{}'".format(new.get(),acc.get())
        mycursor.execute(d)
        mydb.commit()
        messagebox.showinfo("ALERT BOX","SUCCESSFULLY UPDATED")
        frame_c.destroy()

    Frame(frame_c,width=10000,height=59,bg="light green").place(x=0,y=0)

    Frame(frame_c,width=10000,height=2,bg='black').place(x=0,y=60)

    p1 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (24).png")
    m = p1.subsample(1,2)

    Button(frame_c,border=0,font=("Microsoft Yahei UI Light",25) ,bg='white',image=m).place(x=300,y=100)

    p2 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (41).png")
    b2 = p2.subsample(2,2)

    p3 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (49).png")
    b3 = p3.subsample(2,2)

    p3 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (49).png")
    b5 = p3.subsample(2,2)

    p3 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (47).png")
    b4 = p3.subsample(2,2)

    Button(frame_c,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b2).place(x=180,y=260)
    acc=Entry(frame_c,font=("Microsoft Yahei UI Light",25) ,bg='white')
    acc.place(x=700,y=260)

    Button(frame_c,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b3).place(x=220,y=380)
    old=Entry(frame_c,font=("Microsoft Yahei UI Light",25) ,bg='white')
    old.place(x=700,y=380)

    Button(frame_c,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b3).place(x=220,y=500)
    new=Entry(frame_c,font=("Microsoft Yahei UI Light",25) ,bg='white')
    new.place(x=700,y=500)

    Button(frame_c,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b4,command=ok).place(x=440,y=600)

    Button(frame_c,text="BACK",command=frame_c.destroy).place(x=0,y=0)

    win.mainloop()

def withdraw():

    frame_w=Frame(win,width=10000,height=10000,bg='white')
    frame_w.place(x=0,y=0)
    
    def ok():
        m="select money from new where email='{}'".format(acc.get())
        mycursor.execute(m)
        bal=mycursor.fetchone()[0]
        if bal<int(am.get()):
            messagebox.showinfo("ALERT BOX","UNSUFFICIENT BALANCE")
            return
        bal=bal-int(am.get())
        d="update new set money='{}' where email='{}'".format(bal,acc.get())
        mycursor.execute(d)
        mydb.commit()
        messagebox.showinfo("ALERT BOX","SUCCESSFULLY WITHDRAW")
        frame_w.destroy()

    Frame(frame_w,width=10000,height=59,bg="light green").place(x=0,y=0)

    Frame(frame_w,width=10000,height=2,bg='black').place(x=0,y=60)

    p1 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (46).png")
    m = p1.subsample(1,2)

    Button(frame_w,border=1,font=("Microsoft Yahei UI Light",25) ,bg='white',image=m).place(x=100,y=100)

    p2 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (41).png")
    b2 = p2.subsample(2,2)

    p3 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (40).png")
    b3 = p3.subsample(2,2)

    p3 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (47).png")
    b4 = p3.subsample(2,2)

    Button(frame_w,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b2).place(x=200,y=260)
    acc=Entry(frame_w,font=("Microsoft Yahei UI Light",25) ,bg='white')
    acc.place(x=700,y=260)

    Button(frame_w,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b3).place(x=220,y=380)
    am=Entry(frame_w,font=("Microsoft Yahei UI Light",25) ,bg='white')
    am.place(x=700,y=380)

    Button(frame_w,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b4,command=ok).place(x=440,y=600)

    Button(frame_w,text="BACK",command=frame_w.destroy).place(x=0,y=0)

    win.mainloop()

def passbook():

    global a
    m="select money from new where email='{}'".format(a)
    mycursor.execute(m)
    bal=mycursor.fetchone()[0]

    frame_book=Frame(win,width=10000,height=10000,bg='white')
    frame_book.place(x=0,y=0)

    frame2=Frame(frame_book,width=10000,height=59,bg="light green")
    frame2.place(x=0,y=0)

    Frame(frame_book,height=4,width=100000,bg="black").place(x=0,y=60)
    p1 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (23).png")
    m = p1.subsample(1,2)

    Button(frame_book,border=0,font=("Microsoft Yahei UI Light",25) ,bg='white',image=m).place(x=300,y=100)

    Frame(frame_book,height=5,width=10000,bg="black").place(x=0,y=250)

    Label(frame_book,text="Balance:-",font=("Microsoft Yahei UI Light",25) ,bg='white').place(x=100,y=200)
    Label(frame_book,text=bal,font=("Microsoft Yahei UI Light",25) ,bg='white').place(x=250,y=200)

    Label(frame_book,text="DATE",font=("Microsoft Yahei UI Light",25) ,bg='white').place(x=100,y=270)
    Label(frame_book,text="CREDITED",font=("Microsoft Yahei UI Light",25) ,bg='white').place(x=350,y=270)
    Label(frame_book,text="DEBITED",font=("Microsoft Yahei UI Light",25) ,bg='white').place(x=650,y=270)
    Label(frame_book,text="AMOUNT",font=("Microsoft Yahei UI Light",25) ,bg='white').place(x=950,y=270)

    Button(frame_book,text="Back",command=frame_book.destroy).place(x=0,y=0)


    win.mainloop()

def callback():
    webbrowser.open_new(r"https://colab.research.google.com/drive/11hlmoDU0Kdn1diVDNNBuY0U6lZZB5YdH#scrollTo=7AXLAUtv5LIv")

def info():

    frame_info=Frame(win,width=10000,height=10000,bg='white')
    frame_info.place(x=0,y=0)

    frame2=Frame(frame_info,width=10000,height=59,bg="light green")
    frame2.place(x=0,y=0)
    global a
    m="select * from new where email='{}'".format(a)
    mycursor.execute(m)
    r=mycursor.fetchall()
    print(r)

    Label(frame_info,text="ACCOUNT DETAILS",fg='black',bg="white",font=("Microsoft Yahei UI Light",28)).place(x=90,y=100)
    Frame(frame_info,bg="black",width=10000,height=2).place(x=0,y=150)
    Label(frame_info,text='NAME:-',bg='light green',font=("Microsoft Yahei UI Light",23)).place(x=120,y=200)
    Label(frame_info,text=r[0][0],bg='white',font=("Microsoft Yahei UI Light",23)).place(x=280,y=200)

    Label(frame_info,text='AGE:-',bg='light green',font=("Microsoft Yahei UI Light",23)).place(x=120,y=260)
    Label(frame_info,text=r[0][1],bg='white',font=("Microsoft Yahei UI Light",23)).place(x=280,y=260)

    Label(frame_info,text='EMAIL:-',bg='light green',font=("Microsoft Yahei UI Light",23)).place(x=120,y=320)
    Label(frame_info,text=r[0][2],bg='white',font=("Microsoft Yahei UI Light",23)).place(x=280,y=320)

    Label(frame_info,text='DOB:-',bg='light green',font=("Microsoft Yahei UI Light",23)).place(x=120,y=380)
    Label(frame_info,text=r[0][3],bg='white',font=("Microsoft Yahei UI Light",23)).place(x=280,y=380)

    Label(frame_info,text='PASSWORD:-',bg='light green',font=("Microsoft Yahei UI Light",23)).place(x=120,y=440)
    Label(frame_info,text=r[0][4],bg='white',font=("Microsoft Yahei UI Light",23)).place(x=300,y=440)

    Label(frame_info,text='BALANCE:-',bg='light green',font=("Microsoft Yahei UI Light",23)).place(x=120,y=500)
    Label(frame_info,text=r[0][5],bg='white',font=("Microsoft Yahei UI Light",23)).place(x=300,y=500)


    img = ImageTk.PhotoImage(Image.open("image2.png"))

    label = Label(frame_info, image = img)
    label.place(x=690,y=60)

    Button(frame_info,text="BACK",command=frame_info.destroy).place(x=0,y=0)

    win.mainloop()

def edit():

    frame_edit=Frame(win,width=10000,height=10000,bg='white')
    frame_edit.place(x=0,y=0)

    frame2=Frame(frame_edit,width=10000,height=59,bg="light green")
    frame2.place(x=0,y=0)

    def check():
        global a
        d="update new set name='{}', age='{}', email='{}', dob='{}', password='{}'  where email='{}'".format(name.get(),age.get(),email.get(),dob.get(),password.get(),a)
        mycursor.execute(d)
        mydb.commit()
        messagebox.showinfo("ALERT BOX","SUCCESSFULLY UPDATED")
        frame_edit.destroy()


    Label(frame_edit,text="UPDATE ACCOUNT DETAILS",fg='black',bg="white",font=("Microsoft Yahei UI Light",28)).place(x=90,y=100)
    Label(frame_edit,text='NAME',bg='white',font=("Microsoft Yahei UI Light",15)).place(x=120,y=170)
    name=Entry(frame_edit,width=25,fg="black",bg='white',border=1,font=("Microsoft Yahei UI Light",15))
    name.place(x=120,y=220)

    Label(frame_edit,text='AGE',bg='white',font=("Microsoft Yahei UI Light",15)).place(x=120,y=270)
    age=Entry(frame_edit,width=25,fg="black",bg='white',border=1,font=("Microsoft Yahei UI Light",15))
    age.place(x=120,y=320)

    Label(frame_edit,text='EMAIL',bg='white',font=("Microsoft Yahei UI Light",15)).place(x=120,y=370)
    email=Entry(frame_edit,width=25,fg="black",bg='white',border=1,font=("Microsoft Yahei UI Light",15))
    email.place(x=120,y=420)

    Label(frame_edit,text='DATE OF BIRTH',bg='white',font=("Microsoft Yahei UI Light",15)).place(x=120,y=470)
    dob=Entry(frame_edit,width=25,fg="black",bg='white',border=1,font=("Microsoft Yahei UI Light",15))
    dob.place(x=120,y=520)

    Label(frame_edit,text='PASSWORD',bg='white',font=("Microsoft Yahei UI Light",15)).place(x=120,y=570)
    password=Entry(frame_edit,width=25,fg="black",bg='white',border=1,font=("Microsoft Yahei UI Light",15))
    password.place(x=120,y=620)

    Button(frame_edit,text="SUBMIT",bg="light green",fg='white',font=("Microsoft Yahei UI Light",15),command=check).place(x=200,y=670)

    img = ImageTk.PhotoImage(Image.open("image2.png"))

    label = Label(frame_edit, image = img)
    label.place(x=690,y=60)

    Button(frame_edit,text="BACK",command=frame_edit.destroy).place(x=0,y=0)

    win.mainloop()


def send():

    frame_s=Frame(win,width=10000,height=10000,bg='white')
    frame_s.place(x=0,y=0)

    Frame(frame_s,width=10000,height=59,bg="light green").place(x=0,y=0)

    def ok():
        global a
        m="select money from new where email='{}'".format(a)
        mycursor.execute(m)
        bal=mycursor.fetchone()[0]
        if bal < int(am.get()):
            messagebox.showinfo("ALERT BOX","UNSUFFICIENT BALANCE")
            return
        bal=bal-int(am.get())
        d="update new set money='{}' where email='{}'".format(bal,a)
        mycursor.execute(d)

        m="select money from new where email='{}'".format(acc.get())
        mycursor.execute(m)
        bal=mycursor.fetchone()[0]
        bal=bal + int(am.get())
        d="update new set money='{}' where email='{}'".format(bal,acc.get())
        mycursor.execute(d)
        mydb.commit()
        messagebox.showinfo("ALERT BOX","SUCCESSFULLY SEND")
        frame_s.destroy()

    Frame(frame_s,width=10000,height=2,bg='black').place(x=0,y=60)

    p1 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (32).png")
    m = p1.subsample(1,2)

    Button(frame_s,border=0,font=("Microsoft Yahei UI Light",25) ,bg='white',image=m).place(x=300,y=100)

    p2 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (41).png")
    b2 = p2.subsample(2,2)

    p3 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (40).png")
    b3 = p3.subsample(2,2)

    p3 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (32).png")
    b4 = p3.subsample(2,2)

    Button(frame_s,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b2).place(x=200,y=260)
    acc=Entry(frame_s,font=("Microsoft Yahei UI Light",25) ,bg='white')
    acc.place(x=700,y=260)

    Button(frame_s,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b3).place(x=220,y=380)
    am=Entry(frame_s,font=("Microsoft Yahei UI Light",25) ,bg='white')
    am.place(x=700,y=380)

    Button(frame_s,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b4,command=ok).place(x=440,y=600)

    Button(frame_s,text="BACK",command=frame_s.destroy).place(x=0,y=0)

    win.mainloop()


def deposit():

    frame_d=Frame(win,width=10000,height=10000,bg='white')
    frame_d.place(x=0,y=0)
    
    def ok():
        m="select money from new where email='{}'".format(acc.get())
        mycursor.execute(m)
        bal=mycursor.fetchone()[0]
        bal=bal+int(am.get())
        d="update new set money='{}' where email='{}'".format(bal,acc.get())
        mycursor.execute(d)
        mydb.commit()
        messagebox.showinfo("ALERT BOX","SUCCESSFULLY DEPOSIT")
        frame_d.destroy()

    Frame(frame_d,width=10000,height=59,bg="light green").place(x=0,y=0)

    Frame(frame_d,width=10000,height=2,bg='black').place(x=0,y=60)

    p1 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (34).png")
    m = p1.subsample(1,2)

    Button(frame_d,border=1,font=("Microsoft Yahei UI Light",25) ,bg='white',image=m).place(x=300,y=100)

    p2 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (41).png")
    b2 = p2.subsample(2,2)

    p3 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (40).png")
    b3 = p3.subsample(2,2)

    p3 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (47).png")
    b4 = p3.subsample(2,2)

    Button(frame_d,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b2).place(x=200,y=260)
    acc=Entry(frame_d,font=("Microsoft Yahei UI Light",25) ,bg='white')
    acc.place(x=700,y=260)

    Button(frame_d,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b3).place(x=220,y=380)
    am=Entry(frame_d,font=("Microsoft Yahei UI Light",25) ,bg='white')
    am.place(x=700,y=380)

    Button(frame_d,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b4,command=ok).place(x=440,y=600)

    Button(frame_d,text="BACK",command=frame_d.destroy).place(x=0,y=0)

    win.mainloop()

def loan():

    frame_loan=Frame(win,width=10000,height=10000,bg='white')
    frame_loan.place(x=0,y=0)

    Frame(frame_loan,width=10000,height=2,bg='black').place(x=0,y=60)

    p1 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (54).png")
    m = p1.subsample(1,2)

    Button(frame_loan,border=0,font=("Microsoft Yahei UI Light",25) ,bg='white',image=m).place(x=200,y=100)

    p1 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (13).png")
    b1 = p1.subsample(2,2)

    p2 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (14).png")
    b2 = p2.subsample(2,2)

    p3 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (15).png")
    b3 = p3.subsample(2,2)

    p3 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (16).png")
    b4 = p3.subsample(2,2)

    Button(frame_loan,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b1).place(x=440,y=250)

    Button(frame_loan,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b2).place(x=440,y=380)

    Button(frame_loan,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b3).place(x=440,y=530)

    Button(frame_loan,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b4).place(x=440,y=630)

    Button(frame_loan,text="BACK",command=frame_loan.destroy).place(x=0,y=0)

    win.mainloop()

def digital():

    frame_d=Frame(win,width=10000,height=10000,bg='white')
    frame_d.place(x=0,y=0)

    Frame(frame_d,width=10000,height=2,bg='black').place(x=0,y=60)

    p1 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (21).png")
    m = p1.subsample(1,1)

    Button(frame_d,border=1,font=("Microsoft Yahei UI Light",25) ,bg='white',image=m,compound=LEFT).place(x=100,y=70)

    p1 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (22).png")
    b1 = p1.subsample(2,2)

    p2 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (23).png")
    b2 = p2.subsample(2,2)

    p3 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (24).png")
    b3 = p3.subsample(2,2)

    Button(frame_d,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b1,command=info).place(x=200,y=280)

    Button(frame_d,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b2,command=passbook).place(x=200,y=400)

    Button(frame_d,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b3,command=change).place(x=200,y=550)

    p1 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (32).png")
    b4 = p1.subsample(2,2)

    p2 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (26).png")
    b5 = p2.subsample(2,2)

    p3 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (25).png")
    b6 = p3.subsample(2,2)

    Button(frame_d,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b4,command=send).place(x=800,y=280)

    Button(frame_d,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b5,command=edit).place(x=800,y=400)

    Button(frame_d,border=0,font=("Microsoft Yahei UI Light",18) ,bg='white',image=b6).place(x=800,y=550)

    Button(frame_d,text="BACK",command=frame_d.destroy).place(x=0,y=0)
    win.mainloop()

def fast():

    frame_fast=Frame(win,width=10000,height=10000,bg='white')
    frame_fast.place(x=0,y=0)

    

    p1 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (28).png")
    m = p1.subsample(1,1)

    Button(frame_fast,border=0 ,bg='white',image=m).place(x=0,y=20)

    p1 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (29).png")
    b1 = p1.subsample(2,2)

    p2 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (30).png")
    b2 = p2.subsample(2,2)

    p3 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (31).png")
    b3 = p3.subsample(2,2)

    Button(frame_fast,border=0 ,bg='white',image=b1).place(x=440,y=360)

    Button(frame_fast,border=0 ,bg='white',image=b2).place(x=440,y=460)

    Button(frame_fast,border=0,bg='white',image=b3).place(x=440,y=580)

    Frame(frame_fast,width=10000,height=2,bg='black').place(x=0,y=60)

    Button(frame_fast,text="BACK",command=frame_fast.destroy).place(x=0,y=0)

    win.mainloop()

def login():

    frame_create=Frame(win,width=10000,height=10000,bg='white')
    frame_create.place(x=0,y=0)

    frame2=Frame(frame_create,width=10000,height=60,bg="#57a1f8")
    frame2.place(x=0,y=0)

    Frame(frame_create,width=10000,height=2,bg='black').place(x=0,y=60)

    search=Entry(frame2,font=("Microsoft Yahei UI Light",15))
    search.place(x=1000,y=20)
    search.insert(0,"Search")

    p1 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\b1.png")
    b1 = p1.subsample(1,2)

    p2 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\b2.png")
    b2 = p2.subsample(1,2)

    p3 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\b3.png")
    b3 = p3.subsample(1,2)

    p4 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\b4.png")
    b4 = p4.subsample(1,2)

    p5 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\b5.png")
    b5 = p5.subsample(2,2)

    p6 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\b6.png")
    b6 = p6.subsample(1,2)

    photo = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\b7.png")
    b7 = photo.subsample(1,2)

    Button(frame_create,text="DIGITAL\nBANKING ! ",border=1,font=("Microsoft Yahei UI Light",15) ,bg='white',image=b1,compound=LEFT,command=digital).place(x=110,y=200)

    Button(frame_create,text="STOCK ! ",border=1,font=("Microsoft Yahei UI Light",15) ,bg='white',image=b2,compound=LEFT,command=callback).place(x=440,y=200)

    Button(frame_create,text="WITHDRAW ! ",border=1,font=("Microsoft Yahei UI Light",15),command=withdraw ,bg='white',image=b3,compound=LEFT).place(x=770,y=200)

    Button(frame_create,text="LOAN ! ",border=1,font=("Microsoft Yahei UI Light",15) ,bg='white',image=b4,compound=LEFT,command=loan).place(x=110,y=400)

    Button(frame_create,border=1,font=("Microsoft Yahei UI Light",15) ,bg='white',image=b5,compound=LEFT,command=fast).place(x=440,y=400)

    Button(frame_create,text="DEPOSIT ! ",command=deposit,border=1,font=("Microsoft Yahei UI Light",15) ,bg='white',image=b6,compound=LEFT).place(x=770,y=400)

    Button(frame_create,text="EXIT ! ",border=1,font=("Microsoft Yahei UI Light",15) ,bg='white',image=b7,compound=LEFT,command=frame_create.destroy).place(x=440,y=600)

    Button(frame_create,text='BACK',command=frame_create.destroy).place(x=0,y=0)

    win.mainloop()
def create():

    frame_create=Frame(win,width=10000,height=10000,bg='white')
    frame_create.place(x=0,y=0)

    frame2=Frame(frame_create,width=10000,height=59,bg="light green")
    frame2.place(x=0,y=0)

    def signup_values():
        
        formula="INSERT INTO new (name,age,email,dob,password) VALUES(%s, %s,%s,%s,%s)"
        data=(name.get(),age.get(),email.get(),dob.get(),password.get())
        mycursor.execute(formula,data)
        mydb.commit()
        messagebox.showinfo("ALERT BOX","SUCCESSFULLY CREATED")
        frame_create.destroy()

    Label(frame_create,text="CREATE NEW ACCOUNT",fg='black',bg="white",font=("Microsoft Yahei UI Light",28)).place(x=90,y=100)
    Label(frame_create,text='NAME',bg='white',font=("Microsoft Yahei UI Light",15)).place(x=120,y=170)
    name=Entry(frame_create,width=25,fg="black",bg='white',border=1,font=("Microsoft Yahei UI Light",15))
    name.place(x=120,y=220)

    Label(frame_create,text='AGE',bg='white',font=("Microsoft Yahei UI Light",15)).place(x=120,y=270)
    age=Entry(frame_create,width=25,fg="black",bg='white',border=1,font=("Microsoft Yahei UI Light",15))
    age.place(x=120,y=320)

    Label(frame_create,text='EMAIL',bg='white',font=("Microsoft Yahei UI Light",15)).place(x=120,y=370)
    email=Entry(frame_create,width=25,fg="black",bg='white',border=1,font=("Microsoft Yahei UI Light",15))
    email.place(x=120,y=420)

    Label(frame_create,text='DATE OF BIRTH',bg='white',font=("Microsoft Yahei UI Light",15)).place(x=120,y=470)
    dob=Entry(frame_create,width=25,fg="black",bg='white',border=1,font=("Microsoft Yahei UI Light",15))
    dob.place(x=120,y=520)

    Label(frame_create,text='PASSWORD',bg='white',font=("Microsoft Yahei UI Light",15)).place(x=120,y=570)
    password=Entry(frame_create,width=25,fg="black",bg='white',border=1,font=("Microsoft Yahei UI Light",15))
    password.place(x=120,y=620)

    Button(frame_create,text="sign up",bg="light green",fg='white',font=("Microsoft Yahei UI Light",15),command=signup_values).place(x=200,y=670)

    img = ImageTk.PhotoImage(Image.open("image2.png"))

# Create a Label Widget to display the text or Image
    label = Label(frame_create, image = img)
    label.place(x=690,y=60)

    Button(frame_create,text="BACK",command=frame_create.destroy).place(x=0,y=0)

    win.mainloop()

def sign_in(win):
    frame_sign=Frame(win,width=10000,height=10000,bg='white')
    frame_sign.place(x=0,y=0)

    Frame(frame_sign,width=10000,height=50,bg="#57a1f8").place(x=0,y=0)

    p1 = PhotoImage(file = r"C:\Users\dell\Desktop\mysql\AGE (51).png")
    img = p1.subsample(2,2)


# Create a Label Widget to display the text or Image
    label = Label(frame_sign, image = img,bg="white")
    label.place(x=700,y=100)

    def check():
        
        
        try:
            global a
            a=user.get()
            s=(user.get(),)
            d='select password from new where email=%s'
            mycursor.execute(d,s)
            r=mycursor.fetchall()
            if r[0][0]==code.get():
                
                messagebox.showinfo("ALERT BOX","SUCCESSFULLY LOGIN")
                login()
            else:
                messagebox.showinfo("ALERT BOX","INCORRECT PASSWORD")

            
        except:
            messagebox.showinfo("ALERT BOX","INCORRECT ACCOUNT")

    frame=Frame(frame_sign,width=700,height=400,bg="white")
    frame.place(x=0,y=180)
    Label(frame,text="SIGN IN",bg="white",fg="#57a1f8",font=("Microsoft Yahei UI Light",23,"bold")).place(x=300,y=50)

   
    def on_entry(e):
        user.delete(0,'end')

    def on_leave(e):
        name=user.get()
        
        if name=="":
            user.insert(0,"Account")

    user=Entry(frame,width=25,fg="black",bg='white',border=0,font=("Microsoft Yahei UI Light",11))
    user.place(x=220,y=130)
    user.insert(0,"Account")
    user.bind('<FocusIn>',on_entry)
    user.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg="black").place(x=200,y=170)

    def on_entry(e):
        code.delete(0,'end')

    def on_leave(e):
        name=code.get()
        if name=="":
            code.insert(0,"Password")

    code=Entry(frame,width=25,fg="black",bg='white',border=0,font=("Microsoft Yahei UI Light",11))
    code.place(x=220,y=200)
    code.insert(0,"Password")
    code.bind('<FocusIn>',on_entry)
    code.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg="black").place(x=200,y=240)

    Button(frame,width=39,pady=7,text='SIGN IN',bg='#57a1f8',fg='white',border=0,command=check).place(x=210,y=280)
    Label(frame,text="Dont't have an account",fg='black',bg="white",font=("Microsoft Yahei UI Light",9)).place(x=220,y=320)

    Button(frame,width=6,text="Sign Up",border=0,bg="white",cursor='hand2',fg="#57a1f8",command=create).place(x=360,y=320)

    Button(frame_sign,text="Back",command=win.destroy).place(x=0,y=0)
    win.mainloop()


    
sign_in(win)
print(a)

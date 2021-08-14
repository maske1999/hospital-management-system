from tkinter import *
import time
from tkinter import ttk
import datetime
from tkinter import messagebox
from tkinter import font
from tkinter.font import BOLD
import mysql.connector
class hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("hospital management system")
        self.root.geometry("16000x800+0+0")

        #variables
        self.nameoftablate=StringVar()
        self.ref=StringVar()
        self.dose=StringVar()
        self.numberoftablate=StringVar()
        self.lot=StringVar()
        self.idate=StringVar()
        self.edate=StringVar()
        self.daily=StringVar()
        self.finfo=StringVar()
        self.bp=StringVar()
        self.se=StringVar()

        lable_title=Label(self.root,bd=20,text="HOSPITAL MANAGEMENT SYSTEM",fg="red", bg="white",font=("times new roman",50,BOLD))
        lable_title.pack(side=TOP,fill=X)
        #frame
        data_frame=Frame(self.root,bd=5,bg="white",relief=RIDGE)
        data_frame.place(x=15,y=150,width=1530,height=400)

        dataframe_left=LabelFrame(data_frame,bd=1,bg="white",relief=RIDGE,padx=5, font=("carial",10,BOLD),text="Paitent Information")
        dataframe_left.place(x=0,y=1,width=850,height=390)
        dataframe_right=LabelFrame(data_frame,bd=1,bg="white",relief=RIDGE,padx=5, font=("carial",10,BOLD),text="Priscription")
        dataframe_right.place(x=855,y=1,width=650,height=390)
        #button frame
        button_frame=Frame(self.root,bd=1,bg="white",relief=RIDGE,pady=10)
        button_frame.place(x=0,y=550,width=1530,height=70)
        #detail fram3
        datail_frame=Frame(self.root,bd=1,pady=1,bg="white" ,relief=RIDGE)
        datail_frame.place(x=0,y=620,width=1530,height=220)
        #dataframeleft
        lableTablet=Label(dataframe_left,text="name of tablate :",padx=2,pady=10,font=("times new roman",12,BOLD))
        lableTablet.grid(row=0,column=0)

        comtablate=ttk.Combobox(dataframe_left,font=("times new roman",12,BOLD),width=30,textvariable=self.nameoftablate)
        comtablate['values']=('nice','corona vacin','remdisis')
        comtablate.grid(row=0,column=1)
        
        reflable=Label(dataframe_left,text="Refrance No :",padx=2,pady=10,font=("times new roman",12,BOLD))
        reflable.grid(row=1,column=0)
        textref=Entry(dataframe_left,font=("times new roman",12,BOLD),width=30,textvariable=self.ref)
        textref.grid(row=1,column=1)
        
        doslable=Label(dataframe_left,text="Dose :",padx=2,pady=10,font=("times new roman",12,BOLD))
        doslable.grid(row=2,column=0)
        textdos=Entry(dataframe_left,font=("times new roman",12,BOLD),width=30,textvariable=self.dose)
        textdos.grid(row=2,column=1)

        tabnolable=Label(dataframe_left,text="Number of tablet :",padx=2,pady=10,font=("times new roman",12,BOLD))
        tabnolable.grid(row=3,column=0)
        texttabno=Entry(dataframe_left,font=("times new roman",12,BOLD),width=30,textvariable=self.numberoftablate)
        texttabno.grid(row=3,column=1)

        lotlable=Label(dataframe_left,text="Lot :",padx=2,pady=10,font=("times new roman",12,BOLD))
        lotlable.grid(row=4,column=0)
        textlot=Entry(dataframe_left,font=("times new roman",12,BOLD),width=30,textvariable=self.lot)
        textlot.grid(row=4,column=1)

        idatelable=Label(dataframe_left,text="Issue Date :",padx=2,pady=10,font=("times new roman",12,BOLD))
        idatelable.grid(row=5,column=0)
        textidate=Entry(dataframe_left,font=("times new roman",12,BOLD),width=30,textvariable=self.idate)
        textidate.grid(row=5,column=1)

        edatelable=Label(dataframe_left,text="Exp Date :",padx=2,pady=10,font=("times new roman",12,BOLD))
        edatelable.grid(row=6,column=0)
        textedate=Entry(dataframe_left,font=("times new roman",12,BOLD),width=30,textvariable=self.edate)
        textedate.grid(row=6,column=1)
        
        dailable=Label(dataframe_left,text="Daily Dose :",padx=2,pady=10,font=("times new roman",12,BOLD))
        dailable.grid(row=7,column=0)
        textdai=Entry(dataframe_left,font=("times new roman",12,BOLD),width=30,textvariable=self.daily)
        textdai.grid(row=7,column=1)

        selable=Label(dataframe_left,text="Side Effect :",padx=2,pady=10,font=("times new roman",12,BOLD))
        selable.grid(row=2,column=2)
        textse=Entry(dataframe_left,font=("times new roman",12,BOLD),width=30,textvariable=self.se)
        textse.grid(row=2,column=3)
         
        filable=Label(dataframe_left,text="Further Info :",padx=2,pady=10,font=("times new roman",12,BOLD))
        filable.grid(row=0,column=2)
        textfi=Entry(dataframe_left,font=("times new roman",12,BOLD),width=30,textvariable=self.finfo)
        textfi.grid(row=0,column=3)

        bplable=Label(dataframe_left,text="Blood Pressure :",padx=2,pady=10,font=("times new roman",12,BOLD))
        bplable.grid(row=1,column=2)
        textbp=Entry(dataframe_left,font=("times new roman",12,BOLD),width=30,textvariable=self.bp)
        textbp.grid(row=1,column=3)

        # dataframe right
        self.text_pricreption=Text(dataframe_right,font=("times new roman",12,BOLD),width=80,height=25,padx=2,pady=10)
        self.text_pricreption.grid(row=0,column=0)

        #button
        button_pre=Button(button_frame,command=self.prescription_view,text="PRESCRIPTION",width=23,fg="white",bg="green",font=("times new roman",12,BOLD))
        button_pre.grid(row=0,column=0)

        button_predata=Button(button_frame,command=self.prescription,text="PRESCRIPTION DATA",width=23,fg="white",bg="green",font=("times new roman",12,BOLD),padx=10)
        button_predata.grid(row=0,column=1)

        button_del=Button(button_frame,command=self.idelete,text="DELETE",width=23,fg="white",bg="green",font=("times new roman",12,BOLD),padx=10)
        button_del.grid(row=0,column=2)

        button_update=Button(button_frame,command=self.update_data,text="UPDATE",width=23,fg="white",bg="green",font=("times new roman",12,BOLD),padx=10)
        button_update.grid(row=0,column=3)

        button_clear=Button(button_frame,command=self.clear,text="CLEAR",width=23,fg="white",bg="green",font=("times new roman",12,BOLD),padx=10)
        button_clear.grid(row=0,column=4)

        button_exit=Button(button_frame,command=self.exit,text="EXIT",width=23,fg="white",bg="green",font=("times new roman",12,BOLD),padx=10)
        button_exit.grid(row=0,column=5)

        #detail frame
        scroll_x=ttk.Scrollbar(datail_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(datail_frame,orient=VERTICAL)
        self.hosptial_detail=ttk.Treeview(datail_frame,columns=("name of tablate","ref","dose","number of tablate","lot","issue_date","exp_date",
                                                                    "daily_dose","further_info","blood_pressure","side_effect"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)   
        scroll_y.pack(side=RIGHT,fill=Y) 

        scroll_x=ttk.Scrollbar(command=self.hosptial_detail.xview)
        scroll_y=ttk.Scrollbar(command=self.hosptial_detail.yview)
        
        self.hosptial_detail.heading("name of tablate",text="name of tablate")
        self.hosptial_detail.heading("ref", text="Refrance No")
        self.hosptial_detail.heading("dose",text="Dose")
        self.hosptial_detail.heading("number of tablate",text="Number of tablate")
        self.hosptial_detail.heading("lot",text="Lot")
        self.hosptial_detail.heading("issue_date",text="Issue Date")
        self.hosptial_detail.heading("exp_date",text="Exp Date")
        self.hosptial_detail.heading("daily_dose",text="Daily Dose")
        self.hosptial_detail.heading("further_info",text="Further Info")
        self.hosptial_detail.heading("blood_pressure",text="Blood Pressure")
        self.hosptial_detail.heading("side_effect",text="Side Effect")

        self.hosptial_detail["show"]="headings"
        self.hosptial_detail.pack(fill=BOTH, expand=1)

        self.hosptial_detail.column("name of tablate", width=100)
        self.hosptial_detail.column("ref", width=100)
        self.hosptial_detail.column("dose",width=100)
        self.hosptial_detail.column("number of tablate",width=100)
        self.hosptial_detail.column("lot",width=100)
        self.hosptial_detail.column("issue_date",width=100)
        self.hosptial_detail.column("exp_date",width=100)
        self.hosptial_detail.column("daily_dose",width=100)
        self.hosptial_detail.column("further_info",width=100)
        self.hosptial_detail.column("blood_pressure",width=100)
        self.hosptial_detail.column("side_effect",width=100)
        self.hosptial_detail.bind("<ButtonRelease-1>",self.cursor_data)
        self.fetch_data()
    #fuctionality

    def prescription(self):
        if self.nameoftablate.get()=="" or self.ref.get()=="":
            messagebox.showinfo("error",'all fields required')
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='root1999',database='mydata') 
            mycursor=conn.cursor() 
            mycursor.execute("CREATE TABLE IF NOT EXISTS hospital (name_of_tablate VARCHAR(255), ref_no VARCHAR(255),dose VARCHAR(255),number_of_tablate VARCHAR(255),lot VARCHAR(255),IssueDate VARCHAR(255),ExpDate VARCHAR(255),Dailydose VARCHAR(255),Furtherinfo VARCHAR(255),bloodpressure VARCHAR(255),sideeffect VARCHAR(255))")

            mycursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.nameoftablate.get(),
                                                                                                    self.ref.get(),
                                                                                                    self.dose.get(),
                                                                                                    self.numberoftablate.get(),
                                                                                                    self.lot.get(),
                                                                                                    self.idate.get(),
                                                                                                    self.edate.get(),
                                                                                                    self.daily.get(),
                                                                                                    self.finfo.get(),
                                                                                                    self.bp.get(),
                                                                                                    self.se.get()))                                           
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("sucsess","Record inserted successfully")
    
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='root1999',database='mydata') 
        mycursor=conn.cursor() 
        mycursor.execute("select * from hospital")
        rows=mycursor.fetchall()
        if len(rows)!=0:
            self.hosptial_detail.delete(*self.hosptial_detail.get_children())
            for i in rows:
                self.hosptial_detail.insert("",END,values=i)
            conn.commit()
        conn.close()    
    def cursor_data(self,event=""):
        cursor_row=self.hosptial_detail.focus()
        content=self.hosptial_detail.item(cursor_row)
        rows=content["values"]
        self.nameoftablate.set(rows[0])
        self.ref.set(rows[1])
        self.dose.set(rows[2])
        self.numberoftablate.set(rows[3])
        self.lot.set(rows[4])
        self.idate.set(rows[5])
        self.edate.set(rows[6])
        self.daily.set(rows[7])
        self.finfo.set(rows[8])
        self.bp.set(rows[9])
        self.se.set(rows[10])    

    def update_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='root1999',database='mydata') 
        mycursor=conn.cursor() 
        sql="update hospital set name_of_tablate=%s,dose=%s,number_of_tablate=%s,lot=%s,IssueDate=%s,ExpDate=%s,Dailydose=%s,Furtherinfo=%s,bloodpressure=%s,sideeffect=%s where ref_no=%s"
        val=(self.nameoftablate.get(),self.dose.get(),self.numberoftablate.get(),self.lot.get(),self.idate.get(),self.edate.get(),self.daily.get(),self.finfo.get(),self.bp.get(), self.se.get(),self.ref.get())
        mycursor.execute(sql,val)
        messagebox.showinfo("sucees","record updated")
        conn.commit()
        conn.close()
        self.fetch_data()
    def idelete(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='root1999',database='mydata') 
        mycursor=conn.cursor() 
        sql="delete from hospital where ref_no=%s"
        val=(self.ref.get(),)
        mycursor.execute(sql,val)
        messagebox.showinfo(" sucesess","record deleted")
        conn.commit()
        conn.close()
        self.fetch_data()



    def prescription_view(self):
        self.text_pricreption.insert(END," name of tablate \t\t\t"+self.nameoftablate.get()+'\n')
        self.text_pricreption.insert(END," ref no \t\t\t"+self.ref.get()+'\n')
        self.text_pricreption.insert(END," dose \t\t\t"+self.dose.get()+'\n')
        self.text_pricreption.insert(END," number of tablate \t\t\t"+self.numberoftablate.get()+'\n')
        self.text_pricreption.insert(END," lot \t\t\t"+self.lot.get()+'\n')
        self.text_pricreption.insert(END," issue date \t\t\t"+self.idate.get()+'\n')
        self.text_pricreption.insert(END," expiry date \t\t\t"+self.edate.get()+'\n')
        self.text_pricreption.insert(END," daily dose \t\t\t"+self.daily.get()+'\n')
        self.text_pricreption.insert(END," further info \t\t\t"+self.finfo.get()+'\n')
        self.text_pricreption.insert(END," blood pressure \t\t\t"+self.bp.get()+'\n')
        self.text_pricreption.insert(END," side effect \t\t\t"+self.se.get()+'\n')
        
    def clear(self):
        self.nameoftablate.set("")
        self.ref.set("")
        self.dose.set("")
        self.numberoftablate.set("")
        self.lot.set("")
        self.idate.set("")
        self.edate.set("")
        self.daily.set("")
        self.finfo.set("")
        self.bp.set("")
        self.se.set("") 
        self.text_pricreption.delete("1.0",END)  

    def exit(self):
        iexit=messagebox.askyesno("HOSPITAL MANAGEMENT SYSTEM","Conform Exit")
        if iexit>0:
            root.destroy()
            return


root=Tk()
obb=hospital(root)
root.mainloop()
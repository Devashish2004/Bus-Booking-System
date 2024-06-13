from tkinter import *
from tkinter.messagebox import*

import sqlite3

con=sqlite3.Connection('bus_booking_database')

root=Tk()

cur=con.cursor()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

root.title("Enter Journey Details")
Bus_select1=IntVar()

img_Bus=PhotoImage(file=".\\Bus_for_project.png")   
img_home=PhotoImage(file=".\\home.png")             
Button(root,image=img_home,bg="green").grid(row=3,column=40)   
Label(root,image=img_Bus).grid(row=0,column=0,padx=w//3+155,columnspan=81)  
                               

Label(root,text="Online Bus Booking System",font="Arial 35 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=81)
Label(root,text="Enter Journey Details",font="Arial 25 bold",bg="light green",fg="dark green").grid(row=2,column=0,columnspan=81,pady=30)

Label(root,text="From",font="Arial 15 bold").grid(row=3,column=35)
j_from=Entry(root)
j_from.grid(row=3,column=36)

Label(root,text="Journey Date",font="Arial 15 bold").grid(row=3,column=37)
j_date=Entry(root)
j_date.grid(row=3,column=38)

Label(root,text="To",font="Arial 15 bold").grid(row=3,column=33)
j_to=Entry(root)        
j_to.grid(row=3,column=34)



cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,name varchar(20),address varchar(20),phone int(10),email varchar(20))')
cur.execute('create table if not exists bus(bus_id number PRIMARY KEY,type varchar(30),capacity int(5),fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(bus_id) references runs(bus_id),foreign key(route_id) references route(route_id))')
cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
cur.execute('create table if not exists runs(bus_id number,date date ,seat_aval number,PRIMARY KEY(bus_id,date))')
cur.execute('create table if not exists history(pasg_name varchar(20),Gender varchar(12),no_of_seats number,mobile_no number PRIMARY KEY,age number,bus_select number,too varchar(13),fr varchar(13),date date,fare number)')

dict={}
            
def show_buses():
   if(j_to.get().isspace() or j_from.get().isspace() or j_date.get().isspace()):
      showerror("Error","please enter something")
   elif(j_to.get().isnumeric() or j_from.get().isnumeric()):
      showerror("value Missing","Enter city names correctly!")        
   elif(len(j_to.get())==0 or len(j_from.get())==0 or len(j_date.get())==0):
      showerror("value Missing","Enter in all the fields")
   else:
       b_to=j_to.get()
       b_fr=j_from.get()
       b_jd=j_date.get()

       val=(b_to,b_fr,b_jd)
       q='select name,type,seat_aval,capacity,fare,runs.bus_id from operator,bus,runs,route as t,route as f where operator.operator_id=bus.operator_id and bus.bus_id=runs.bus_id and bus.route_id=t.route_id and t.station_name=? and f.station_name=? and date=?'
       cur.execute(q,val)
       res1=cur.fetchall()
       #print(res1)
       
   

       c=1
       for t1 in res1:
           dict.update({c:t1})
           m=0
           for b in t1:
               Bus1=Radiobutton(root,text="BUS"+str(c),variable=Bus_select1,value=c,font="Arial 10 bold")
               Bus1.grid(row=6+c,column=33)
               Label(root,text=b,font="Arial 10 bold").grid(row=6+c,column=34+m)
               m=m+1
           c=c+1
       print(res1)

       Label(root,text=" ").grid(row=4,column=0)
       Label(root,text="Select Bus",font="Arial 13 bold",fg="dark green").grid(row=5,column=33)
       Label(root,text="Operator",font="Arial 13 bold",fg="dark green").grid(row=5,column=34)
       Label(root,text="Bus Type",font="Arial 13 bold",fg="dark green").grid(row=5,column=35)
       Label(root,text="Available",font="Arial 13 bold",fg="dark green").grid(row=5,column=36)
       Label(root,text="Capacity",font="Arial 13 bold",fg="dark green").grid(row=5,column=37)
       Label(root,text="Fare",font="Arial 13 bold",fg="dark green").grid(row=5,column=38)
       Button(root,text="Proceed To Book",font="Arial 13 bold",bg="light green",fg="black",command=proceed_to_booking).grid(row=6,column=39)
       
      

Button(root,text="Show Bus",font="Arial 15 bold",bg="light green",fg="black",command=show_buses).grid(row=3,column=39)
        
def proceed_to_booking():
    if Bus_select1.get()==0:
        showerror('select something','Please Select Bus')
    else:
        k=Bus_select1.get()
        p_detl=dict[k]
        
        Label(root,text="Fill Passenger Details To Book The Bus Ticket",font="Arial 20 bold",bg="light blue",fg="red").grid(row=13,column=0,columnspan=81,pady=30)

        Label(root,text="Name",font="Arial 15 bold").grid(row=14,column=33)
        p_name=Entry(root)
        p_name.grid(row=14,column=34)

        Label(root,text="Gender",font="Arial 15 bold").grid(row=14,column=35)
        p_gender=StringVar()
        p_gender.set("Gender")
        opt=("Male","Female","Other")
        d_menu=OptionMenu(root,p_gender,*opt).grid(row=14,column=36)

        Label(root,text="No. Of Seats",font="Arial 15 bold").grid(row=14,column=37)
        p_seats=Entry(root)
        p_seats.grid(row=14,column=38)

        Label(root,text="Mobile No.",font="Arial 15 bold").grid(row=14,column=39)
        p_mob=Entry(root)
        p_mob.grid(row=14,column=40)
        x=int(len(p_mob.get()))

        Label(root,text="Age",font="Arial 15 bold").grid(row=14,column=41)
        p_age=Entry(root)
        p_age.grid(row=14,column=42)

        def passenger_detail():
            if(len(p_name.get())==0 or len(p_seats.get())==0 or len(p_age.get())==0 or len(p_mob.get())==0):
                showerror("Missing","Enter all the fields")
            elif(p_name.get().isnumeric()):
                showerror("Missing","Enter Name correctly!")
            elif(p_seats.get().isalpha()):
                showerror("Error","Enter the seat in numeric")
            elif(len(p_mob.get())!=10) or p_mob.get().isalpha():
                showerror("Error","Enter 10 digit Mobile no.")
            elif(p_age.get().isalpha() or int(p_age.get())<=0 or int(p_age.get())>120 ):
                showerror("Missing","Enter age correctly!")
            else:
                if(askyesno('Confirm','Do you want to proceed ?')):
                            m=int(p_detl[2])
                            n=int(p_seats.get())
                            if(m-n>=0):
                                query1='update runs set seat_aval=(?) where bus_id=? and date=?'
                                value1=((m-n),p_detl[5],j_date.get())
                                cur.execute(query1,value1)
                                con.commit()
                            value=(p_name.get(),p_gender.get(),p_seats.get(),p_mob.get(),p_age.get(),p_detl[0],j_to.get(),j_from.get(),j_date.get(),p_detl[4])
                            query='insert into history(pasg_name,Gender,no_of_seats,mobile_no,age,bus_select,too,fr,date,fare)values(?,?,?,?,?,?,?,?,?,?)'
                            cur.execute(query,value)
                            con.commit() 
                            showinfo("Success","Booked Successfully")
                            s=int(p_seats.get())
                            f=int(p_detl[4])
                            v=s*f
                            showinfo('Fare','Fare is Rs.'+str(v))
                            if(askyesnocancel('Ticket','Want to get the TICKET')):
                               
                               root.destroy()
                               self.Page4_Check_Your_Booking()
                            else:
                               root.destroy()
                               self.Page2_Home_Page()
                else:
                   
                   showerror('Error','Seats not available')

        
        Button(root,text="Book Seat",font="Arial 13 bold",bg="light green",fg="black",command=passenger_detail).grid(row=14,column=43)

def Page_2_Home_Page():
    root.destroy()
    import Page_2_Home_Page
Button(root,image=img_home,bg='green').grid(row=3,column=40)
                                                                                
 
root.mainloop()


from tkinter import*
from tkinter.messagebox import*
import sqlite3
con=sqlite3.Connection('bus_booking_database')
cur=con.cursor()
root=Tk()
root.title("Add Bus Running Details")
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
fr=Frame(root)
fr.grid(row=0,column=2,columnspan=10)
img_Bus=PhotoImage(file=".\\Bus_for_project.png")
Label(fr,image=img_Bus).grid(row=0,column=2,padx=w//9)
fr.grid(row=1,column=2,columnspan=10)
Label(fr,text="Online Bus Booking System",font="Arial 30 bold",bg="light blue",fg="red").grid(row=1,column=2,pady=40) 
Label(root,text='Add Bus Running Details',font="Arial 20 bold",bg="white",fg="green" ).grid(row=2,column=2,columnspan=10)
Label(root,text='').grid(row=3,column=0,padx=50)

cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,name varchar(20),address varchar(20),phone int(10),email varchar(20))')
cur.execute('create table if not exists bus(bus_id number PRIMARY KEY,type varchar(30),capacity int(5),fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(bus_id) references runs(bus_id),foreign key(route_id) references route(route_id))')
cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
cur.execute('create table if not exists runs(bus_id number,date date ,seat_aval number,PRIMARY KEY(bus_id,date))')
cur.execute('create table if not exists history(pasg_name varchar(20),Gender varchar(12),no_of_seats number,mobile_no number PRIMARY KEY,age number,bus_select number,too varchar(13),fr varchar(13),date date,fare number)')


Label(root,text='Bus Id',font="Arial 12 bold").grid(row=3,column=1)
bus_id=Entry(root,font="Arial 12 bold")        
bus_id.grid(row=3,column=2)

Label(root,text='Running Date',font="Arial 12 bold").grid(row=3,column=3)
run_date=Entry(root,font="Arial 12 bold")
run_date.grid(row=3,column=4)

Label(root,text='Seat Available',font="Arial 12 bold").grid(row=3,column=5)
seat_avlb=Entry(root,font="Arial 12 bold")
seat_avlb.grid(row=3,column=6)

def addd():
    if len(bus_id.get())==0 or len(run_date.get())==0 or len(seat_avlb.get())==0:
        showerror('Value Missing','Please Enter The Values')
    elif(bus_id.get().isalpha()):
        showerror('Error','Enter Bus Id in numeric')
    
    elif(seat_avlb.get().isalpha()):
        showerror('Error','Enter Seat available in numeric')
    else:
        busid=bus_id.get()
        b_date=run_date.get()
        b_seat=seat_avlb.get()
        n=(busid,b_date,b_seat)
        qm='insert into runs(Bus_id ,date,seat_aval ) values(?,?,?)'
        cur.execute(qm,n)
        con.commit()
        
        bus_id.delete(0,END)
        run_date.delete(0,END)
        seat_avlb.delete(0,END)
        
        showinfo('Add  runs Entry','Bus runs Record Added')
        cur.execute('select * from runs')
        re=cur.fetchall()
        print(re)
    
        
        
def dell():
    if len(bus_id.get())==0 or len(run_date.get())==0 or len(seat_avlb.get())==0:
        showerror('Value Missing','Please Enter The Values')
    elif(bus_id.get().isalpha()):
        showerror('Error','Enter Bus Id in numeric')
    
    elif(seat_avlb.get().isalpha()):
        showerror('Error','Enter Seat available in numeric')
    else:
        y=bus_id.get()
        qq='select Bus_id from runs where Bus_id=?'
        cur.execute(qq,y)
        rest=cur.fetchall()
        if(rest):
            showinfo('found','runs Id Exist')
            x1=bus_id.get()
            query='delete from runs where Bus_id=?'
            cur.execute(query,x1)
            con.commit()
            
            bus_id.delete(0,END)
            run_date.delete(0,END)
            seat_avlb.delete(0,END)
 
            
            showinfo('Deleted','Runs Id Deleted')
            showinfo('Entry Deleted','Record Deleted Successfully')
        else:
            bus_id.delete(0,END)
            run_date.delete(0,END)
            seat_avlb.delete(0,END)
            showerror('error','Runs id did not exist')
        
    



Button(root,text="Add Run",font="Arial 15 bold",bg="light green",command=addd).grid(row=3,column=7,padx=50)   
Button(root,text="Delete Run",font="Arial 15 bold",bg="light green",fg="black",command=dell).grid(row=3,column=8,pady=50)
Home_img=PhotoImage(file=".\\home.png")   
Button(root,image=Home_img,bg="green").grid(row=4,column=8)       

root.mainloop()

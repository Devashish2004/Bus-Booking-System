from tkinter import*
from tkinter.messagebox import*
import sqlite3
con=sqlite3.Connection('bus_booking_database')
root=Tk()
root.title('Check Booking')
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
fr=Frame(root)
fr.grid(row=0,column=0,columnspan=20)
img_Bus=PhotoImage(file=".\\Bus_for_project.png")
Label(fr,image=img_Bus).grid(row=0,column=0,padx=w//4+210,columnspan=20)
fr.grid(row=1,column=0,columnspan=20)
cur=con.cursor()

cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,name varchar(20),address varchar(20),phone int(10),email varchar(20))')
cur.execute('create table if not exists bus(bus_id number PRIMARY KEY,type varchar(30),capacity int(5),fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(bus_id) references runs(bus_id),foreign key(route_id) references route(route_id))')
cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
cur.execute('create table if not exists runs(bus_id number,date date ,seat_aval number,PRIMARY KEY(bus_id,date))')
cur.execute('create table if not exists history(pasg_name varchar(20),Gender varchar(12),no_of_seats number,mobile_no number PRIMARY KEY,age number,bus_select number,too varchar(13),fr varchar(13),date date,fare number)')

def f1():
    root.destroy()
    import page2_book_seat
    
Label(fr,text="Online Bus Booking System",font="Arial 20 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=20,pady=17)
Label(root,text="Check Your Booking",font="Arial 15 bold",fg='black',bg="light green").grid(row=2,column=0,pady=20,columnspan=20)
Label(root,text="").grid(row=3,column=0,padx=190)

Label(root,text="Enter your Mobile No:",font="Arial 12 bold").grid(row=3,column=3)
enter_mobno=Entry(root,font="Arial 12 bold")
enter_mobno.grid(row=3,column=4)

def mob():
    if(len(enter_mobno.get())==0):
        showerror("Value Missing","Enter all details!!")
    elif(len(enter_mobno.get())!=10):
        showerror("entered wrong value","enter correct mobile no")
    elif(not(enter_mobno.get().isnumeric())):
        showerror("Wrong Value","Enter correct mobile no")
    else:

        fra=Frame(root,relief="groove",bd=7)
        fra.grid(row=5,column=0,columnspan=100)

        val=enter_mobno.get()
        cur.execute('select * from history where mobile_no=(?)',[val])

        result3=cur.fetchall()
        if(result3):
            Label(root,text="Bus ticket",font='arial 15 bold',fg='green').grid(row=4,column=2,columnspan=5)
            Label(fra,text="passenger:",font='Arial 10 bold',fg='red').grid(row=3,column=0)
            Label(fra,text=result3[0][0],font='Arial 10 bold').grid(row=3,column=1)
        
            Label(fra,text="gender:",font='Arial 10 bold',fg='red').grid(row=3,column=3)
            Label(fra,text=result3[0][1],font='Arial 10 bold').grid(row=3,column=4)
        
            Label(fra,text="no Of Seat:",font='Arial 10 bold',fg='red').grid(row=4,column=0)
            Label(fra,text=result3[0][2],font='Arial 10 bold').grid(row=4,column=1)

            Label(fra,text="bus no:",font='Arial 10 bold',fg='red').grid(row=5,column=3)
            Label(fra,text=result3[0][5],font='Arial 10 bold').grid(row=5,column=4)

            Label(fra,text="phone:",font='Arial 10 bold',fg='red').grid(row=4,column=3)
            Label(fra,text=result3[0][3],font='Arial 10 bold').grid(row=4,column=4)
        
            Label(fra,text="age:",font='Arial 10 bold',fg='red').grid(row=5,column=0)
            Label(fra,text=result3[0][4],font='Arial 10 bold').grid(row=5,column=1)
        
        
            Label(fra,text="from:",font='Arial 10 bold',fg='red').grid(row=6,column=0)
            Label(fra,text=result3[0][6],font='Arial 10 bold').grid(row=6,column=1)
        
        
        
            Label(fra,text="travel on:",font='Arial 10 bold',fg='red').grid(row=7,column=0)
            Label(fra,text=result3[0][8],font='Arial 10 bold' ).grid(row=7,column=1)

            Label(fra,text="to:",font='Arial 10 bold',fg='red').grid(row=6,column=3)
            Label(fra,text=result3[0][7],font='Arial 10 bold').grid(row=6,column=4)
            Label(fra,text="fare:",font='Arial 10 bold',fg='red').grid(row=7,column=3)
            Label(fra,text=result3[0][2]*result3[0][9],font='Arial 10 bold').grid(row=7,column=4)
            value=str(result3[0][2]*result3[0][9])

            Label(root,text="Your fare price is  Rs "+value,font='Arial 15 bold',fg='blue').grid(row=9,column=0,columnspan=82)
        else:
            showerror('wrong mobile no','no booking found with this mobile no')
            if(askyesno('continue Booking','Do you want to continue booking?')):
                root.destroy()
                import page3_Enter_Journey_Details_Show_Bus
        
         
Button(root,text="Check Booking",font="Arial 12 bold",command=mob).grid(row=3,column=5)
img_home=PhotoImage(file=".\\home.png")             
Button(root,image=img_home,bg="green",command=f1).grid(row=3,column=7)
        


root.mainloop()

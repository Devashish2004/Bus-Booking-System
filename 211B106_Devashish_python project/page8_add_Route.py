from tkinter import*
from tkinter.messagebox import*
import sqlite3
con=sqlite3.Connection('bus_booking_database')
cur=con.cursor()
root=Tk()
root.title("Add Route")
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
fr=Frame(root)
fr.grid(row=0,column=2,columnspan=10)
img_Bus=PhotoImage(file=".\\Bus_for_project.png")
Label(fr,image=img_Bus).grid(row=0,column=2,padx=w//10)
fr.grid(row=1,column=2,columnspan=10)
Label(fr,text="Online Bus Booking System",font="Arial 30 bold",bg="light blue",fg="red").grid(row=1,column=2,pady=40) 
Label(root,text='Add Bus Route Details',font="Arial 20 bold",bg="white",fg="green" ).grid(row=2,column=2,columnspan=10)
Label(root,text='').grid(row=3,column=0,padx=100)

cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,name varchar(20),address varchar(20),phone int(10),email varchar(20))')
cur.execute('create table if not exists bus(bus_id number PRIMARY KEY,type varchar(30),capacity int(5),fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(bus_id) references runs(bus_id),foreign key(route_id) references route(route_id))')
cur.execute('create table if not exists route(route_id number,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
cur.execute('create table if not exists runs(bus_id number,date date ,seat_aval number,PRIMARY KEY(bus_id,date))')
cur.execute('create table if not exists history(pasg_name varchar(20),Gender varchar(12),no_of_seats number,mobile_no number PRIMARY KEY,age number,bus_select number,too varchar(13),fr varchar(13),date date,fare number)')


Label(root,text='Route Id',font="Arial 12 bold").grid(row=3,column=1)
route_id=Entry(root,font="Arial 12 bold")   
route_id.grid(row=3,column=2)

Label(root,text='Station Name',font="Arial 12 bold").grid(row=3,column=3)
st_name=Entry(root,font="Arial 12 bold")
st_name.grid(row=3,column=4)

Label(root,text='Station ID',font="Arial 12 bold").grid(row=3,column=5)
st_id=Entry(root,font="Arial 12 bold")
st_id.grid(row=3,column=6)

def Add():
    if len(route_id.get())==0 or len(st_name.get())==0 or len(st_id.get())==0:
        showerror('Value Missing','Please Enter The Values')
    elif(route_id.get().isalpha()):
        showerror('Error','Enter Route Id in numeric')
    elif(st_name.get().isnumeric()):
        showerror('Error','Enter Station Name correctly')
    
    elif(st_id.get().isalpha()):
        showerror('Error','Enter Station Id in numeric')
    else:
        
        q='insert into route(route_id,station_name,station_id) values(?,?,?)'
        y=(route_id.get(),st_name.get(),st_id.get())
        cur.execute(q,y)
        con.commit() 
        showinfo('Add  Route Entry','Bus route Record Added')
        q2='select * from route where route_id=? and station_id=?'
        v2=(route_id.get(),st_id.get())
        cur.execute(q2,v2)
 
        result9=cur.fetchall()
        Label(root,text=result9).grid(row=4,column=4)
        route_id.delete(0,END)
        st_name.delete(0,END)
        st_id.delete(0,END)
        print(result9)
    
def dell():
    if len(route_id.get())==0 or len(st_name.get())==0 or len(st_id.get())==0:
        showerror('Value Missing','Please Enter The Values')
    elif(route_id.get().isalpha()):
        showerror('Error','Enter Route Id in numeric')
    elif(st_name.get().isnumeric()):
        showerror('Error','Enter Station Name correctly')
    elif(st_id.get().isalpha()):
        showerror('Error','Enter Station Id in numeric')
    else:    
        
        que='select route_id from route where route_id=?'
        yy=route_id.get()
        cur.execute(que,yy)
        ress=cur.fetchall()
        
        if(ress):
            showinfo('found','Route Id Exist')
            x=route_id.get()
            query='delete from route where route_id=?'
            cur.execute(query,x)
            con.commit()
            Label(root,text='                        ',font='arial 10 bold').grid(row=4,column=4)
            route_id.delete(0,END)
            st_name.delete(0,END)
            st_id.delete(0,END)
            showinfo('Deleted','Route Id Deleted')
            showinfo('Bus Route Entry Delete','Bus Route Record Deleted Successfully')
        else:
            route_id.delete(0,END)
            st_name.delete(0,END)
            st_id.delete(0,END)
            showerror('Error','Route Id not Exist')
    

Button(root,text="Add Route",font="Arial 15 bold",bg="light green",command=Add).grid(row=3,column=7,padx=10)   
Button(root,text="Delete Route",font="Arial 15 bold",bg="light green",fg="red",command=dell).grid(row=3,column=8,pady=50)
Home_img=PhotoImage(file=".\\home.png")   
Button(root,image=Home_img,bg="green").grid(row=4,column=8)       

root.mainloop()

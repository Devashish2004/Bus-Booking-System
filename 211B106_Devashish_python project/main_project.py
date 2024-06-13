from tkinter import*
from tkinter.messagebox import*

#DEVASHISH LAXKAR(B3) 211B106



class Test:
    def page9_Add_running(self):
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
        cur.execute('create table if not exists runs(bus_id number,date varchar(20),seat_aval number,PRIMARY KEY(bus_id,date))')
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
        
        def page2_book_seat():
            root.destroy()
            self.page2_book_seat()
        Button(root,text="Add Run",font="Arial 15 bold",bg="light green",command=addd).grid(row=3,column=7,padx=50)   
        Button(root,text="Delete Run",font="Arial 15 bold",bg="light green",fg="black",command=dell).grid(row=3,column=8,pady=50)
        Home_img=PhotoImage(file=".\\home.png")   
        Button(root,image=Home_img,bg="green",command=page2_book_seat).grid(row=4,column=8)       
        
        root.mainloop()

#DEVASHISH LAXKAR(B3) 211B106

  
    def page8_add_Route(self):
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
        cur.execute('create table if not exists runs(bus_id number,date varchar(20),seat_aval number,PRIMARY KEY(bus_id,date))')
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
        def page2_book_seat():
            root.destroy()
            self.page2_book_seat()

        Button(root,image=Home_img,bg="green",command=page2_book_seat).grid(row=4,column=8)       

        root.mainloop()

#DEVASHISH LAXKAR(B3) 211B106

    def page7_bus_details(self):
        import sqlite3

        root=Tk()
        root.title('Bus_Details')
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        fr=Frame(root)
        fr.grid(row=0,column=2,columnspan=10)

        img_Bus=PhotoImage(file=".\\Bus_for_project.png")

        Label(fr,image=img_Bus).grid(row=0,column=2,padx=w//15)

        fr.grid(row=1,column=2,columnspan=10)

        Label(fr,text="Online Bus Booking System",font="Arial 30 bold",bg="light blue",fg="red").grid(row=1,column=2,pady=40) 

        Label(root,text='Add Bus Details',font="Arial 20 bold",bg="white",fg="green" ).grid(row=2,column=2,columnspan=10)

        con=sqlite3.Connection('bus_booking_database')
        cur=con.cursor()
        cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,name varchar(20),address varchar(20),phone int(10),email varchar(20))')
        cur.execute('create table if not exists bus(bus_id number PRIMARY KEY,type varchar(30),capacity int(5),fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(bus_id) references runs(bus_id),foreign key(route_id) references route(route_id))')
        cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
        cur.execute('create table if not exists runs(bus_id number,date varchar(20),seat_aval number,PRIMARY KEY(bus_id,date))')
        cur.execute('create table if not exists history(pasg_name varchar(20),Gender varchar(12),no_of_seats number,mobile_no number PRIMARY KEY,age number,bus_select number,too varchar(13),fr varchar(13),date date,fare number)')



        Label(root,text='Bus Id',font="Arial 12 bold").grid(row=3,column=1)

        bus_id=Entry(root,font="Arial 12 bold")        
        bus_id.grid(row=3,column=2)

        Label(root,text='Bus Type',font="Arial 12 bold").grid(row=3,column=3)

        Bus_type=StringVar()
        opt=["AC 2X2","AC 3X2","Non AC 3X2","Non AC 2X2","Non-AC-Sleeper 2X1","AC-Sleeper 2X1"]


        Bus_type.set('Bustype')
        d_menu=OptionMenu(root,Bus_type,*opt).grid(row=3,column=4)          

        Label(root,text='Capacity',font="Arial 12 bold").grid(row=3,column=5)
        bus_cap=Entry(root,font="Arial 12 bold")
        bus_cap.grid(row=3,column=6,padx=0)

        Label(root,text='Fare Rs',font="Arial 12 bold").grid(row=3,column=7,padx=0)


        fare=Entry(root,font="Arial 12 bold")
        fare.grid(row=3,column=8,padx=0)

        Label(root,text='Operator ID',font="Arial 12 bold").grid(row=3,column=9,padx=0)


        op_id=Entry(root,font="Arial 10 bold")
        op_id.grid(row=3,column=10,padx=0)

        Label(root,text='Route ID',font="Arial 12 bold").grid(row=3,column=11,padx=0)


        route_id=Entry(root,font="Arial 12 bold")
        route_id.grid(row=3,column=12,pady=90)

        def bus_details1():
            if len(op_id.get())==0 or len(route_id.get())==0 or len(fare.get())==0 or len(bus_cap.get())==0 or len(bus_id.get())==0:
                showerror('Value Missing','Please Enter The Values')
            elif(op_id.get().isalpha()):
                showerror('Error','Enter Operator Id in numeric')
            elif(route_id.get().isalpha()):
                showerror('Error','Enter Route Id in numeric')
            elif(fare.get().isalpha()):
                showerror('Error','Enter Fare in numeric')
            elif(bus_cap.get().isalpha()):
                showerror('Error','Enter Capacity in numeric')
            elif(bus_id.get().isalpha()):
                showerror('Error','Enter Bus id in numeric')
            else:
                z=(bus_id.get(),Bus_type.get(),bus_cap.get(),fare.get(),op_id.get(),route_id.get())
                q=('insert into bus(bus_id,type,capacity,fare,route_id,operator_id) values(?,?,?,?,?,?)')
                cur.execute(q,z)
                con.commit()
                op_id.delete(0,END)
                route_id.delete(0,END)
                fare.delete(0,END)
                bus_cap.delete(0,END)
                bus_id.delete(0,END) 
                showinfo('Add Bus Entry','Bus Record Added')
                cur.execute('select * from bus')
                res=cur.fetchall()
                print(res)
            
                
        def Edit_Bus():
            if len(op_id.get())==0 or len(route_id.get())==0 or len(fare.get())==0 or len(bus_cap.get())==0 or len(bus_id.get())==0:
                showerror('Value Missing','Please Enter The Values')
            elif(op_id.get().isalpha()):
                showerror('Error','Enter Operator Id in numeric')
            elif(route_id.get().isalpha()):
                showerror('Error','Enter Route Id in numeric')
            elif(fare.get().isalpha()):
                showerror('Error','Enter Fare in numeric')
            elif(bus_cap.get().isalpha()):
                showerror('Error','Enter Capacity in numeric')
            elif(bus_id.get().isalpha()):
                showerror('Error','Enter Bus id in numeric')
            else:
                z1=(bus_id.get())
                q1='select * from bus where bus_id=?'
                cur.execute(q1,z1)
                resss=cur.fetchall()
                if(resss):
                    showinfo('Found','record found')
                    x=(Bus_type.get(),bus_cap.get(),fare.get(),route_id.get(),op_id.get(),bus_id.get())
                    q5='update bus set type=?,capacity=?,fare=?,route_id=?,operator_id =? where bus_id=?'
                    cur.execute(q5,x)
                    con.commit()
                    cur.execute('select * from bus')
                    result6=cur.fetchall()
                    #print(result6)
                    showinfo('Bus Entry Edit','Bus Record Edited Successfully') 
                else:
                    showerror('not found','error')

                op_id.delete(0,END)
                route_id.delete(0,END)


                fare.delete(0,END)
                bus_cap.delete(0,END)
                bus_id.delete(0,END)    
                #print(resss)
                
        

        Button(root,text="Add Bus",font="Arial 15 bold",bg="light green",command=bus_details1).grid(row=4,column=7)    


        Button(root,text="Edit Bus",font="Arial 15 bold",bg="light green",command=Edit_Bus).grid(row=4,column=8)

        Home_img=PhotoImage(file=".\\home.png")
        def page2_book_seat():
            root.destroy()
            self.page2_book_seat() 
        
        Button(root,image=Home_img,bg="green",command=page2_book_seat).grid(row=4,column=9)       
        root.mainloop()
#--------------------------------------------#DEVASHISH LAXKAR(B3) 211B106
    def page6_Operator_details(self):
        import sqlite3
        con=sqlite3.Connection('bus_booking_database')
        cur=con.cursor()
           
        
        root=Tk()

        root.title('Operator Details')

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        fr=Frame(root)

        cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,name varchar(20),address varchar(20),phone int(10),email varchar(20))')
        cur.execute('create table if not exists bus(bus_id number PRIMARY KEY,type varchar(30),capacity int(5),fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(bus_id) references runs(bus_id),foreign key(route_id) references route(route_id))')
        cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
        cur.execute('create table if not exists runs(bus_id number,date varchar(20),seat_aval number,PRIMARY KEY(bus_id,date))')
        cur.execute('create table if not exists history(pasg_name varchar(20),Gender varchar(12),no_of_seats number,mobile_no number PRIMARY KEY,age number,bus_select number,too varchar(13),fr varchar(13),date date,fare number)')


        fr.grid(row=0,column=0,columnspan=100)
        img_Bus=PhotoImage(file=".\\Bus_for_project.png")
        Label(fr,image=img_Bus).grid(row=0,column=0,padx=w//10+420,columnspan=100)
        fr.grid(row=1,column=0,columnspan=100)

        operator_id=0
        operator_name=0
        phone_no=0
        dddress=0    
        mail=0

        Label(fr,text="Online Bus Booking System",font="Arial 30 bold",bg="light blue",fg="red").grid(row=1,column=0,pady=40,columnspan=100) 

        Label(root,text='Add Bus Operator Details',font="Arial 17 bold",bg="white",fg="green" ).grid(row=2,column=0,columnspan=100,pady=5) 

        Label(root,text='Operator id',font="Arial 11 bold").grid(row=3,column=47)

        operator_id=Entry(root,font="Arial 10 bold")     
        operator_id.grid(row=3,column=48)

        Label(root,text='Name',font="Arial 11 bold").grid(row=3,column=49)

        operator_name=Entry(root,font="Arial 10 bold")
        operator_name.grid(row=3,column=50)          

        Label(root,text='Address',font="Arial 11 bold").grid(row=3,column=51)

        address=Entry(root,font="Arial 10 bold")
        address.grid(row=3,column=52)

        Label(root,text='Phone',font="Arial 11 bold").grid(row=3,column=53)

        ph_no=Entry(root,font="Arial 10 bold")     
        ph_no.grid(row=3,column=54)

        Label(root,text='Email',font="Arial 11 bold").grid(row=3,column=55)

        mail=Entry(root,font="Arial 10 bold")     
        mail.grid(row=3,column=56)

        def details():
            if(len(operator_id.get())==0 or len(operator_name.get())==0 or len(address.get())==0 or len(ph_no.get())==0 or len(mail.get())==0):
                showerror('Value Missing','Please Enter The Values')
            elif(operator_id.get().isalpha()):
                showerror('Error','Enter Operator Id in numeric')
            elif(operator_name.get().isnumeric()):
                showerror('Error','Enter Operator Name correctly')
            elif(address.get().isnumeric()):
                showerror('Error','Enter Address correctly')
            elif(ph_no.get().isalpha()):
                showerror('Error','Enter Mobile no. correctly')
            elif(len(ph_no.get())!=10):
                showerror('Error','Enter Mobile no. correctly 10 digits')
            else:
                operatorid1=operator_id.get()
                operatorname1=operator_name.get()
                address_op1=address.get()
                phoneno1=ph_no.get()
                operatoremail1=mail.get()

                q='insert into operator(operator_id,Name,address,phone,email) values(?,?,?,?,?)'
                v=(operatorid1,operatorname1,address_op1,phoneno1,operatoremail1)
                cur.execute(q,v)
                con.commit()
                cur.execute('select * from operator')
                res=cur.fetchall()
                Label(root,text=res,font='arial 11 bold').grid(row=4,column=10,columnspan=100)
                
                operator_id.delete(0,END)
                operator_name.delete(0,END)
                address.delete(0,END)
                ph_no.delete(0,END)
                mail.delete(0,END)
                showinfo('Operator Entry','Operator Record Added successfully')
                print(res)
                
        def edit_details():
            if(len(operator_id.get())==0 or len(operator_name.get())==0 or len(address.get())==0 or len(ph_no.get())==0 or len(mail.get())==0):
                showerror('Value Missing','Please Enter The Values')
            elif(operator_id.get().isalpha()):
                showerror('Error','Enter Operator Id in numeric')
            elif(operator_name.get().isnumeric()):
                showerror('Error','Enter Operator Name correctly')
            elif(address.get().isnumeric()):
                showerror('Error','Enter Address correctly')
            elif(ph_no.get().isalpha()):
                showerror('Error','Enter Mobile no. correctly')
            elif(len(ph_no.get())!=10):
                showerror('Error','Enter Mobile no. correctly 10 digits')
            else:

                operatorid1=operator_id.get()
                operatorname1=operator_name.get()

                address_op1=address.get()
                phoneno1=ph_no.get()

                operatoremail1=mail.get()
                del_id=operator_id.get()

                q1=('select operator_id from operator where operator_id=?')
                cur.execute(q1,operatorid1)

                result4=cur.fetchall()
                if(result4):
                    showinfo('Found','Operator ID Exist')
                    qu1='update operator set name=?,address=?,phone=?,email=? where operator_id=?'
                    va1=(operatorname1,address_op1,phoneno1,operatoremail1,operatorid1)
                    cur.execute(qu1,va1)
                    con.commit()

                    qu2='select * from operator where operator_id=?'
                    cur.execute(qu2,operatorid1)
                    result5=cur.fetchall()            
                    Label(root,text=result5,font='arial 11 bold').grid(row=4,column=10,columnspan=100)
                    
                    operator_id.delete(0,END)
                    operator_name.delete(0,END)
                    address.delete(0,END)
                    ph_no.delete(0,END)
                    mail.delete(0,END)
                    showinfo('Operator Entry','Operator Record updated')
                else:
                    showerror('not found!','operator id does not exists!!!')

        def page2_book_seat():
            root.destroy()
            self.page2_book_seat()        
          
        Button(root,text="Add",font="Arial 15 bold",bg="light green",command=details).grid(row=3,column=58,padx=0)   

        Button(root,text="Edit",font="Arial 15 bold",bg="light green",command=edit_details).grid(row=3,column=60,pady=20)

        img1=PhotoImage(file=".\\home.png")    

        Button(root,image=img1,bg="light green",command=page2_book_seat).grid(row=3,column=61)
        


        root.mainloop()
#-----------------------------------------#DEVASHISH LAXKAR(B3) 211B106
    def page5_check_booking(self):
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
        cur.execute('create table if not exists runs(bus_id number,date varchar(20),seat_aval number,PRIMARY KEY(bus_id,date))')
        cur.execute('create table if not exists history(pasg_name varchar(20),Gender varchar(12),no_of_seats number,mobile_no number PRIMARY KEY,age number,bus_select number,too varchar(13),fr varchar(13),date date,fare number)')

        
            
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
                
                
                    Label(fra,text="To:",font='Arial 10 bold',fg='red').grid(row=6,column=0)
                    Label(fra,text=result3[0][6],font='Arial 10 bold').grid(row=6,column=1)
                
                
                
                    Label(fra,text="travel on:",font='Arial 10 bold',fg='red').grid(row=7,column=0)
                    Label(fra,text=result3[0][8],font='Arial 10 bold' ).grid(row=7,column=1)


                    Label(fra,text="From:",font='Arial 10 bold',fg='red').grid(row=6,column=3)
                    Label(fra,text=result3[0][7],font='Arial 10 bold').grid(row=6,column=4)


                    Label(fra,text="fare:",font='Arial 10 bold',fg='red').grid(row=7,column=3)
                    Label(fra,text=result3[0][2]*result3[0][9],font='Arial 10 bold').grid(row=7,column=4)
                    value=str(result3[0][2]*result3[0][9])

                    Label(root,text="Your fare price is  Rs "+value,font='Arial 15 bold',fg='blue').grid(row=9,column=0,columnspan=82)
                else:
                    showerror('wrong mobile no','no booking found with this mobile no')
                    if(askyesno('continue Booking','Do you want to continue booking?')):
                        root.destroy()
                        self.page3_Enter_Journey_Details_Show_Bus()
                
        def page2_book_seat():
            root.destroy()
            self.page2_book_seat()        

        Button(root,text="Check Booking",font="Arial 12 bold",command=mob).grid(row=3,column=5)

        img_home=PhotoImage(file=".\\home.png")             
        Button(root,image=img_home,bg="green",command=page2_book_seat).grid(row=3,column=7)
        

        root.mainloop()

#---------------------------------------------#DEVASHISH LAXKAR(B3) 211B106
    def page4_new_details_to_database(self):
        root=Tk()
        root.title('Add new details')

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))

        fr=Frame(root)
        fr.grid(row=0,column=0,columnspan=10)
        img_Bus=PhotoImage(file=".\\Bus_for_project.png")

        Label(fr,image=img_Bus).grid(row=0,column=0,padx=w//4+200)
        fr.grid(row=1,column=0,columnspan=10)


        def page6_Operator_details():
            root.destroy()
            self.page6_Operator_details()
        def page7_bus_details():
            root.destroy()
            self.page7_bus_details()
        def page8_add_Route():
            root.destroy()
            self.page8_add_Route()
        def page9_Add_running():
            root.destroy()
            self.page9_Add_running()

        Button(root,text="New Operator",font="Arial 15 bold",bg="green",fg="black",command=page6_Operator_details).grid(row=3,column=1)

        Button(root,text="New Bus",font="Arial 15 bold",bg="orange",fg="black",command=page7_bus_details).grid(row=3,column=2)

        Label(fr,text="Online Bus Booking System",font="Arial 25 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=20,pady=20)

        Label(root,text="Add New Details to DataBase",font="Arial 25 bold",fg='green',bg="white").grid(row=2,column=0,pady=20,columnspan=20)

        Label(root,text="").grid(row=3,column=0,padx=150)


        Button(root,text="New Route",font="Arial 15 bold",bg="sky blue",fg="black",command=page8_add_Route).grid(row=3,column=3)

        Button(root,text="New Run",font="Arial 15 bold",fg='black',bg='red',command=page9_Add_running).grid(row=3,column=4)

        
        root.mainloop()

#-----------------------------------------
    def page3_Enter_Journey_Details_Show_Bus(self):
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

        cur.execute('create table if not exists runs(bus_id number,date varchar(20),seat_aval number,PRIMARY KEY(bus_id,date))')

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
                                    s=int(p_seats.get())
                                    f=int(p_detl[4])
                                    v=s*f
                                    showinfo('Fare','Fare is Rs.'+str(v))
                                    showinfo("Success","Booked Successfully")
                                    if(askyesnocancel('Ticket','Want to get the TICKET')):
                                        
                                        root.destroy()
                                        self.page5_check_booking()
                                    
                        else:
                           
                           showerror('Error','Seats not available')

                
                Button(root,text="Book Seat",font="Arial 13 bold",bg="light green",fg="black",command=passenger_detail).grid(row=14,column=43)

        def page2_book_seat():
            root.destroy()
            self.page2_book_seat()

        Button(root,image=img_home,bg='green',command=page2_book_seat).grid(row=3,column=40)
                                                                                        
         
        root.mainloop()

#-------------------------------------------------#DEVASHISH LAXKAR(B3) 211B106
    def page2_book_seat(self):
        
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))

        fr=Frame(root)
        fr.grid(row=0,column=0,columnspan=10)

        img_Bus=PhotoImage(file=".\\Bus_for_project.png")


        Label(fr,image=img_Bus).grid(row=0,column=1,padx=w//3+140)


        fr.grid(row=1,column=0,columnspan=10)


        Label(fr,text="Online Bus Booking System",font="Arial 25 bold",bg="light blue",fg="red").grid(row=1,column=1,pady=50)


        Label(root,text="").grid(row=2,column=0,padx=w//9)

        def page3_Enter_Journey_Details_Show_Bus():
            root.destroy()
            self.page3_Enter_Journey_Details_Show_Bus()
             
        def page4_new_details_to_database():
            root.destroy()
            self.page4_new_details_to_database()
        def page5_check_booking():
            root.destroy()
            self.page5_check_booking()


        Button(root,text="Seat Booking",font="Arial 15 bold",bg="light green",fg="black",command=page3_Enter_Journey_Details_Show_Bus).grid(row=2,column=1,columnspan=2)

        Button(root,text="Check Booked Seat",font="Arial 15 bold",bg="spring green",fg="black",command=page5_check_booking).grid(row=2,column=3)

        Button(root,text="Add Bus Details",font="Arial 15 bold",bg="dark green",fg="black",command=page4_new_details_to_database).grid(row=2,column=3,columnspan=5)


        Label(root,text="For Admin Only",font="Arial 11 bold",fg='red').grid(row=3,column=4)

        
        root.mainloop()
#---------------------------------- #DEVASHISH LAXKAR(B3) 211B106       
    def page1_front_page(self):
        
        root=Tk()
        root.title('Online Bus Booking System')
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file=".\\Bus_for_project.png")


        Label(root,image=img).pack()

        Label(root,text="Online Bus Booking System",bg='light blue',fg='red',font='arial 25 bold').pack(pady=20)

        Label(root,text="NAME: DEVASHISH LAXKAR",font='arial 16 bold',fg='blue').pack(pady=20)

        Label(root,text="ER: 211B106",font='arial 16 bold',fg='blue').pack(pady=20)

        Label(root,text="MOB: 9653928124",font='arial 16 bold',fg='blue').pack(pady=20)

        Label(root,text="Submmited to: DR.MAHESH KUMAR",bg='light blue',fg='red',font='arial 25 bold').pack()

        Label(root,text="Python based learning",font='arial 12 bold',fg='red').pack()

        def close(e=0):
            
            root.destroy()
            self.page2_book_seat()
        root.bind('<KeyPress>',close)
        root.mainloop()



t=Test()
t.page1_front_page()

        

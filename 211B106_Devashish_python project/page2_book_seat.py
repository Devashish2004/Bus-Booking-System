from tkinter import*
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
Button(root,text="Seat Booking",font="Arial 15 bold",bg="light green",fg="black").grid(row=2,column=1,columnspan=2)

Button(root,text="Check Booked Seat",font="Arial 15 bold",bg="spring green",fg="black").grid(row=2,column=3)

Button(root,text="Add Bus Details",font="Arial 15 bold",bg="dark green",fg="black").grid(row=2,column=3,columnspan=5)

Label(root,text="For Admin Only",font="Arial 11 bold",fg='red').grid(row=3,column=4)

def fun_A():
    root.destroy()
    import page3_Enter_Journey_Details_Show_Bus
def fun_B():
    root.destroy()
    import page5_check_booking
def fun_C():
    root.destroy()
    import page4_new_details_to_database


root.mainloop()

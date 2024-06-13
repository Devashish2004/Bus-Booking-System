from tkinter import*
root=Tk()
root.title('Add new details')
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

fr=Frame(root)
fr.grid(row=0,column=0,columnspan=10)
img_Bus=PhotoImage(file=".\\Bus_for_project.png")

Label(fr,image=img_Bus).grid(row=0,column=0,padx=w//4+200)
fr.grid(row=1,column=0,columnspan=10)

Button(root,text="New Operator",font="Arial 15 bold",bg="green",fg="black").grid(row=3,column=1)

Button(root,text="New Bus",font="Arial 15 bold",bg="orange",fg="black").grid(row=3,column=2)

Label(fr,text="Online Bus Booking System",font="Arial 25 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=20,pady=20)

Label(root,text="Add New Details to DataBase",font="Arial 25 bold",fg='green',bg="white").grid(row=2,column=0,pady=20,columnspan=20)

Label(root,text="").grid(row=3,column=0,padx=150)


Button(root,text="New Route",font="Arial 15 bold",bg="sky blue",fg="black").grid(row=3,column=3)

Button(root,text="New Run",font="Arial 15 bold",fg='black',bg='red').grid(row=3,column=4)


root.mainloop()

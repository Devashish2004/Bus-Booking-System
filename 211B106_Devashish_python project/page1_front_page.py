from tkinter import*
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

def close(page2_book_seat):
    root.destroy()
root.bind('<Motion>',close)
root.mainloop()



root.mainloop()

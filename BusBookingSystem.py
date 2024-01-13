from tkinter import *
from tkinter import messagebox
import random
import tkinter.ttk as ttk
import sqlite3
import re
from datetime import datetime, timedelta

class BusBookingSystem(Tk):
    #Front Page of the System.\\Bus_for_project.png
    def front_page():
        root=Tk()
        root.title("Bus booking system")
        icon=PhotoImage(file="buslogo.png")
        root.iconphoto(True,icon)
        w=root.winfo_screenwidth() 
        h=root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        busImage=PhotoImage(file="Bus_for_project.png")
        Label(root,image=busImage).pack()
        Label(root,text="                             ").pack()
        Label(root,text="Online Bus Booking System",font='Arial 20 bold',fg='Red',bg="gray61").pack()
        Label(root,text="                             ").pack()
        Label(root,text="Name : Vansh Verma",font='Arial 11 bold',fg='Blue').pack()
        Label(root,text="Enrollment No. : 221B431",fg="BLue",font='Arial 11 bold').pack()#.grid(row=3,column=0,pady=h//50)
        Label(root,text="Mobile : 8962022963",fg="BLue",font='Arial 11 bold').pack()#.grid(row=4,column=0,pady=h//50)
        Label(root,text="                             ").pack()
        Label(root,text="Submitted to : Dr. Mahesh Kumar",fg="Red",bg="gray61",font='Arial 20 bold').pack()#.grid(row=5,column=0,pady=h//25)
        Label(root,text="                             ").pack()
        Label(root,text="PROJECT BASED LEARNING",font='Arial 15 bold',fg="Blue").pack()#.grid(row=6,column=0)
        Label(root,text='Enter SPACE to continue',font='Arial 18 bold',fg="Blue",pady=20).pack()
        def close(x=0):
            root.destroy()
            obj.Home_page()
        root.bind('<space>',close)
        root.mainloop()

    def Admin_page():
        root = Tk()
        root.title("Admin Page")
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        
        
        
        # Create a centered box
        box_width = 300
        box_height = 200
        x = (w - box_width) // 2
        y = (h - box_height) // 2

        admin_box = Toplevel(root)
        admin_box.geometry(f'{box_width}x{box_height}+{x}+{y}')
        admin_box.title("Authentication")

         # Login form widgets
        username_label = Label(admin_box, text="Username:")
        username_label.pack(pady=5)
        username_entry = Entry(admin_box)
        username_entry.pack(pady=5)

        password_label = Label(admin_box, text="Password:")
        password_label.pack(pady=5)
        password_entry = Entry(admin_box, show="*")
        password_entry.pack(pady=5)


        authenticated = False  

        def authenticate():
            nonlocal authenticated #using the variable created outside
            # Replace this with your actual authentication logic
            if username_entry.get() == "admin" and password_entry.get() == "password":
                messagebox.showinfo("Login Successful", "Welcome, Admin!")
                authenticated = True #setting this true
                admin_box.destroy() # Close the admin box after successful login
                content_admin_page() #displaying the content

            else:
                messagebox.showwarning("Login Failed", "Invalid username or password")

        #binding ENTER key with lOGIN button
        admin_box.bind("<Return>", lambda event=None: authenticate())

        login_button = Button(admin_box, text="Login", command=authenticate)
        login_button.pack(pady=10)

        # Keep the admin_box above the admin page
        admin_box.transient(root)
        admin_box.grab_set()

        #Close the window if the admin bx is closed without authenticating
        def on_admin_box_close():
             if not authenticated:
                root.destroy()

        admin_box.protocol("WM_DELETE_WINDOW", on_admin_box_close)


        #content of the Admin Page
        def content_admin_page():
    
            label = Label(root, text="Admin Page", fg="blue", font="Arial 20 bold", bg=root.cget("bg"))
            label.place(relx=0.5, rely=0, anchor="n")
            
            #add content here
            
            


            def on_close():
                root.destroy()
            root.protocol("WM_DELETE_WINDOW", on_close)
            
        
        
        
        root.mainloop()

    #admin Page End







    #Home Page of the System
    def Home_page():
        root=Tk()
        root.title("Bus booking system")
        icon=PhotoImage(file="buslogo.png")
        root.iconphoto(True,icon)
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file='Bus_for_project.png')
        Label(root,image=img).grid(row=0,column=0,columnspan=3,padx=w//2.5)
        Label(root,text="Online Bus Booking System",fg="Red",bg="gray61",font="Arial 20 bold").grid(row=1,column=0,columnspan=3)
        #Seat booking page
        def seat_booking_page(x=0):
            root.destroy()
            obj.Seat_Booking_page()
            #Check Booked page
        def check_booking_page(y=0):
            root.destroy()
            obj.Checking_booking()
            #Add Bus Details page
        def add_bus_details_page(z=0):
            root.destroy()
            obj.Add_new_bus_details_page()
        def Admin_page(m=0):
            root.destroy()
            obj.Admin_page()
            #Buttons
        b1=Button(root,text="Seat Booking", font='Arial 15 bold',bg='orchid2',command=seat_booking_page).grid(row=2,column=0)
        b2=Button(root,text="Check Booked Seat", font='Arial 15 bold',bg='orchid3', command=check_booking_page).grid(row=2,column=1)
        b3=Button(root,text="Add Bus Details", font='Arial 15 bold',bg='orchid4',command=add_bus_details_page).grid(row=2,column=2,pady=h//15)
        b4=Button(root,text="For Admin Only",font='Arial 10 bold',fg="Red",command=Admin_page).grid(row=5,column=2)
        root.mainloop()
    
    #Seating Booking Page of the System222
    def Seat_Booking_page():
        root=Tk()
        root.title("Bus booking system")
        icon=PhotoImage(file="buslogo.png")
        root.iconphoto(True,icon)
        with sqlite3.connect('Bus_Booking.db') as con:
            cur=con.cursor()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        #gender drop_menu options
        gender_type=StringVar()
        gender_type.set("Gender")
        options_gender_type=["Male","Female","Others"]
        #adding bus image to the page
        busImage=PhotoImage(file='Bus_for_project.png')
        home_Image=PhotoImage(file='home.png')
        Label(root,image=busImage).grid(row=0,column=0,padx=w//2.5,columnspan=8)
        #Adding Application name
        Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font='Arial 20 bold').grid(row=1,column=0,columnspan=8)
        Label(root,text='Enter Journey Details',bg='pale green',fg='dark green',font='Arial 15 bold').grid(row=2,column=0,columnspan=8,pady=h//20)
        #function to check if all fields are filled or not

        def checkTo(boarding):
            return boarding.isalpha()

        def checkFrom(destinate):
            return destinate.isalpha()

        def checkDate(datee):
            if re.fullmatch(r'\d{4}-\d{2}-\d{2}', datee) and datetime.today() <= datetime.strptime(datee, '%Y-%m-%d') <= datetime.today() + timedelta(days=365):

                return True

            return False
                
        def check_seat_mob_age(num):
            return num.isnumeric()

        def check_seat_age(num):
            num1=int(num)
            if(num1>0 and num1<100):
                return num.isnumeric()
            else:
                return False

        def bookingref():
            return (random.randint(10000,99999))

        #yes no and the end
        def sure(name,seats,mobile,age,JDate,going,idd):
            booking_ref=bookingref()
            bkddate=cur.execute("Select Date('now')")
            bookedDate=bkddate.fetchall()
            fare=cur.execute('Select distinct Fare from Bus where Bus_ID=?;',(idd,))
            faree=fare.fetchall()
            avail=cur.execute('Select distinct Seats_Available from Run where Bus_ID=?;',(idd,))
            leftseat=avail.fetchall()
            x=(int)(seats)
            seatleft=leftseat[0][0]-x
            cur.execute('Update Run set Seats_Available=? where Bus_ID=?;',(seatleft,idd,))
            price=faree[0][0]*x
            mobilee=(int)(mobile)
            temp=cur.execute('Select count(*) from Passenger_details')
            idpass=temp.fetchall()
            operatorName=cur.execute('Select op.Name from Bus as b, Operator as op where op.Operator_ID=b.Operator_ID and b.Bus_ID=?;',(idd,))
            operatorNamee=operatorName.fetchall()
            passengerid=[111,112,113,114,115,116,117,118,119,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,11122,11123,11124,11125,11126,11127,11128,11129,11130]
            passengerDetails=cur.execute('''insert into Passenger_details(Passenger,Seats,Age,Booking_ref,travelDate,Phone,Fare,Bus_details,Booked_date,Boarding_point,Gender,passengerID)
            values(?,?,?,?,?,?,?,?,?,?,?,?);''',(name,seats,age,booking_ref,JDate,mobilee,price,operatorNamee[0][0],bookedDate[0][0],going,gender_type.get(),passengerid[idpass[0][0]]))
            con.commit()
            root.destroy()
            obj.Booking_Details()

        def checkFilling():
            if len(goingTo.get())==0:
                messagebox.showerror('Value missing','Enter Boarding')
                return
            elif len(destination.get())==0:
                messagebox.showerror('Value missing','Enter Destination')
                return 
            elif len(Jdate.get())==0:
                messagebox.showerror('Value missing','Enter Date')
                return
            else:
                if checkTo(goingTo.get())==True and checkFrom(destination.get())==True and checkDate(Jdate.get())==True:
                    showDetails(Jdate.get(),destination.get(),goingTo.get())
                else:
                    messagebox.showerror('Invalid Entry',"Enter Details Properly")

        name_entt=''
        mobile_entt=0
        age_entt=0
        seats_entt=0

        def showDetails(Jdate,fromm,tto):
            temp=cur.execute('''Select distinct op.Name ,b.Type, b.Capacity, b.Fare, b.Bus_ID from Operator as op, Bus as b, Route as r, Run as rn
            where r.Route_ID=b.Route_ID and op.Operator_ID=b.Operator_ID and rn.Date=? and rn.Bus_ID=b.Bus_ID and r.stationName=? and 
            r.destinationName=?;''',(Jdate,fromm,tto,))
            details=temp.fetchall()
            select_text = Label(root, text = "Select Bus", fg = "green",pady=h//30)
            select_text.grid(row = 4, column=0)
            opt_text = Label(root, text = "Operator", fg = "green")
            opt_text.grid(row = 4, column=1)

            type_text = Label(root, text = "Bus Type", fg = "green")
            type_text.grid(row = 4, column=2)

            available_text = Label(root, text = "Available/Capacity", fg = "green")
            available_text.grid(row = 4, column=3)

            fare_text = Label(root, text = "Fare", fg = "green")
            fare_text.grid(row = 4, column=4)

            j=1
            x=5
            ip_type=IntVar()
            for i in range(0,len(details)):
                r=ttk.Radiobutton(root,text='Bus'+str(j),variable=ip_type, value=details[i][4])
                r.grid(row=5+i,column=0)
                temp1=cur.execute('''Select distinct rn.Seats_Available from Operator as op, Bus as b, Run as rn where op.Operator_ID=b.Operator_ID and b.Bus_ID=rn.Bus_ID and b.Capacity=?;''',(details[i][2],))
                xyz=temp1.fetchall()
                Label(root,text=details[i][0]).grid(row=5+i,column=1)
                Label(root,text=details[i][1]).grid(row=5+i,column=2)
                Label(root,text=str(xyz[0][0])+"/"+str(details[i][2])).grid(row=5+i,column=3)
                Label(root,text=details[i][3]).grid(row=5+i,column=4)
                x+=1
                j+=1            
            
            book_button = Button(root, text="Proceed to Book", bg = "lightgreen", command =lambda:book(ip_type.get(),x,Jdate,fromm))
            book_button.grid(row =5 , column= 5, pady=h//50)
            

        def book(idd,x,JDate,going):
            if idd!=0:
                fill_label = Label(root, text = "Fill Passenger Details to book the bus ticket" , fg = 'red' , bg = 'lightblue', font = 'Arian 14 bold')
                fill_label.grid(row = x+1, column = 0, columnspan = 8,pady=h//30)

                name_text = Label(root, text = "Name")
                name_text.grid(row = x+2, column=0)

                name_ent = Entry(root)
                name_ent.grid(row =x+2, column=1)
                name_entt=name_ent.get()

                Label(root,text='Gender',font='Arial 13').grid(row=x+2,column=2)
                d_menu=OptionMenu(root,gender_type,*options_gender_type)
                d_menu.grid(row=x+2,column=3)

                seats_text = Label(root, text = "No of Seats")
                seats_text.grid(row = x+2, column=4)

                seats_ent = Entry(root)
                seats_ent.grid(row =x+2, column=5)

                mobile_text = Label(root, text = "Mobile No")
                mobile_text.grid(row = x+2, column=6)

                mobile_ent = Entry(root)
                mobile_ent.grid(row =x+2, column=7)

                age_text = Label(root, text = "Age")
                age_text.grid(row = x+3, column=4,pady=h//50)

                age_ent = Entry(root)
                age_ent.grid(row =x+3, column=5)

                book_button = Button(root, text = "Book Seat", bg ="lightgreen", command =lambda:checking(name_ent.get(),seats_ent.get(),mobile_ent.get(),age_ent.get(),JDate,going,idd))
                book_button.grid(row = x+3, column=6)
            else:
                messagebox.showerror('Selection error','Bus not selected')


        def checking(name,seats,mobileNumber,age,JDate,going,idd):
            a=cur.execute('Select Seats_Available from Run where Bus_ID=?;',(idd,))
            enw=a.fetchall()
            cap=enw[0][0]
            capac=int(cap)
            def checkseatslimit(x):
                y=int(x)
                if capac>y and y>0:
                    return True
                else:
                    return False
            # aage=(int)(age)
            if len(name)==0:
                messagebox.showerror('Invalid Entry',"Enter Name Properly")
                return
            elif len(str(mobileNumber))<10:
                messagebox.showerror('Invalid Entry',"Enter Number Properly")
                return
            elif len(str(age))==0:
                messagebox.showerror('Invalid Entry',"Enter Age Properly")
                return
            elif len(str(seats))==0 or checkseatslimit(seats)==False:
                messagebox.showerror('Invalid Entry',"Enter seats Properly")
                return
            elif gender_type.get() not in options_gender_type:
                messagebox.showerror('Invalid Entry',"Enter Gender properly")
                return
            else:       
                if checkTo(name)==True and check_seat_mob_age(seats)==True and check_seat_mob_age(mobileNumber)==True and check_seat_age(age)==True:
                    sure(name,seats,mobileNumber,age,JDate,going,idd)
                else:
                    messagebox.showwarning('Invalid Entry',"Enter Details Properly")
        #to
        Label(root,text="To:").grid(row=3,column=0)
        goingTo=Entry(root)
        goingTo.grid(row=3,column=1)
        tto=goingTo.get()

        #from
        Label(root,text="From:").grid(row=3,column=2)
        destination=Entry(root)
        destination.grid(row=3,column=3)
        fromm=destination.get()

        #Journey date
        Label(root,text="Journey Date:").grid(row=3,column=4)
        Label(root,text="(YYYY-MM-DD)").grid(row=4,column=5)

        Jdate=Entry(root)
        Jdate.grid(row=3,column=5)

        def homePage():
            root.destroy()
            obj.Home_page()

        #Buttons
        Button(root,text="Show Bus",bg="pale green",command=checkFilling).grid(row=3,column=6)
        Button(root,image=home_Image,command=homePage).grid(row=3,column=7)
        #Button(root,image=home_Image).grid(row=3,column=7)
        root.mainloop()
    
    #Booking Details
    def Booking_Details():
        root=Tk()
        root.title("Bus booking system")
        icon=PhotoImage(file="buslogo.png")
        root.iconphoto(True,icon) 

        with sqlite3.connect('Bus_Booking.db') as con:
            cur=con.cursor()
        root.title("Bus Booking System")
        h,w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))
        #bus image
        busImage=PhotoImage(file='Bus_for_project.png')
        home_Image=PhotoImage(file='home.png')
        Label(root,image=busImage).grid(row=0,column=0,padx=w//2.5,columnspan=3)
        Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font='Arial 20 bold').grid(row=1,column=0,columnspan=4)
        Label(root,text="Bus Ticket").grid(row=2,column=0,columnspan=3,pady=h//40)

        passengerid=[111,112,113,114,115,116,117,118,119,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,11122,11123,11124,11125,11126,11127,11128,11129,11130]
        temp=cur.execute('Select count(*) from Passenger_details')
        idpasse=temp.fetchall()

        temp1=cur.execute('Select * from Passenger_details where passengerID=?;',(passengerid[idpasse[0][0]-1],))
        alldetails=temp1.fetchall()

        final = Frame(root,relief='groove',bd=5)
        final.grid(row = 3, column =0, columnspan=3)

        #passengerName
        passenger_text = Label(final, text = "Passenger: ")
        passenger_text.grid(row =3, column=0)
        passenger_text1 = Label(final, text = alldetails[0][0])
        passenger_text1.grid(row =3, column=1)

        #passengerseat
        seats_text = Label(final, text = "No of seats: ")
        seats_text.grid(row =4, column=0)
        seats_text1 = Label(final, text = alldetails[0][1])
        seats_text1.grid(row =4, column=1)

        #Age
        age_text = Label(final, text = "Age: ")
        age_text.grid(row =5, column=0)
        age_text1 = Label(final, text = alldetails[0][2])
        age_text1.grid(row =5, column=1)

        #booking_Ref
        bookingref=Label(final, text = "Booking Ref: ")
        bookingref.grid(row =6, column=0)
        bookingref1=Label(final, text = alldetails[0][3])
        bookingref1.grid(row =6, column=1)

        #Travel_date
        bookingref=Label(final, text = "Travel Date: ")
        bookingref.grid(row =7, column=0)
        bookingref1=Label(final, text = alldetails[0][4])
        bookingref1.grid(row =7, column=1)

        #gender
        g_text = Label(final, text = "Gender: ")
        g_text.grid(row =3, column=2)
        g_text1 = Label(final, text = alldetails[0][10])
        g_text1.grid(row =3, column=3)

        #Mobile Number
        phone_text = Label(final, text = "Phone: ")
        phone_text.grid(row =4, column=2)
        phone_text1 = Label(final, text = alldetails[0][5])
        phone_text1.grid(row =4, column=3)

        #Price
        flare_text = Label(final, text = "Fare Rs: ")
        flare_text.grid(row =5, column=2)
        flare_text1 = Label(final, text =alldetails[0][6])
        flare_text1.grid(row =5, column=3)

        #Bus
        detail_text = Label(final, text = "Bus Detail: ")
        detail_text.grid(row =6, column=2)
        detail_text1 = Label(final, text = alldetails[0][7])
        detail_text1.grid(row =6, column=3)

        #Booked on
        booked_text = Label(final, text = "Booked On: ")
        booked_text.grid(row =7, column=2)
        booked_text1 = Label(final, text = alldetails[0][8])
        booked_text1.grid(row =7, column=3)

        #Boarding
        point_text = Label(final, text = "Boarding Point: ")
        point_text.grid(row =8, column=2)
        point_text1 = Label(final, text = alldetails[0][9])
        point_text1.grid(row =8, column=3)

        price=alldetails[0][6]*alldetails[0][1]

        last_text = Label(final, text = "Total amount Rs"+str(price)+" to be paid at the time of boarding the bus",font="Arial 8 italic")
        last_text.grid(row =9, column=2)

        messagebox.showinfo("Booking conformed", "Booked!!!")

        def checking2():
            root.destroy()
            obj.Home_page()

        Button(root,image=home_Image,font='Arial 15',bg='pale green',command=checking2).grid(row=2,column=2     )

        root.mainloop()

    #checking booking
    def Checking_booking():
        root=Tk()
        root.title("Bus booking system")
        icon=PhotoImage(file="buslogo.png")
        root.iconphoto(True,icon)

        with sqlite3.connect('Bus_Booking.db') as con:
            cur=con.cursor()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        busImage=PhotoImage(file='Bus_for_project.png')
        home_Image=PhotoImage(file='home.png')
        Label(root,image=busImage).grid(row=0,column=0,padx=w//2.5,columnspan=12)
        Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font='Arial 20 bold').grid(row=1,column=0,columnspan=12,pady=h/50)
        Label(root,text='Check Bus Booking',fg='dark green',font='Arial 15 bold',bg='pale green').grid(row=2,column=0,columnspan=12)
        Label(root,text='Enter Your Mobile No:',font='Arial 10 bold').grid(row=3,column=4,pady=h/50)
        mobNumber=Entry(root)
        mobNumber.grid(row=3,column=5)
        def checknumber(s):
            count=0
            for i in s:
                if i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
                    count+=1
            if count==10:
                return True
            else:
                return False
        def entrycheck():
            if len(mobNumber.get())!=10:
                messagebox.showerror('Value missing','Enter correct Mobile Number')
            elif checknumber(mobNumber.get())==False:
                messagebox.showerror('Invalid input','Enter number properly')
            else:
                mobile=mobNumber.get()
                temp=cur.execute('Select * from Passenger_details where Phone=?;',(mobile,))
                alldetails=temp.fetchall()
                temp1=cur.execute('Select passengerID from Passenger_details where Phone=?;',(mobile,))
                passID=temp1.fetchall()
                final = Frame(root,relief='groove',bd=5)
                final.grid(row = 5, column =4, columnspan=3,pady=h//20)
                #passengerName
                passenger_text = Label(final, text = "Passenger: ")
                passenger_text.grid(row =5, column=0)          
                passenger_text1 = Label(final, text = alldetails[0][0])
                passenger_text1.grid(row =5, column=1)

                #passengerseat
                seats_text = Label(final, text = "No of seats: ")
                seats_text.grid(row =6, column=0)
                seats_text1 = Label(final, text = alldetails[0][1])
                seats_text1.grid(row =6, column=1)

                #Age
                age_text = Label(final, text = "Age: ")
                age_text.grid(row =7, column=0)
                age_text1 = Label(final, text = alldetails[0][2])
                age_text1.grid(row =7, column=1)

                #booking_Ref
                bookingref=Label(final, text = "Booking Ref: ")
                bookingref.grid(row =8, column=0)
                bookingref1=Label(final, text = alldetails[0][3])
                bookingref1.grid(row =8, column=1)

                #Travel_date
                bookingref2=Label(final, text = "Travel Date: ")
                bookingref2.grid(row =9, column=0)
                bookingref3=Label(final, text = alldetails[0][4])
                bookingref3.grid(row =9, column=1)

                #gender
                g_text = Label(final, text = "Gender: ")
                g_text.grid(row =5, column=2)
                g_text1 = Label(final, text = alldetails[0][10])
                g_text1.grid(row =5, column=3)

                #Mobile Number
                phone_text = Label(final, text = "Phone: ")
                phone_text.grid(row =6, column=2)
                phone_text1 = Label(final, text = alldetails[0][5])
                phone_text1.grid(row =6, column=3)

                #Price
                flare_text = Label(final, text = "Fare Rs: ")
                flare_text.grid(row =7, column=2)
                flare_text1 = Label(final, text =alldetails[0][6])
                flare_text1.grid(row =7, column=3)

                #Bus
                detail_text = Label(final, text = "Bus Detail: ")
                detail_text.grid(row =8, column=2)
                detail_text1 = Label(final, text = alldetails[0][7])
                detail_text1.grid(row =8, column=3)

                #Booked on
                booked_text = Label(final, text = "Booked On: ")
                booked_text.grid(row =9, column=2)
                booked_text1 = Label(final, text = alldetails[0][8])
                booked_text1.grid(row =9, column=3)

                #Boarding
                point_text = Label(final, text = "Boarding Point: ")
                point_text.grid(row =10, column=2)
                point_text1 = Label(final, text = alldetails[0][9])
                point_text1.grid(row =10, column=3)

                price=alldetails[0][6]*alldetails[0][1]
                last_text = Label(final, text = "Total amount Rs"+str(price)+" to be paid at the time of boarding the bus",font="Arial 8 italic")
                last_text.grid(row =11, column=2)

        Button(root,text='Check Booking',command=entrycheck).grid(row=3,column=6)
        def checking2():
            root.destroy()
            obj.Home_page()

        Button(root,image=home_Image,font='Arial 15',bg='pale green',command=checking2).grid(row=3,column=8 )
        root.mainloop()

    #Adding new bus details page
    def Add_new_bus_details_page():
        root=Tk()
        root.title("Bus booking system")
        icon=PhotoImage(file="buslogo.png")
        root.iconphoto(True,icon)

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))

        #Adding bus image 
        busImage=PhotoImage(file='Bus_for_project.png')
        Label(root,image=busImage).grid(row=0,column=0,padx=w//2.5,columnspan=12)

        #Adding text
        Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font='Arial 20 bold').grid(row=1,column=0,columnspan=12)

        #Page Detail
        Label(root,text='Add New Details to Database',fg='green',font='Arial 15 bold').grid(row=2,column=0,pady=h/40,columnspan=12)

        def seat_booking_page1(x=0):
            root.destroy()
            obj.New_Operator()

        def seat_booking_page2(x=0):
            root.destroy()
            obj.New_Bus()

        def seat_booking_page3(x=0):
            root.destroy()
            obj.New_Route()

        def seat_booking_page4(x=0):
            root.destroy()
            obj.New_Run()

        #Buttons
        Button(root,text='New Operator',bg='pale green',font='Arial 15',command=seat_booking_page1).grid(row=3,column=4)
        Button(root,text='New Bus',font='Arial 15',bg='salmon1',command=seat_booking_page2).grid(row=3,column=5)
        Button(root,text='New Route',font='Arial 15',bg='cornflower Blue',command=seat_booking_page3).grid(row=3,column=6)
        Button(root,text='New Run',font='Arial 15',bg='indian red',command=seat_booking_page4).grid(row=3,column=7)
        root.mainloop()

    #Adding new operator
    def New_Operator():
        root=Tk()
        root.title("Bus booking system")
        icon=PhotoImage(file="buslogo.png")
        root.iconphoto(True,icon)

        with sqlite3.connect('Bus_Booking.db') as con:
            cur=con.cursor()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))

        #Bus image
        busImage=PhotoImage(file='Bus_for_project.png')
        homeImage=PhotoImage(file='home.png')
        Label(root,image=busImage).grid(row=0,column=0,padx=w//2.5,columnspan=15)

        #online bus booking system
        Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font='Arial 25 bold').grid(row=1,column=0,columnspan=15)
        Label(root,text='Add Bus Operation Details',fg='green',font='Arial 20 bold').grid(row=2,column=0,pady=h/40,columnspan=15)

        def checkname(name):
            return name.isalpha()

        def checkphone(phone):
            count=0
            for i in phone:
                if i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
                    count+=1
            if count==10:
                return True
            else:
                return False

        def checkemail(email):
            counta=0
            countb=0
            for i in email:
                if i=='@':
                    counta+=1
                if i=='.':
                    countb+=1
            if counta==1 and countb>0:
                return True
            else:
                return False

        def checking2():
            root.destroy()
            obj.Home_page()

        def checking1():
            if len(op_id.get())==0 or len(name.get())==0 or len(address.get())==0 or len(phone.get())!=10 or len(email_id.get())==0:
                messagebox.showerror('Value Error','Enter details properly')
            else:
                if checkname(name.get())==False:
                    messagebox.showerror('Value Error','Enter details properly')
                elif checkphone(phone.get())==False:
                    messagebox.showerror('Value Error','Enter details properly')
                elif checkemail(email_id.get())==False:
                    messagebox.showerror('Value Error','Enter details properly')
                else:
                    idd=op_id.get()
                    nam=name.get()
                    addr=address.get()
                    mob=phone.get()
                    email=email_id.get()
                    cur.execute('Update Route set Name=? and Address=? and email_ID=? and Phone=? where Operator_ID=?;',(idd,nam,addr,mob,email,))

        #checking the enter values
        def checking():
            if len(op_id.get())==0 or len(name.get())==0 or len(address.get())==0 or len(phone.get())!=10 or len(email_id.get())==0:
                messagebox.showerror('Value Error','Enter details properly')
            else:
                if checkname(name.get())==False:
                    messagebox.showerror('Value Error','Enter details properly')
                elif checkphone(phone.get())==False:
                    messagebox.showerror('Value Error','Enter details properly')
                elif checkemail(email_id.get())==False:
                    messagebox.showerror('Value Error','Enter details properly')
                else:
                    insertintodata()
                    op_id.delete(0,END)
                    name.delete(0,END)
                    address.delete(0,END)
                    email_id.delete(0,END)
                    phone.delete(0,END)

        def insertintodata(*args):
            oprtr=op_id.get()
            NaMe=name.get()
            addrs=address.get()
            email=email_id.get()
            mob=phone.get()
            cur.execute('''insert into Operator(Operator_ID,Name,Address,email_ID,Phone) values(?,?,?,?,?);''',(oprtr,NaMe,addrs,email,mob))
            con.commit()
            messagebox.showinfo('Operator Entry','Added Succesfully')

        #Operator ID
        Label(root,text='Operator id',font='Arial 13').grid(row=3,column=2)
        op_id=Entry(root)
        op_id.grid(row=3,column=3)


        #Name   
        Label(root,text='Name',font='Arial 13').grid(row=3,column=4)
        name=Entry(root)
        name.grid(row=3,column=5)



        #Address
        Label(root,text='Address',font='Arial 13').grid(row=3,column=6)
        address=Entry(root)
        address.grid(row=3,column=7)


        #Phone
        Label(root,text='Phone',font='Arial 13').grid(row=3,column=8)
        phone=Entry(root)
        phone.grid(row=3,column=9)


        #Email ID
        Label(root,text='Email id',font='Arial 13').grid(row=3,column=10)
        email_id=Entry(root)
        email_id.grid(row=3,column=11)


        # Buttons for add edit and home
        Button(root,text='Add',font='Arial 15',bg='pale green',command=checking).grid(row=3,column=12)
        Button(root,text='Edit',font='Arial 15',bg='pale green',command=checking1).grid(row=3,column=13)
        Button(root,image=homeImage,font='Arial 15',bg='pale green',command=checking2).grid(row=4,column=2,columnspan=15,pady=h/50)

        root.mainloop()
    
    #Adding New Bus
    def New_Bus():
        root=Tk()
        root.title("Bus booking system")
        icon=PhotoImage(file="buslogo.png")
        root.iconphoto(True,icon)
        with sqlite3.connect('Bus_Booking.db') as con:
            cur=con.cursor()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))

        bus_type=StringVar()
        bus_type.set("Bus Type")
        options_Bus_Type=["AC 2X2","Non-AC 2X2","AC 3X2","Non-AC 3X2","AC Sleeper 2X1","Non-AC Sleeper 2X1"]
        #Bus image 
        busImage=PhotoImage(file='Bus_for_project.png')
        homeImage=PhotoImage(file='home.png')
        Label(root,image=busImage).grid(row=0,column=0,padx=w//2.5,columnspan=15)

        def checkcapacity(cap):
            return cap.isnumeric()

        def checkfare(num):
            return num.isnumeric()

        def checking2():
            root.destroy()
            obj.Home_page()

        def checking():
            if len(busid.get())==0 or len(capacity.get())==0 or len(fare.get())==0 or len(operator.get())==0 or len(route.get())==0:
                messagebox.showerror('Value Error','Enter Details properly')
            else:   
                if checkcapacity(capacity.get())==False:
                    messagebox.showerror('Value Error','Enter Details properly')
                elif checkfare(fare.get())==False:
                    messagebox.showerror('Value Error','Enter Details properly')
                else:   
                    insertintodata()

        def checking1():
            if len(busid.get())==0 or len(capacity.get())==0 or len(fare.get())==0 or len(operator.get())==0 or len(route.get())==0:
                messagebox.showerror('Value Error','Enter Details properly')
            else:
                if checkcapacity(capacity.get())==False:
                    messagebox.showerror('Value Error','Enter Details properly')
                elif checkfare(fare.get())==False:
                    messagebox.showerror('Value Error','Enter Details properly')
                else:
                    buss=busid.get()
                    cap=capacity.get()
                    price=fare.get()
                    oprtr=operator.get()
                    rout=route.get()
                    bustype=bus_type.get()
                    cur.execute('''Update Bus set Type=? and Capacity=? and Fare=? and Route_ID=? and  Operator_ID=? where Bus_ID=?;''',(str(bustype),cap,price,oprtr,rout,buss,))
                    con.commit()
                    

            
        def insertintodata(*args):
            buss=busid.get()
            capacty=capacity.get()
            price=fare.get()
            optr=operator.get()
            routte=route.get()
            bustype=bus_type.get()
            cur.execute('''insert into bus(Bus_ID,Type,Capacity,Fare,Route_ID,Operator_ID) values(?,?,?,?,?,?);''',(buss,bustype,capacty,price,routte,optr))
            con.commit()
            cur.execute('''select * from bus where Bus_ID=?;''',(buss,))
            seethrough=cur.fetchall()
            if(seethrough):
                messagebox.showerror('entry already exists')
            messagebox.showinfo('Bus Entry','Added Succesfully')
        
        #online bus booking system
        Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font='Arial 25 bold').grid(row=1,column=0,columnspan=15)
        Label(root,text='Add Bus Details',fg='green',font='Arial 20 bold').grid(row=2,column=0,pady=h/40,columnspan=15)

        #Bus ID
        Label(root,text='Bus ID',font='Arial 13').grid(row=3,column=2)
        busid=Entry(root)
        busid.grid(row=3,column=3)

        #drop down menu option
        Label(root,text='Bus Type',font='Arial 13').grid(row=3,column=4)
        d_menu=OptionMenu(root,bus_type,*options_Bus_Type)
        d_menu.grid(row=3,column=5)

        #capacity
        Label(root,text='Capacity',font='Arial 13').grid(row=3,column=6)
        capacity=Entry(root)
        capacity.grid(row=3,column=7)

        #Fare Price
        Label(root,text='Fare Rs.',font='Arial 13').grid(row=3,column=8)
        fare=Entry(root)
        fare.grid(row=3,column=9)

        #Operator ID
        Label(root,text='Operator ID',font='Arial 13').grid(row=3,column=10)
        operator=Entry(root)
        operator.grid(row=3,column=11)

        #Route ID
        Label(root,text='Route ID',font='Arial 13').grid(row=3,column=12)
        route=Entry(root)
        route.grid(row=3,column=13)

        # Buttons for add edit and home
        Button(root,text='Add',font='Arial 15',bg='pale green',command=checking).grid(row=4,column=7,pady=h/10)
        Button(root,text='Edit',font='Arial 15',bg='pale green',command=checking1).grid(row=4,column=8)
        Button(root,image=homeImage,font='Arial 15',bg='pale green',command=checking2).grid(row=4,column=9)
        root.mainloop()

    #Adding New Route
    def New_Route():
        root=Tk()
        root.title("Bus booking system")
        icon=PhotoImage(file="buslogo.png")
        root.iconphoto(True,icon)
         
        with sqlite3.connect('Bus_Booking.db') as con:
            cur=con.cursor()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))

        #Bus image 
        busImage=PhotoImage(file='Bus_for_project.png')
        homeImage=PhotoImage(file='home.png')
        Label(root,image=busImage).grid(row=0,column=0,padx=w//2.5,columnspan=15)

        #online bus booking system
        Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font='Arial 25 bold').grid(row=1,column=0,columnspan=15)
        Label(root,text='Add Bus Route Details',fg='green',font='Arial 20 bold').grid(row=2,column=0,pady=h/40,columnspan=15)

        def checkname(name):
            return name.isalpha()

        def checknum(num):
            return num.isnumeric()

        def checking2():
            root.destroy()
            obj.Home_page()


        def check():
            if len(route.get())==0 or len(sname.get())==0 or len(stationid.get())==0 or len(dname.get())==0 or len(destinationid.get())==0:
                messagebox.showerror("value Error","Enter Details Properly")
            else:
                if checknum(route.get())==False:
                    messagebox.showerror("value Error","Enter Details Properly")
                elif checkname(sname.get())==False:
                    messagebox.showerror("value Error","Enter Details Properly")
                elif checknum(stationid.get())==False:
                    messagebox.showerror("value Error","Enter Details Properly")
                elif checkname(dname.get())==False:
                    messagebox.showerror("value Error","Enter Details Properly")
                elif checknum(destinationid.get())==False:
                    messagebox.showerror("value Error","Enter Details Properly")
                else:
                    showdetails()
                    route.delete(0,END)
                    sname.delete(0,END)
                    stationid.delete(0,END)
                    destinationid.delete(0,END)
                    dname.delete(0,END)

        def check1():
            if len(route.get())==0 or len(sname.get())==0 or len(stationid.get())==0 or len(dname.get())==0 or len(destinationid.get())==0:
                messagebox.showerror("value Error","Enter Details Properly")
            else:
                if checknum(route.get())==False:
                    messagebox.showerror("value Error","Enter Details Properly")
                elif checkname(sname.get())==False:
                    messagebox.showerror("value Error","Enter Details Properly")
                elif checknum(stationid.get())==False:
                    messagebox.showerror("value Error","Enter Details Properly")
                elif checkname(dname.get())==False:
                    messagebox.showerror("value Error","Enter Details Properly")
                elif checknum(destinationid.get())==False:
                    messagebox.showerror("value Error","Enter Details Properly")
                else:
                    r=route.get()
                    s=sname.get()
                    sid=stationid.get()
                    did=destinationid.get()
                    d=dname.get()
                    cur.execute('Delete from Route where Route_ID=? and stationName=? and Station_ID=? and destinationName=? and destinatin_ID=?;',(r,s,sid,d,did,))
                    con.commit()

        def insertintodata(*args):
            routte=route.get()
            name=sname.get()
            station=stationid.get()
            ddname=dname.get()
            destation=destinationid.get()
            cur.execute('''insert into Route(Route_ID, Station_ID, stationName, destinationName, Destination_ID) values(?,?,?,?,?);''',(routte,station,name,ddname,destation))
            con.commit()
            messagebox.showinfo('Route Entry','Added Succesfully')

        def showdetails():
            insertintodata()
            Label(root,text='Route Details',fg='Red',bg='LightBlue1',font='Arial 15').grid(row=6,column=0, columnspan=15,pady=h//30)
            Label(root,text='Route ID: ',font='Arial 13').grid(row=7,column=3)
            Label(root,text=route.get(),font='Arial 13').grid(row=7,column=4)
            Label(root,text='Station Name: ',font='Arial 13').grid(row=7,column=5)
            Label(root,text=sname.get(),font='Arial 13').grid(row=7,column=6)
            Label(root,text='Station Id: ',font='Arial 13').grid(row=7,column=7)
            Label(root,text=stationid.get(),font='Arial 13').grid(row=7,column=8)
            Label(root,text='Destination Name: ',font='Arial 13').grid(row=7,column=5)
            Label(root,text=dname.get(),font='Arial 13').grid(row=7,column=6)
            Label(root,text='Destination Id: ',font='Arial 13').grid(row=7,column=7)
            Label(root,text=destinationid.get(),font='Arial 13').grid(row=7,column=8)

        #Route ID
        Label(root,text='Route ID',font='Arial 10').grid(row=3,column=3)
        route=Entry(root)
        route.grid(row=3,column=4)

        #Station Name
        Label(root,text='Station Name',font='Arial 10').grid(row=3,column=5)
        sname=Entry(root)
        sname.grid(row=3,column=6)

        #Station ID
        Label(root,text='Station ID',font='Arial 10').grid(row=3,column=7)
        stationid=Entry(root)
        stationid.grid(row=3,column=8)

        #Destination ID
        Label(root,text='Destination Name',font='Arial 10').grid(row=3,column=9)
        dname=Entry(root)
        dname.grid(row=3,column=10)

        #destination Name
        Label(root,text='Destination ID',font='Arial 10').grid(row=3,column=11)
        destinationid=Entry(root)
        destinationid.grid(row=3,column=12)

        # Buttons for add edit and home
        Button(root,text='Add Route',font='Arial 10',bg='pale green',command=check).grid(row=3,column=13)
        Button(root,text='Delete Route',font='Arial 10',bg='pale green',fg="Red",command=check1).grid(row=3,column=14)
        Button(root,image=homeImage,font='Arial 10',bg='pale green',command=checking2).grid(row=5,column=8,pady=h/10)

        root.mainloop()
    
    #Adding New Run
    def New_Run():
        root=Tk()
        root.title("Bus booking system")
        icon=PhotoImage(file="buslogo.png")
        root.iconphoto(True,icon)

        with sqlite3.connect('Bus_Booking.db') as con:
            cur=con.cursor()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))

        #Bus image 
        busImage=PhotoImage(file='Bus_for_project.png')
        homeImage=PhotoImage(file='home.png')
        Label(root,image=busImage).grid(row=0,column=0,padx=w//2.5,columnspan=13)

        #online bus booking system
        Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font='Arial 25 bold').grid(row=1,column=0,columnspan=13)
        Label(root,text='Add Bus Route Details',fg='green',font='Arial 20 bold').grid(row=2,column=0,pady=h/40,columnspan=13)

        def checking2():
            root.destroy()
            obj.Home_page()

        def check():
            if len(busid.get())==0 or len(runningDate.get())==0 or len(seatAvail.get())==0:
                messagebox.showerror("value Error","Enter Details Properly")
            else:
                showdetails()

        def check1():   
            if len(busid.get())==0 or len(runningDate.get())==0 or len(seatAvail.get())==0:
                messagebox.showerror("value Error","Enter Details Properly")
            else:
                buss=busid.get()
                runn=runningDate.get()
                seats=seatAvail.get()
                cur.execute('Delete from Run where Bus_ID=? and Date=? and Seats_Available=?;',(buss,runn,seats,))
                cur.commit()

        def insertintodata(*args):
            buss=busid.get()
            rDate=runningDate.get()
            seats=seatAvail.get()
            cur.execute('''insert into Run(Bus_ID, Date, Seats_Available) values(?,?,?);''',(buss,rDate,seats))
            con.commit()
            messagebox.showinfo('Route Entry','Added Succesfully')

        def showdetails():
            insertintodata()
            Label(root,text='Bus Details',fg='Red',bg='LightBlue1',font='Arial 15').grid(row=5,column=0, columnspan=13,pady=h//30)
            Label(root,text='Bus ID: ',font='Arial 13').grid(row=6,column=3)
            Label(root,text=busid.get(),font='Arial 13').grid(row=6,column=4)
            Label(root,text='Running Date: ',font='Arial 13').grid(row=6,column=5)
            Label(root,text=runningDate.get(),font='Arial 13').grid(row=6,column=6)
            Label(root,text='Seat Availability: ',font='Arial 13').grid(row=6,column=7)
            Label(root,text=seatAvail.get(),font='Arial 13').grid(row=6,column=8)


        #Bus ID
        Label(root,text='Bus ID',font='Arial 13').grid(row=3,column=2,pady=h/20)
        busid=Entry(root)
        busid.grid(row=3,column=3)

        #Running Date
        Label(root,text='Running Date',font='Arial 13').grid(row=3,column=4)
        runningDate=Entry(root)
        runningDate.grid(row=3,column=5)

        #Seat Available
        Label(root,text='Seat Available',font='Arial 13').grid(row=3,column=6)
        seatAvail=Entry(root)
        seatAvail.grid(row=3,column=7)

        # Buttons for add edit and home
        Button(root,text='Add Run',font='Arial 15',bg='pale green',command=check).grid(row=3,column=9)
        Button(root,text='Delete Run',font='Arial 15',bg='pale green',fg="Black",command=check1).grid(row=3,column=10)
        Button(root,image=homeImage,font='Arial 15',bg='pale green',command=checking2).grid(row=4,column=8,pady=h/20)
        root.mainloop()

if __name__=="__main__":
    obj=BusBookingSystem
    obj.front_page()

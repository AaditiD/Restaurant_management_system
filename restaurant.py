from tkinter import *
import random
import time
from tkinter import filedialog
import os
from tkinter import messagebox  # Import the os module

root = Tk()
root.geometry("1000x700+0+0")
root.resizable(0, 0)
root.title("Restaurant Management System")
root.configure(bg="#FFF4E6")

Tops = Frame(root, bg="#FFF4E6", width=1000, height=50, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=500, height=650, relief=SUNKEN, bg="#FFF4E6")
f1.pack(side=LEFT)

f2 = Frame(root, width=500, height=650, relief=SUNKEN, bg="#FFF4E6")
f2.pack(side=RIGHT)
# ------------------TIME--------------
localtime = time.asctime(time.localtime(time.time()))
# -----------------INFO TOP------------
lblinfo = Label(Tops, font=('aria', 20, 'bold'),
                text="Restaurant Management System", fg="orange", bd=10, anchor='w', bg="#FFF4E6")
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=('aria', 12,),
                text=localtime, fg="orange", anchor=W, bg="#FFF4E6")
lblinfo.grid(row=1, column=0)

# ---------------Calculator------------------
text_Input = StringVar()
operator = ""

txtdisplay = Entry(f2, font=('ariel', 16, 'bold'), textvariable=text_Input, bd=5,
                   insertwidth=7, bg="white", justify='right')
txtdisplay.grid(columnspan=4)


def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def clrdisplay():
    global operator
    operator = ""
    text_Input.set("")


def eqals():
    global operator
    try:
        sumup = str(eval(operator))
    except Exception as e:
        sumup = "Error: " + str(e)
    text_Input.set(sumup)
    operator = ""


def Ref():
    x = random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    try:
        cof = float(Fries.get()) if Fries.get() else 0
        colfries = float(Largefries.get()) if Largefries.get() else 0
        cob = float(Burger.get()) if Burger.get() else 0
        cofi = float(Filet.get()) if Filet.get() else 0
        cochee = float(Cheese_burger.get()) if Cheese_burger.get() else 0
        codr = float(Drinks.get()) if Drinks.get() else 0
    except ValueError:
        costofmeal = "Error: Invalid input"
        PayTax = 0
        Totalcost = 0
        Ser_Charge = 0
        Service = ""
        OverAllCost = ""
        PaidTax = ""
    else:
        costoffries = cof * 25
        costoflargefries = colfries * 40
        costofburger = cob * 35
        costoffilet = cofi * 50
        costofcheeseburger = cochee * 50
        costofdrinks = codr * 35

        costofmeal = "Rs.", str('%.2f' % (costoffries + costoflargefries + costofburger + costoffilet +
                                          costofcheeseburger + costofdrinks))
        PayTax = ((costoffries + costoflargefries + costofburger + costoffilet +
                   costofcheeseburger + costofdrinks) * 0.33)
        Totalcost = (costoffries + costoflargefries + costofburger + costoffilet +
                     costofcheeseburger + costofdrinks)
        Ser_Charge = ((costoffries + costoflargefries + costofburger + costoffilet +
                       costofcheeseburger + costofdrinks) / 99)
        Service = "Rs.", str('%.2f' % Ser_Charge)
        OverAllCost = "Rs.", str('%.2f' % (PayTax + Totalcost + Ser_Charge))
        PaidTax = "Rs.", str('%.2f' % PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)



def qexit():
    root.destroy()


def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")



btn7 = Button(f2, padx=16, pady=16, bd=4, fg="black",
              font=('ariel', 16, 'bold'), text="7", bg="orange", command=lambda: btnclick(7))
btn7.grid(row=2, column=0)

btn8 = Button(f2, padx=16, pady=16, bd=4, fg="black",
              font=('ariel', 16, 'bold'), text="8", bg="orange", command=lambda: btnclick(8))
btn8.grid(row=2, column=1)

btn9 = Button(f2, padx=16, pady=16, bd=4, fg="black",
              font=('ariel', 16, 'bold'), text="9", bg="orange", command=lambda: btnclick(9))
btn9.grid(row=2, column=2)

Addition = Button(f2, padx=16, pady=16, bd=4, fg="black",
                    font=('ariel', 16, 'bold'), text="+", bg="orange", command=lambda: btnclick("+"))
Addition.grid(row=2, column=3)
# ---------------------------------------------------------------------------------------------
btn4 = Button(f2, padx=16, pady=16, bd=4, fg="black",
              font=('ariel', 16, 'bold'), text="4", bg="orange", command=lambda: btnclick(4))
btn4.grid(row=3, column=0)

btn5 = Button(f2, padx=16, pady=16, bd=4, fg="black",
              font=('ariel', 16, 'bold'), text="5", bg="orange", command=lambda: btnclick(5))
btn5.grid(row=3, column=1)

btn6 = Button(f2, padx=16, pady=16, bd=4, fg="black",
              font=('ariel', 16, 'bold'), text="6", bg="orange", command=lambda: btnclick(6))
btn6.grid(row=3, column=2)

Substraction = Button(f2, padx=16, pady=16, bd=4, fg="black",
                      font=('ariel', 16, 'bold'), text="-", bg="orange", command=lambda: btnclick("-"))
Substraction.grid(row=3, column=3)
# -----------------------------------------------------------------------------------------------
btn1 = Button(f2, padx=16, pady=16, bd=4, fg="black",
              font=('ariel', 16, 'bold'), text="1", bg="orange", command=lambda: btnclick(1))
btn1.grid(row=4, column=0)

btn2 = Button(f2, padx=16, pady=16, bd=4, fg="black",
              font=('ariel', 16, 'bold'), text="2", bg="orange", command=lambda: btnclick(2))
btn2.grid(row=4, column=1)

btn3 = Button(f2, padx=16, pady=16, bd=4, fg="black",
              font=('ariel', 16, 'bold'), text="3", bg="orange", command=lambda: btnclick(3))
btn3.grid(row=4, column=2)

multiply = Button(f2, padx=16, pady=16, bd=4, fg="black",
                  font=('ariel', 16, 'bold'), text="*", bg="orange", command=lambda: btnclick("*"))
multiply.grid(row=4, column=3)
# ------------------------------------------------------------------------------------------------
btn0 = Button(f2, padx=16, pady=16, bd=4, fg="black",
              font=('ariel', 16, 'bold'), text="0", bg="orange", command=lambda: btnclick(0))
btn0.grid(row=5, column=0)

btnc = Button(f2, padx=16, pady=16, bd=4, fg="black",
              font=('ariel', 16, 'bold'), text="c", bg="orange", command=clrdisplay)
btnc.grid(row=5, column=1)

btnequal = Button(f2, padx=16, pady=16, bd=4, width=8, fg="black",
                  font=('ariel', 16, 'bold'), text="=", bg="orange", command=eqals)
btnequal.grid(columnspan=4)

Decimal = Button(f2, padx=16, pady=16, bd=4, fg="black",
                   font=('ariel', 16, 'bold'), text=".", bg="orange", command=lambda: btnclick("."))
Decimal.grid(row=5, column=2)

Division = Button(f2, padx=16, pady=16, bd=4, fg="black",
                   font=('ariel', 16, 'bold'), text="/", bg="orange", command=lambda: btnclick("/"))
Division.grid(row=5, column=3)
status = Label(f2, font=('aria', 10, 'bold'), width=16,
               text="", bd=2, relief=SUNKEN, bg="#FFF4E6")
status.grid(row=7, columnspan=3)

# ---------------------------------------------------------------------------------------
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()


lblreference = Label(f1, font=('aria', 12, 'bold'),
                     text="Order No.", fg="orange", bd=10, anchor='w', bg="#FFF4E6")
lblreference.grid(row=0, column=0)
txtreference = Entry(f1, font=('ariel', 12, 'bold'), textvariable=rand, bd=6,
                      insertwidth=4, bg="orange", justify='right', state=DISABLED)
txtreference.grid(row=0, column=1)

lblfries = Label(f1, font=('aria', 12, 'bold'),
                  text="Fries Meal", fg="orange", bd=10, anchor='w', bg="#FFF4E6")
lblfries.grid(row=1, column=0)
txtfries = Entry(f1, font=('ariel', 12, 'bold'), textvariable=Fries, bd=6,
                  insertwidth=4, bg="orange", justify='right')
txtfries.grid(row=1, column=1)

lblLargefries = Label(f1, font=('aria', 12, 'bold'),
                       text="Lunch Meal", fg="orange", bd=10, anchor='w', bg="#FFF4E6")
lblLargefries.grid(row=2, column=0)
txtLargefries = Entry(f1, font=('ariel', 12, 'bold'), textvariable=Largefries, bd=6,
                       insertwidth=4, bg="orange", justify='right')
txtLargefries.grid(row=2, column=1)


lblburger = Label(f1, font=('aria', 12, 'bold'),
                    text="Burger Meal", fg="orange", bd=10, anchor='w', bg="#FFF4E6")
lblburger.grid(row=3, column=0)
txtburger = Entry(f1, font=('ariel', 12, 'bold'), textvariable=Burger, bd=6,
                    insertwidth=4, bg="orange", justify='right')
txtburger.grid(row=3, column=1)

lblFilet = Label(f1, font=('aria', 12, 'bold'),
                  text="Pizza Meal", fg="orange", bd=10, anchor='w', bg="#FFF4E6")
lblFilet.grid(row=4, column=0)
txtFilet = Entry(f1, font=('ariel', 12, 'bold'), textvariable=Filet, bd=6,
                  insertwidth=4, bg="orange", justify='right')
txtFilet.grid(row=4, column=1)

lblCheese_burger = Label(f1, font=('aria', 12, 'bold'),
                          text="Cheese burger", fg="orange", bd=10, anchor='w', bg="#FFF4E6")
lblCheese_burger.grid(row=5, column=0)
txtCheese_burger = Entry(f1, font=('ariel', 12, 'bold'), textvariable=Cheese_burger, bd=6,
                          insertwidth=4, bg="orange", justify='right')
txtCheese_burger.grid(row=5, column=1)

# --------------------------------------------------------------------------------------
lblDrinks = Label(f1, font=('aria', 12, 'bold'),
                   text="Drinks", fg="orange", bd=10, anchor='w', bg="#FFF4E6")
lblDrinks.grid(row=0, column=2)
txtDrinks = Entry(f1, font=('ariel', 12, 'bold'), textvariable=Drinks, bd=6,
                   insertwidth=4, bg="orange", justify='right')
txtDrinks.grid(row=0, column=3)

lblcost = Label(f1, font=('aria', 12, 'bold'),
                 text="cost", fg="orange", bd=10, anchor='w', bg="#FFF4E6")
lblcost.grid(row=1, column=2)
txtcost = Entry(f1, font=('ariel', 12, 'bold'), textvariable=cost, bd=6,
                 insertwidth=4, bg="orange", justify='right', state=DISABLED)
txtcost.grid(row=1, column=3)

lblService_Charge = Label(f1, font=('aria', 12, 'bold'),
                           text="Service Charge", fg="orange", bd=10, anchor='w', bg="#FFF4E6")
lblService_Charge.grid(row=2, column=2)
txtService_Charge = Entry(f1, font=('ariel', 12, 'bold'), textvariable=Service_Charge, bd=6,
                           insertwidth=4, bg="orange", justify='right', state=DISABLED)
txtService_Charge.grid(row=2, column=3)

lblTax = Label(f1, font=('aria', 12, 'bold'),
                text="Tax", fg="orange", bd=10, anchor='w', bg="#FFF4E6")
lblTax.grid(row=3, column=2)
txtTax = Entry(f1, font=('ariel', 12, 'bold'), textvariable=Tax, bd=6,
                insertwidth=4, bg="orange", justify='right', state=DISABLED)
txtTax.grid(row=3, column=3)

lblSubtotal = Label(f1, font=('aria', 12, 'bold'),
                     text="Subtotal", fg="orange", bd=10, anchor='w', bg="#FFF4E6")
lblSubtotal.grid(row=4, column=2)
txtSubtotal = Entry(f1, font=('ariel', 12, 'bold'), textvariable=Subtotal, bd=6,
                     insertwidth=4, bg="orange", justify='right', state=DISABLED)
txtSubtotal.grid(row=4, column=3)

lblTotal = Label(f1, font=('aria', 12, 'bold'),
                   text="Total", fg="orange", bd=10, anchor='w', bg="#FFF4E6")
lblTotal.grid(row=5, column=2)
txtTotal = Entry(f1, font=('ariel', 12, 'bold'), textvariable=Total, bd=6,
                   insertwidth=4, bg="orange", justify='right', state=DISABLED)
txtTotal.grid(row=5, column=3)

# -----------------------------------------buttons------------------------------------------
lblTotal = Label(f1, text="---------------------", fg="white", bg="#FFF4E6")
lblTotal.grid(row=6, columnspan=3)

btnTotal = Button(f1, padx=16, pady=16, bd=10, fg="black",
                  font=('ariel', 12, 'bold'), width=8, text="TOTAL", bg="orange", command=Ref)
btnTotal.grid(row=7, column=1)

btnreset = Button(f1, padx=16, pady=16, bd=10, fg="black",
                  font=('ariel', 12, 'bold'), width=8, text="RESET", bg="orange", command=reset)
btnreset.grid(row=7, column=2)

btnexit = Button(f1, padx=16, pady=16, bd=10, fg="black",
                font=('ariel', 12, 'bold'), width=8, text="EXIT", bg="orange", command=qexit)
btnexit.grid(row=7, column=3)


def price():
    roo = Toplevel()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    roo.configure(bg="#FFF4E6")
    lblinfo = Label(roo, font=('aria', 12, 'bold'),
                    text="ITEM", fg="black", bd=5, bg="#FFF4E6")
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 12, 'bold'),
                    text="_____________", fg="white", anchor=W, bg="#FFF4E6")
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 12, 'bold'),
                    text="PRICE", fg="black", anchor=W, bg="#FFF4E6")
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 12, 'bold'),
                    text="Fries Meal", fg="orange", anchor=W, bg="#FFF4E6")
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 12, 'bold'),
                    text="25", fg="orange", anchor=W, bg="#FFF4E6")
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 12, 'bold'),
                    text="Lunch Meal", fg="orange", anchor=W, bg="#FFF4E6")
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 12, 'bold'),
                    text="40", fg="orange", anchor=W, bg="#FFF4E6")
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 12, 'bold'),
                    text="Burger Meal", fg="orange", anchor=W, bg="#FFF4E6")
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 12, 'bold'),
                    text="35", fg="orange", anchor=W, bg="#FFF4E6")
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 12, 'bold'),
                    text="Pizza Meal", fg="orange", anchor=W, bg="#FFF4E6")
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 12, 'bold'),
                    text="50", fg="orange", anchor=W, bg="#FFF4E6")
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 12, 'bold'),
                    text="Cheese Burger", fg="orange", anchor=W, bg="#FFF4E6")
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 12, 'bold'),
                    text="30", fg="orange", anchor=W, bg="#FFF4E6")
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 12, 'bold'),
                    text="Drinks", fg="orange", anchor=W, bg="#FFF4E6")
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 12, 'bold'),
                    text="35", fg="orange", anchor=W, bg="#FFF4E6")
    lblinfo.grid(row=6, column=3)

    roo.mainloop()

def save_bill():
    # Use the order number as the filename
    filename = f"Order_{rand.get()}.txt"
    filepath = os.path.join(os.getcwd(), filename) # Saves to current directory
    try:
        with open(filepath, "w") as f:
            f.write("Restaurant Management System\n")
            f.write("--------------------------------\n")
            f.write(f"Order No.: {rand.get()}\n")
            f.write(f"Date: {localtime}\n")
            f.write("--------------------------------\n")
            f.write("Items\t\t\tQuantity\tPrice\n")
            f.write("--------------------------------\n")
            if Fries.get():
                f.write(f"Fries Meal\t\t\t{Fries.get()}\tRs. {float(Fries.get()) * 25:.2f}\n")
            if Largefries.get():
                f.write(f"Lunch Meal\t\t\t{Largefries.get()}\tRs. {float(Largefries.get()) * 40:.2f}\n")
            if Burger.get():
                f.write(f"Burger Meal\t\t\t{Burger.get()}\tRs. {float(Burger.get()) * 35:.2f}\n")
            if Filet.get():
                f.write(f"Pizza Meal\t\t\t{Filet.get()}\tRs. {float(Filet.get()) * 50:.2f}\n")
            if Cheese_burger.get():
                f.write(f"Cheese Burger\t\t\t{Cheese_burger.get()}\tRs. {float(Cheese_burger.get()) * 50:.2f}\n")
            if Drinks.get():
                f.write(f"Drinks\t\t\t{Drinks.get()}\tRs. {float(Drinks.get()) * 35:.2f}\n")
            f.write("--------------------------------\n")
            f.write(f"Cost of Meal:\t\t{cost.get()}\n")
            f.write(f"Service Charge:\t\t{Service_Charge.get()}\n")
            f.write(f"Tax:\t\t\t{Tax.get()}\n")
            f.write(f"Subtotal:\t\t{Subtotal.get()}\n")
            f.write(f"Total:\t\t\t{Total.get()}\n")
            f.write("--------------------------------\n")
            f.write("Thank you for dining with us!\n")
        print(f"Bill saved successfully to {filepath}")
    except Exception as e:
        print(f"Error saving bill: {e}")
        messagebox.showerror("Error", f"Could not save the bill. Error: {e}")

btnprice = Button(f1, padx=16, pady=16, bd=10, fg="black",
                  font=('ariel', 12, 'bold'), width=8, text="PRICE", bg="orange", command=price)
btnprice.grid(row=7, column=0)

btn_save_bill = Button(f1, padx=16, pady=16, bd=10, fg="black",
                  font=('ariel', 12, 'bold'), width=8, text="Save Bill", bg="orange", command=save_bill)
btn_save_bill.grid(row=8, column=1)

root.mainloop()

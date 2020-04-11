from tkinter import *

expression = ""


# Function to update expressiom
# in the text entry box
def button_click(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def button_equal():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))

        equation.set(total)

        # initialze the expression variable
        # by empty string
        expression = ""

        # if error is generate then handle
    # by the except block
    except:

        equation.set(" error ")
        expression = ""

    # Function to clear the contents


# of text entry box
def Button_clear():
    global expression
    expression = ""
    equation.set("")




if __name__=="__main__":




    root=Tk()
    root.title("Simple Calculator")

    equation=StringVar()



    e=Entry(root,textvariable=equation,width=35,borderwidth=5).grid(row=0,column=0,columnspan=3,padx=10,pady=10)

    b1=Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1)).grid(row=3,column=0)
    b2=Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2)).grid(row=3,column=1)
    b3=Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3)).grid(row=3,column=2)

    b4=Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4)).grid(row=2,column=0)
    b5=Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5)).grid(row=2,column=1)
    b6=Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6)).grid(row=2,column=2)

    b7=Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7)).grid(row=1,column=0)
    b8=Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8)).grid(row=1,column=1)
    b9=Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9)).grid(row=1,column=2)
    b0=Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0)).grid(row=4,column=0)

    btn_add=Button(root,text="+",padx=39,pady=20,command=lambda:button_click("+")).grid(row=5,column=0)
    btn_sub = Button(root, text="-", padx=39, pady=20, command=lambda: button_click("-")).grid(row=6, column=0)
    btn_mul = Button(root, text="X", padx=39, pady=20, command=lambda: button_click("*")).grid(row=6, column=1)
    btn_div = Button(root, text="/", padx=39, pady=20, command=lambda: button_click("/")).grid(row=6, column=2)

    btn_equal=Button(root,text="=",padx=91,pady=20,command=button_equal).grid(row=5,column=1,columnspan=2)
    btn_clr=Button(root,text="Clear",padx=79,pady=20,command=Button_clear).grid(row=4,column=1,columnspan=2)


    root.mainloop()
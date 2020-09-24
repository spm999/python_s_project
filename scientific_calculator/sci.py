from tkinter import *
import math
#import parser
import tkinter.messagebox
#import matplotlib

root = Tk()
root.title("Scientific Calculator")
root.configure(background="light blue")
root.resizable(width=True, height=True)
root.geometry("480x568+0+0")

calc = Frame(root)
calc.grid()


class Calc():
    def __init__(self):
        self.total=0
        self.current=""
        self.input_value=True
        self.check_sum=False
        self.op=""
        self.result=False


    def numberEnter(self,num):
        self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current=secondnum
            self.input_value=False
        else:
            if secondnum=='.':
                if secondnum in firstnum:
                    return
            self.current=firstnum+secondnum
        self.display(self.current)


    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())
            


    def display(self, value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0,value)


        

    def valid_function(self):
        if self.op=="add":
            self.total+=self.current
        if self.op=="sub":
            self.total-=self.current
        if self.op=="multi":
            self.total*=self.current
        if self.op=="divide":
            self.total/=self.current
        if self.op=="mod":
            self.total%=self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)



    def operation(self,op):
        self.current=float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False


    def pi(self):
       self.result=False
       self.current=math.pi
       self.display(self.current)
       

    def sin(self):
       self.result=False
       self.current=math.sin(math.radians(float(txtDisplay.get())))
       self.display(self.current)

       

    def tan(self):
       self.result=False
       self.current=math.tan(math.radians(float(txtDisplay.get())))
       self.display(self.current)

       

    def cos(self):
       self.result=False
       self.current=math.cos(math.radians(float(txtDisplay.get())))
       self.display(self.current)


    def sinh(self):
       self.result=False
       self.current=math.sinh(float(txtDisplay.get()))
       self.display(self.current)


    def tanh(self):
       self.result=False
       self.current=math.tanh(float(txtDisplay.get()))
       self.display(self.current)


    def cosh(self):
       self.result=False
       self.current=math.cosh(float(txtDisplay.get()))
       self.display(self.current)

    def asinh(self):
       self.result=False
       self.current=math.asinh(float(txtDisplay.get()))
       self.display(self.current)

    def acosh(self):
       self.result=False
       self.current=math.acosh(float(txtDisplay.get()))
       self.display(self.current)
    def atanh(self):
       self.result=False
       self.current=math.atanh(float(txtDisplay.get()))
       self.display(self.current)   


    def log(self):
       self.result=False
       self.current=math.log10(float(txtDisplay.get()))
       self.display(self.current)


    def ln(self):
       self.result=False
       self.current=math.log(float(txtDisplay.get()))
       self.display(self.current)  


    def gcd(self):
       self.result=False
       self.current=math.gcd(float(int(txtDisplay.get())))
       self.display(self.current)


    def exp(self):
       self.result=False
       self.current=math.exp(float(txtDisplay.get()))
       self.display(self.current)


    def inverse(self):
       self.result=False
       self.current=1/int(txtDisplay.get())
       self.display(self.current)   


       
    def clear_entry(self):
       self.result=False
       self.current="0"
       self.display(0)
       self.input_value=True

    def all_clear(self):
       self.clear_entry()
       self.total=0

    def sqroot(self):
        self.result=False
        self.current=math.sqrt(float(txtDisplay.get()))
        self.display(self.current)


    def nPr(self):
        self.result=False
        self.current=math.perm(float(txtDisplay.get()))#,float(txt.Display.get()))
        self.display(self.current)
    

   
    def facto(self):
        self.result=False
        self.current=math.factorial(float(txtDisplay.get()))
        self.display(self.current) 
    
       
added_value=Calc()

            
        
txtDisplay=Entry(calc, font=('arial',20,'bold'), bg="light blue", bd=30,width=28, justify=RIGHT)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")


numberpad="789456123"
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6,height=2,font=('arial',20,'bold'),bd=4,text=numberpad[i]))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i]["command"]=lambda x=numberpad [i]: added_value.numberEnter(x)
        i+=1
#============================================================#Number Pad#================================================
btnClear=Button(calc,text=chr(67),width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="light blue",command=added_value.clear_entry).grid(row=1,column=0,pady=1)
btnAllClear=Button(calc,text=chr(67)+chr(69),width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="light blue",command=added_value.all_clear).grid(row=1,column=1,pady=1)
btnSqrt=Button(calc,text="√",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="light blue",command=added_value.sqroot).grid(row=1,column=2,pady=1)
btnAdd=Button(calc,text="+",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="light blue",command=lambda: added_value.operation("add")).grid(row=1,column=3,pady=1)
btnSub=Button(calc,text="-",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="light blue",command=lambda: added_value.operation("sub")).grid(row=2,column=3,pady=1)
btnMul=Button(calc,text="*",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="light blue",command=lambda: added_value.operation("multi")).grid(row=3,column=3,pady=1)
btnDiv=Button(calc,text=chr(247),width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="light blue",command=lambda: added_value.operation("divide")).grid(row=4,column=3,pady=1)
btnDot=Button(calc,text=".",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="light blue",command=lambda: added_value.numberEnter(".")).grid(row=5,column=2,pady=1)
btnMod=Button(calc,text="%",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="light blue",command=lambda: added_value.operation("mod")).grid(row=5,column=3,pady=1)
btnEql=Button(calc,text="=",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="light blue",command=added_value.sum_of_total).grid(row=5,column=1,pady=1)
btnZero=Button(calc,text="0",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="light blue",command=lambda: added_value.numberEnter(0)).grid(row=5,column=0,pady=1)

#================================================================Scientific Calculator=====================================

btntan=Button(calc,text="tan",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="white",command=added_value.tan).grid(row=2,column=6,pady=1)
btnCos=Button(calc,text="cos",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="white",command=added_value.cos).grid(row=2,column=4,pady=1)
btnSin=Button(calc,text="sin",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="white",command=added_value.sin).grid(row=2,column=5,pady=1)



#=============================================================================================================================#

#btnGCD=Button(calc,text="GCD",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="light blue",command=added_value.gcd).grid(row=5,column=4,pady=1)

btnXinverse=Button(calc,text="1/x",width=6,height=2,font=('arial',20, 'bold'),bd=4,bg="light blue",command=added_value.inverse).grid(row=4,column=5,pady=1)
btnlog=Button(calc,text="ln",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="white",command=added_value.ln).grid(row=3,column=4,pady=1)
btnln=Button(calc,text="log ",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="white",command=added_value.log).grid(row=3,column=5,pady=1)
btnExp=Button(calc,text="e^x",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="white",command=added_value.exp).grid(row=3,column=6,pady=1)


#=================================================================================================================================#
btnTanh=Button(calc,text="tanh",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="light blue",command=added_value.tanh).grid(row=1,column=6,pady=1)
btnSinh=Button(calc,text="sinh",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="light blue",command=added_value.sinh).grid(row=1,column=5,pady=1)
btnCosh=Button(calc,text="cosh",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="light blue",command=added_value.cosh).grid(row=1,column=4,pady=1)

#==================================================================================================================================#
#btnLcm=Button(calc,text="LCM",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="light blue",command=added_value.Lcm).grid(row=3,column=7,pady=1)
#btnnPr=Button(calc,text="nPr",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="white",command=added_value.nPr).grid(row=4,column=4,pady=1)
#btnnCr=Button(calc,text="nCr",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="white").grid(row=4,column=5,pady=1)
btnFacto=Button(calc,text="n!",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="white",command=added_value.facto).grid(row=4,column=6,pady=1)
btnPi=Button(calc,text="pi",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="white",command=added_value.pi).grid(row=4,column=4,pady=1)



#btnClear=Button(calc,text="",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="light blue").grid(row=5,column=4,pady=1)
btnClear=Button(calc,text="asinh",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="light blue",command=added_value.asinh).grid(row=5,column=4,pady=1)
btnClear=Button(calc,text="acosh",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="light blue",command=added_value.acosh).grid(row=5,column=5,pady=1)
btnClear=Button(calc,text="atanh",width=6, height=2,font=('arial',20, 'bold'),bd=4,bg="light blue",command=added_value.atanh).grid(row=5,column=6,pady=1)


lblDisplay=Label(calc,text="Scientific",font=('arial',30,'bold'),justify=CENTER)
lblDisplay.grid(row=0, column=4,columnspan=4 )
#============================================Graph=====================================================

                 
#==============================================Menu====================================================
def iExit():
    iExit=tkinter.messagebox.askyesno("Scientific Calculator","Do you really want to exit")
    if iExit>0:
        root.destroy()
        return


def Scientific():
    root.configure(width=False,height=False)
    root.geometry("830x570+0+0")

def Graph():
    root.resizable(width=False,Height=False)
    root.geometry("500x500+0+0")


def ihelp():
    ihelp=tkinter.messagebox.showinfo(title="Help",message="Use number buttons to provide the input to calculator \n After pressing the number use the operation")
    return 


menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Scientific",command=Scientific)
#filemenu.add_command(label="Graph",command=Graph)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=iExit)

'''editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Paste")'''

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="View Help",command=ihelp)

root.configure(menu=menubar)
root.mainloop()

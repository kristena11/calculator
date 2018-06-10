from tkinter import *
 
class Calculator:
    def __init__(self, master):
        #constructor input argument: the master argument 
        self.master = master
        #set title(method from tk master) 
        master.title("Calculator")
        #create text box to record and show each number the user inputs, set size and colors
        self.screen = Text(master, state='disabled', width=30, height=3,background="white", foreground="blue")
        
        #create grid on the screen to sisplay the buttons 
        self.screen.grid(row=0,column=0,columnspan=4)
        self.screen.configure(state='normal')
        
        self.equation = ''
        #create button objects with the below createButton method; pass value 
        b1 =  self.createButton('AC',None)
        b2 = self.createButton('%')
        b3 = self.createButton('/')
        b4 = self.createButton(7)
        b5 = self.createButton(8)
        b6 = self.createButton(9)
        b7 = self.createButton('*')
        b8 = self.createButton(4)
        b9 = self.createButton(5)
        b10 = self.createButton(6)
        b11 = self.createButton('-')
        b12 = self.createButton(1)
        b13 = self.createButton(2)
        b14 = self.createButton(3)
        b15 = self.createButton('+')
        b16 = self.createButton(0, True)
        b17 = self.createButton('.')
        b18 = self.createButton('=',None)
        
        #put each button object in a list 
        buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18]
        
        # loop to place buttons on grid 
        b1.grid(row=1, column=0, columnspan=1)
        
        count = 0
        #start in row 1
        r = 1
        #initalize colum, can only have 4 c in row
        c = 0
        #start button loop
        for b in buttons:
            #special colum to span 2 button spaces
            if b == b1:
                #columspand 2 instead of default 1
                b.grid(row=r, column=c, columnspan=2, sticky='we')
                #add 2 c since it takes up two button spaces
                c += 2
            #special button to span 2 button spaces   
            elif b == b16:
                #span 2 columns
                b.grid(row=r, column=c, columnspan=2, sticky='we')
                #add 2 to c increment since it spans 2 column
                c += 2
            else:
                #rest set single colum in row
                b.grid(row=r,column=c)
                c += 1
             #if column exceds 4 add 1 row so next item in loop will show in next row   
            if c >= 4:
                c = c - 4
                r += 1
        
     #method to create each button with defaule width    
    def createButton(self,val,write=True,width=7):
        return Button(self.master, text=val,command = lambda: self.click(val,write), width=width)
    
    def click(self,text,write):
        if write == None:
 
            
            if text == '=' and self.equation: 
                self.equation= re.sub(u"%", '/', self.equation)
                print(self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer,newline=True)
            elif text == u"AC":
                self.clear_screen()
                     
        else:
            self.insert_screen(text)
            
    def clear_screen(self):
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete('1.0', END)
 
    def insert_screen(self, value,newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(END,value)
        self.equation += str(value)
        self.screen.configure(state ='disabled')        
        
#create widget tk represents window       
root = Tk()
#add calculator class to main loop 
my_gui = Calculator(root)
#start loop 
root.mainloop()
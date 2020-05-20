from tkinter import *
from tkinter import ttk
from  tkinter import messagebox
landing=Tk()
# tk=Tk()
landing.title('Enter player Names')
landing.geometry('530x575')
root=Tk()

root.title('Tic Tac Toe')
root.geometry('530x575')
player=1
p1 = StringVar()
p2 = StringVar()

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)
def checkWinner():
    if(button1['text']=='X' and button2['text']=='X' and button3['text']=='X' or
       button4['text']=='X' and button5['text']=='X' and button6['text']=='X' or
       button7['text']=='X' and button8['text']=='X' and button9['text']=='X' or
       button1['text']=='X' and button4['text']=='X' and button7['text']=='X' or
       button2['text']=='X' and button5['text']=='X' and button8['text']=='X' or
       button3['text']=='X' and button6['text']=='X' and button9['text']=='X' or
       button1['text']=='X' and button5['text']=='X' and button9['text']=='X' or
       button3['text']=='X' and button5['text']=='X' and button7['text']=='X'):
       disableButton()
       messagebox._show('Winner',p1.get())
       
    if(button1['text']=='O' and button2['text']=='O' and button3['text']=='O' or
       button4['text']=='O' and button5['text']=='O' and button6['text']=='O' or
       button7['text']=='O' and button8['text']=='O' and button9['text']=='O' or
       button1['text']=='O' and button4['text']=='O' and button7['text']=='O' or
       button2['text']=='O' and button5['text']=='O' and button8['text']=='O' or
       button3['text']=='O' and button6['text']=='O' and button9['text']=='O' or
       button1['text']=='O' and button5['text']=='O' and button9['text']=='O' or
       button3['text']=='O' and button5['text']=='O' and button7['text']=='O'):
       disableButton()
       messagebox._show('Winner ',p2.get())
      
      

def buttonPressed(buttonNumber):
    global player
    if buttonNumber==1 and player==1:
        button1.config(text='X')
        player=2
    elif buttonNumber==1 and player==2:
        button1.config(text='O')
        player=1
    elif buttonNumber==2 and player==1:
        button2.config(text='X')
        player=2
    elif buttonNumber==2 and player==2:
        button2.config(text='O')
        player=1
    elif buttonNumber==3 and player==1:
        button3.config(text='X')
        player=2
    elif buttonNumber==3 and player==2:
        button3.config(text='O')
        player=1
    elif buttonNumber==4 and player==1:
        button4.config(text='X')
        player=2
    elif buttonNumber==4 and player==2:
        button4.config(text='O')
        player=1
    elif buttonNumber==5 and player==1:
        button5.config(text='X')
        player=2
    elif buttonNumber==5 and player==2:
        button5.config(text='O')
        player=1
    elif buttonNumber==6 and player==1:
        button6.config(text='X')
        player=2
    elif buttonNumber==6 and player==2:
        button6.config(text='O')
        player=1
    elif buttonNumber==7 and player==1:
        button7.config(text='X')
        player=2
    elif buttonNumber==7 and player==2:
        button7.config(text='O')
        player=1
    elif buttonNumber==8 and player==1:
        button8.config(text='X')
        player=2
    elif buttonNumber==8 and player==2:
        button8.config(text='O')
        player=1
    elif buttonNumber==9 and player==1:
        button9.config(text='X')
        player=2
    elif buttonNumber==9 and player==2:
        button9.config(text='O')
        player=1            
    checkWinner()




def displayGame():
    global button1,button2,button3,button4,button5,button5,button6,button7,button8,button9
    button1=ttk.Button(root,text='',command=lambda:buttonPressed(1))
    button1.grid(row=0,column=0,ipadx=50,ipady=50)
    button2=ttk.Button(root,text='',command=lambda:buttonPressed(2))
    button2.grid(row=0,column=1,ipadx=50,ipady=50)
    button3=ttk.Button(root,text='',command=lambda:buttonPressed(3))
    button3.grid(row=0,column=2,ipadx=50,ipady=50)
    button4=ttk.Button(root,text='',command=lambda:buttonPressed(4))
    button4.grid(row=1,column=0,ipadx=50,ipady=50)
    button5=ttk.Button(root,text='',command=lambda:buttonPressed(5))
    button5.grid(row=1,column=1,ipadx=50,ipady=50)
    button6=ttk.Button(root,text='',command=lambda:buttonPressed(6))
    button6.grid(row=1,column=2,ipadx=50,ipady=50)
    button7=ttk.Button(root,text='',command=lambda:buttonPressed(7))
    button7.grid(row=2,column=0,ipadx=50,ipady=50)
    button8=ttk.Button(root,text='',command=lambda:buttonPressed(8))
    button8.grid(row=2,column=1,ipadx=50,ipady=50)
    button9=ttk.Button(root,text='',command=lambda:buttonPressed(9))
    button9.grid(row=2,column=2,ipadx=50,ipady=50)

def check_empty():
    if player1_name.get() and player2_name.get():
        landing.destroy()
        displayGame()
    else:
        messagebox._show('error','enter both names')  
p1label=Label(landing,text='Player X')
p1label.grid(row=3,column=0)
p1label=Label(landing,text='Player Y')
p1label.grid(row=4,column=0)
player1_name = Entry(landing, textvariable=p1)
player1_name.grid(row=3, column=1)
player2_name = Entry(landing, textvariable=p2)
player2_name.grid(row=4, column=1)
btn=Button(landing,text='Ok',command=check_empty)
btn.grid(row=5,column=1,ipadx=20,ipady=10)
root.mainloop()
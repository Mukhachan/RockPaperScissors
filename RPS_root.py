from tkinter import *
import sys
import random
from time import sleep


opp=random.randint(1,3)
x = 0

if opp==1:
    gg="Rock"
elif opp==2:
    gg="Scissors"
else:
    gg="Paper"

# DEF - ALL LOGIC #

def output_EXIT(event):
    sleep(0.25)
    sys.exit()

def output_RETRY(event):
    sleep(0.25)
    LabelOPP.delete(0, END)
    LabelOPP.insert(0, 'Opponent choise:')    
    Labelresult.delete(0, END)
    Labelresult.insert(0, 'Result')  

def output_R(event):        # ROCK #
    opp=random.randint(1,3)
    sleep(0.2)

    if opp==1: 
        gg="Rock"
        res = 'DRAW'
        print('Your choise: rock!')        
        print(res)
        

    elif opp==2:
        gg="Scissors"
        res = 'You win!'
        print('Your choise: rock!')
        print(res)

    elif opp==3:
        gg="Paper"
        res = 'You lose'
        print('Your choise: rock!')
        print(res)

    LabelOPP.delete(0, END)
    LabelOPP.insert(0, gg)    
    Labelresult.delete(0, END)
    Labelresult.insert(0, res)
    print(f'Opponent: {gg}')

def output_P(event):        # PAPER #
    opp=random.randint(1,3)
    sleep(0.2)

    if opp==1:
        gg="Rock"
        res = 'You win!'
        print('Paper')
        print(res)
        
    elif opp==2:
        gg="Scissors"
        res = 'You lose'
        print('Paper')
        print(res)

    elif opp==3:
        gg="Paper"
        res = 'DRAW'
        print('Paper') 
        print(res)  

    LabelOPP.delete(0, END)
    LabelOPP.insert(0, gg)    
    Labelresult.delete(0, END)
    Labelresult.insert(0, res)
    print(f'Opponent: {gg}')

def output_S(event):        # SCISSORS #
    opp=random.randint(1,3)
    sleep(0.2)

    if opp==1:
        gg="Rock"
        res= 'You lose'
        print('Scissors')
        print(res)

    elif opp==2:
        gg="Scissors"
        res='DRAW'
        print('Scissors')
        print(res)

    elif opp==3:
        gg="Paper"
        res='You win!'
        print('Scissors')   
        print(res)

    LabelOPP.delete(0, END)
    LabelOPP.insert(0, gg)     
    Labelresult.delete(0, END)
    Labelresult.insert(0, res)    
    print(f'Opponent: {gg}')

# root #
root = Tk()
root.title("Rock-Paper-Scissors")
root.geometry('550x250')
root.resizable(0,0)

# Entry #
Labelresult = Entry(justify=CENTER)
Labelresult.insert(0, 'Result')

LabelOPP = Entry(justify=CENTER)
LabelOPP.insert(0, 'Opponent choise')

# Labels #
Label1 = Label(root, text='Your result: ')
Label2 = Label(root, text='Opponent choise: ')

# buttons #
ButtonStart = Button(root, text= "start", width=15, height=2)
ButtonQuit = Button(root, text='Quit')
ButtonRetry = Button(root, text='Retry')

btn1 = Button(root, text='1\n Rock', width=20, height=2)
btn2 = Button(root, text='2\n Paper', width=20, height=2)
btn3 = Button(root, text='3\n Scissors', width=20, height=2)


# grids #
#ButtonStart.grid(pady=10, row=1, column=1)#
ButtonQuit.grid(pady=10, padx=5,row=4, column=2, sticky=E)
ButtonRetry.grid(padx=5, row=4, column=0, sticky=W)

btn1.grid(pady=20, row=2, column=0)
btn2.grid(padx=20,row=2, column=1)
btn3.grid(row=2, column=2)

Labelresult.grid(row=4, column=1)
LabelOPP.grid(row=5, column=1)

Label1.grid(row=4, column=0, sticky=E)
Label2.grid(row=5, column=0, sticky=E)

# bind #
ButtonQuit.bind("<Button-1>", output_EXIT)
ButtonRetry.bind('<Button-1>', output_RETRY)

btn1.bind('<Button-1>', output_R)
btn2.bind('<Button-1>', output_P)
btn3.bind('<Button-1>', output_S)

root.mainloop()
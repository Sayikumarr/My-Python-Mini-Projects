from tkinter import *
import tkinter.messagebox
import random

techbeta = Tk()
techbeta.title("TechBeta.info - Luck Tac Toe")
techbeta.iconbitmap('D:\Saikumar\Downloads\insta_tech_tv9_icon.ico')

global rclick, flag, player2_name, player1_name, playerb, playera, rclick, n
rclick=False
playera = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()

player1_name = Entry(techbeta, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player1_name.insert(0, 'Shizuka')
player2_name = Entry(techbeta, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)
player2_name.insert(0, 'Nobita')

def reset():
    global rclick,t,l,flag, player2_name, player1_name, playerb, playera
    t=8
    l=[1,2,3,4,5,6,7,8,9]
    
    
    def btnClick(buttons):
        global rclick,flag,rclick,flag, player2_name, player1_name, playerb, playera
        global n,l,t
            
        if buttons["text"] == "Reset":
            reset()
            
        elif buttons == button10 and rclick == False:
            a=random.randint(0,t)
            n=l[a]
            l.remove(n)
            t=t-1
            if n==1:
                button1["bg"] = "Red"
            elif n==2:
                button2["bg"] = "Red"
            elif n==3:
                button3["bg"] = "Red"
            elif n==4:
                button4["bg"] = "Red"
            elif n==5:
                button5["bg"] = "Red"
            elif n==6:
                button6["bg"] = "Red"
            elif n==7:
                button7["bg"] = "Red"
            elif n==8:
                button8["bg"] = "Red"
            elif n==9:
                button9["bg"] = "Red"
            rclick = True
            playerb = p2.get() + "-Blue Wins!"
            playera = p1.get() + "-Red Wins!"
            checkForWin()
                
        elif buttons == button12 and rclick == True:
            a=random.randint(0,t)
            n=l[a]
            l.remove(n)
            t=t-1
            if n==1:
                button1["bg"] = "Blue"
            elif n==2:
                button2["bg"] = "Blue"
            elif n==3:
                button3["bg"] = "Blue"
            elif n==4:
                button4["bg"] = "Blue"
            elif n==5:
                button5["bg"] = "Blue"
            elif n==6:
                button6["bg"] = "Blue"
            elif n==7:
                button7["bg"] = "Blue"
            elif n==8:
                button8["bg"] = "Blue"
            elif n==9:
                button9["bg"] = "Blue"
            rclick = False
            checkForWin()
            
    def disableButton():
        button10.configure(state=DISABLED)
        button12.configure(state=DISABLED)
    
    def checkForWin():
        if (button1['bg'] == 'Red' and button2['bg'] == 'Red' and button3['bg'] == 'Red' or
            button4['bg'] == 'Red' and button5['bg'] == 'Red' and button6['bg'] == 'Red' or
            button7['bg'] =='Red' and button8['bg'] == 'Red' and button9['bg'] == 'Red' or
            button1['bg'] == 'Red' and button5['bg'] == 'Red' and button9['bg'] == 'Red' or
            button3['bg'] == 'Red' and button5['bg'] == 'Red' and button7['bg'] == 'Red' or
            button1['bg'] == 'Red' and button2['bg'] == 'Red' and button3['bg'] == 'Red' or
            button1['bg'] == 'Red' and button4['bg'] == 'Red' and button7['bg'] == 'Red' or
            button2['bg'] == 'Red' and button5['bg'] == 'Red' and button8['bg'] == 'Red' or
            button7['bg'] == 'Red' and button6['bg'] == 'Red' and button9['bg'] == 'Red'):
            disableButton()
            tkinter.messagebox.showinfo("Luck Tac Toe", playera)

        elif (button1['bg'] == 'Blue' and button2['bg'] == 'Blue' and button3['bg'] == 'Blue' or
              button4['bg'] == 'Blue' and button5['bg'] == 'Blue' and button6['bg'] == 'Blue' or
              button7['bg'] == 'Blue' and button8['bg'] == 'Blue' and button9['bg'] == 'Blue' or
              button1['bg'] == 'Blue' and button5['bg'] == 'Blue' and button9['bg'] == 'Blue' or
              button3['bg'] == 'Blue' and button5['bg'] == 'Blue' and button7['bg'] == 'Blue' or
              button1['bg'] == 'Blue' and button2['bg'] == 'Blue' and button3['bg'] == 'Blue' or
              button1['bg'] == 'Blue' and button4['bg'] == 'Blue' and button7['bg'] == 'Blue' or
              button2['bg'] == 'Blue' and button5['bg'] == 'Blue' and button8['bg'] == 'Blue' or
              button7['bg'] == 'Blue' and button6['bg'] == 'Blue' and button9['bg'] == 'Blue'):
              disableButton()
              tkinter.messagebox.showinfo("Luck Tac Toe", playerb)
              
        elif(t == -1):
            tkinter.messagebox.showinfo("Luck Tac Toe", "It is a Tie")
    
    
  

    buttons = StringVar()

    label = Label( techbeta, text="Player Red:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
    label.grid(row=1, column=0)

    label = Label( techbeta, text="Player Blue:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
    label.grid(row=2, column=0)

    button1 = Button(techbeta, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button1))
    button1.grid(row=3, column=0)

    button2 = Button(techbeta, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button2))
    button2.grid(row=3, column=1)

    button3 = Button(techbeta, text=' ',font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button3))
    button3.grid(row=3, column=2)

    button4 = Button(techbeta, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button4))
    button4.grid(row=4, column=0)

    button5 = Button(techbeta, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button5))
    button5.grid(row=4, column=1)

    button6 = Button(techbeta, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button6))
    button6.grid(row=4, column=2)

    button7 = Button(techbeta, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button7))
    button7.grid(row=5, column=0)

    button8 = Button(techbeta, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button8))
    button8.grid(row=5, column=1)

    button9 = Button(techbeta, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button9))
    button9.grid(row=5, column=2)
    
    button10 = Button(techbeta, text='Red', font='Times 20 bold', bg='black', fg='red', height=2, width=8, command=lambda: btnClick(button10))
    button10.grid(row=6, column=0)
    
    button11 = Button(techbeta, text='Reset', font='Times 20 bold', bg='gray', fg='black', height=2, width=8, command=lambda: btnClick(button11))
    button11.grid(row=6, column=1)
    
    button12 = Button(techbeta, text='Blue', font='Times 20 bold', bg='black', fg='Blue', height=2, width=8, command=lambda: btnClick(button12))
    button12.grid(row=6, column=2)
    
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)
   

tech_menu = Menu(techbeta)
techbeta.configure(menu=tech_menu)

tech_reset = Menu(tech_menu, tearoff=False)
tech_menu.add_cascade(label='Reset Game!', command=reset)

tech_exit = Menu(tech_menu, tearoff=False)
tech_menu.add_cascade(label='Exit', command=techbeta.quit)


reset()
techbeta.mainloop()
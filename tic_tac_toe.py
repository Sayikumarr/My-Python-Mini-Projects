from tkinter import *
import tkinter.messagebox
techbeta = Tk()
techbeta.title("TechBeta.info - Tic Tac Toe")
techbeta.iconbitmap('D:\Saikumar\Downloads\insta_tech_tv9_icon.ico')

global bclick, flag, player2_name, player1_name, playerb, playera
playera = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()

player1_name = Entry(techbeta, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player1_name.insert(0, 'Nobita')
player2_name = Entry(techbeta, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)
player2_name.insert(0, 'Shizuka')

def reset():
    global bclick,flag
    bclick = True
    flag = 0
    
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



    def btnClick(buttons):
        global bclick, flag, player2_name, player1_name, playerb, playera
        if buttons["text"] == " " and bclick == True:
            buttons["text"] = "  "
            buttons["bg"] = "Red"
            bclick = False
            playerb = p2.get() + "-Blue Wins!"
            playera = p1.get() + "-Red Wins!"
            checkForWin()
            flag += 1


        elif buttons["text"] == " " and bclick == False:
            buttons["text"] = "   "
            buttons["bg"] = "Blue"
            bclick = True
            checkForWin()
            flag += 1
        else:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")



    def checkForWin():
        if (button1['text'] == '  ' and button2['text'] == '  ' and button3['text'] == '  ' or
            button4['text'] == '  ' and button5['text'] == '  ' and button6['text'] == '  ' or
            button7['text'] =='  ' and button8['text'] == '  ' and button9['text'] == '  ' or
            button1['text'] == '  ' and button5['text'] == '  ' and button9['text'] == '  ' or
            button3['text'] == '  ' and button5['text'] == '  ' and button7['text'] == '  ' or
            button1['text'] == '  ' and button2['text'] == '  ' and button3['text'] == '  ' or
            button1['text'] == '  ' and button4['text'] == '  ' and button7['text'] == '  ' or
            button2['text'] == '  ' and button5['text'] == '  ' and button8['text'] == '  ' or
            button7['text'] == '  ' and button6['text'] == '  ' and button9['text'] == '  '):
            disableButton()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", playera)

        elif(flag == 8):
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

        elif (button1['text'] == '   ' and button2['text'] == '   ' and button3['text'] == '   ' or
              button4['text'] == '   ' and button5['text'] == '   ' and button6['text'] == '   ' or
              button7['text'] == '   ' and button8['text'] == '   ' and button9['text'] == '   ' or
              button1['text'] == '   ' and button5['text'] == '   ' and button9['text'] == '   ' or
              button3['text'] == '   ' and button5['text'] == '   ' and button7['text'] == '   ' or
              button1['text'] == '   ' and button2['text'] == '   ' and button3['text'] == '   ' or
              button1['text'] == '   ' and button4['text'] == '   ' and button7['text'] == '   ' or
              button2['text'] == '   ' and button5['text'] == '   ' and button8['text'] == '   ' or
              button7['text'] == '   ' and button6['text'] == '   ' and button9['text'] == '   '):
            disableButton()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)



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
   

tech_menu = Menu(techbeta)
techbeta.configure(menu=tech_menu)

tech_reset = Menu(tech_menu, tearoff=False)
tech_menu.add_cascade(label='Reset Game!', command=reset)

tech_exit = Menu(tech_menu, tearoff=False)
tech_menu.add_cascade(label='Exit', command=techbeta.quit)


reset()
techbeta.mainloop()
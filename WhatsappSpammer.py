import time
import tkinter as tk
from tkinter.ttk import Label

import pyautogui

# general functions
grp = False
reckless = False
name = ""

# declaring main root
root = tk.Tk()
root.title("WhatsApp Auto Message")

#setting icon

photo = tk.PhotoImage(file ="new.png")
root.iconphoto(False, photo)


# setting window size
root.geometry("525x360")
root.minsize(525, 360)
root.maxsize(525, 360)

# made to store name and other values
name_var = tk.StringVar()
msg_var = tk.StringVar()
time_var = tk.StringVar()


def setname():
    global name
    name = name_var.get()


def recklessmode():
    global reckless
    reckless = not reckless
    if reckless:
        reck_label = tk.Label(root, text='Reckless Mode', font=('calibre', 10, 'bold'), fg='green')
        reck_label.place(x=220, y=325, width=100, height=30)
    else:
        reck_label = tk.Label(root, text='', font=('calibre', 10, 'bold'))
        reck_label.place(x=220, y=325, width=100, height=30)


def sendmessage():
    num = int(time_var.get())
    if (num > 100) and not reckless:
        large()
        return None
    msg = msg_var.get()
    count = 0
    while count < num:
        count = count + 1
        print(count, end=", ")
        pyautogui.moveTo(int(pyautogui.size().width / 768) * 1020, int(pyautogui.size().height / 768) * 685,
                         duration=0.0005)
        pyautogui.click(int(pyautogui.size().width / 768) * 1020, int(pyautogui.size().height / 768) * 685,
                        duration=0.0005)
        # pyautogui.click(1020, 685, duration=0.0005)
        if not grp: pyautogui.typewrite(msg)
        if grp: pyautogui.typewrite("@" + name)
        if grp: pyautogui.typewrite(["tab"])
        if grp: pyautogui.typewrite(msg)
        pyautogui.typewrite(["enter"])
        if pyautogui.position() != p: break
    pyautogui.hotkey("altleft", "tab", duration=0.5)


def grpmode():
    global grp
    grp = not grp
    if (grp):
        grp_label = tk.Label(root, text='GROUP MODE: ' + name, font=('calibre', 10, 'bold'), fg='green', anchor='w')
        grp_label.place(x=50, y=325, width=150, height=30)
    else:
        grp_label = tk.Label(root, text='', font=('calibre', 10, 'bold'))
        grp_label.place(x=50, y=325, width=150, height=30)


def stickers():
    num = int(time_var.get())
    if (num > 200) and not reckless:
        large()
        return None
    p = 0
    while True:
        p = pyautogui.position()
        time.sleep(5)

        if p == pyautogui.position():
            break
    c = 0
    while c < num:
        c = c + 1
        pyautogui.click(p, duration=0.1)
        if pyautogui.position() != p: break
    pyautogui.hotkey("altleft", "tab", duration=0.5)


def large():
    top = tk.Toplevel(root)
    top.geometry("380x45")
    top.minsize(380, 45)
    top.maxsize(380, 45)
    top.title("Warning!!!!")
    Label(top, text="  Number Seem To be Large!!! Use reckless Mode", font=('Mistral 12 bold')).place(x=0, y=0)
    Label(top, text="      Loop Cannot be stopped in the middle!!!!", font=('Mistral 12 bold')).place(x=0, y=23)


def readme():
    top = tk.Toplevel(root)
    top.geometry("500x450")
    top.minsize(500, 450)
    top.maxsize(500, 450)
    top.title("Readme me")
    Label(top, text=" Welcome to Whatsapp Spammer By Saket \n\n********************************************************************************************\nONCE STARTED LOOP CAN NOT BE STOPPED IN THE MIDDLE\nINTERFERING MAY CAUSE MALFUNCTIONS IN YOUR PC\n********************************************************************************************\n\nHOW TO USE(MESSAGE)\n********************************************************************************************\n*Open Your Whatsapp Web Or App In Full Screen Mode\n*Overlay The App Window Over It\n*Type In a Message And Select Count\n*Select Chat You Want To Send Message To(Open That Chat In Whatsapp)\n*Click On \"Send Message\" To Start The SPAM\n\nHOW TO SEND STICKERS\n********************************************************************************************\n*Select Count\n*Click On Send Stickers\n*Open Stickers In Whatsapp and Hover The Mouse Over Any Sticker\n*Make The Mouse Statinary(BOOM!!)\n\n********************************************************************************************\n**WITHOUT RECKLESS MODE MAX COUNT IS 200 FOR STICKERS\n\n**WITHOUT RECKLESS MODE MAX COUNT IS 100 FOR MESSAGES\n********************************************************************************************\n", font='Mistral 10 bold').place(x=0, y=0)


# G U I
# canvas size
canvas = tk.Canvas(root, height=400, width=400)
canvas.pack()

# inside blue frame
frame = tk.Frame(root, bg="#263042")
frame.place(relheight=0.8, relwidth=0.8, rely=0.1, relx=0.1)

# upper title and DEV name
title_label = tk.Label(canvas, text='WhatsApp Spammer', font=('calibre', 10, 'bold'))
dev_label = tk.Label(root, text='by Saket', font=('calibre', 10, 'bold'))
dev_label.place(x=250, y=325, width=400, height=30)

# space above name pad
empty_label = tk.Label(frame, text="", bg="#263042")

# name pads and entry
name_label = tk.Label(frame, text='Name ', font=('calibre', 12, 'bold'), bg="#263042", fg="white")
name_entry = tk.Entry(frame, textvariable=name_var, font=('calibre', 10, 'normal'))
name_btn = tk.Button(frame, text='Set Name', command=setname)

# number of times
time_label = tk.Label(frame, text='Count ', font=('calibre', 12, 'bold'), bg="#263042", fg="white")
time_entry = tk.Entry(frame, textvariable=time_var, font=('calibre', 10, 'normal'))
time_btn = tk.Button(frame, text='Reckless Mode', command=recklessmode)

# message entry box
message_label = tk.Label(frame, text='     Message ', font=('calibre', 12, 'bold'), bg="#263042", fg="white")
message_entry = tk.Entry(frame, textvariable=msg_var, font=('calibre', 10, 'normal'))
message_entry.place(x=10, y=100, width=400, height=100)

# all buttons
# send message
message_btn = tk.Button(frame, text='Send Message', command=sendmessage)
message_btn.place(x=18, y=220, width=80, height=40)

# stickers
sticker_btn = tk.Button(frame, text='Send Stickers', command=stickers)
sticker_btn.place(x=118, y=220, width=80, height=40)

# group mode
grpMode_btn = tk.Button(frame, text='Toggle Group', command=grpmode)
grpMode_btn.place(x=218, y=220, width=80, height=40)

# readme
grpMode_btn = tk.Button(frame, text='Readme', command=readme)
grpMode_btn.place(x=318, y=220, width=80, height=40)

empty_label.grid(row=0)
name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
name_btn.grid(row=1, column=2, padx=30)
message_label.grid(row=3, column=0)
time_label.grid(row=2, column=0)
time_entry.grid(row=2, column=1)
time_btn.grid(row=2, column=2, padx=30)
title_label.grid(row=1, column=0)
root.mainloop()

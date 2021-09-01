#ON/OFF Button with py firmata App and Change Image and Text
from tkinter import *#import everything from tkinter mofule
from pyfirmata import Arduino, util#importing Arduino and utility from pyfirmata mpdule
board = Arduino('Com11')# Create a variable name board and assign the Arduino board and COM Port
root=Tk()# Application window name is root and assign tkinter
root.geometry('800x600')# Application window Size
root.title("PYFIRMATA APP")# Application Tiltle
root.iconbitmap("python_logo_icon.ico")
Appname=Label(root,text="WELCOME TO ANOKHAUTOMATION",fg="purple",font=("Arial",32,"bold"))
Appname.pack(pady=10)

global relay_1
relay_1=True
# Create a Label for Load1
relay1label=Label(root,text="Click  Button1",fg="green",font=("Arial",32,"bold"))
relay1label.pack(pady=10)
#Define our Switch function
def Switch_1():
    global relay_1
    if relay_1:
        board.digital[12].write(1)  # ON the led on Digitalpin 12
        on_button_1.config(image=off_image)# change on_button image
        relay1label.config(text="LAMP 1 is Off",fg="blue")# change relay1 label
        relay_1=False
    else:
        board.digital[12].write(0)  # ON the led on Digitalpin 12
        on_button_1.config(image=on_image)# change on_button image
        relay1label.config(text="LAMP 1 is ON",fg="red")# change relay1 label
        relay_1=True
on_image =PhotoImage(file='OnLamp-icon.png')# image of OFF LAMP
off_image =PhotoImage(file='OffLamp-icon.png')# image of ON LAMP
on_button_1=Button(root,image=off_image,borderwidth=0,command=Switch_1)
on_button_1.pack(pady=5)# Created a button to control the Digital Pin 12 of Arduino
#Appname=Label(root,text="WELCOME TO ANOKHAUTOMATION",fg="yellow",font=("Arial",32,"bold"))
#Appname.pack(pady=10)
root.mainloop()
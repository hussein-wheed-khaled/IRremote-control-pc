import serial.tools.list_ports
import pyautogui
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
from threading import Thread
from tkinter import *
from tkinter import messagebox
from customtkinter import *
import ttkbootstrap as tb
















def working():
 global window
 global start
 global la


 window = tb.Window(title="EasyIR")
 window.iconbitmap("remote-control.ico")

 window.geometry("600x200")
 style=tb.Style()
 style.configure("success.TButton",font=(" ",14,"bold"))



 start=tb.Button(window,text="Start",command=recieve_input,bootstyle="success",width=10,style="success.TButton")
 start.pack(side=BOTTOM,pady=20)
 la=Label(window,text="press start to get input from remote control")
 la.pack(side=TOP)

 window.mainloop()

def recieve_input():
 global x,y
 global value1
 global packet

 x=20
 y=20

 start.destroy()
 la.destroy()

 def val(a):
     global v

     x = 10
     y = 10
     v=-20
     def select(event):
         v=-20
         x=20
         y=20
         while True:

             window.update_idletasks()
             window.update()
             packet = arduino.readline()

             print(packet)

             if check.get()=="enb":
              if packet == b'FEF906\r\n':
                 v += 2
                 if v > 0:
                     v = 0
                 volume.SetMute(0, None)
                 volume.SetMasterVolumeLevel(v, None)
              elif packet == b'FED12E\r\n':
                 v -= 2
                 if v < -50:
                     v = -50
                 volume.SetMute(0, None)
                 volume.SetMasterVolumeLevel(v, None)
              elif packet == b'FE0BF4\r\n':
                 volume.SetMute(1, None)

              if packet == b'right\r\n':

                 x += int(scale.get())
                 pyautogui.moveTo(x, y, 0.2)

              elif packet == b'left\r\n':
                 x -= int(scale.get())
                 pyautogui.moveTo(x, y, 0.2)

              elif packet == b's+\r\n':
                 pyautogui.scroll(int(scale2.get()))

              elif packet == b's-\r\n':
                 pyautogui.scroll(-int(scale2.get()))

              elif packet == b'down\r\n':
                 y += int(scale.get())
                 pyautogui.moveTo(x, y, 0.2)


              elif packet == b'up\r\n':
                 y -= int(scale.get())
                 pyautogui.moveTo(x, y, 0.2)

              elif packet == b'ok\r\n':
                 pyautogui.click()

              if packet == b'FEE916\r\n':
                 pyautogui.hotkey("tab")

              if packet == b'FE718E\r\n':

                 pyautogui.hotkey("right")

              elif packet == b'FE31CE\r\n':
                 pyautogui.hotkey("left")

              elif packet == b'FE8976\r\n':
                 pyautogui.hotkey("down")

              elif packet == b'FE916E\r\n':
                 pyautogui.hotkey("up")
              elif packet == b'FE29D6\r\n':
                 pyautogui.hotkey("enter")






     while True:

         window.update_idletasks()
         window.update()
         packet = arduino.readline()


         print(packet)

         if packet == b'right\r\n':

             x += int(scale.get())
             pyautogui.moveTo(x, y, 0.2)

         elif packet == b'left\r\n':
             x -= int(scale.get())
             pyautogui.moveTo(x, y, 0.2)

         elif packet == b's+\r\n':
             pyautogui.scroll(int(scale2.get()))

         elif packet == b's-\r\n':
             pyautogui.scroll(-int(scale2.get()))

         elif packet == b'down\r\n':
             y += int(scale.get())
             pyautogui.moveTo(x, y, 0.2)


         elif packet == b'up\r\n':
             y -= int(scale.get())
             pyautogui.moveTo(x, y, 0.2)

         elif packet == b'ok\r\n':
             pyautogui.click()

         if packet == b'FEE916\r\n':
             pyautogui.hotkey("tab")


         if packet == b'FE718E\r\n':

             pyautogui.hotkey("right")

         elif packet == b'FE31CE\r\n':
             pyautogui.hotkey("left")

         elif packet == b'FE8976\r\n':
             pyautogui.hotkey("down")

         elif packet == b'FE916E\r\n':
             pyautogui.hotkey("up")
         elif packet == b'FE29D6\r\n':
             pyautogui.hotkey("enter")
         check.bind("<Button-1>", select)





















 la1=CTkLabel(window,text="mouse sensitivity :")
 la1.pack(side=TOP)

 la2 = CTkLabel(window, text="scroll sensitivity :")
 la2.place(x=250,y=60)
 scale=CTkSlider(window,from_=40,to=160,command=val)
 scale.pack()



 check=CTkCheckBox(window,text="Enable control sound ",variable=StringVar(),onvalue="enb")
 check.place(x=200,y=130)




 scale2 = CTkSlider(window, from_=70, to=200, command=val)
 scale2.place(x=200,y=90)

 print(scale.get())







def checking():

 for i in range(10):
    port = "COM" + str(i)
    time.sleep(0.3)

    try:
        global arduino
        arduino = serial.Serial(port=port, baudrate=9600, timeout=0.3)
    except:

        continue

 ports = serial.tools.list_ports.comports()

 for p in ports:
    with open("temp.txt", "w") as d:
        d.write(p.description)
 with open("temp.txt", "r+") as dd:
    ss = dd.readline()
    if "CH340" not in ss:
        root = Tk()
        root.iconbitmap("remote-control.ico")
        root.overrideredirect(1)
        root.withdraw()
        messagebox.showerror("Error", "error no port detected please make sure you connect the reader to your pc")
        exit()
    else:
        working()


checking()




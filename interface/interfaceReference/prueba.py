try:
    import Tkinter as tk
except:
    import tkinter as tk
    

class Test():
   def __init__(self):
       self.root = tk.Tk()
       self.label=tk.Label(self.root,
                           text = "Label")
       self.label2=tk.Label(self.root,
                           text = "cafcaca")
       self.buttonForget = tk.Button(self.root,
                          text = 'Click to hide Label',
                          command=lambda: self.label.pack_forget())
       self.buttonRecover = tk.Button(self.root,
                          text = 'Click to show Label',
                          command=lambda: self.label.pack())       
       
       self.buttonForget.pack()
       self.buttonRecover.pack()
       self.label2.pack(side="bottom")
       self.label.pack(side="bottom")

       self.root.mainloop()

   def quit(self):
       self.root.destroy()
        
app = Test()
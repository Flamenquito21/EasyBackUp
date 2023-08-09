import tkinter as tk
import customtkinter
import tksvg
def openWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = tk.Toplevel(root,takefocus=True)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    tk.Label(newWindow,
          text ="This is a new window").pack()
    

root = tk.Tk() #root widget is main windows
root.title("Simple BackUp")
root.minsize(480, 270)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x=(screen_width-screen_width/2)/2
y=(screen_height-screen_height/2)/2
root.geometry('{}x{}+{}+{}'.format(int(screen_width/2),int(screen_height/2),int(x),int(y)))

root.configure(background="#FFF")

header= tk.Frame(root)
header.pack(fill="both")

photo1 = tksvg.SvgImage(file="C:/Users/Andres/Desktop/scriptPython/img/moon.svg")
photoimage1 = photo1.subsample(20,20)
tk.Button(header,image=photoimage1,activebackground='yellow').pack(side='right')


choseFrame  =  tk.Frame(root,  bg='grey')
choseFrame.pack(side='top',  fill='both',  padx=10,  pady=5,  expand=True)

simpleackupbutton= tk.Button(choseFrame,text="fsafewsf",command=openWindow,bg="purple")
simpleackupbutton.grid(row=0,column=0)
autoBackupbutton= tk.Button(choseFrame,text="fsafewsf",command=openWindow)
autoBackupbutton.grid(row=0,column=1)
choseFrame.grid_rowconfigure(0,weight=1)
choseFrame.grid_columnconfigure(0,weight=1)
choseFrame.grid_columnconfigure(1,weight=1)


# text = tk.Label(root, text="Welcome to Simple BackUp",borderwidth=20)
# text.pack()

# image = tk.PhotoImage(file="cat.gif",format="gif")
# img = tk.Label(root, image=image)
# img.pack()

# button= tk.Button(root,text="fsafewsf",command=openWindow)
# button.pack(fill=tk.X)
# img = tk.Label(root, image=image)
# img.pack()
# img = tk.Label(root, image=image)
# img.pack(fill=tk.X)


# label_frame = tk.LabelFrame(root, text='This is Label Frame')
# label_frame.pack(expand='yes', fill='both')
root.mainloop()
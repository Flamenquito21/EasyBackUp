import customtkinter
from customtkinter import filedialog
import tkfilebrowser
from interface.customTkinterInteface.listFilesAndFolder import FilesAndFoldersList,FileOrFolder
import os

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

#Definiendo como se abrira la pestaña y el titulo
root = customtkinter.CTk() 
root.title("Simple BackUp")
root.iconbitmap()#icono barra titulo
root.minsize(480, 270)




screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x=(screen_width-screen_width/2)/2
y=(screen_height-screen_height/2)/2
root.geometry('{}x{}+{}+{}'.format(int(screen_width/2),int(screen_height/2),int(x),int(y)))

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure((0,1,2),weight=1)

Title=customtkinter.CTkFont('Arial',size=20,weight='bold')
def button_function():
    print("button pressed")
    
def open_toplevel():
        print('Se abre ventana')
        # if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
        #     self.toplevel_window = OptionView(self)  # create window if its None or destroyed
        # else:
        #     self.toplevel_window.focus()  # if window exists focus it

menuBar=customtkinter.CTkFrame(master=root,height=int(screen_height)/20) # type: ignore
menuBar.grid(column=0,row=0,sticky="ew",columnspan=3)
buttonOption=customtkinter.CTkButton(master=menuBar, text="Configuration",command=open_toplevel)
buttonOption.pack(side='left',  fill='both',  padx=5,  pady=5)
buttonReportProblem=customtkinter.CTkButton(master=menuBar, text="ReportProblem")
buttonReportProblem.pack(side='left',  fill='both',  padx=5,  pady=5)





leftPanel=customtkinter.CTkFrame(master=root)
leftPanel.grid(column=0,row=1,padx=5, pady=10,sticky="nsew")

leftPanel.grid_rowconfigure(2, weight=1)
leftPanel.grid_columnconfigure((0,1),weight=1)
leftPanel.grid_anchor(anchor='center')


TitleLeft=customtkinter.CTkLabel(master=leftPanel, text="Select folders and files",font=Title)
TitleLeft.grid(column=0,row=0,sticky='nsew',columnspan=2,pady=(40,20))

listFileAndFolder=FilesAndFoldersList(master=leftPanel)


def selectAndInsertFiles():
    fileNames= tkfilebrowser.askopenfilenames(title='Select folder o folders',okbuttontext='Select')
    for FileOrFolderName in fileNames:
        listFileAndFolder.addFilesOrFolder(FileOrFolder(master=listFileAndFolder,nameFileOrFolder=FileOrFolderName))
    print('llega')
    listFileAndFolder.refreshAllFrame()

def selectAndInsertFolders():
    folderNames= tkfilebrowser.askopendirnames(title='Select folder o folders',okbuttontext='Select')
    for FileOrFolderName in folderNames:
        listFileAndFolder.addFilesOrFolder(FileOrFolder(master=listFileAndFolder,nameFileOrFolder=FileOrFolderName))
    print('llega')
    listFileAndFolder.refreshAllFrame()

simpleBackUpButton=customtkinter.CTkButton(master=leftPanel, text="Select files",command=selectAndInsertFiles,width=70)
simpleBackUpButton.grid(column=0,row=1,sticky='e',padx=(20,10))
simpleBackUpButton=customtkinter.CTkButton(master=leftPanel, text="Select folders",command=selectAndInsertFolders,width=70)
simpleBackUpButton.grid(column=1,row=1,sticky='w',padx=(10,20))

listFileAndFolder.grid(column=0,row=2,sticky='nsew',pady=(40,20),padx=20,columnspan=2)




centerPanel=customtkinter.CTkFrame(master=root)
centerPanel.grid(column=1,row=1,padx=5, pady=10,sticky="nsew")
centerPanel.grid_rowconfigure(2, weight=1)
centerPanel.grid_columnconfigure((0),weight=1)
centerPanel.grid_anchor(anchor='center')

TitleCenter=customtkinter.CTkLabel(master=centerPanel, text="Opcion de de BackUp",font=Title)
TitleCenter.grid(column=0,row=0,sticky='nsew',pady=(40,20))
# AutoBackUpButton=customtkinter.CTkButton(master=centerPanel, text="Make AutoBackUp")#Valorar si se puede puede poner setUp BackUp
# AutoBackUpButton.pack(anchor="center",expand=True)
# AutoBackUpButton=customtkinter.CTkButton(master=centerPanel, text="Make AutoBackUp")#Valorar si se puede puede poner setUp BackUp
# AutoBackUpButton.pack(anchor="center",expand=True)
customtkinter.CTkRadioButton(master=centerPanel, text='Programable').grid(column=0,row=1,sticky='n')
customtkinter.CTkRadioButton(master=centerPanel, text='caca').grid(column=0,row=2,sticky='n')





rightPanel=customtkinter.CTkFrame(master=root)
customtkinter.CTkLabel(master=rightPanel,text="Destino",font=Title).pack()
rightPanel.grid(column=2,row=1,padx=5, pady=10,sticky="nsew")

root.mainloop()
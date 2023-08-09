# Pertenece al ichero listGilesAndFolder.py
import customtkinter
from PIL import Image, ImageTk
from globalArrays.fileOrFolderToBackUp import filesAndFoldersArray


class FilesAndFoldersList(customtkinter.CTkScrollableFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.filesAndFolders=filesAndFoldersArray

    def addFilesOrFolder(self,frameFileOrFolder):
            
            self.filesAndFolders.add(frameFileOrFolder)
    
    def refreshAllFrame(self):
        print('Hola')
        for fileOrFolder in self.filesAndFolders:
            fileOrFolder.pack(fill='x',pady=2)
        print(self.filesAndFolders)

        

class FileOrFolder(customtkinter.CTkFrame):
    
    def __init__(self,master,nameFileOrFolder,**kwargs):
        super().__init__(master, **kwargs)
    
        self.name=customtkinter.CTkLabel(master= self, text=nameFileOrFolder,compound='top')
        
        def deleteFileOrFolder():
            self.forget()
            filesAndFoldersArray.remove(self)  
            print(filesAndFoldersArray)

        self.button=customtkinter.CTkButton(master= self, 
                                            text='',
                                            command=deleteFileOrFolder,
                                            height=20,width=20,
                                            border_spacing=0,
                                            fg_color='transparent',
                                            hover=False,
                                            image=customtkinter.CTkImage(size=(15,15),dark_image=Image.open('C:/Users/Andres/Desktop/scriptPython/assets/delete.png')))#Se debe dejar las funciones sin parentesis para que se ejecute la funcion cuando se clica en el boton
        # self.pack_configure(side='left')
        self.button.pack(side='right')
        # self.name.pack(side='right',expand=False,fill='x',anchor='w',in_=self)
        self.name.pack(side='left',in_=self)

        def on_resize(event):
            print(f'Window resized to {event.width}x{event.height}')
        self.bind('<Configure>', on_resize)
        def hover(event):
            customtkinter.CTkLabel(master=self,text= '...').place(x=0,y=0)
        self.name.bind('<Enter>', hover)

    def __repr__(self):
        return "FileOrFolder(%s, %s)" % (self.name, self.button)
    def __eq__(self, other):
        if isinstance(other, FileOrFolder):
            print("aaaaa")
            return ((self.name.cget('text') == other.name.cget('text')))
        else:
            return False
    def __ne__(self, other):
        return (not self.__eq__(other))
    def __hash__(self):
        return hash(self.name.cget('text'))
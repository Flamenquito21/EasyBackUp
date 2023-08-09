import shutil #CopyFiles
import os #take info files
import json #yo read config.json
import tkinter #Interface
# ficheroEscrito = open('fechaModificacion.ficherito','w')
# for i in range(1000):
#     ficheroEscrito.write((str('{}a '.format(i))))
# ficheroEscrito.close()

#Obteniendo la fecha antigua de modificación
file=open('config.json','r') 
data=file.read()
file.close()
jsonData=json.loads(data)

for f in range(len(jsonData['AutoBackups'])):#travel autobackups
    for i in range(len(jsonData['AutoBackups'][f]['filesOrFolder'])):#travel files

        folderOrFilePath=jsonData['AutoBackups'][f]['filesOrFolder'][i]['path']#Path storage in config.json
        
        if os.path.exists(folderOrFilePath):
            modifiedFileDate=os.path.getmtime(folderOrFilePath)#The modification date of file or folder which we must make a copy
            
            if os.path.isfile(folderOrFilePath):
                if(jsonData['AutoBackups'][f]['filesOrFolder'][i]['modification']!=modifiedFileDate):
                    #Copy the file or folder in pathWhereCopyFiles
                    shutil.copy2(src=folderOrFilePath,dst=jsonData['AutoBackups'][f]['pathWhereCopyFiles'])
                    

            else:
                #get the name of folder which we need to copy into the pathWhereCopyFiles
                folders=folderOrFilePath.split("/")
                nameLastFolder=folders[len(folders)-1]#If we have in config json "path:":"C:/Users/moco/Desktop/cacatua" the initialization value is cacatua

                try:
                    if(jsonData['AutoBackups'][f]['filesOrFolder'][i]['modification']!=modifiedFileDate):
                        print("Caca")             
                        shutil.rmtree(path=jsonData['AutoBackups'][f]['pathWhereCopyFiles']+'/'+nameLastFolder)
                except FileNotFoundError:
                    print("No se encontro el fichero a borrar en el backup")
                finally:
                    shutil.copytree(src=folderOrFilePath,dst=jsonData['AutoBackups'][f]['pathWhereCopyFiles']+'/'+nameLastFolder,symlinks=True,dirs_exist_ok=True)
            
            #rewrite the json with the new modicated date
            jsonData['AutoBackups'][f]['filesOrFolder'][i]['modification']=modifiedFileDate
            writeFichero=open('config.json','w')
            writeFichero.write(json.dumps(jsonData))
            print("FicheroModificado: {}".format(folderOrFilePath))
            writeFichero.close

        else:
            print('No existe el fichero o directorio')





        


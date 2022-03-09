from tkinter import *
from tkinter.filedialog import askopenfilename

def CargarArchivo():
    root = Tk()
    root.withdraw()
    root.update()
    pathString = askopenfilename(filetypes=[("Text files","*.form")])
    if pathString:
        openFile = open(pathString,'r')
        ArchivoEntrada = openFile.read()
    root.destroy()

VentanaPrincipal = Tk()
VentanaPrincipal.geometry("1200x600")
VentanaPrincipal.title("Formularios USAC")


botonCargar = Button(VentanaPrincipal, text="Cargar Archivo", width=15, height=5, font=("Arial", 12, "italic"), command= CargarArchivo)
botonAnalizar = Button(VentanaPrincipal, text="Analizar Archivo", width=15, height=5, font=("Arial", 12, "italic"))
Titulo = Label(VentanaPrincipal, text = "Generador de Formularios USAC", font=("Arial", 16, "italic"))


Titulo.place(x=300,y=25,width=600)
botonCargar.place(x=0, y=0)
botonAnalizar.place(x=0, y=85)






VentanaPrincipal.mainloop()

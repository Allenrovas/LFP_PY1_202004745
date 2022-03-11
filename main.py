from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from Analizador import AnalizadorLexico


def CargarArchivo():
    root = Tk()
    root.withdraw()
    root.update()
    pathString = askopenfilename(filetypes=[("Text files","*.data")])
    if pathString:
        openFile = open(pathString,'r')
        ArchivoEntrada = openFile.read()
    root.destroy()
    Entrada.delete(1.0,END)
    print("Jijija")
    Entrada.insert(1.0,ArchivoEntrada)

def AnalizarArchivo():
    lexico = AnalizadorLexico()
    lexico.analizar(Entrada.get())

def callbackFunc(event):
    if listasReportes.get() == "Reporte de Tokens":
        print("hi")
    elif listasReportes.get() == "Reporte de Errores":
        print("hi 2")
    elif listasReportes.get() == "Manual de Usuario":
        print("hi3")
    elif listasReportes.get() == "Manual Técnico":
        print("hi4")

VentanaPrincipal = Tk()
VentanaPrincipal.geometry("1200x600")
VentanaPrincipal.title("Formularios USAC")
VentanaPrincipal.config(bg="SkyBlue1")


botonCargar = Button(VentanaPrincipal, text="Cargar Archivo", width=15, height=1, font=("Arial", 12, "italic"), command= CargarArchivo)
botonAnalizar = Button(VentanaPrincipal, text="Analizar Archivo", width=15, height=1, font=("Arial", 12, "italic"), command= AnalizarArchivo)
Titulo = Label(VentanaPrincipal, text = "Generador de Formularios USAC", font=("Arial", 16, "italic"),  bg="SkyBlue1")
TituloReportes = Label(VentanaPrincipal, text = "Reportes", font=("Arial", 16, "italic"),  bg="SkyBlue1")
listasReportes = ttk.Combobox(VentanaPrincipal, font=("Arial", 12, "italic"), width=20, height=5,state="readonly", values=["Reporte de Tokens","Reporte de Errores","Manual de Usuario","Manual Técnico"])
listasReportes.current(0)
listasReportes.bind("<<ComboboxSelected>>", callbackFunc)
Entrada = Text(VentanaPrincipal, font=("Arial", 12, "italic"))
BarraVertical = Scrollbar(Entrada)
BarraHorizontal = Scrollbar(Entrada ,orient=HORIZONTAL)
Entrada.config(yscrollcommand=BarraVertical.set,wrap = "none",xscrollcommand=BarraHorizontal.set)
BarraHorizontal.pack(side = BOTTOM, fill = X)
BarraHorizontal.config(command=Entrada.xview)
BarraVertical.pack(side = RIGHT, fill = Y)
BarraVertical.config(command=Entrada.yview)


VariableAnalizar = Entrada
print(VariableAnalizar)

Titulo.place(x=300,y=25,width=600)
TituloReportes.place(x=1000,y=0,width=100)
botonCargar.place(x=0, y=0)
botonAnalizar.place(x=0, y=45)
listasReportes.place(x=975,y=30)
Entrada.place(x= 25,y=90,width=1150,height=500 )






VentanaPrincipal.mainloop()

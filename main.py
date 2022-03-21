from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from tkinter import messagebox
from Analizador import AnalizadorLexico
from os import system, startfile
ComprobacionCarga = False


def CargarArchivo():
    root = Tk()
    root.withdraw()
    root.update()
    pathString = askopenfilename(filetypes=[("Text files","*.form")])
    if pathString:
        openFile = open(pathString,'r')
        ArchivoEntrada = openFile.read()
    root.destroy()
    Entrada.delete(1.0,END)
    Entrada.insert(1.0,ArchivoEntrada)


def AnalizarArchivo():
    global ComprobacionCarga
    lexico = AnalizadorLexico()
    ArchivoAnalizar= Entrada.get("1.0",END)
    lexico.AnalizadorLexico(ArchivoAnalizar)
    lexico.generarHtml()
    lexico.imprimirTokens()
    lexico.imprimirErrores()
    

    
def callbackFunc(event):
    global ComprobacionCarga
    lexico = AnalizadorLexico()
    ArchivoAnalizar= Entrada.get("1.0",END)
    lexico.AnalizadorLexico(ArchivoAnalizar)
    if listasReportes.get() == "Reporte de Tokens":
        lexico.reporteTokens()

    elif listasReportes.get() == "Reporte de Errores":
        lexico.reporteErrores()

    elif listasReportes.get() == "Manual de Usuario":
        startfile('Documentacion\ManualUsuario.pdf')

    elif listasReportes.get() == "Manual Técnico":
        startfile('Documentacion\ManualTecnico.pdf')

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

Titulo.place(x=300,y=25,width=600)
TituloReportes.place(x=1000,y=0,width=100)
botonCargar.place(x=0, y=0)
botonAnalizar.place(x=0, y=45)
listasReportes.place(x=975,y=30)
Entrada.place(x= 25,y=90,width=1150,height=500 )

VentanaPrincipal.mainloop()

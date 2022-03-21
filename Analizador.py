from Token import Token
from Error import Error
from prettytable import PrettyTable
from Atributos import Atributos
from os import system, startfile

ListaAtributos = []
Entrada1 = ''

class AnalizadorLexico:

    def __init__(self) -> None:
        self.listaTokens  = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 0
        self.buffer = ''
        self.estado = 0
        self.i = 0
    
    def AnalizadorLexico(self, Entrada):
        global Entrada1
        global ListaAtributos
        self.listaTokens = []
        self.listaErrores = []
        ListaAuxiliar = []
        ListaAuxiliar2 = []
        ListaAuxiliar3 = []

        linea = 1
        columna = 1
        buffer = ''
        centinela = '¬'
        estado = 0
        Entrada += centinela
        Entrada1 = Entrada

        i = 0
        while i< len(Entrada):
            c = Entrada[i]

            if estado == 0:
                if c == '~':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'guionOndulado', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '[':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'corcheteIzquierdo', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ']':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'corcheteDerecho', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '<':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'menorQue', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '>':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'mayorQue', linea, columna))
                    buffer = ''
                    columna += 1
                    j=0
                    tipo = None
                    valor = None
                    fondo = None
                    nombre = None
                    evento = None
                    while j < len(ListaAuxiliar):
                        if ListaAuxiliar[j] == "tipo":
                           tipo = ListaAuxiliar2[j]
                        elif ListaAuxiliar[j] == "valor":
                            valor = ListaAuxiliar2[j]
                        elif ListaAuxiliar[j] == "fondo":
                            fondo = ListaAuxiliar2[j]
                        elif ListaAuxiliar[j] == "nombre":
                            nombre = ListaAuxiliar2[j]
                        elif ListaAuxiliar[j] == "info":
                            evento = ListaAuxiliar[j]
                        elif ListaAuxiliar[j] == "entrada":
                            evento = ListaAuxiliar[j]

                        j += 1
                    objeto = Atributos(tipo,valor,fondo,ListaAuxiliar3,nombre,evento)
                    ListaAtributos.append(objeto)
                    ListaAuxiliar = []
                    ListaAuxiliar2 = []
                    ListaAuxiliar3 = []
                elif c == ':':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'dosPuntos', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ',':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'coma', linea, columna))
                    buffer = ''
                    columna += 1
                elif  c == '"':
                    buffer += c
                    columna += 1
                    estado = 1   
                elif  c == "'":
                    buffer += c
                    columna += 1
                    estado = 1
                elif c.isalpha() or c.isdigit():
                    buffer += c
                    columna += 1
                    estado = 2
                elif c == '\n':
                    linea += 1
                    columna = 1
                elif c in ['\t',' ']:
                    columna += 1
                elif c == '\r':
                    pass
                elif c == centinela:
                    print('Se aceptó la cadena!')
                    break
                else:
                    buffer += c
                    self.listaErrores.append(Error('Caracter ' + buffer + ' no reconocido en el lenguaje.', linea, columna))
                    buffer = ''
                    columna += 1
            
            
            elif estado == 1:
                if  c == '"':
                    buffer += c
                    self.listaTokens.append(Token(buffer, "cadenaComillas", linea, columna))
                    ListaAuxiliar2.append(buffer)
                    buffer = ""
                    columna += 1
                    estado = 0
                if  c == "'" :
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'cadenaComillasSimple', linea, columna))
                    ListaAuxiliar3.append(buffer)
                    buffer = ""
                    columna += 1
                    estado = 0
                elif c == '\n':
                    buffer += c
                    linea += 1
                    columna = 1
                elif c == '\r':
                    buffer += c
                else:
                    buffer += c
                    columna += 1
                pass
                    
            elif estado == 2:
                if c.isalpha() or c.isdigit():
                    buffer += c
                    columna += 1
                else:
                    if buffer == 'tipo':
                        self.listaTokens.append(Token(buffer, 'tipo', linea, columna))
                        ListaAuxiliar.append(buffer)
                    elif buffer == 'valor':
                        self.listaTokens.append(Token(buffer, 'valor', linea, columna))
                        ListaAuxiliar.append(buffer)
                    elif buffer == 'fondo':
                        self.listaTokens.append(Token(buffer, 'fondo', linea, columna))
                        ListaAuxiliar.append(buffer)
                    elif buffer == 'valores':
                        self.listaTokens.append(Token(buffer, 'valores', linea, columna))
                        ListaAuxiliar.append(buffer)
                    elif buffer == 'nombre':
                        self.listaTokens.append(Token(buffer, 'nombre', linea, columna))
                        ListaAuxiliar.append(buffer)
                    elif buffer == 'evento':
                        self.listaTokens.append(Token(buffer, 'evento', linea, columna))
                        ListaAuxiliar.append(buffer)
                    elif buffer == 'formulario':
                        self.listaTokens.append(Token(buffer, 'formulario', linea, columna))
                    elif buffer == 'info':
                        self.listaTokens.append(Token(buffer, 'info', linea, columna))
                        ListaAuxiliar.append(buffer)
                    elif buffer == 'entrada':
                        self.listaTokens.append(Token(buffer, 'entrada', linea, columna))
                        ListaAuxiliar.append(buffer)    
                    i -= 1
                    estado = 0
                    buffer = ''
            i += 1
        for objeto in ListaAtributos:
            print(objeto.tipo,objeto.valor,objeto.fondo,objeto.nombre,objeto.valores,objeto.evento)

    def imprimirTokens(self):
        '''Imprime una tabla con los tokens'''
        x = PrettyTable()
        x.field_names = ["Lexema","linea","columna","tipo"]
        for token in self.listaTokens:
            x.add_row([token.lexema, token.linea, token.columna,token.tipo])
        print(x)

    def imprimirErrores(self):
        '''Imprime una tabla con los errores'''
        x = PrettyTable()
        x.field_names = ["Descripcion","linea","columna"]
        for error_ in self.listaErrores:
            x.add_row([error_.descripcion, error_.linea, error_.columna])
        print(x)
    
    def reporteTokens(self):
        CuerpoHtml= """<!DOCTYPE html>
        <html lang=es>
        <head>
        <meta charset = "utf-8 ">
        <title>REPORTES</title>
        <style type = "text/css">
        body{
            margin: 0;
            font-family: Trebuchet MS, sans-serif;
            background-color: #fefbe9;
            background:linear-gradient(45deg,aqua,#02C7FF, #02A5FF , #0251FF , #022BFF, #6302FF,  #9402FF, #CA02FF ,#FF02F7);
        }
        .topnav {
            overflow: hidden;
            background-color: #DC143C;
            text-align: center;
        }
        table {
            border-collapse: collapse;
            width: 50%;
        }
        td, th {
            font-family: bahnschrift;
            border: 1px solid #000;
            text-align: center;
            padding: 8px;
        }
        h2{
            color: #000000;
        }</style>
        </head>
        <body>
        <div align="center" class="topnav"> 
            <h1 style = "color: black; ">REPORTE TOKENS</h1></div><br></br>
        <table align="center">
        <tr>
        <th colspan="5" style="background-color: black; color: white;">Tokens</th>
        </tr>
        <tr>
            <th colspan="1"style="background-color: black; color: white;">Lexema</th>
            <th colspan="1"style="background-color: black; color: white;">Linea</th>
            <th colspan="1"style="background-color: black; color: white;">Columna</th>
            <th colspan="1"style="background-color: black; color: white;">Tipo</th>
        </tr>
        </tr>"""
        for token in self.listaTokens:
            CuerpoHtml+= """<tr class = "table-primary">"""
            CuerpoHtml+= """<th>"""+str(token.lexema)+"""</th>"""
            CuerpoHtml+= """<th>"""+str(token.linea)+"""</th>"""
            CuerpoHtml+= """<th>"""+str(token.columna)+"""</th>"""
            CuerpoHtml+= """<th>"""+str(token.tipo)+"""</th>"""
            CuerpoHtml+= """</tr>"""
        CuerpoHtml+="""</table>
        </div>
        </body>
        </html>"""
        ruta = 'ReporteTokens.html'
        archivo = open(ruta,'w')
        archivo.write(CuerpoHtml)
        startfile('ReporteTokens.html')
        print("Se ha generado el html con los reportes.")
    
    def reporteErrores(self):
        CuerpoHtml= """<!DOCTYPE html>
        <html lang=es>
        <head>
        <meta charset = "utf-8 ">
        <title>REPORTES</title>
        <style type = "text/css">
        body{
            margin: 0;
            font-family: Trebuchet MS, sans-serif;
            background-color: #fefbe9;
            background:linear-gradient(45deg,aqua,#02C7FF, #02A5FF , #0251FF , #022BFF, #6302FF,  #9402FF, #CA02FF ,#FF02F7);
        }
        .topnav {
            overflow: hidden;
            background-color: #DC143C;
            text-align: center;
        }
        table {
            border-collapse: collapse;
            width: 50%;
        }
        td, th {
            font-family: bahnschrift;
            border: 1px solid #000;
            text-align: center;
            padding: 8px;
        }
        h2{
            color: #000000;
        }</style>
        </head>
        <body>
        <div align="center" class="topnav"> 
            <h1 style = "color: black; ">REPORTE ERRORES</h1></div><br></br>
        <table align="center">
        <tr>
        <th colspan="5" style="background-color: black; color: white;">Errores</th>
        </tr>
        <tr>
            <th colspan="1"style="background-color: black; color: white;">Descripcion</th>
            <th colspan="1"style="background-color: black; color: white;">Linea</th>
            <th colspan="1"style="background-color: black; color: white;">Columna</th>
        </tr>
        </tr>"""
        for error in self.listaErrores:
            CuerpoHtml+= """<tr class = "table-primary">"""
            CuerpoHtml+= """<th>"""+str(error.descripcion)+"""</th>"""
            CuerpoHtml+= """<th>"""+str(error.linea)+"""</th>"""
            CuerpoHtml+= """<th>"""+str(error.columna)+"""</th>"""
            CuerpoHtml+= """</tr>"""
        CuerpoHtml+="""</table>
        </div>
        </body>
        </html>"""
        ruta = 'ReporteErrores.html'
        archivo = open(ruta,'w')
        archivo.write(CuerpoHtml)
        startfile('ReporteErrores.html')
        print("Se ha generado el html con los reportes.")
    
    def generarHtml(self):
        global ListaAtributos
        global Entrada1
        ListaAtributos.pop(0)
        ListaAtributos.pop(0)
        ListaAtributos.pop()
        CuerpoHtml= """<!DOCTYPE html>
        <html lang=es>
        <head>
        <meta charset = "utf-8 ">
        <title>REPORTES</title>
        <style type = "text/css">
        body{
            margin: 0;
            font-family: Trebuchet MS, sans-serif;
            background-color: #fefbe9;
            background:linear-gradient(45deg,aqua,#02C7FF, #02A5FF , #0251FF , #022BFF, #6302FF,  #9402FF, #CA02FF ,#FF02F7);
        }
        .topnav {
            overflow: hidden;
            background-color: #DC143C;
            text-align: center;
        }
        table {
            border-collapse: collapse;
            width: 50%;
        }
        td, th {
            font-family: bahnschrift;
            border: 1px solid #000;
            text-align: center;
            padding: 8px;
        }
        h2{
            color: #000000;
        }</style>
        </head>
        <body>
        <div align="center" class="topnav"> 
            <h1 style = "color: black; ">Formulario</h1></div><br></br><form>"""
        
        for objeto in ListaAtributos:
            valor = ''
            fondo = ''
            nombre = ''
            try:
                for a in objeto.valor:
                    if a == '"':
                        pass
                    else:
                        valor +=a
            except:
                pass
            try:   
                for b in objeto.fondo:
                    if b == '"':
                        pass
                    else:
                        fondo += b
            except:
                pass
            try:
                for c in objeto.nombre:
                    if c == '"':
                        pass
                    else:
                        nombre += c
            except:
                pass
            if objeto.tipo == '"etiqueta"':
                CuerpoHtml+= """<div class="mb-3" align="center">
                                    <label for="""+str(valor)+""" class="form-label">"""+str(valor) 
                CuerpoHtml+="""</label></div>"""
            elif objeto.tipo == '"texto"':
                CuerpoHtml+= """<div class="mb-3" align="center">
                                    <input type="text" class="form-control" id="""+str(objeto.valor)+'placeholder='+str(objeto.fondo)+">" 
                CuerpoHtml+="""</div>"""
            elif objeto.tipo =='"grupo-radio"':
                CuerpoHtml+= """<div class="mb-3" align="center">
                                    <p>"""+str(nombre)+":</p>"
                CuerpoHtml+= "<p>"
                for valores in objeto.valores:
                    CuerpoHtml+=str(valores)+"""<input type="radio" name="""+str(objeto.nombre)+""" /><br />"""
                CuerpoHtml+="""</p></div>"""
            elif objeto.tipo =='"grupo-option"':
                CuerpoHtml+= """<div class="mb-3" align="center">
                                    <p>"""+str(nombre)+":</p>"
                CuerpoHtml+= "<p><select>"
                for valores in objeto.valores:
                    CuerpoHtml+="<option>"+str(valores)+"</option>"
                CuerpoHtml+="""</select></p></div>"""
            elif objeto.tipo == '"boton"':
                CuerpoHtml+="""<div class="mb-3" align="center">
                                <button onclick=" """+valor+ '()" id="'+valor+'"'+"""type="submit" class="btn btn-outline-dark">"""+valor+"</button></form></div>"
                CuerpoHtml+='<iframe id="iframe'+valor+'"> </iframe>'
                if objeto.evento == "info":
                    CuerpoHtml += """
                    <script>
                        var sendBtn = document.getElementById(" """+valor+'");'
                    CuerpoHtml+= """var frame = document.getElementById('iframe"""+valor+"')"
                    CuerpoHtml+= """
                        sendBtn.addEventListener('click', (event) => {
                            frame.innerHTML ="""+Entrada1+"})</script>"
                 
                
        CuerpoHtml+="""</form></div>
        </body>
        </html>"""
        ruta = 'Formulario.html'
        archivo = open(ruta,'w')
        archivo.write(CuerpoHtml)
        startfile('Formulario.html')
        print("Se ha generado el html con el formulario.")  
            
from curses.ascii import isdigit
from Token import Token
from Error import Error

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
        self.listaTokens = []
        self.listaErrores = []


        linea = 1
        columna = 1
        buffer = ''
        centinela = '¬'
        estado = 0
        Entrada += centinela

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
                    self.listaTokens.append(Token(buffer, 'cadena', linea, columna))
                    self.titulos.append(buffer)
                    buffer = ''
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
                    elif buffer == 'valor':
                        self.listaTokens.append(Token(buffer, 'valor', linea, columna))
                    elif buffer == 'fondo':
                        self.listaTokens.append(Token(buffer, 'fondo', linea, columna))
                    elif buffer == 'valores':
                        self.listaTokens.append(Token(buffer, 'valores', linea, columna))
                    elif buffer == 'nombre':
                        self.listaTokens.append(Token(buffer, 'nombre', linea, columna))
                    elif buffer == 'evento':
                        self.listaTokens.append(Token(buffer, 'evento', linea, columna))
                    elif buffer == 'FILTROS':
                        self.listaTokens.append(Token(buffer, 'FILTROS', linea, columna))
                    buffer = ''
                    i -= 1
                    estado = 0

            
            
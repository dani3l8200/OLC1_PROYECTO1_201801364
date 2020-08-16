from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from LexicoJS import * 

aver = ""
analizador = AnalizadorLexicoJS()
colores = AnalizadorLexicoJS()
class GUI:

    def __init__(self, window):
        self.ventana = window
        self.ventana.title("PROYECTO ! OLC")

        frame = LabelFrame(self.ventana, text = '')
        frame.grid(row=0,column=0,columnspan=20,pady=20)

        #############################################_MENU_#############################################
        self.cargar = Button(frame, text ="Cargar", command = self.fileMenu)
        self.cargar.grid(row=0,column=0)

        self.ejecutar = Button(frame, text ="Ejecutar", command = self.analizar)
        self.ejecutar.grid(row=0,column=1)

        self.salir = Button(frame, text ="Salir", command = self.terminar)
        self.salir.grid(row=0,column=2)

        ############################################_ENTRADA_############################################
        Label(frame,text='Archivo de Entrada:').grid(row=3,column=5)
        self.entrada = Text(frame, height=30, width=60)
        self.entrada.grid(row=4,column=5)

        Label(frame,text='   =>   ').grid(row=4,column=15)

        Label(frame,text='Resultado:').grid(row=3,column=16)
        self.salida = Text(frame, height=30, width=60)
        self.salida.grid(row=4,column=16)

        Label(frame,text='              ').grid(row=3,column=20)
    #END


    def fileMenu(self):
        filename = askopenfilename() 
        archivo = open(filename,"r")
        texto = archivo.read()
        archivo.close()
        self.pintarColores(texto)
        return
    #END

    def pintarColores(self,entrada):
        colores.analizadorColoresJS(entrada)
        printval  =  myListColores.headval
        while printval is not None:
            test = ""
            if printval.getToken().getTipo() == "RESERVADA":
                self.entrada.tag_config('reserved',foreground="red")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'reserved')
           
            elif printval.getToken().getTipo() == "NUMEROS" or printval.getToken().getTipo() == "BOOLEAN":

                self.entrada.tag_config('bool_int',foreground="blue")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'bool_int')

            elif printval.getToken().getTipo() == "ID":
    
                self.entrada.tag_config('variables',foreground="green")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'variables')


            elif printval.getToken().getTipo() == "COMENTARIOS":
        
                self.entrada.tag_config('comment',foreground="gray58")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'comment')

            elif printval.getToken().getTipo() == "CONT_FOR_CHAR" or printval.getToken().getTipo() == "CONT_FOR_STRING":
                self.entrada.tag_config('string_char',foreground="gold")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'string_char')

            elif printval.getToken().getTipo() == "ESPACIOS" or printval.getToken().getTipo() == "OTROS":

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test)
            
            elif printval.getToken().getTipo() == "OPERADORES":
            
                self.entrada.tag_config('operadores',foreground="dark orange")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'operadores')

            elif printval.getToken().getTipo() == "COMENTARIO_ESPECIAL":
                
                self.entrada.tag_config('especial',foreground="cyan2")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'especial')

            printval = printval.next
        return

    def analizar(self):
        texto = self.entrada.get("1.0",END)
        analizador.analizadorJS(texto)
        print(myListTokens[3].getToken().getLex())
        
        reportHTMLTokens()
        self.printSalida()
    #END


    def printSalida(self):
        texto = "Finalizo el analisis"
        self.salida.insert(INSERT,texto)

        messagebox.showerror("Error", "Texto a mostrar:\n")
    #END


    def terminar(self):
        self.ventana.destroy()
        return
    #END
#END

###################################################################################################
if __name__ == '__main__':
    root = Tk()
    app = GUI(root)
    root.mainloop()
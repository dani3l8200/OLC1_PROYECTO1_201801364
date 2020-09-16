from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.font import Font
from LexicoJS import * 
from LexicoHTML import * 

aver = ""
AnalizadorJS = AnalizadorLexicoJS()
coloresJS = AnalizadorLexicoJS()
AnalizadorHTML = AnalizadorLexicoHTML()
coloresHTML = AnalizadorLexicoHTML()
class GUI:
    archivo = ""
    def __init__(self, window):
        self.ventana = window
        self.ventana.title("PROYECTO ! OLC")
        self.ventana.configure(background='SpringGreen')

        frame = LabelFrame(self.ventana)
        frame.grid(row=0,column=0,columnspan=10,pady=10)
        frame.configure(background='SpringGreen')
        #############################################_MENU_#############################################
        barraMenu = Menu(self.ventana)
        self.ventana.config(menu = barraMenu, width = 1000, height = 600)
        archivoMenu = Menu(barraMenu, tearoff=0)
        #############################################SUB MENU EJECUTAR#############################################
        archivoEjecutar = Menu(archivoMenu, tearoff=0)
        archivoEjecutar.add_command(label = "JS", command = self.analizar)
        archivoEjecutar.add_command(label = "CSS", command = self.analizar)
        archivoEjecutar.add_command(label = "HTML", command = self.analizar)
        archivoEjecutar.add_command(label = "SINTACTICO", command = self.analizar)
        #############################################MENU Abrir#############################################
        archivoOpen = Menu(archivoMenu, tearoff =0)
        archivoOpen.add_command(label = "JS", command = self.fileMenuJS)
        archivoOpen.add_command(label = "CSS", command = self.fileMenuCSS)
        archivoOpen.add_command(label = "HTML", command = self.fileMenuHTML)
        archivoOpen.add_command(label = "SINTACTICO", command = self.fileMenuSintactico)
        #############################################MENU Archivo#############################################
        archivoMenu.add_command(label = "Nuevo", command = self.Nuevo)
        archivoMenu.add_command(label = "Guardar", command = self.Guardar)
        archivoMenu.add_command(label = "Guardar Como", command = self.GuardarComo)
        archivoMenu.add_cascade(label = "Abrir", menu = archivoOpen)
        archivoMenu.add_cascade(label = "Ejecutar", menu = archivoEjecutar)
        archivoMenu.add_separator()
        archivoMenu.add_command(label = "Salir", command = self.terminar)
        #############################################MENU REPORTES#############################################
        archivoReportes = Menu(barraMenu, tearoff=0)
        archivoReportes.add_command(label = "AUTOMATA JS", command = self.analizar)
        archivoReportes.add_command(label = "ERRORES JS", command = self.analizar)
        archivoReportes.add_command(label = "BITACORA CSS", command = self.analizar)
        archivoReportes.add_command(label = "ERRORES CSS", command = self.analizar)
        archivoReportes.add_command(label = "ERRORES HTML", command = self.analizar)
        archivoReportes.add_command(label = "ERRORES SINTACTICOS", command = self.analizar)
        #############################################MENU PRINCIPAL#############################################
        barraMenu.add_cascade(label = "Archivo", menu = archivoMenu)
        barraMenu.add_cascade(label = "Reportes", menu = archivoReportes)
        barraMenu.add_command(label = "Info", command = self.info)
        barraMenu.add_command(label = "Salir", command = self.terminar)
        barraMenu.configure(background='SpringGreen')
        ############################################_ENTRADA_############################################
        Label(frame,text='Archivo de Entrada:',background='salmon').grid(row=3,column=0)
        self.entrada = scrolledtext.ScrolledText(frame, height=30, width=80,bg='linen')
        self.entrada.grid(row=4,column=0,padx=30)

        

        Label(frame,text='   =>   ').grid(row=4,column=1)

        Label(frame,text='Resultado:',background='salmon').grid(row=3,column=2)
        self.salida = scrolledtext.ScrolledText(frame, height=30, width=80,bg='snow4')
        self.salida.grid(row=4,column=2,padx=30)

    #END


    def fileMenuJS(self):
        filename = askopenfilename() 
        archivo = open(filename,"r")
        texto = archivo.read()
        archivo.close()
        self.pintarColoresJS(texto)
        messagebox.showinfo("CARGA","SE CARGO CORRECTAMENTE EL ARCHIVO JS")
        return

    def fileMenuCSS(self):
        filename = askopenfilename() 
        archivo = open(filename,"r")
        texto = archivo.read()
        archivo.close()
        messagebox.showinfo("CARGA","SE CARGO CORRECTAMENTE EL ARCHIVO CSS")
        return
    
    def fileMenuHTML(self):
        filename = askopenfilename() 
        archivo = open(filename,"r")
        texto = archivo.read()
        archivo.close()
        self.pintarColoresHTML(texto)
        messagebox.showinfo("CARGA","SE CARGO CORRECTAMENTE EL ARCHIVO HTML")
        return

    def fileMenuSintactico(self):
        filename = askopenfilename() 
        archivo = open(filename,"r")
        texto = archivo.read()
        archivo.close()
        messagebox.showinfo("CARGA","SE CARGO CORRECTAMENTE EL ARCHIVO SINTACTICO")
        return
    #END

    def Nuevo(self):
        self.entrada.delete(1.0, END)
        self.salida.delete(1.0, END)
    def Guardar(self):
        if self.archivo == "":
            self.GuardarComo()
        else:
            guardarInfo = open(self.archivo,"w")
            guardarInfo.write(self.entrada.get("1.0",END))
            guardarInfo.close()
   
    def GuardarComo(self):
        guardarInfo = asksaveasfilename(title = "Guardar Archivo",initialdir = "/home/dani3l8200/Descargas")
        writeFile = open(guardarInfo, "w+")
        writeFile.write(self.entrada.get("1.0",END))
        writeFile.close()
        self.archivo = guardarInfo
        
    def pintarColoresJS(self,entrada):
        coloresJS.analizadorColoresJS(entrada)
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

    def pintarColoresHTML(self, entrada):
        coloresHTML.ColoresHTML(entrada)
        printval  =  listTokensCHTML.headval
        while printval is not None:
            test = ""
            if printval.getToken().getTipo() == "RESERVADA":
                self.entrada.tag_config('reserved',foreground="red")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'reserved')

            elif printval.getToken().getTipo() == "ID HTML":
    
                self.entrada.tag_config('variables',foreground="green")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'variables')

            elif printval.getToken().getTipo() == "ID":
        
                self.entrada.tag_config('string_special',foreground="white",background="black",)

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'string_special')


            elif printval.getToken().getTipo() == "COMENTARIO":
        
                self.entrada.tag_config('comment',foreground="gray58")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'comment')

            elif printval.getToken().getTipo() == "CONT_FOR_CHAR" or printval.getToken().getTipo() == "CONT_FOR_STRING":
                self.entrada.tag_config('string_char',foreground="gold")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'string_char')

            elif printval.getToken().getTipo() == "ESPACIOS":

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test)
            
            elif printval.getToken().getTipo() == "OPERADOR":
            
                self.entrada.tag_config('operadores',foreground="dark orange")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'operadores')

            elif printval.getToken().getTipo() == "ERRORES":
                
                self.entrada.tag_config('errores',foreground="white",background="red")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'errores')

            printval = printval.next
        return

    

    def analizar(self):
        texto = self.entrada.get("1.0",END)
        
        if self.var.get() == 1:
            AnalizadorJS.analizadorJS(texto) 
            reportHTMLTokens()
            reportHTMLTokensErrors()
            self.printSalida()
        else: 
            print('opcion no valida')
        
       
    #END


    def printSalida(self):
        texto = "Finalizo el analisis"
        self.salida.insert(INSERT,texto)

        messagebox.showerror("Error", "Texto a mostrar:\n")
    #END


    def terminar(self):
        salir = messagebox.askokcancel("Salir", "Está seguro que desea salir?")
        if salir:
            self.ventana.destroy()
        return
    
    def info(self):
        messagebox.showinfo("INFO","JUAN DANIEL ENRIQUE ROMAN BARRIENTOS - 201801364")
    #END
#END

###################################################################################################
if __name__ == '__main__':
    root = Tk()
    app = GUI(root)
    root.mainloop()
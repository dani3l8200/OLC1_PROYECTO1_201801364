#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.font import Font
from LexicoJS import * 
from LexicoHTML import * 
from LexicoSJS import * 
from LexicoCSS import *
import os.path
aver = ""
AnalizadorJS = AnalizadorLexicoJS()
coloresJS = AnalizadorLexicoJS()
AnalizadorHTML = AnalizadorLexicoHTML()
coloresHTML = AnalizadorLexicoHTML()
AnalizadorLJS = AnalizadorLexicoSJS()
coloresSJS = AnalizadorLexicoSJS()
CssLexico = AnalizadorLexicoCSS()
coloresCSS = AnalizadorLexicoCSS()

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
        archivoEjecutar.add_command(label = "JS", command = self.AnalizarJS)
        archivoEjecutar.add_command(label = "CSS", command = self.AnalizarCSS)
        archivoEjecutar.add_command(label = "HTML", command = self.AnalizarHTML)
        archivoEjecutar.add_command(label = "SINTACTICO", command = self.AnalizarSintactic)
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
        archivoReportes.add_command(label = "AUTOMATA JS", command = self.ReportAutomata)
        archivoReportes.add_command(label = "ERRORES JS", command = self.ReportErrorsJS)
        archivoReportes.add_command(label = "BITACORA CSS", command = self.ReportBitacora)
        archivoReportes.add_command(label = "ERRORES CSS", command = self.ReportErrorsCSS)
        archivoReportes.add_command(label = "ERRORES HTML", command = self.ReportErrorsHTML)
        archivoReportes.add_command(label = "ERRORES SINTACTICOS", command = self.ReportErrorsSintacticos)
        #############################################MENU PRINCIPAL#############################################
        barraMenu.add_cascade(label = "Archivo", menu = archivoMenu)
        barraMenu.add_cascade(label = "Reportes", menu = archivoReportes)
        barraMenu.add_command(label = "Info", command = self.info)
        barraMenu.add_command(label = "Limpiar Listas", command = self.eraseLista)
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
        filename = askopenfilename(title = "Abrir Archivo", initialdir = "/home/dani3l8200/Escritorio") 
        archivo = open(filename,"r")
        texto = archivo.read()
        self.pintarColoresJS(texto)
        archivo.close()
        messagebox.showinfo("CARGA","SE CARGO CORRECTAMENTE EL ARCHIVO JS")
        return

    def fileMenuCSS(self):
        filename = askopenfilename(title = "Abrir Archivo", initialdir = "/home/dani3l8200/Escritorio") 
        archivo = open(filename)
        texto = archivo.read()
        self.pintarColoresCSS(texto)
        archivo.close()
        texto = ""
        messagebox.showinfo("CARGA","SE CARGO CORRECTAMENTE EL ARCHIVO CSS")
        return
    
    def fileMenuHTML(self):
        filename = askopenfilename(title = "Abrir Archivo", initialdir = "/home/dani3l8200/Escritorio") 
        archivo = open(filename,"r")
        texto = archivo.read()
        self.pintarColoresHTML(texto)
        archivo.close()
        messagebox.showinfo("CARGA","SE CARGO CORRECTAMENTE EL ARCHIVO HTML")
        return

    def fileMenuSintactico(self):
        filename = askopenfilename(title = "Abrir Archivo", initialdir = "/home/dani3l8200/Escritorio") 
        archivo = open(filename,"r")
        texto = archivo.read()
        self.pintarColoresSJS(texto)
        archivo.close()
        messagebox.showinfo("CARGA","SE CARGO CORRECTAMENTE EL ARCHIVO SINTACTICO")
        return
    #END

    def eraseLista(self):
        listTokensLCSS.RemoveItem()
        listTokensECSS.RemoveItem()
        listReportBCSS.RemoveItem()
        listColoresCSS.RemoveItem()
        myListTokens.RemoveItem()
        myListErrors.RemoveItem()
        myListColores.RemoveItem()
        listTokensLHTML.RemoveItem()
        listTokensEHTML.RemoveItem()
        listTokensCHTML.RemoveItem()
        listTokensLSintactico.RemoveItem()
        listTokensESintactico.RemoveItem()
        listTokensCSintactico.RemoveItem()
        listErrorSintactico.RemoveItem()


    def AnalizarJS(self):
        texto = self.entrada.get("1.0",END)
        AnalizadorJS.analizadorJS(texto)
        directory = "/home/output/js/"
        fileName = "/home/output/js/salida.js"
        try:
            os.makedirs(directory,exist_ok=True)
        except OSError as error:
            messagebox.showinfo("advertencia","La carpeta ya fue creada")
        file = open(fileName, "w")
        printval  =  myListTokens.headval
        while printval is not None:
            file.write(printval.getToken().getLex())
            printval = printval.next
        file.close()
        myNulls = myListErrors.headval
        text3 = ":~$                                        ERRORES LEXICOS JS      \n"
        self.salida.insert(INSERT,text3)
        while myNulls is not None:
            text2 = f':~$ Token: {myNulls.getToken().getTipo()} Lexema: {myNulls.getToken().getLex()} Columna: {myNulls.getToken().getColumna()} Fila: {myNulls.getToken().getFila()}\n'
            self.salida.insert(INSERT,text2)
            myNulls = myNulls.next
        messagebox.showinfo("EXITO","SE FINALIZO EL ANALISIS LEXICO EN JS")
        

    
    def AnalizarCSS(self):
        texto = self.entrada.get("1.0", END)
        CssLexico.AnalizadorCSS(texto)
        directory = "/home/output/css/"
        fileName = "/home/output/css/salida.css"
        try:
            os.makedirs(directory,exist_ok=True)
        except OSError as error:
            messagebox.showinfo("advertencia","La carpeta ya fue creada")
        file = open(fileName, "w")
        printval  =  listTokensLCSS.headval
        while printval is not None:
            file.write(printval.getToken().getLex())
            printval = printval.next
        file.close()
        myNulls = listTokensECSS.headval
        text3 = ":~$                             ERRORES LEXICOS CSS      \n"
        self.salida.insert(INSERT,text3)
        while myNulls is not None:
            text2 = f':~$ Token: {myNulls.getToken().getTipo()} Lexema: {myNulls.getToken().getLex()} Columna: {myNulls.getToken().getColumna()} Fila: {myNulls.getToken().getFila()}\n'
            self.salida.insert(INSERT,text2)
            myNulls = myNulls.next
        messagebox.showinfo("EXITO","SE FINALIZO EL ANALISIS LEXICO EN CSS")
    
    def AnalizarHTML(self):
        texto = self.entrada.get("1.0",END)
        AnalizadorHTML.AnalizadorHTML(texto)
        directory = "/home/output/html/"
        fileName = "/home/output/html/salida.html"
        try:
            os.makedirs(directory,exist_ok=True)
        except OSError as error:
            messagebox.showinfo("advertencia","La carpeta ya fue creada")
        file = open(fileName, "w")
        printval  =  listTokensLHTML.headval
        while printval is not None:
            file.write(printval.getToken().getLex())
            printval = printval.next
        file.close()
        myNulls = listTokensEHTML.headval
        text3 = ":~$                             ERRORES LEXICOS HTML      \n"
        self.salida.insert(INSERT,text3)
        while myNulls is not None:
            text2 = f':~$ Token: {myNulls.getToken().getTipo()} Lexema: {myNulls.getToken().getLex()} Columna: {myNulls.getToken().getColumna()} Fila: {myNulls.getToken().getFila()}\n'
            self.salida.insert(INSERT,text2)
            myNulls = myNulls.next
        messagebox.showinfo("EXITO","SE FINALIZO EL ANALISIS LEXICO EN HTML")
        
        


    def AnalizarSintactic(self):
        texto = self.entrada.get("1.0",END)
        AnalizadorLJS.AnalizadorSJS(texto)
        SintacticoJS(listTokensLSintactico)
        

    
    def ReportTokensJS(self):
        reportHTMLTokens()
    def ReportErrorsJS(self):
        reportHTMLTokensErrors()
    def ReportAutomata(self):
        if myListErrors.headval == None: 
            AnalizadorJS.Graficar()
        else:
            messagebox.showerror("ERROR","HAY ERRORES LEXICOS")
    
    def ReportBitacora(self):
        CssLexico.ReportBitacoraCSS()
        myNulls = listReportBCSS.headval
        text3 = ":~$                             REPORTE BITACORA      \n"
        self.salida.insert(INSERT,text3)
        while myNulls is not None:
            text2 = f':~$ State: {str(myNulls.getToken().getState())} Token: {myNulls.getToken().getTok()} ITERACIONES: {str(myNulls.getToken().getIteracion())} Aceptacion: {str(myNulls.getToken().getAceptacion())}\n'
            self.salida.insert(INSERT,text2)
            myNulls = myNulls.next
        


    def ReportErrorsHTML(self):
        AnalizadorHTML.ReportLErrorsHTML()

    def ReportErrorsCSS(self):
        CssLexico.ReportTokensErrorCSS()

    def ReportErrorsSintacticos(self):
        ReportHTMLSintactico()

    def Nuevo(self):
        self.entrada.delete(1.0, END)
        self.salida.delete(1.0, END)
        self.archivo = ""
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

    def pintarColoresSJS(self, entrada):
        coloresSJS.AnalizadorSJSColores(entrada)
        printval  =  listTokensCSintactico.headval
        while printval is not None:
            test = ""
            if printval.getToken().getTipo() == "ID":
    
                self.entrada.tag_config('variables',foreground="green")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'variables')


            elif printval.getToken().getTipo() == "ESPACIOS":

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test)
            
            elif printval.getToken().getTipo() == "OPERADOR":
            
                self.entrada.tag_config('operadores',foreground="dark orange")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'operadores')

            elif printval.getToken().getTipo() == "ERRORES":
                
                self.entrada.tag_config('errores',foreground="black",background="sienna2")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'errores')
            
            elif printval.getToken().getTipo() == "NUMEROS" or printval.getToken().getTipo() == "DECIMAL":
    
                self.entrada.tag_config('bool_int',foreground="blue")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'bool_int')

            printval = printval.next
        return

    def pintarColoresCSS(self, entrada):
        coloresCSS.ColoresCSS(entrada)
        printval  =  listColoresCSS.headval
        while printval is not None:
            test = ""
            if printval.getToken().getTipo() == "RESERVADA":
                self.entrada.tag_config('reserved',foreground="red")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'reserved')

            elif printval.getToken().getTipo() == "ID":
    
                self.entrada.tag_config('variables',foreground="green")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'variables')

            elif printval.getToken().getTipo() == "ESPACIOS":

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test)
            
            elif printval.getToken().getTipo() == "OPERADOR":
            
                self.entrada.tag_config('operadores',foreground="dark orange")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'operadores')

            elif printval.getToken().getTipo() == "ERRORES":
                
                self.entrada.tag_config('errores',foreground="black",background="sienna2")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'errores')
            
            elif printval.getToken().getTipo() == "NUMEROS" or printval.getToken().getTipo() == "PORCENTAJE":
    
                self.entrada.tag_config('bool_int',foreground="blue")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'bool_int')

            elif printval.getToken().getTipo() == "CONT_FOR_STRING":

                self.entrada.tag_config('string_char',foreground="gold")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'string_char')
                
            elif printval.getToken().getTipo() == "OTROS":
    
                self.entrada.tag_config('otros',foreground="black")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'otros')
            
            elif printval.getToken().getTipo() == "COMENTARIOS":
            
                self.entrada.tag_config('comment',foreground="gray58")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'comment')

            elif printval.getToken().getTipo() == "COMENTARIO_ESPECIAL":
                
                self.entrada.tag_config('especial',foreground="cyan2")

                test += printval.getToken().getLex()

                self.entrada.insert(INSERT,test,'especial')

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
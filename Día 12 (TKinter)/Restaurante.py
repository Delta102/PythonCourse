from tkinter import *

def inicio():
    ## INICIALIZAR TKINTER
    aplicacion = Tk()

    ## TAMAÑO DE LA VENTANA
    aplicacion.geometry('1020x680') 

    ## EVITAR CAMBIO DE TAMAÑO EN LA VENTANA
    aplicacion.resizable(0, 0)

    ## TITULO DE APLICACION
    aplicacion.title('Mi Restaurante - Sistema de Facturación')

    ## COLOR DE FONDO DE LA VENTANA
    aplicacion.config(bg = 'burlywood')  ## También es válido el formato RGB

    ## PANELES
    methodPanels(aplicacion)



    ## EVITAR QUE LA PANTALLA SE CIERRE
    aplicacion.mainloop()   # Esto permite que la aplicación se cierre


def methodPanels(aplicacion):
    ## PANEL
    panelSuperior = Frame(aplicacion, bd = 1, relief=FLAT)
    panelSuperior.pack(side = TOP)  ## Esto me indica la posicion del panel

    ## ETIQUETA TITULO
    etiquetaTitulo = Label(panelSuperior, text='Sistema de Facturación', fg = 'azure4', 
                          font=('Dosis', 49), bg = 'burlywood', width= 27)
    etiquetaTitulo.grid(row = 0, column = 0)

    ## PANEL IZQUIERDO
    panelIzquierdo = Frame(aplicacion, bd = 1, relief=FLAT)
    panelIzquierdo.pack(side = LEFT)

    ## PANEL COSTOS
    panelCostos = Frame(aplicacion, bd = 1, relief=FLAT)
    panelCostos.pack(side = BOTTOM)

    ## PANEL COMIDAS
    panelComidas = LabelFrame(panelIzquierdo, text = 'Comida', font =('Dosis', 19, 'bold'), bd = 1, relief=FLAT, fg='azure4')
    panelComidas.pack(side = LEFT)

    ## PANEL BEBIDAS
    panelBebidas = LabelFrame(panelIzquierdo, text = 'Bebidas', font =('Dosis', 19, 'bold'), bd = 1, relief=FLAT, fg='azure4')
    panelBebidas.pack(side = LEFT)

    ## PANEL POSTRES
    panelPostres = LabelFrame(panelIzquierdo, text = 'Comida', font =('Dosis', 19, 'bold'), bd = 1, relief=FLAT, fg='azure4')
    panelPostres.pack(side = LEFT)
    ## ------------------------------------------------------------------------------------------------------------------------------- ##
    ## PANEL DERECHA
    panelDerecho = Frame(aplicacion, bd = 1, relief=FLAT)
    panelDerecho.pack(side = RIGHT)

    ## PANEL CALCULADORA
    panelCalculadora = Frame(panelDerecho, bd = 1, relief=FLAT, bg = 'burlywood')
    panelCalculadora.pack() # Por defecto va en la parte superior, TOP

    ## PANEL RECIBOS
    panelRecibo = Frame(panelDerecho, bd = 1, relief=FLAT, bg = 'burlywood')
    panelRecibo.pack()

    ## ------------------------------------------------------------------------------------------------------------------------------- ##
    ## PANEL BOTONES
    panelBotones = Frame(panelDerecho, bd=1, relief=FLAT, bg = 'burlywood')
    panelBotones.pack()


inicio()
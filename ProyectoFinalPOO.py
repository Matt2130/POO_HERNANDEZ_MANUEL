import tkinter as tk
#módulos restantes de tkinter
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

from ProyectoFinalPOOclientes import *
from ProyectoFinalPOOConexion import * #Enlace de la interfaz con la conexion y la bd

class tiendaBl: #creación de una clase para crear la interfaz
    global base
    base = None
    
    global textBoxn_clientes #asignación para almacenar datos en las variables
    textBoxn_clientes = None
    
    global textBoxnombres
    textBoxnombres = None
    
    global textBoxdireccion
    textBoxdireccion = None
    
    global textBoxtelefono
    textBoxtelefono = None
    
    global combo
    combo = None
    
    global groupBox
    groupBox = None
    
    global tree
    tree = None
    
def tienda(): #función que llamará a la interfaz
        global textBoxn_clientes
        global textBoxnombres
        global textBoxdireccion
        global textBoxtelefono
        global combo
        global base
        global tree #variables globales
        global groupBox
        
        try: #función try catch en python
            base = Tk() 
            base.geometry("1300x300") #tamaño de venta
            base.title("BD_clientes") #nombre de la ventana
            
            groupBox = LabelFrame(base, text="Datos del cliente", padx=5,pady=5) #espaciados) #control que almacenara controles mas pequeños con datos (contenedor de controles)
            groupBox.grid(row=0,column=0,padx=10,pady=10) #comienzan en 0 las celdas
            
            Labeln_clientes = Label(groupBox,text="n°_cliente:",width=13,font=("arial",12)).grid(row=0,column=0) 
            textBoxn_clientes = Entry(groupBox)
            textBoxn_clientes.grid(row=0,column=1) 
            
            Labelnombres = Label(groupBox,text="nombre:",width=13,font=("arial",12)).grid(row=1,column=0) 
            textBoxnombres = Entry(groupBox)
            textBoxnombres.grid(row=1,column=1) 
            
            Labeldireccion = Label(groupBox,text="dirección:",width=13,font=("arial",12)).grid(row=2,column=0) 
            textBoxdireccion = Entry(groupBox)
            textBoxdireccion.grid(row=2,column=1) 
            
            Labeltelefono = Label(groupBox,text="télefono:",width=13,font=("arial",12)).grid(row=3,column=0) 
            textBoxtelefono = Entry(groupBox)
            textBoxtelefono.grid(row=3,column=1) 
            
            LabelFecha = Label(groupBox,text="tipo de compra:",width=13,font=("arial",12)).grid(row=4,column=0)
            seleccionFecha = tk.StringVar()
            combo = ttk.Combobox(groupBox,values=["En línea","En físico"],textvariable=seleccionFecha)
            combo.grid(row=4,column=1)
            seleccionFecha.set("En línea") #poner por defecto una opción
            
            Button(groupBox,text="Agregar",width=10,command=guardarRegistros).grid(row=5,column=0) #Creación de los botones para el CRUD
            Button(groupBox,text="Actualizar",width=10,command=modificarRegistros).grid(row=5,column=1)
            Button(groupBox,text="Eliminar",width=10,command=eliminarRegistros).grid(row=5,column=2)
            
            groupBox = LabelFrame(base,text="Lista de los clientes",padx=5,pady=5,)
            groupBox.grid(row=0,column=1,padx=5,pady=5) #Creación del segundo control
            
            #Creación de un Treeview
            #Configuración de las columnas
            
            tree = ttk.Treeview(groupBox,columns=("n° cliente","nombre","dirección","télefono"),show='headings',height=5,)
            tree.column("# 1",anchor=CENTER)
            tree.heading("# 1",text="n° cliente")
            tree.column("# 2",anchor=CENTER)
            tree.heading("# 2",text="nombre")
            tree.column("# 3",anchor=CENTER)
            tree.heading("# 3",text="dirección")
            tree.column("# 4",anchor=CENTER)
            tree.heading("# 4",text="télefono")
            
            #agregar datos de la tabla
            #mostrar tabla
            for row in Clientes.mostrarClientes():
                tree.insert("","end",values=row)
                
            #ejecutar al hacer click y mostrar los resultdos en los Entry
            #cuando se le de click al treeview se ejecutara la función registo
            tree.bind("<<TreeviewSelect>>",seleccionarRegistro)
            
            tree.pack()
            
            base .mainloop()
        
        except ValueError as error:
            print("Error al mostrar la interfaz, error: {}".format(error))
    
def guardarRegistros():
        
        global textBoxnombres,textBoxdireccion,textBoxtelefono,combo,groupBox
        
        try:
        #verificar si los widgets estan inicializados
            if textBoxnombres is None or textBoxdireccion is None or textBoxtelefono is None or combo is None:
                print("Los widgets no están inicializados")
                return
        
            nombres = textBoxnombres.get()
            dirección = textBoxdireccion.get()
            télefono = textBoxtelefono.get()
            tipoDeCompra = combo.get()
            
            Clientes.ingresoDeClientes(nombres,dirección,télefono,tipoDeCompra)
            messagebox.showinfo("Información","Los datos fueron guardados") 
            
            actualizarTreeView()
            
            #limpiar los campos
        
            textBoxnombres.delete(0,END)
            textBoxdireccion.delete(0,END)
            textBoxtelefono.delete(0,END)    
        
        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))

def actualizarTreeView():
    global tree
    
    try:
        #Borrar todos los elementos actuales del TreeView
        tree.delete(*tree.get_children())
        
        #obtener los nuevos datos que deseamos mostrar
        datos = Clientes.mostrarClientes()
        
        #Insertar los nuevos datos en el treeView
        for row in Clientes.mostrarClientes():
            tree.insert("","end",values=row)
            
    except ValueError as error:
        print("Error al actualizar tabla {}".format(error))
   
def seleccionarRegistro(event):
    try:
        itemSeleccionado = tree.focus()
        
        if itemSeleccionado:
            #obtener el ID del elemento seleccionado
            values = tree.item(itemSeleccionado)['values']
            
            #establecer los valores en los widgets (los controles de la interfaz) Entry
        
            textBoxn_clientes.delete(0,END)
            textBoxn_clientes.insert(0,values[0])
            textBoxnombres.delete(0,END)
            textBoxnombres.insert(0,values[1])
            textBoxdireccion.delete(0,END)
            textBoxdireccion.insert(0,values[2])
            textBoxtelefono.delete(0,END)
            textBoxtelefono.insert(0,values[3])
            combo.set(values[4])
            
    except ValueError as error:
        print("Error al seleccionar registro {}".format(error))

def modificarRegistros():
        
        global textBoxn_clientes,textBoxnombres,textBoxdireccion,textBoxtelefono,combo,groupBox
        
        try:
        #verificar si los widgets estan inicializados
            if textBoxn_clientes is None or textBoxnombres is None or textBoxdireccion is None or textBoxtelefono is None or combo is None:
                print("Los widgets no están inicializados")
                return

            n_clientes = textBoxn_clientes.get()
            nombres = textBoxnombres.get()
            dirección = textBoxdireccion.get()
            telefono = textBoxtelefono.get()
            tipoDeCompra = combo.get()
            
            Clientes.modificarClientes( n_clientes,nombres,dirección,telefono,tipoDeCompra)
            messagebox.showinfo("Información","Los datos fueron actualizados") 
            
            actualizarTreeView()
            
            #limpiar los campos
            textBoxn_clientes.delete(0,END)            
            textBoxnombres.delete(0,END)
            textBoxdireccion.delete(0,END)
            textBoxtelefono.delete(0,END)    
        
        except ValueError as error:
            print("Error al modificar los datos {}".format(error))
            
def eliminarRegistros():
        
        global textBoxn_clientes,textBoxnombres,textBoxdireccion,textBoxtelefono
        
        try:
        #verificar si los widgets estan inicializados
            if textBoxn_clientes is None:
                print("Los widgets no están inicializados")
                return

            n_clientes = textBoxn_clientes.get()
            
            Clientes.eliminarClientes(n_clientes)
            messagebox.showinfo("Información","Los datos fueron eliminados") 
            
            actualizarTreeView()
            
            #limpiar los campos
            textBoxn_clientes.delete(0,END)            
            textBoxnombres.delete(0,END)
            textBoxdireccion.delete(0,END)
            textBoxtelefono.delete(0,END)    
        
        except ValueError as error:
            print("Error al modificar los datos {}".format(error))
            
tienda() #llamar a la función para mostrar la interfaz
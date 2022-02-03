from tkinter import *
from tkinter import messagebox
import struct, os
class app(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Hashing")
        self.geometry("480x380")
        self.configure(bg="lightblue")
        self.titulo = Label(self,text="Hashing", font="Times 16 underline", bg="lightblue" )
        self.titulo.place(x=200, y = 15)
        self.e1 = Entry(self)
        self.e1.place(x= 200, y =90 )
        self.l1 = Label(self,text="Código:", font="Times 10", bg="lightblue"  )
        self.l1.place(x=100, y = 90)
        self.e2 = Entry(self)
        self.e2.place(x= 200, y =120 )
        self.l2 = Label(self,text="Nombre:" , font="Times 10 ", bg="lightblue" )
        self.l2.place(x=100, y = 120)
        self.e3 = Entry(self)
        self.e3.place(x= 200, y =150 )
        self.l3 = Label(self,text="Dirección:", font="Times 10 ", bg="lightblue"  )
        self.l3.place(x=100, y = 150)
        self.e4 = Entry(self)
        self.e4.place(x= 200, y =180 )
        self.l4 = Label(self,text="Edad:", font="Times 10 ", bg="lightblue"  )
        self.l4.place(x=100, y = 180)
        self.e5 = Entry(self)
        self.e5.place(x= 200, y =210 )
        self.l5 = Label(self,text="Correo:", font="Times 10", bg="lightblue" )
        self.l5.place(x=100, y = 210)
        self.e6 = Entry(self)
        self.e6.place(x= 200, y =240)
        self.l6 = Label(self,text="Teléfono:", font="Times 10 ", bg="lightblue"  )
        self.l6.place(x=100, y = 240)
        self.l7 = Label(self,text="Buscar/modificar:", font="Times 10 ", bg= "lightblue" )
        self.l7.place(x=70, y = 280)
        self.e7 = Entry(self)
        self.e7.place(x= 200, y =280 )
        self.b1 = Button(self,text="Buscar", command = self.buscar )
        self.b1.place(x=350, y = 320)
        self.b2 = Button(self,text="Preparar", command = self.preparar)
        self.b2.place(x=360, y = 90)
        self.b3 = Button(self,text="Ingresar", command= self.ingresar )
        self.b3.place(x=360, y = 130)
        self.b4 = Button(self,text="Modificar" , command = self.modificar)
        self.b4.place(x=250, y = 320)
        self.b5 = Button(self,text="Borrar" , command = self.borrar)
        self.b5.place(x=130, y = 320)
        self.datos = (self.e1, self.e2, self.e3, self.e4, self.e5, self.e6)
        
    def buscar(self):
        self.limpiar()
        buscado = self.e7.get()
        if (buscado == ""):
            messagebox.showerror("Error", "Ingrese un código")
        else:
            pos = self.hashing(buscado)
            self.regl = self.leer(pos)
            if(self.regl[6]!=-1):  
                    if (self.regl[0] == buscado):
                        self.mostrar(pos)
                    else:
                        pos2=self.regl[6]
                        self.mostrar(pos2)
            else:
                if (self.regl[0] == buscado):
                        self.mostrar(pos)
                else:
                    messagebox.showerror("Error", "código no existente")
            self.e7.delete(0, END)
    def preparar(self):
        reg=("@","","",0,"","",-1)
        for i in range(100):
            self.escribir(i,reg)
        self.limpiar()
    def ingresar(self):
            codigo = self.e1.get()
            nombre = self.e2.get()
            direccion = self.e3.get()
            edad = int(self.e4.get())
            correo = self.e5.get()
            telefono = self.e6.get()
            if (codigo == "" or nombre== "" or direccion == "" or correo == "" or telefono == ""):
                messagebox.showerror("Error", "Error de vacios")
            else:
                reg = (codigo, nombre, direccion, edad, correo, telefono, -1)
                pos = self.hashing(codigo)
                codig = self.leer(pos)[0]
                caden = self.leer(pos)[6]
                regl = self.leer(pos)
                if (codig != "@"):
                    if (codig == codigo):
                        messagebox.showerror("Error", "El código ya existe")
                    if (caden == -1):
                        pos2=pos
                        pos = self.tamaño()
                        regl = (regl[0], regl[1], regl[2], regl[3], regl[4], regl[5], pos)
                        self.escribir(pos2, regl)
                    else:
                        pos = caden  
                self.escribir(pos, reg)
            self.limpiar()
    def modificar(self):
        buscado= self.e7.get()
        if buscado == "" :
            messagebox.showerror("Error"," Debe ingresar el código del archivo" )
        else:
            pos = self.hashing(buscado)
            self.regl = self.leer(pos)
            if(self.regl[0]==buscado):
                print("es igual")
            else:
                pos=self.regl[6]
                self.regl = self.leer(pos)
            if (self.e2.get()==""):
                nombre = self.regl[1]
            else:
                nombre = self.e2.get()
            if (self.e3.get()==""):
                direccion = self.regl[2]
            else:
                direccion = self.e3.get()
            if (self.e4.get()==""):
                edad = self.regl[3]
            else:
                edad = int(self.e4.get())
            if (self.e5.get()==""):
                correo = self.regl[4]
            else:
                correo = self.e5.get()
            if (self.e6.get()==""):
                telefono = self.regl[1]
            else:
                telefono = self.e6.get()
            reg = (self.regl[0], nombre, direccion, edad, correo, telefono, self.regl[6])
            self.escribir(pos,reg)
            self.limpiar()

    def limpiar(self):
        for i in  (self.datos):
            i.delete(0 , "end")

    def mostrar(self,p):
        self.limpiar()
        leer = self.leer(p)
        for i in range(6):
            self.datos[i].insert(0, str(leer[i]))
    
    def abrir(self):
        nombre="ar5.txt"
        modo="r+b" if os.path.isfile(nombre) else "w+b"
        self.archivo=open(nombre,modo)
        self.formato = "6s 30s 60s i 60s 15s i"
        self.registroreg = struct.calcsize(self.formato)

    def cerrar(self):
        self.archivo.close()

    def escribir(self,pos,reg):
        p = pos* self.registroreg
        r = (reg[0].ljust(6).encode("utf-8"),reg[1].ljust(30).encode("utf-8"),reg[2].ljust(60).encode("utf-8"), reg[3], reg[4].ljust(60).encode("utf-8"), reg[5].ljust(15).encode("utf-8"), reg[6])
        buffer = struct.pack(self.formato, *r)
        self.archivo.seek(p)
        self.archivo.write(buffer)

    def leer(self, pos):
        p = pos * self.registroreg
        self.archivo.seek(p)
        buffer = self.archivo.read(self.registroreg)
        r = struct.unpack(self.formato, buffer)
        reg = ( r[0].decode("utf-8").strip(),r[1].decode("utf-8").strip(),r[2].decode("utf-8").strip(), r[3], r[4].decode("utf-8").strip(), r[5].decode("utf-8").strip(), r[6])
        return reg
        
    def hashing (self,codigo):
        pos = 0
        for i in (codigo):
            pos += ord(i)
        pos = pos%100
        return (pos)

    def tamaño(self):
        self.archivo.seek(0,2)
        return self.archivo.tell()//self.registroreg
    def borrar(self):
        buscado= self.e7.get()
        if buscado == "" :
            messagebox.showerror("Error"," Debe ingresar el código del archivo" )
        else:
            pos = self.hashing(buscado)
            self.regl = self.leer(pos)
            if(self.regl[0]==buscado):
                print("es igual")
            else:
                pos=self.regl[6]
                self.regl = self.leer(pos)
            cadena=self.regl[6]
            self.escribir(pos,["-","","",0,"","",cadena])
            self.limpiar()
forma = app()
forma.abrir()
forma.mainloop()
forma.cerrar()

#DOCUMENTACIÓN INTERNA
#Programador:Sofia  Velásquez
#Datos del programador: Sofiamishel2003@gmail.com
#Fin: Aprender el uso de hashing abierto
#Lenguaje: python 3.7
#Net Framewor: 4.5
#Recursos: Python, visual studio
#Descripción: Desarrollar un programa que prepare un archivo y se le puede ingresar, con hashing abierto y modificar  y buscar
#Ultima modificación 18/07/2021




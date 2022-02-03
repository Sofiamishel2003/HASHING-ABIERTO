from tkinter import*
from tkinter import Tk, Entry, Label, Button, messagebox
import struct, os
from tkinter import font
import sys
from tkinter.font import families
class forma(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("430x310")
        self.config(bg="lightblue")
        self.lb=Label(self,text="Ordenamiento Hashi Abierto", font="Arial 15 underline", bg="lightblue")
        self.lb.place(x=110,y=10)
        self.b1=Button(self,text="BUSCAR",  command=lambda:self.ir(0))
        self.b1.place(x=290,y=260)
        self.b2=Button(self,text="PREPARAR ARCHIVO", command=self.preparar)
        self.b2.place(x=290,y=130)
        self.b3=Button(self,text="AGREGAR", command=lambda:self.ingresar(0))
        self.b3.place(x=290,y=170)
        self.e1=Label(self,text="Código:", bg="lightblue", font="Times 11")
        self.e1.place(x=70,y=70)
        self.c1=Entry(self)
        self.c1.place(x=150,y=70)
        self.e3=Label(self,text="Nombre:", bg="lightblue", font="Times 11")
        self.e3.place(x=70,y=100)
        self.c3=Entry(self)
        self.c3.place(x=150,y=100)
        self.e4=Label(self,text="Dirección:", bg="lightblue", font="Times 11")
        self.e4.place(x=70,y=130)
        self.c4=Entry(self)
        self.c4.place(x=150,y=130)
        self.e5=Label(self,text="Edad:", bg="lightblue", font="Times 11")
        self.e5.place(x=70,y=160)
        self.c5=Entry(self)
        self.c5.place(x=150,y=160)
        self.e6=Label(self,text="Correo:", bg="lightblue", font="Times 11")
        self.e6.place(x=70,y=190)
        self.c6=Entry(self)
        self.c6.place(x=150,y=190)
        self.e7=Label(self,text="Teléfono:", bg="lightblue", font="Times 11")
        self.e7.place(x=70,y=220)
        self.c7=Entry(self)
        self.c7.place(x=150,y=220)
        self.datos = (self.c1, self.c3,self.c4, self.c5, self.c6, self.c7)
        self.LL=Label(self, bg="lightblue", font="Times 15")
        self.LL.place(x=30,y=270)
        self.bt4=Button(self,text="BORRAR",command=lambda:self.ir(1))
        self.bt4.place(x=290,y=200)
    
    def abrir(self):
        nombre = os.path.join(sys.path[0],"datos.txt")
        modo = "r+b" if os.path.isfile(nombre) else "w+b"   
        self.archivo = open(nombre, modo)
        self.formato = "6s 30s 30s i 30s 8s"
        self.tamr = struct.calcsize(self.formato)

    def leer(self,pos):
        p = pos * self.tamr
        self.archivo.seek(p)
        buffer = self.archivo.read(self.tamr)
        bd = struct.unpack(self.formato, buffer)
        reg = (bd[0].decode("utf-8").strip(),bd[1].decode("utf-8").strip(), bd[2].decode("utf-8").strip(), bd[3], bd[4].decode("utf-8").strip(),bd[5].decode("utf-8").strip())
        return reg  

    def hashing(self, cod):
        pos = 0
        for i in cod:
            pos += ord(i)
        return pos%100

    def buscar(self, n):
        if n>=0:
            pos = self.hashing(str(n))
            while True:
                reg = self.leer(pos)
                if reg[0] == str(n):
                    return reg, pos
                elif reg[0]=="@" or pos>=120:
                    return reg, -1
                else:
                    pos += 1

    def limpiar(self):
        for e in self.datos:
            e.delete(0,'end')

    def mostrar(self,r, pos):
        self.limpiar()
        for i in range(6):
            self.datos[i].insert(0,str(r[i]))

    def ir(self, modo):
        try:
            n = int(self.c1.get())
        except:
            messagebox.showerror("Error","Codigo invalido")
            n = -1
        reg, pos = self.buscar(n)
        if pos==-1:
            messagebox.showerror("Error","No se encotro el registro")
        else:
            if modo==0:
                self.mostrar(reg, pos)
            elif modo==1:
                if messagebox.askyesno('Borrar','Desar Borrar el registro'):
                    self.escribir(pos, ["-","","",0,"",""])
        
            

    def ingresar(self, modo):
            cod = self.c1.get()
            nom = self.c3.get()
            dir = self.c4.get()
            edad = int(self.c5.get())
            correo = self.c6.get()
            tel = self.c7.get()
            if cod=="" or nom=="" or dir=="" or correo=="" or tel=="":
                messagebox.showerror("Campos vacios", "Debe ingresar todos los datos")
            else:
                reg = (cod, nom, dir, edad, correo, tel)
                if modo == 0 :
                    pos = self.hashing(cod)
                    pos = self.directo(pos,cod)
                elif modo==1:
                    r, pos = self.buscar(int(cod))
                if pos == -1:
                    messagebox.showerror("ERROR","Solo puede ingresar posiciones menores a 120")
                elif pos == -2:
                    messagebox.showerror("Error","El codigo ya existe")
                else:                        
                    self.escribir(pos, reg)       
            self.limpiar()     
    def directo(self, pos, cod2):
        if pos<=120:
            cod = self.leer(pos)[0]
            if cod=="@" or cod=="-":
                return pos
            elif cod == cod2:
                return -2
            else:
                return self.directo(pos+1, cod2)
        else:
            return -1

    def preparar(self):
        self.archivo.seek(0,0)
        for i in range(100):
            self.escribir(i,["@","","",0,"",""])

    def cerrar(self):
        self.archivo.close()

    def escribir(self,pos,reg):
        bd = (reg[0].ljust(6).encode("utf-8"), 
              reg[1].ljust(30).encode("utf-8"), 
              reg[2].ljust(30).encode("utf-8"), 
              reg[3], 
              reg[4].ljust(30).encode("utf-8"),
              reg[5].ljust(8).encode("utf-8"))
        buffer = struct.pack(self.formato, *bd)
        self.archivo.seek(pos*self.tamr)
        self.archivo.write(buffer)


prg = forma()
prg.abrir()
prg.mainloop()
prg.cerrar()
#DOCUMENTACIÓN INTERNA
#Programador:Sofia  Velásquez
#Datos del programador: Sofiamishel2003@gmail.com
#Fin: Experimentar más con el hashi
#Lenguaje: python
#Net Framewor: 4.5
#Recursos: visual studio
#Descripción: Desarrollar un programa que puedaabrir un archivo, buscar dentro de los registros con metodo hashing y borrar registros
#Ultima modificación 26/01/2021
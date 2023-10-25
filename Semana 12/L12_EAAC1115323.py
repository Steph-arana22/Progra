class persona:
   def __init__(self):
       self.Nombres=""
       self.Apellidos=""
       self.Apellido_Casada=""
       self.Fecha_nacimiento=""

   def mostrar_nombres(self):
       return self.Nombres

   def mostrar_apellidos(self):
       return self.Apellidos

   def mostrar_apellido_casada(self):
       return self.Apellido_Casada

   def mostrar_fecha_nacimiento(self):
       return self.Fecha_nacimiento

   def ingresar_nombres(self,Nombres):
       self.Nombres=Nombres

   def ingresar_apellidos(self,Apellidos):
       self.Apellidos=Apellidos

   def ingresar_apellido_casada(self,Apellido_Casada):
       self.Apellido_Casada=Apellido_Casada

   def ingresar_fecha_nacimiento(self,Fecha_nacimiento):
       self.Fecha_nacimiento=Fecha_nacimiento

persona1=persona()
persona1.ingresar_nombres(input("Ingrese sus nombres: "))
persona1.ingresar_apellidos(input("Ingrese sus apellidos: "))
persona1.ingresar_apellido_casada(input("Ingrese su apellido de casada (si no tiene, deje en blanco el espacio): "))
persona1.ingresar_fecha_nacimiento(input("Ingrese su fecha de nacimiento: "))

print(persona1.mostrar_nombres() + " " + persona1.mostrar_apellidos())
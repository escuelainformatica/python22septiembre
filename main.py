class Producto():
    nombre: str = ""
    precio: int = 0

    def __init__(self, **kwargs):
        # operacion ternaria  <valor si es verdadero> if <condicion> else <valor si falso>
        self.nombre = kwargs['nombre'] if ('nombre' in kwargs) else 'sin nombre'
        self.precio = kwargs['precio'] if ('precio' in kwargs.keys()) else 0

    def __add__(self, other) -> int:
        if (isinstance(other, Producto)):
            return self.precio + other.precio
        if (isinstance(other, int)):
            return self.precio + other

    def __str__(self) -> str:
        # "%s %s".format()
        return f"{self.nombre},{self.precio}"


class Persona():
    nombre: str = ""
    apellido: str = ""

    def mostrarme(self):
        print(self.nombre + " " + self.apellido)


class Cliente(Persona):
    rut: str = ""

    def __init__(self, **kwargs) -> None:
        self.rut = kwargs['rut']
        self.nombre = kwargs['nombre']
        self.apellido = kwargs['apellido']

    def mostrarme(self):
        super().mostrarme()  # mostrarme de persona
        print("rut:" + self.rut)


susan = Persona()
susan.nombre = "Susan"
susan.apellido = "R."
susan.mostrarme()

numero: int = 20  # numero=Int(20)

# peter=Cliente(nombre="Peter")
john = Cliente(rut="1-9", nombre="john", apellido="doe")  # john es una instancia del tipo Cliente

john.mostrarme()

# anna=Cliente   # anna es la clase cliente
# peter=anna()

print(john)

print('-------------------')

producto1 = Producto(nombre='cocacola', precio=500)
producto2 = Producto(nombre='fanta', precio=2000)
producto3 = Producto(nombre='sprite')
print(producto1 + producto2)  # producto1.__add__(producto2)
print(producto1 + 200)

print(producto3)  # str(producto3) producto3.__str__()

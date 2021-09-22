class Cliente():
    rut:str=""
    nobmre:str=""

class DetalleFactura():
    producto:str=""
    precio_unitario:int=0
    cantidad:int=0

    def __init__(self,producto,precio,cantidad):
        self.producto=producto
        self.precio_unitario=precio
        self.cantidad=cantidad

class Facturas():
    cliente:Cliente=None
    detalle:list=list()

cliente=Cliente()
cliente.rut="1-2"
cliente.nobmre="john"

det1=DetalleFactura("honorarios",1,222)
det2=DetalleFactura("manos de obra",1,222)
det3=DetalleFactura("descuento",1,222)

factura=Facturas()
factura.campo="hola mundo"
factura.cliente=cliente
factura.detalle.append(det1)
factura.detalle.append(det2)
factura.detalle.append(det3)
factura.detalle.append('hola')
factura.detalle.append(30)


print(factura)
from carrito import carrito
from pagos import validar_metodo_pago

def generar_factura(carrito, total, metodo_pago):
    factura = {
    "Productos" : [],
    "total" : total,
    "Método de pago" : metodo_pago
    }

    for item in carrito:
        nuevos_productos = { "producto" : item["producto"],
                            "cantidad" : item["cantidad"]}     
              
        factura["Productos"].append(nuevos_productos)
    return factura
generar_lafactura = generar_factura(carrito, 111111, validar_metodo_pago("Visa"))
print(generar_lafactura)


    
        

        
    
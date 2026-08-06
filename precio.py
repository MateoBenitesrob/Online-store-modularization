# Crear 2 funciones: una definidad "subtotal" y otra "total", en "sutotal" vamos a necesitar el carrito,
# y en el otro necesitaremos el carrito y subtotal.
from carrito import carrito
def subtotal(carrito):
    subtotal = 0
    for item in carrito:
        subtotal += item["precio"] * item["cantidad"]
    return subtotal



def total(carrito, subtotal):

    if len(carrito) == 0:
        return 0
    
    IGV = subtotal * 18 / 100
    total = IGV + subtotal
    return total
elsubtotal = subtotal(carrito)
eltotal = total(carrito, elsubtotal)

print(f"Subtotal: S/. {elsubtotal:.2f}")
print(f"Total a pagar (con IGV): S/. {eltotal:.2f}")
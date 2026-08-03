from inventario import verificar_stock
from inventario import inventario

carrito = []

def agregar_producto(carritos, inventario, producto, cantidad):

    
    if verificar_stock(inventario, producto, cantidad):
        nuevo_item = {
                "producto" : producto,
                "cantidad" : cantidad
            }
        carritos.append(nuevo_item)
        return True
    return False
agregar_elproducto = agregar_producto(carrito, inventario, "Computadora", 1)



#   
def eliminar_producto(carrito, producto):
    for i in range(len(carrito)):
        # Compara el valor de la clave 'producto' en el diccionario actual
        if carrito[i]["producto"] == producto:
            carrito.pop(i)
            return True     
    return False

print("Cantidad de elementos en el carrito:", len(carrito))
eliminar_unproducto = eliminar_producto(carrito, "Computadora")



def mostrar_carrito(carrito):
    if len(carrito) == 0:
        print("carrito vacio")
    else:
        for i in range(len(carrito)):
            print(carrito[i]["producto"], carrito[i]["cantidad"])
            
mostrar_carritoo = mostrar_carrito(carrito)

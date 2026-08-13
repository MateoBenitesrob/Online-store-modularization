# Interfaz
from carrito import carrito
from compra import realizar_compra
from inventario import inventario
from carrito import agregar_producto # carritos, inventario, producto, cantidad, precio
import time


print("=" * 30)
entrada1 = input("Bienvenido. Escriba SI, si quiere continuar o NO si desea salir: ").lower()
print("=" * 30)
if entrada1 == "si":
    
    print(inventario)
    producto = input("Escriba el nombre exacto del producto que desea comprar: ")
    time.sleep(1)
    print("=" * 30)
    if producto in inventario:
        try:
            cantidad = input("Escriba el número de productos que desea comprar en digitos: ")
            time.sleep(1)
            print("=" * 30)

            cantidad_productos = int(cantidad)
            #cambiar una linea el if
            agregar_unproducto = agregar_producto(carrito, inventario, producto, cantidad_productos, inventario[producto]["precio"])
            if agregar_unproducto:
            
                try:
                    metodo_pago = input("Escriba el método de pago con el que desee pagar la compra: ").lower()
                    realizar_compra(carrito, metodo_pago)
                except ValueError:
                    print("Escriba nuevamente su  método de pago correcto.")

            else: 
                print("La cantidad de productos que usted desea agregar superá al stock actual. Inténte que su cantidad sea igual o menor a la cantidad del stock.")
        except ValueError:
            print("Escribe la cantidad de productos que deseas agregar en cifras.")
    else:
        print("Producto no encontrado, inténtelo de nuevo.")
elif entrada1 == "no":
    print("Cerrando programa")
    exit()
else:
    print("Escriba una de las siguientes opciones nuevamente.")
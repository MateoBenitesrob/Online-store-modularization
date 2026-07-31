inventario = {
    "RTX 5090" : {
    "precio" : 7000,
    "stock" : 7,
    "proveedor" : "nvidia"
    },
    "Computadora" :{
        "precio" : 1000,
        "stock" : 4,
        "proveedor" : "corpac"
    },
    "Monitor" : {
        "precio" : 500,
        "stock" : 9,
        "proveedor" : "samsung"
    }}

reservas = []

# VERIFICAR STOCK
def verificar_stock(inventario, producto, cantidad):
    stock_actual = inventario[producto]["stock"]

    return stock_actual >= cantidad

hay_stock = verificar_stock(inventario, "Computadora", 10)

# ACTUALIZAR  EL STOCK
def actualizar_stock(inventario, producto, cantidad):
    stock_actual = inventario[producto]["stock"]

    if stock_actual >= cantidad:
        inventario[producto]["stock"] -= cantidad
        return True
    else:
        return False

actualice_stock = actualizar_stock(inventario, "Computadora", 3)

    
# RESERVAR PRODUCTO
def reservar_producto(reservas, inventario, producto, cantidad):
    reserva = {
        "producto" : producto,
        "cantidad" : cantidad
    }
    

    if verificar_stock(inventario, producto, cantidad) == True:
        actualizar_stock(inventario, producto, cantidad)
        reservas.append(reserva)
        return reserva
    else:
        return False
reservar_unproducto = reservar_producto(reservas, inventario, "Computadora", 1)
print(reservar_unproducto)
print(reservas)
print(inventario["Computadora"])
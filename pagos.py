#⏳ Validar método de pago
#⏳ Procesar pago
#⏳ Confirmar pago
import time


# Se evalúa el método de pago
def validar_metodo_pago(metodo_pago):
    metodos_validos = ["tarjeta",
                        "yape",
                          "plin",
                            "payPal",
                              "visa",
                                "mastercard"
                                    ]
    if metodo_pago in metodos_validos:
        return True
    return False



# Se procesa el pago
def procesar_pago(metodo_pago, monto):

    if validar_metodo_pago(metodo_pago):
      print(f"Procesando pago de S/{monto} con {metodo_pago}...")
      time.sleep(1)
      return True
    else:
      print("el sistema no pudo aceptar su método de pago.")
      return False



# Finalmente el pago se confirma
def confirmar_pago(pago_exitoso):
   if pago_exitoso:
      print("Se a realizado exitosamente el pago.")
      return True
   else:
      print("Ha ocurrido un error al confirmar el pago, inténtelo de nuevo.")

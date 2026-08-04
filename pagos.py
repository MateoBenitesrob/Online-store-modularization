#⏳ Validar método de pago
#⏳ Procesar pago
#⏳ Confirmar pago


# Se evalúa el método de pago
def validar_metodo_pago(metodo_pago):
    metodos_validos = ["Tarjeta",
                        "Yape",
                          "Plin",
                            "PayPal",
                              "Visa",
                                "Mastercard"
                                    ]
    if metodo_pago in metodos_validos:
        return True
    return False
validar_metodo_depago = validar_metodo_pago("Visa")
print(validar_metodo_depago)


# Se procesa el pago
def procesar_pago(metodo_pago, monto):

    if validar_metodo_pago(metodo_pago):
      print(f"Procesando pago de S/{monto} con {metodo_pago}...")
      return True
    else:
      print("el sistema no pudo aceptar su método de pago")
      return False
procesar_unpago = procesar_pago("Visa", 11111)


# Finalmente el pago se confirma
def confirmar_pago(pago_exitoso):
   if pago_exitoso:
      print("Se a realizado exitosamente el pago")
      return True
   else:
      print("Ha ocurrido un error al confirmar el pago, inténtelo de nuevo")

#⏳ Validar método de pago
#⏳ Procesar pago
#⏳ Confirmar pago

def validar_metodo_pago(metodo_pago):

    metodos_validos = ["Tarjeta", "Yape", "Plin", "PayPal"]
    if metodo_pago in metodos_validos:
        return True
    return False
validar_metodo_depago = validar_metodo_pago("Visa")
print(validar_metodo_depago)
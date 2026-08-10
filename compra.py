from carrito import carrito
from pagos import validar_metodo_pago # Necesita método de pago
from precio import subtotal # Necesita carrito
from precio import total # Necesita carrito y subtotal
from pagos import procesar_pago # Necesita método de pago y TOTAL
from pagos import confirmar_pago # confirmar pago exitoso
from factura import generar_factura # Necesita carrito, total y método de pago

def realizar_compra(carrito, metodo_pago):
    if not carrito:
        print("El carrito esta vacio")
        return False
    if validar_metodo_pago(metodo_pago):

        monto_subtotal = subtotal(carrito)
        monto_total = total(carrito, monto_subtotal)

        pago_exitoso = procesar_pago(metodo_pago, monto_total)

        if not pago_exitoso:
            return False

        pago_confirmado = confirmar_pago(pago_exitoso)

        if not pago_confirmado:
            return False

        factura_generada = generar_factura(
            carrito, monto_total, metodo_pago
        )

        return factura_generada
    else:
        print("ERROR: método de pago no registado en el sistema, inténtelo con otro método de pago.")
        return False

from carrito import carrito
from pagos import validar_metodo_pago # Necesita método de pago
from precio import subtotal # Necesita carrito
from precio import total # Necesita carrito y subtotal
from pagos import procesar_pago # Necesita método de pago y TOTAL
from pagos import confirmar_pago # Necesita método de pago
from factura import generar_factura # Necesita carrito, total y método de pago

def realizar_compra(carrito, metodo_pago):
    if not carrito:
        print("Error: El carrito está vacío.")
        return False

    if validar_metodo_pago(metodo_pago):
        
        monto_subtotal = subtotal(carrito)
        monto_total = total(carrito, monto_subtotal) 
        
        
        procesar_pago(metodo_pago, monto_total)
        confirmar_pago(metodo_pago)
        
        
        generar_factura(carrito, monto_total, metodo_pago)
        
        print("La compra fue realizada con éxito. Gracias por comprar.")
        return True # Indicamos que la operación fue un éxito
    else:
        print("Error: Método de pago no válido.")
        return False




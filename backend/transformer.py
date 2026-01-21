from datetime import datetime

def transformar_pedidos(data):
    pedidos = data.get("pedidos", [])
    
    pedidos_formateados = []
    total_items = 0
    monto_total_bruto = 0
    monto_total_descuentos = 0
    pedidos_por_estado = {"PENDIENTE":0, "ENVIADO":0, "ENTREGADO":0, "CANCELADO":0}
    clientes_unicos = set()
    ciudades = set()

    estado_badge_map = {
        "PENDIENTE": "warning",
        "ENVIADO": "info",
        "ENTREGADO": "success",
        "CANCELADO": "danger"
    }

    metodo_pago_map = {
        "TARJETA_CREDITO": "Tarjeta de Crédito",
        "TARJETA_DEBITO": "Tarjeta de Débito",
        "TRANSFERENCIA": "Transferencia"
    }

    for pedido in pedidos:
        subtotal = sum(item["precio_unitario"] * item["cantidad"] for item in pedido["items"])
        descuento = sum(int(item["precio_unitario"] * item["cantidad"] * item["descuento_porcentaje"] / 100) for item in pedido["items"])
        total = subtotal - descuento

        total_items += sum(item["cantidad"] for item in pedido["items"])
        monto_total_bruto += subtotal
        monto_total_descuentos += descuento

        estado_upper = pedido["estado"].upper()
        pedidos_por_estado[estado_upper] = pedidos_por_estado.get(estado_upper, 0) + 1

        clientes_unicos.add(pedido["cliente"]["id"])
        ciudades.add(pedido["cliente"]["direccion"]["ciudad"])

        fecha_formateada = datetime.fromisoformat(pedido["fecha_creacion"].replace("Z", "+00:00")).strftime("%d/%m/%Y")

        pedidos_formateados.append({
            "id": pedido["pedido_id"],
            "fecha": fecha_formateada,
            "cliente_nombre": pedido["cliente"]["nombre_completo"],
            "cliente_email": pedido["cliente"]["email"],
            "ciudad": pedido["cliente"]["direccion"]["ciudad"],
            "estado": pedido["estado"].capitalize(),
            "estado_badge": estado_badge_map.get(estado_upper, "secondary"),
            "metodo_pago": metodo_pago_map.get(pedido["metodo_pago"], pedido["metodo_pago"]),
            "cantidad_items": len(pedido["items"]),
            "subtotal": subtotal,
            "descuento": descuento,
            "total": total,
            "tiene_notas": bool(pedido.get("notas"))
        })

    resumen = {
        "total_pedidos": len(pedidos),
        "total_items": total_items,
        "monto_total_bruto": monto_total_bruto,
        "monto_total_descuentos": monto_total_descuentos,
        "monto_total_neto": monto_total_bruto - monto_total_descuentos,
        "pedidos_por_estado": pedidos_por_estado
    }

    resultado = {
        "resumen": resumen,
        "pedidos_formateados": pedidos_formateados,
        "clientes_unicos": len(clientes_unicos),
        "ciudades": list(ciudades)
    }

    return resultado

productos = ["Corrector", "Rubor", "Lip Gloss"]
precios = [150, 200, 120]

def calcular_total(cantidades, precios):
    total = 0
    for i in range (len(cantidades)):
        total += cantidades[i] * precios[i]
    return total

print("Bienvenida a tienda de maquillaje💄 EMIL COSMETICS💄")
nombre = input ("Ingresa tu nombre: ")

cantidades = []
print("Selecciona tu pedido:")
for i in range(len(productos)):
    print(f"{i+1}. {productos[i]} - ${precios[i]}")
    cantidad = int(input(f"Cuantos {productos[i]} quieres? "))
    cantidades.append(cantidad)

total = calcular_total(cantidades, precios)

# Aplicar descuento del 10% si es mayor a $300
if total > 300:
    descuento = total * 0.10
    total_final = total - descuento
else:
    descuento = 0
    total_final = total

# Imprimir recibo
print("\n" + "="*30)
print("💄 EMIL COSMETICS💄")
print("="*30)
print(f"Cliente: {nombre}")
print("-"*30)

for i in range(len(productos)):
    if cantidades[i] > 0:
        subtotal = cantidades[i] * precios[i]
        print(f"{productos[i]}: {cantidades[i]} x ${precios[i]} = ${subtotal}")

print("-"*30)
print(f"Subtotal: ${total}")
if descuento > 0:
    print(f"Descuento: -${descuento}")
print(f"Total: ${total_final}")
print("="*30)
print("¡Gracias por tu compra! ✨")
print("="*30)
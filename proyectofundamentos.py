# -*- coding: utf-8 -*-
"""ProyectoFundamentos.ipynb

# **VER LOS PRODUCTOS EN STOCK**
"""

def main():
  #se crea la categoria:
  categoria = input("Defina la categoría del producto (ej. Mouse, Teclados): ")
  # Validamos que la categoría no tenga números
   #while es un BUCLE esto se ejecuta siempre y cuando la condición sea verdadera
   #el .replace(" ", "") es para que si el programa detecta un espacio no de error y siga corriendo
   #.isalpha() detecta que los nombres de los productos sean letras y no números
  while not categoria.replace(" ", "").isalpha():
        print("Error: El nombre de la categoría debe contener solo letras.")
        categoria = input("Ingrese la categoría nuevamente: ")
  #detalle del producto
  # Pedimos la nombre del producto
  nombre = input(f"Ingrese el nombre del producto para {categoria}: ")
  #la "f" es para colocar variables dentro del texto
  # Pedimos la marca
  marca = input(f"¿Cuál es la marca de este {nombre}?: ")
  #la "f" es para colocar variables dentro del texto
  #cantidades
  stock_inicial = int(input(f"Stock inicial de {nombre} ({marca}): "))
  #la "f" es para colocar variables dentro del texto
  venta = int(input(f"¿Cuántas unidades de {nombre} se vendieron?: "))
  #la "f" es para colocar variables dentro del texto
  # Validación de stock real
  # El ciclo se repite si la venta es mayor al stock o si es negativa
  while venta > stock_inicial or venta < 0:
    print(f"Error: No puedes vender {venta}. Solo hay {stock_inicial} en stock.")
    #la "f" es para colocar variables dentro del texto
    venta = int(input("Ingrese una cantidad de venta válida: "))
  stock_actual = stock_inicial - venta
  #reporte final
  print("\n" + "="*55)
  print(f"SISTEMA DE INVENTARIO - CATEGORÍA: {categoria.upper()}")
  #la "f" es para colocar variables dentro del texto
  #{nombre.upper()} Toma la variable y la convierte en mayusculas
  print("="*55)
  # Mostramos la jerarquía: Categoría > Producto (Marca)
  print(f"DETALLE: {categoria} > {nombre.capitalize()} ({marca})")
  #la "f" es para colocar variables dentro del texto
  print(f"ESTADO ACTUAL: {stock_actual} unidades disponibles")
  #la "f" es para colocar variables dentro del texto
  print("-" * 55) #Aqui se imprime 55 veces -
  # Alerta de repocision
  if stock_actual < 5:
        print(f"AVISO: Reponer {nombre} en la sección de {categoria}.")
  else:
        print(" Stock en niveles óptimos.")
  print("="*55)
main()

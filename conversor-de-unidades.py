
# Definir tipo de cambio
pulgada_a_cm = 2.54
result = 0

try:
    # Solicita al usuario una medida y la convierte a float
    medida = float(input("Ingrese la medida que desea cambiar de cm a pulgada: "))
    print(f"Resultado: {medida / pulgada_a_cm:.2f} pulgadas")  # Ejemplo de conversión
except ValueError:
    # Maneja el caso donde el input no puede ser convertido a float
    print("Error: La entrada no es un número válido.")


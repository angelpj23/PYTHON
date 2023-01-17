try:
    print("Conversion de temperatura grados Celcius a grados Farenheit")
    C = int(input("Digite la temperatura:\n "))
    F = 9 // 5 * C + 32
    print(f"La cantidad de Celcius {C} equivale a: {F} grados Farenheit")
except ValueError:
    print("solo se aceptan letras")

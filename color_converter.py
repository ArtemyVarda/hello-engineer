def color_hex(r, g, b):
    if (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
        hex_color = f"#{r:02X}{g:02X}{b:02X}"
        return hex_color
    else:
        print("Ошибка: все значения должны быть в диапазоне от 0 до 255")


r = int(input("Введите значение R (0-255): "))
g = int(input("Введите значение G (0-255): "))
b = int(input("Введите значение B (0-255): "))
result = color_hex(r, g, b)
print(result)
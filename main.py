def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mcd_multiple(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result

nums = []

while True:
    try:
        num = int(input("Ingresa un número (0 para terminar): "))
        if num < 0:
            print("Por favor, ingresa un número positivo.")
        else:
            nums.append(num)
            if num == 0:
                break
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

if len(nums) < 2:
    print("Debes ingresar al menos dos números.")
else:
    mcd = mcd_multiple(nums)
    print("El máximo común divisor de los números ingresados es:", mcd)

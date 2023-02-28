def is_fibonacci(num):
    if num == 0:
        return True
    a = 0
    b = 1
    while b <= num:
        if b == num:
            return True
        a = b
        b = a + b
    return False

valor = int(input("Digite um número inteiro: "))
if is_fibonacci(valor):
    print(f"O número {valor} pertence à sequência de Fibonacci.")
else:
    print(f"O número {valor} não pertence à sequência de Fibonacci.")
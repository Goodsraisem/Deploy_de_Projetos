from Verificador import multi7, multi5


try:
    num: int = int(input("Por favor, insira um número inteiro\n"))

except ValueError:
    print("Por favor, insira somente números inteiros")

rps5 = multi5(num)
rps7 = multi7(num)

if rps5 == 0:
    if rps7 == 0:
        print("miss")
        assert rps7, rps5 == 0
    else:
        print(rps7)
        assert rps7 != 0
else:
    try:
        print(rps5+rps7)
        assert rps7, rps5 != 0
    except TypeError:
        print(rps5)
        assert rps5 != 0


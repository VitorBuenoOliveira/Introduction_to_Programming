frutas = ["abacaxi","banana"]
tenta = 0
for x in range(10):
    tenta += 1
    escolha =  input(f"Tentativa {tenta}.Escolha uma fruta: ")

    if escolha.lower() == "desisto":
        print("Obrigado pela participação")
        break
    if escolha.lower() in frutas:
        print("Parabéns, você acertou!")
        break
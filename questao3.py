import random
print ("------vamos jogar pedra, papel ou tesoura?------")
print (" escolha a opçao a baixo:")
print("[1] pedra ")
print("[2] papel")   
print("[3] tesoura")
resp = int(input("sua escolha: "))
computador = random.randint(1, 3)
if resp == 1:
    print ("Você escolheu pedra")        
elif resp == 2:
        print ("Você escolheu papel")
elif resp == 3:
        print ("Você escolheu tesoura")
else:
        print ("escolha invalida")
opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}
if resp not in [1, 2, 3]:
    print("Escolha inválida")
else:
    print(f"\nVocê escolheu: {opcoes[resp]}")
    print(f"Computador escolheu: {opcoes[computador]}\n")

    # Verifica quem venceu
    if resp == computador:
        print("Empate!")
    elif (resp == 1 and computador == 3) or \
         (resp == 2 and computador == 1) or \
         (resp == 3 and computador == 2):
        print("Você venceu!")
    else:
        print("Computador venceu!")
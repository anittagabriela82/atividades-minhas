print ("------vamos jogar pedra, papel ou tesoura?------")
print (" escolha a opçao a baixo:")
print("[1] pedra ")
print("[2] papel")   
print("[3] tesoura")
resp = int(input("sua escolha: "))
if resp == 1:
    print ("Você escolheu pedra")        
elif resp == 2:
        print ("Você escolheu papel")
elif resp == 3:
        print ("Você escolheu tesoura")
else:
        print ("escolha invalida")
hamburguer = 25.00
batata_frita = 15.00        
refrigerante = 8.00
print("---------Cardápio---------")
print("[1] - Hambúrguer - R$25,00")
print("[2] - Batata Frita - R$15,00")   
print("[3] - Refrigerante - R$8,00")
resp = int(input("Escolha o número do produto desejado: "  ))
computador = random.randint(1, 3)
if resp == 1:
    print ("Você escolheu Hambúrguer - R$25,00")        
elif resp == 2:
        print ("Você escolheu Batata Frita - R$15,00")
elif resp == 3:
        print (" Você escolheu Refrigerante - R$8,00")
else:
        print (" Opção inválida ")
                  
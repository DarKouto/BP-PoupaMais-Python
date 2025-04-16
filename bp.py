print("Desconto BP Poupa Mais em Python por DarKouto. V1.0\n")

valor1 = float(input("Quanto combustível meteu o Condutor 1? (€) "))
valor_total = float(input("Qual foi o valor total sem desconto? (€) "))
valor_final = float(input("Qual foi o preço final com desconto? (€) "))

valor2 = (valor_total-valor1)
percentagem1 = (100*valor1)/valor_total
percentagem2 = (100*valor2)/valor_total
conta1 = (percentagem1*valor_final)/100
conta2 = (percentagem2*valor_final)/100

print(
    "\nO Condutor 1 meteu:",round(valor1,2),"€",
    "\nO Condutor 2 meteu:",round(valor2,2),"€",
    "\nPercentagem Condutor 1:",round(percentagem1,2),"%",
    "\nPercentagem Condutor 2:",round(percentagem2,2),"%",
    "\nCondutor 1 paga:",round(conta1,2),"€",
    "\nCondutor 2 paga:",round(conta2,2),"€")

sair = input("\nPrima ENTER para sair")

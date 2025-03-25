print("Desconto BP Poupa Mais em Python por DarKouto. V1.0\n")

valor1 = float(input("Quanto combustível meteu o Condutor 1? (€) "))
valorTotal = float(input("Qual foi o valor total sem desconto? (€) "))
valorFinal = float(input("Qual foi o preço final com desconto? (€) "))

valor2 = (valorTotal-valor1)
percentagem1 = (100*valor1)/valorTotal
percentagem2 = (100*valor2)/valorTotal
conta1 = (percentagem1*valorFinal)/100
conta2 = (percentagem2*valorFinal)/100

print(
    "\nO Condutor 1 meteu:",round(valor1,2),"€",
    "\nO Condutor 2 meteu:",round(valor2,2),"€",
    "\nPercentagem Condutor 1:",round(percentagem1,2),"%",
    "\nPercentagem Condutor 2:",round(percentagem2,2),"%",
    "\nCondutor 1 paga:",round(conta1,2),"€",
    "\nCondutor 2 paga:",round(conta2,2),"€")

sair = input("\nPrima ENTER para sair")

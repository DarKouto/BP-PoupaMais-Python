print("Desconto BP Poupa Mais em Python por DarKouto. V1.0\n");

valorSusana = float(input("Quanto combustível meteu a Susana? (€) "))
valorTotal = float(input("Qual foi o valor total sem desconto? (€) "))
valorFinal = float(input("Qual foi o preço final com desconto? (€) "))

valorDaniel = (valorTotal-valorSusana)
percentagemSusana = (100*valorSusana)/valorTotal
percentagemDaniel = (100*valorDaniel)/valorTotal
contaSusana = (percentagemSusana*valorFinal)/100
contaDaniel = (percentagemDaniel*valorFinal)/100

print(
    "\nA Susana meteu:",round(valorSusana,2),"€",
    "\nO Daniel meteu:",round(valorDaniel,2),"€",
    "\nPercentagem Susana:",round(percentagemSusana,2),"%",
    "\nPercentagem Daniel:",round(percentagemDaniel,2),"%",
    "\nSusana paga:",round(contaSusana,2),"€",
    "\nDaniel paga:",round(contaDaniel,2),"€")

sair = input("\nPrima ENTER para sair")
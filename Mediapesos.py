## uma empresa de caminhoes de transporte cabem exatamente 100 caixas de iguais dimensoes
## o peso pode varias dependendo do seu conteudo 
## algoritmo para calcular o peso total das caixas que serao colocadas em um caminhao e que exiba qual o peso medio de cada caixa

peso_total = 0.0 #iniciamos o peso total com 0

for x in range(1,6): #o loop vai se repetir 100 vezes, uma para cada caixa
    peso_atual = float(input("Informe o peso da caixa em kg: ")) #leitura do peso da caixa
    peso_total = peso_total + peso_atual #acumulamos o peso da caixa no peso total

    media = peso_total / 5#calculamos a media dividindo o peso total pelo numero de caixas

##exibicao dos resultados. ##format e uma funcao que permite inserir variaveis dentro de uma string
print("O peso total das caixas e: {}. \nA media de peso por caixa e: {}".format(peso_total, media)  )
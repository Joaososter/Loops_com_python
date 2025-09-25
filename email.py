##algoritmo para que o usuario seja obrigado a responder uma pergunta com "42"

##variavel de resposta

resposte = "0" ##iniciamos a variavel com um valor diferente de "42"
while resposte != "42": ##usamos o while para repetir a pergunta até que a resposta seja "42"
    resposte = input("Qual é a resposta para a vida, o universo e tudo mais? ")
print("parabens, você acertou!") ##quando a resposta for "42", o loop termina e essa mensagem é exibida


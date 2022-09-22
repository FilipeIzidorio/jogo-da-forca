import random
import time

lista_palavras = ['gato' ,'elefante','cachorro','cobra','aranha','arara','veado','aguia','baleia','vaca','ovelha']

palavra = random.choice(lista_palavras)



tentativas = 0

chances = 7

letras_escolhidas = []

estado_atual = ["_"] * len(palavra)

print ("Bem vindo ao jogo da forca")
print ("Seu objetivo é tentar acertar a palavra secreta")
print ("Você terá que tentar uma letra por vez")
print ("Caso você acerte, a letra será colocada na palavra para que você chegue mais perto de acertar")
print ("Caso você erre, você perderá uma chance, você tem no máximo", chances, "tentativas")
print('Olá sou seu amigo da forca deseja Jogar ?')
jogar = str(input('sim ou não : '))

if jogar == "sim":
	print('você tem 7 chances para acertar a palavra secreta ')
	print('\033[31mPensando em palavra...')
	time.sleep(3)
	print('\033[32mPalavra escolhida com sucesso.')
	print('\033[0mA palavra escolhida tem {} letras'.format(len(palavra)))
	print("\n\033[36mdiga,é um nome de animal! ")
	print('\n\033[0m',estado_atual)

else:
	print("Até a proxima!!")
	exit()


while tentativas < chances and ''.join(estado_atual) != palavra:

	letra = input("\n\nQual letra você quer tentar? ")

	while letra in letras_escolhidas:
		print ("Você escolheu uma letra que já tinha tentado, escolha outra")
		letra = input("\nQual letra você quer tentar? ")

	letras_escolhidas.append(letra)

	if letra in palavra:
		print ("Parabéns, você acertou a letra!")
		for i in range(len(palavra)):
			if letra == palavra[i]:
				estado_atual[i] = letra
	else:
		print ("Que pena, você errou!")
		tentativas = tentativas + 1
		if tentativas == 1:
			print("  _______     ")
			print(" |/      |    ")
			print(" |      (_)   ")
			print(" |            ")
			print(" |            ")
			print(" |            ")
		elif tentativas ==2:
			print("  _______     ")
			print(" |/      |    ")
			print(" |      (_)   ")
			print(" |      \     ")
			print(" |            ")
			print(" |            ")
		elif tentativas ==3:
			print("  _______     ")
			print(" |/      |    ")
			print(" |      (_)   ")
			print(" |      \|    ")
			print(" |            ")
			print(" |            ")
		elif tentativas == 4:
			print("  _______     ")
			print(" |/      |    ")
			print(" |      (_)   ")
			print(" |      \|/   ")
			print(" |            ")
			print(" |            ")

		elif tentativas==5:
			print("  _______     ")
			print(" |/      |    ")
			print(" |      (_)   ")
			print(" |      \|/   ")
			print(" |       |    ")
			print(" |            ")
		elif tentativas ==6:
			print("  _______     ")
			print(" |/      |    ")
			print(" |      (_)   ")
			print(" |      \|/   ")
			print(" |       |    ")
			print(" |      /     ")
		elif tentativas ==7:
			print("  _______     ")
			print(" |/      |    ")
			print(" |      (_)   ")
			print(" |      \|/   ")
			print(" |       |    ")
			print(" |      / \   ")

		print(" |            ")
		print("_|___         ")
		print()

	# quantas tentativas ele tem
	print ("Você já fez", tentativas, "tentativas erradas e ainda tem", chances-tentativas, "tentativas" )

	# qual o estado atual da palavra
	print ("Esse é o estado atual:")
	print (estado_atual)

	# quais as letras ele já tentou
	print ("\nAs letras que você já tentou são:")
	for item in letras_escolhidas:
		print (item, end=" ")

# fazer um final pro jogo
if tentativas == chances:
	print ("\n\n")
	print("Puxa, você foi enforcado!")
	print("\n     GAME OVER  ")
	print('\033[31m')
	print("    _______________         ")
	print("   /               \       ")
	print("  /                 \      ")
	print("//                   \/\  ")
	print("\|   XXXX     XXXX   | /   ")
	print(" |   XXXX     XXXX   |/     ")
	print(" |   XXX       XXX   |      ")
	print(" |                   |      ")
	print(" \__      XXX      __/     ")
	print("   |\     XXX     /|       ")
	print("   | |           | |        ")
	print("   | I I I I I I I |        ")
	print("   |  I I I I I I  |        ")
	print("   \_             _/       ")
	print("     \_         _/         ")
	print("       \_______/           ")
else:
	print("\n\n\033[33mParabéns, você ganhou!")
	print("       ___________      ")
	print("      '._==_==_=_.'     ")
	print("      .-\\:      /-.    ")
	print("     | (|:.     |) |    ")
	print("      '-|:.     |-'     ")
	print("        \\::.    /      ")
	print("         '::. .'        ")
	print("           ) (          ")
	print("         _.' '._        ")
	print("        '-------'       ")


print ("\033[0mA palavra era",'*\033[33m',palavra,'\033[0m*')

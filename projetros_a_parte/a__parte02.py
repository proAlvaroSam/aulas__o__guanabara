import random

def adivinhar_numero():
    # Gera um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    print("Bem-vindo ao jogo de adivinhar o número!")
    print("Tente adivinhar o número entre 1 e 100.")

    while True:
        # Pede ao jogador para digitar um número
        tentativa = int(input("Digite seu palpite: "))
        tentativas += 1

        # Compara o palpite do jogador com o número secreto
        if tentativa < numero_secreto:
            print("O número é maior!")
        elif tentativa > numero_secreto:
            print("O número é menor!")
        else:
            print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")
            break

# Chama a função para iniciar o jogo
adivinhar_numero()

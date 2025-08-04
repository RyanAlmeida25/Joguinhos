import random
import os

def jogo_advinho():
    caminho = os.path.join(os.path.dirname(__file__), "palavras_5_letras.txt")
    try:
        with open(caminho, "r", encoding="utf-8") as file:
            tentativas = 5
            letras_adivinhadas = []
            palavras_5_letras = file.read().splitlines()
            palavra_secreta = random.choice(palavras_5_letras)
            palavra_mostrar = "_" * len(palavra_secreta)

            while tentativas > 0:
                resp = input("Digite uma letra: ").lower()

                if resp in palavra_secreta:
                    if resp not in letras_adivinhadas:
                        letras_adivinhadas.append(resp)
                        palavra_mostrar = ''.join(
                            letra if letra in letras_adivinhadas else '_' for letra in palavra_secreta
                        )
                        print("Letra correta!")
                        print(f"Palavra: {palavra_mostrar}")
                    else:
                        print("Você já tentou essa letra.")
                else:
                    tentativas -= 1
                    print(f"Errada! Você ainda tem {tentativas} tentativas.")

                if all(letra in letras_adivinhadas for letra in palavra_secreta):
                    print(f"\nParabéns! Você descobriu a palavra: {palavra_secreta}")
                    break

            if tentativas == 0:
                print(f"\nVocê perdeu. A palavra era: {palavra_secreta}.")

    except FileNotFoundError:
        print("Arquivo de palavras não encontrado.")
        return

jogo_advinho()

import random

def jogo():
    escolha_pc = random.randint(1, 100)
    tentativas = 0
    while True:
        resp = int(input("Digite um número entre 1 e 100: "))
        if resp != escolha_pc:
            tentativas += 1
        if resp < escolha_pc:
            print('Tente um número maior.')
        elif resp > escolha_pc:
            print('Tente um número menor.')
        else:
            print(f'Parabéns, você acertou! a resposta era {escolha_pc}.')
            print(f'Tentativas: {tentativas}')
            break

    print(escolha_pc)

jogo()

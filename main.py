from DFS import run_dfs
from a_algorithm import run_star

def main():    
    while True:
        inp = input('Selecione um dos algoritmos\n1- Algoritmo A*\n2- Busca por profundidado\n3- Sair\n')

        if inp == '1':
            run_star()
        if inp == '2':
            run_dfs()
        if inp == '3':
            print('Saindo do programa...')
            break

if __name__ == '__main__':
    main()

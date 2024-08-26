'''eu sei que eu disse q eu ia entregar em c++, mas a semana foi corrida demais, e eu achei q era sjf e prioridade,
realmente esqueci do paralelismo, mas eu vou refazer em c++'''
import multiprocessing as mp
import time

#definindo a lista para a soma
arrayParaSoma = list(range(1,1000001))


#definir a função para executar a soma
#soma os elementos do valor mínimo até o valor máximo usando um for
def somaLista(min, max, queue):
    soma = 0 
    for i in range(min, max):
        soma += arrayParaSoma[i]
    queue.put(soma)

#soma da posição lista[min] até lista [max]
#armazena isso na variavel 'soma'

if __name__ == '__main__':

    fila = mp.Queue()

    p1 = mp.Process(target=somaLista, args=(0, 166667, fila))
    #soma os elementos arrayParaSoma[0] até o elemento na posição arrayParaSoma[166666] = 1+2+3+4+5+6+7+8...+1666666
    p2 = mp.Process(target=somaLista, args=(166667, 333335, fila))
    #soma os elementos arrayParaSoma[166667] até o elemento na posição arrayParaSoma[333334] = 166667 + 166668 + 16669 + ... + 333334
    p3 = mp.Process(target=somaLista, args=(333335, 500003, fila))   
    p4 = mp.Process(target=somaLista, args=(500003, 666670, fila))
    p5 = mp.Process(target=somaLista, args=(666670, 833337, fila))
    p6 = mp.Process(target=somaLista, args=(833337, 1000000, fila))


    inicio = time.time()

    #inicia todos os processos
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()

    #'junta' todos os processos
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()

    fim = time.time()

    resultadoFinal = 0

    #enquanto a fila não estiver vazia
    #soma o elemento dela na variável 'resultadoFinal'

    while fila.empty() == False:
        resultadoFinal += fila.get()

    print(f'''O resultado da soma é: {resultadoFinal}''')
    print(f'''O tempo de execução foi: {fim-inicio}''')
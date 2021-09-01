import numpy as np
from random import uniform, randint, choice
from collections import deque

class Sala:

    def __init__(self, size, lista_obstaculos, locais_sujeira, aspirador, posicao_aspirador, posicao_base_recarregamento):
        self.vazio = 0
        self.obstaculo = 1
        self.sujeira = 2
        self.locais_sujeira = locais_sujeira
        self.piso = np.zeros((size[0], size[1]), dtype=int)

        for x in range(len(lista_obstaculos)):  # distribuindo obstaculos
            self.piso[lista_obstaculos[x][0]
                      ][lista_obstaculos[x][1]] = self.obstaculo

        self.piso[posicao_aspirador[0]][posicao_aspirador[1]] = 3
        self.posicao_aspirador = posicao_aspirador
        self.aspirador = aspirador
        self.posicao_base = posicao_base_recarregamento

    # Escreva seu código aqui levando em conta que:
     # o piso recebe valor vazio em todo lugar e
     # você deve colocar obstáculos nas coordenadas recebidas no 2o parâmetro do construtor
     # a sujeira deve ser atualizada no método step() pois, mesmo quando o agente limpa,
     # a sujeira deverá reaparecer com certa probabilidade
    def update_matrix(self):
        norte, sul, leste, oeste = self.get_vizinhos(self.posicao_aspirador)

        nova_posicao, piso_limpo = self.aspirador.action_agent_program(
            [norte, sul, leste, oeste])
    
        print("nova_posicao:", nova_posicao)
        print("piso_limpo:", piso_limpo)

        linha = self.posicao_aspirador[0]
        coluna = self.posicao_aspirador[1]

        linha_nova = nova_posicao[0]
        coluna_nova = nova_posicao[1]

        # if (self.piso[linha_nova][coluna_nova] == self.posicao_base):

        self.piso[linha][coluna] = 0
        self.piso[linha_nova][coluna_nova] = 3

        self.posicao_aspirador = nova_posicao

    def get_vizinhos(self, pos):
        norte, sul, leste, oeste = -1, -1, -1, -1
        if(pos[0] > 0):
            norte = self.piso[pos[0] -
                              1][pos[1]]

        if(pos[0] < len(self.piso)-1):
            sul = self.piso[pos[0] +
                            1][pos[1]]
                            
        if(pos[1] < len(self.piso[0])-1):
            leste = self.piso[pos[0]
                              ][pos[1]+1]

        if(pos[1] > 0):
            oeste = self.piso[pos[0]
                              ][pos[1]-1]
                              
        return norte,sul,leste,oeste

    def step(self):  # atualiza sujeira, realiza a interação do agente-ambiente

        for x in range(len(self.piso)):
            for y in range(len(self.piso[0])):
                probabilidade = uniform(0, 1)

                if (self.posicao_aspirador == self.posicao_base):
                    self.piso[self.posicao_aspirador[0]
                              ][self.posicao_aspirador[1]] = 3
                elif (self.posicao_aspirador != self.posicao_base):
                    self.piso[self.posicao_base[0]][self.posicao_base[1]] = 4

                if (self.piso[x][y] == 0):
                    if((x, y) in self.locais_sujeira):
                        if(probabilidade < 0.1):
                            self.piso[x][y] = self.sujeira
                            # print(probabilidade)
                    else:
                        if(probabilidade < 0.01):
                            self.piso[x][y] = self.sujeira
                            # print(probabilidade)

        print(self.piso)

        self.aspirador.print_status()

        self.update_matrix()
     # Escreva seu código aqui levando em conta o pseudo-código para
     # adicionar sujeira com maior probabilidade em certos locais:

     # atualização da sujeira
     # for i até dim M
     #  for j até dim N
     #      r = rand(0,1)
     #      se (i,j) pertence a hot_spots_sujeira
     #      então
     #            se r < 0.1 então piso(i,j) = sujeira
     #      senão se r < 0.01 então piso(i,j) = sujeira

     # chamar o programa do agente e atualiza suas coordenadas a partir da
     # ação recomendada pelo próprio agente
     # imprimir o estado do ambiente
     # imprimir o estado do Agente aspirador

    def run(self, N):  # chama step N vezes para simular o agente e o seu ambiente
        for i in range(N):
            print("\n--------------------------------------------\n")
            print("Passo:", i)
            self.step()
        print(self.piso)


class Aspirador:

    def __init__(self, energia_aspirador, M, N, posicao_aspirador):
        self.energia = energia_aspirador
        self.movimentos = {
            "norte": lambda l: [l[0]-1, l[1]],
            "sul": lambda l: [l[0]+1, l[1]],
            "oeste": lambda l: [l[0], l[1]-1],
            "leste": lambda l: [l[0], l[1]+1],
        }

        # diz respeito à celula imediatamente à frente do agente se obstáculo
        self.status_percepcao = ["sujo", "vazio", "obstaculo"]

      # consulta o ambiente para obter as coordenadas
        # registra as experiências do robô.
        self.modelo_ambiente = np.zeros((M, N), dtype=int)
        self.modelo_ambiente[posicao_aspirador[0]][posicao_aspirador[1]] = 4
      # no modelo é guardado: contador de sujeira (0...MAX) ou obstáculo (-1)
        self.posicao_base = posicao_aspirador
        self.posicao_aspirador = posicao_aspirador

    # definida a partir do contador de sujeira e da posição atual.
    # avaliação_heurística = np.array([dimX, dimY], int)
    def percepcao(self):
        return 0

    def update_matrix(self, posicao, tipo):
        if (tipo == 3):
            linha = self.posicao_aspirador[0]
            coluna = self.posicao_aspirador[1]
            print("posicao_aspirador:", self.posicao_aspirador)
            print("posicao_base:", self.posicao_base)
            if [linha, coluna] != self.posicao_base:
                self.modelo_ambiente[linha][coluna] = 0
            else:
                self.modelo_ambiente[linha][coluna] = 4
            self.posicao_aspirador = posicao

        linha_nova = posicao[0]
        coluna_nova = posicao[1]

        self.modelo_ambiente[linha_nova][coluna_nova] = tipo

    def update_posicao(self, direcao):
        # retornar posição atual utilizando a função do set acoes em cima da posição atual do aspirador
        # posicao = self.posicao_aspirador
        # print(self.posicao_aspirador)
        nova_posicao = self.movimentos[f'{direcao}'](self.posicao_aspirador)
        # print(self.posicao_aspirador)
        # if((nova_posicao[0] < len(self.modelo_ambiente) and nova_posicao[0] >= 0) and (nova_posicao[1] < len(self.modelo_ambiente[0]) and (nova_posicao[1] > 0))):
        #     posicao = nova_posicao
        # else:
        #     nova_posicao = posicao

        # if(posicao != self.posicao_aspirador):
        # print("nova posicao:", nova_posicao)
        self.update_matrix(nova_posicao, 3)

        return nova_posicao

    def limpar(self, cords, pos):
        print("comando: limpou")
        self.energia -= 5
        limpou = True
        return self.andar(cords, pos, limpou)

    def carregar(self, cords, pos):
        print("comando: carregou")
        self.energia = 100
        return self.andar(cords, pos)

    def andar(self, cords, pos, limpou = False):
        print("comando: andou")
        self.energia -= 1 
        posicao = self.update_posicao(cords[pos])
        return (posicao, limpou)

    def registra_obstaculo(self, cords, pos):
        print("comando: registrou obstáculo")
        posicao_obstaculo = self.movimentos[f'{cords[pos]}'](self.posicao_aspirador) 
        self.update_matrix(posicao_obstaculo, 1)
        return(self.posicao_aspirador, False)

    def registra_sujeira(self, cords, pos):
        print("comando: registrou sujeira")
        posicao_sujeira = self.movimentos[f'{cords[pos]}'](self.posicao_aspirador) 
        self.update_matrix(posicao_sujeira, 2)
        return(self.posicao_aspirador, False)

    def registra_sensores(self, percepcoes, cords):
        for i in range(len(percepcoes)):
            if percepcoes[i] == 1:
                self.registra_obstaculo(cords, i)
            if percepcoes[i] == 2:
                self.registra_sujeira(cords, i)

    def action_agent_program(self, percepcoes):
        # realizar busca heurística usando a avaliação heurística, o modelo do ambiente e a percepção corrente.
        # considerar que ele deve retornar à base quando a bateria estiver crítica
        print("sensores:", percepcoes)

        cords = ["norte", "sul", "leste", "oeste"]
        funcoes_validas = {0: self.andar, 2: self.limpar, 4: self.carregar}
        
        self.registra_sensores(percepcoes, cords)
                
        funcao_invalida = True
        while(funcao_invalida):
            pos = randint(0,3)
            lista_chaves = list(funcoes_validas.keys())
            if percepcoes[pos] in lista_chaves:
                funcao_invalida = False
                return funcoes_validas[percepcoes[pos]](cords, pos)
                    
    # imprime posição do agente, o seu modelo interno do ambiente, nível da bateria

    def print_status(self):
        print("Posição do Aspirador:", self.posicao_aspirador)
        print("Nível de bateria:", self.energia)
        print("Modelo interno do ambiente:")
        print(self.modelo_ambiente)


# Código de teste
######################
# criar aspirador com 100% de energia

# TODO voltar para a base
def main():
    """Função principal da aplicação.
    """
    M = 5
    N = 5
    posicao_inicial_aspirador = [0, 0]

    meu_aspirador = Aspirador(100, M, N, posicao_inicial_aspirador)

    # cria o ambiente contendo o meu aspirador
    ambiente = Sala((M, N), [(1, 2), (2, 1), (3, 1)], [
        (2, 2), (1, 1)], meu_aspirador, posicao_inicial_aspirador, (0, 0))

    # simula 10 passos do ambiente
    ambiente.run(50)


if __name__ == "__main__":
    main()

    

# tem 4 sensores

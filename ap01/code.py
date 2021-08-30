import numpy as np
from random import uniform


class Sala:

    def __init__(self, size, lista_obstaculos, locais_sujeira, aspirador, posicao_aspirador, posicao_base_recarregamento):
        self.vazio = 0
        self.obstaculo = 1
        self.sujeira = 2
        self.locais_sujeira = locais_sujeira
        self.piso = np.zeros((size[0], size[1]), dtype=int)
        
        for x in range(len(lista_obstaculos)): #distribuindo obstaculos
            self.piso[lista_obstaculos[x][0]][lista_obstaculos[x][1]] = self.obstaculo

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
        
        nova_posicao = self.aspirador.update_posicao('oeste')#teste hihihi

        linha = self.posicao_aspirador[0]
        coluna = self.posicao_aspirador[1]
        
        linha_nova = nova_posicao[0]
        coluna_nova = nova_posicao[1]
        
        self.piso[linha][coluna] = 0
        self.piso[linha_nova][coluna_nova] = 3

        self.posicao_aspirador = nova_posicao


    
    def step(self):  # atualiza sujeira, realiza a interação do agente-ambiente

        for x in range(len(self.piso)):
            for y in range(len(self.piso[0])):
                probabilidade = uniform(0, 1)
                
                if (self.posicao_aspirador == self.posicao_base):
                    self.piso[self.posicao_aspirador[0]][self.posicao_aspirador[1]] = 3
                elif (self.posicao_aspirador != self.posicao_base):
                    self.piso[self.posicao_base[0]][self.posicao_base[1]] = 4
                
                if (self.piso[x][y] == 0):
                    if((x, y) in self.locais_sujeira):
                        if(probabilidade < 0.1):
                            self.piso[x][y] = self.sujeira
                            #print(probabilidade)
                    else:
                        if(probabilidade < 0.01):
                            self.piso[x][y] = self.sujeira
                            #print(probabilidade)
        
        print(self.piso)
        
        self.aspirador.print_status()
        
        self.update_matrix()
        
        print()
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
            print("Passo:", i)
            self.step()

class Aspirador:

    def __init__(self, energia_aspirador, M, N, posicao_aspirador):
        self.energia = energia_aspirador
        self.movimentos = {
                        "norte": lambda l: [l[0]-1,l[1]],
                        "sul": lambda l: [l[0]+1,l[1]],
                        "oeste": lambda l: [l[0],l[1]-1],
                        "leste": lambda l: [l[0],l[1]+1],
                        }

        # diz respeito à celula imediatamente à frente do agente se obstáculo
        self.status_percepcao = ["sujo", "vazio", "obstaculo"]

      # consulta o ambiente para obter as coordenadas
        # registra as experiências do robô.
        self.modelo_ambiente = np.zeros((M, N), dtype=int)
      # no modelo é guardado: contador de sujeira (0...MAX) ou obstáculo (-1)
        self.posicao_aspirador = posicao_aspirador

    # definida a partir do contador de sujeira e da posição atual.
    # avaliação_heurística = np.array([dimX, dimY], int)
    def percepcao(self): 
        return 0
    
    def update_matrix(self,posicao,tipo):
        #nova_posicao = self.aspirador.update_posicao(self.aspirador.movimentos[f'{direcao}'](direcao))#teste hihihi
        #print(self.posicao_aspirador)
        if (tipo == 3):
            linha = self.posicao_aspirador[0]
            coluna = self.posicao_aspirador[1]
            self.modelo_ambiente[linha][coluna] = 0

        linha_nova = posicao[0]
        coluna_nova = posicao[1]
        
        self.modelo_ambiente[linha_nova][coluna_nova] = tipo

        self.posicao_aspirador = posicao
        #print(self.posicao_aspirador)

    def update_posicao(self, direcao):
        #retornar posição atual utilizando a função do set acoes em cima da posição atual do aspirador
        #ta andando so pra um lado HAUDHUASHDUASHDUASHdAUSD
        criterio = lambda k: not (k[0] > len(self.modelo_ambiente)-1) and (k[1] < len(self.modelo_ambiente[0]))
        posicao = self.posicao_aspirador
        print(self.posicao_aspirador)
        nova_posicao = self.movimentos[f'{direcao}'](self.posicao_aspirador)
        print(self.posicao_aspirador)
        if not ((nova_posicao[0] > len(self.modelo_ambiente)-1 or nova_posicao[0] < -len(self.modelo_ambiente)) or (nova_posicao[1] > len(self.modelo_ambiente[0])-1 or nova_posicao[1] < -len(self.modelo_ambiente[1]))):
            posicao = nova_posicao
        else:
            nova_posicao = posicao

        #print(self.posicao_aspirador)
        
        '''
        if nova_posicao[0] >= 0 and nova_posicao[1] >= 0:
            if not (nova_posicao[0] > len(self.modelo_ambiente)-1) and (nova_posicao[1] < len(self.modelo_ambiente[0])):
                self.posicao_aspirador = nova_posicao
        '''
        if(posicao != self.posicao_aspirador):
            self.update_matrix(nova_posicao,3)
        
        return posicao
            

    def action_agent_program(self, percepção):
        print("teste")
       # realizar busca heurística usando a avaliação heurística, o modelo do ambiente e a percepção corrente.
       # considerar que ele deve retornar à base quando a bateria estiver crítica

    def print_status(self):  # imprime posição do agente, o seu modelo interno do ambiente, nível da bateria
        print("Posição do Aspirador:", self.posicao_aspirador)
        print("Nível de bateria:", self.energia)
        print("Modelo interno do ambiente:")
        print(self.modelo_ambiente)

# Código de teste
######################
# criar aspirador com 100% de energia

def main():
    """Função principal da aplicação.
    """
    M = 4
    N = 4
    posicao_inicial_aspirador = [0, 0]

    meu_aspirador = Aspirador(100, M, N, posicao_inicial_aspirador)

    # cria o ambiente contendo o meu aspirador
    ambiente = Sala((M, N), [(1, 2), (2, 1)], [
                    (2, 2), (1, 1)], meu_aspirador, posicao_inicial_aspirador, (0, 0))

    # simula 10 passos do ambiente
    ambiente.run(10)


if __name__ == "__main__":
    main()

#tem 4 sensores
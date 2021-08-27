import numpy as np
from random import uniform


class Sala:

    def __init__(self, size, lista_obstaculos, hot_spots_sujeira, aspirador, posicao_aspirador, posicao_base_recarregamento):
        self.vazio = 0
        self.obstaculo = 1
        self.sujeira = 2
        self.aspirador = aspirador
        self.hot_spots_sujeira = hot_spots_sujeira
        self.piso = np.zeros((size[0], size[1]), dtype=int)
        for x in range(len(lista_obstaculos)):
            self.piso[lista_obstaculos[x][0]
                      ][lista_obstaculos[x][1]] = self.obstaculo

        self.piso[posicao_aspirador[0]][posicao_aspirador[1]] = 3

        print(self.piso)
        self.pos_aspirador = posicao_aspirador
        self.pos_base = posicao_base_recarregamento

    # Escreva seu código aqui levando em conta que:
     # o piso recebe valor vazio em todo lugar e
     # você deve colocar obstáculos nas coordenadas recebidas no 2o parâmetro do construtor
     # a sujeira deve ser atualizada no método step() pois, mesmo quando o agente limpa,
     # a sujeira deverá reaparecer com certa probabilidade

    def step(self):  # atualiza sujeira, realiza a interação do agente-ambiente

        for x in range(len(self.piso)):
            for y in range(len(self.piso[0])):
                probabilidade = uniform(0, 1)
                if (self.pos_aspirador == self.pos_base):
                    self.piso[self.pos_aspirador[0]][self.pos_aspirador[1]] = 3
                elif (self.pos_aspirador != self.pos_base):
                    self.piso[self.pos_base[0]][self.pos_base[1]] = 4
                
                if (self.piso[x][y] == 0):
                    if((x, y) in self.hot_spots_sujeira):
                        if(probabilidade < 0.1):
                            self.piso[x][y] = self.sujeira
                            #print(probabilidade)
                    else:
                        if(probabilidade < 0.01):
                            self.piso[x][y] = self.sujeira
                            #print(probabilidade)
        
        print(self.piso)
        print("Energia atual:", self.aspirador.get_energia())
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

    def __init__(self, energia_aspirador, M, N):
        self.energia = energia_aspirador
        self.actions = ["norte", "oeste", "leste",
                        "sul", "aspirar", "recarregar"]
        # diz respeito à celula imediatamente à frente do agente se obstáculo
        self.status_percepção = ["sujo", "vazio", "obstaculo"]

      # consulta o ambiente para obter as coordenadas
        # registra as experiências do robô.
        self.modelo_ambiente = np.array([M, N], int)
      # no modelo é guardado: contador de sujeira (0...MAX) ou obstáculo (-1)

   # definida a partir do contador de sujeira e da posição atual.
    # avaliação_heurística = np.array([dimX, dimY], int)
    def update_posição(self, nova_posicao):
        print("aaaaa")

    def action_agent_program(self, percepção):
        print("teste")
       # realizar busca heurística usando a avaliação heurística, o modelo do ambiente e a percepção corrente.
       # considerar que ele deve retornar à base quando a bateria estiver crítica

    def print_status():  # imprime posição do agente, o seu modelo interno do ambiente, nível da bateria
        print("asd")

    def get_energia(self):
        return self.energia


# Código de teste
######################
# criar aspirador com 100% de energia

def main():
    """Função principal da aplicação.
    """
    M = 4
    N = 4
    meu_aspirador = Aspirador(100, M, N)

    # cria o ambiente contendo o meu aspirador
    ambiente = Sala((M, N), [(1, 2), (2, 1)], [
                    (2, 2), (1, 1)], meu_aspirador, (0, 0), (0, 0))
    # simula 10 passos do ambiente
    ambiente.run(10)


if __name__ == "__main__":
    main()

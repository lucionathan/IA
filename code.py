import numpy as np

class Sala:

    def __init__(self, size, lista_obstáculos, hot_spots_sujeira, aspirador, posicao_aspirador, posicao_base_recarregamento):
        self.vazio = 0
        self.obstáculo = 1
        self.sujeira = 2
        self.aspirador = aspirador
        self.piso = np.array([size[0], size[1]], int).fill(0)
        
        # for x in range(len(self.piso)):
        #     for y in range(len(self.piso[0])):
        print("asd")

        self.hot_spots_sujeira  = hot_spots_sujeira   # onde há sujeira 
        self.pos_aspirador = posicao_aspirador
        self.pos_base = posicao_base_recarregamento

    # Escreva seu código aqui levando em conta que: 
     # o piso recebe valor vazio em todo lugar e 
     # você deve colocar obstáculos nas coordenadas recebidas no 2o parâmetro do construtor
     # a sujeira deve ser atualizada no método step() pois, mesmo quando o agente limpa,
     # a sujeira deverá reaparecer com certa probabilidade

    def step(self): # atualiza sujeira, realiza a interação do agente-ambiente

        print("abubleble") 
     # Escreva seu código aqui levando em conta o pseudo-código para 
     # adicionar sujeira com maior probabilidade em certos locais:
    
     #atualização da sujeira 
     #for i até dim M
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

    def run(self, N):
        print("asd") #chama step N vezes para simular o agente e o seu ambiente

class Aspirador:

    def __init__(self, energia_aspirador, M, N):
        self.energia = energia_aspirador
        self.actions = ["frente", "esq", "dir", "tras", "aspirar", "recarregar"]
        self.status_percepção = ["sujo", "vazio", "obstaculo"] #diz respeito à celula imediatamente à frente do agente se obstáculo

      #consulta o ambiente para obter as coordenadas
        self.modelo_ambiente = np.array([M, N], int)      # registra as experiências do robô.
      # no modelo é guardado: contador de sujeira (0...MAX) ou obstáculo (-1)

   # definida a partir do contador de sujeira e da posição atual. 
    # avaliação_heurística = np.array([dimX, dimY], int)
    def update_posição(self, nova_posicao):
        print("aaaaa")
    def action_agent_program(self, percepção):
        print("teste")
       # realizar busca heurística usando a avaliação heurística, o modelo do ambiente e a percepção corrente.
       # considerar que ele deve retornar à base quando a bateria estiver crítica
  
    def print_status(): #imprime posição do agente, o seu modelo interno do ambiente, nível da bateria
        print("asd")


# Código de teste
######################
#criar aspirador com 100% de energia

def main():
    """Função principal da aplicação.
    """
    M=10
    N=10
    meu_aspirador = Aspirador(100, M,N)

    #cria o ambiente contendo o meu aspirador
    ambiente  = Sala((M,N), [(5,5),(5,4),(5,3)],[(2,2),(3,3)], meu_aspirador, (0,0), (0,0))

    #sumila 100 passos do ambiente
    ambiente.run(100)


if __name__ == "__main__":
    main()

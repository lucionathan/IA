# IA

Nesta atividade, implemente um Notebook no Google Colaboratory com uma estrategia de busca em um grid MxN, com um agente Aspirador de pó em um ambiente que possui obstáculos e que aspira a sujeira do ambiente ao encontrá-la. Este agente precisará manter um modelo do ambiente, internamente, com o propósito de acumular evidências (a partir de seus sensores) da presença de obstáculos fixos e da frequência de ocorrência de sujeira. O robô tem uma bateria que começa com 100% de carga, mas que descarrega 1% a cada movimento (esquerda, direita etc) e 5% a cada ação de aspirar a sujeira.

Ambiente: uma sala MxN, que deverá conter o agente aspirador (o construtor da classe "Sala" recebe este agente), além das coordenados 2D do agente e da base de recarrecamento.

Ações: mover para esquerda, mover para trás, mover para direita, ir em frente e aspirar a sujeira, recarregar bateria (que ocorre em um único passo de simulação).

Considerações: O Agente tem energia para percorrer um certo número de quadrados e toma a decisão para voltar a base para recarregar de modo a evitar que a energia acabe antes de chegar à base.

Objetivos: O agente deverá otimizar uma medida de desempenho que envolva: aspirar a maior quantidade de sujeira enquanto evita descarregar a bateria distante da base. Isto implicará que, enquanto a carga da bateria for suficiente, estará buscando encontrar sujeira nos locais mais prováveis (a partir do modelo interno do ambiente e de uma avaliação heurística), mas quando a bateria começar a atingir um nível crítico (que inviabilizaria o retorno à base) o agente deverá buscar retornar à base para recarregar a bateria. A base é de recarregamento rápido, e um único passo de simulação do ambiente deverá ser necessário para que o agente tenha sua bateria recarregada.

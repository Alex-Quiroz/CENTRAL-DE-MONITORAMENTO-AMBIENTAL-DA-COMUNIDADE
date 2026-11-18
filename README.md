# CENTRAL-DE-MONITORAMENTO-AMBIENTAL-DA-COMUNIDADE

# Integrantes
Alexander Josue Quiroz Cocarico    RM: 571948

# Ambiente escolhido
O ambiente monitorado é uma escola, com foco em salas de aula, onde o conforto térmico, a qualidade do ar e o nível de ruído influenciam diretamente a saúde, a concentração e o aprendizado dos estudantes e o trabalho dos professores.

# Objetivo da solução
Simular uma central de monitoramento que:

1. Recebe uma sequência de leituras informadas pelo usuário (temperatura, PM2,5 e ruído);
2. Emite alertas quando uma leitura ultrapassa os limites de referência;
3. Calcula média, mínimo e máximo de cada parâmetro;
4. Conta as ocorrências críticas por parâmetro e as leituras com pelo menos um parâmetro crítico, com o respectivo percentual;
5. Classifica o estado geral do ambiente;
6. Salva um relatório em .txt e informa o nome do arquivo gerado;
7. Permite iniciar uma nova sequência, reiniciando dados e contadores

# Limites de referência adotados
# Temperatura
Limite adotado: 18,0 a 25,0 °C<br>
Fonte de referência: https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-partitaria-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-17-nr-17 <br>
Justificativa: Para ambientes climatizados com atividades intelectuais (como salas de aula), a norma atualizada determina que a temperatura do ar seja mantida entre 18°C e 25°C

# PM2.5
Limite adotado: 25 µg/m³ (média de 24 horas)
Fonte de referência: ABNT NBR 17037
Justificativa: Para o ambiente interno de uma escola no Brasil, o limite legal de referência para partículas finas (PM2,5) é de até 25 µg/m³ (média de 24 horas). Esse parâmetro é estabelecido pela norma ABNT NBR 17037

# Ruido
Limite adotado: 40 dB
Fonte de referência: ABNT NBR 10152:2017
Justificativa: Conforme os parâmetros de referência estabelecidos pela ABNT NBR 10152:2017 e pelas diretrizes da Organização Mundial da Saúde (OMS), o ruído de fundo em salas de aula deve situar-se entre 35 dB e 40 dB

# Instruções para executar o programa
1. Salve o código em um arquivo, por exemplo monitoramento.py
2. Abra o terminal na pasta do arquivo.
3. Execute: python monitoramento.py
4. Siga as instruções na tela:
* Informe a quantidade de leituras (deve ser maior que zero);<br>
* Para cada leitura, informe temperatura (°C), PM2.5 (µg/m³) e ruído (dB);<br>
* Ao final, o programa exibe os resultados e gera o relatório;<br>
* Responda S para iniciar uma nova sequência ou N para encerrar.

# Saida
O relatório é salvo na pasta de execução, com o nome relatorio_escola.txt. Ele contém: identificação do ambiente, quantidade de leituras, limites e unidades, média/mínimo/máximo, ocorrências críticas por parâmetro, quantidade e percentual de leituras críticas, classificação geral e a observação de que se trata de uma simulação.

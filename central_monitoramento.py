# Central de monitoramento

# Limite para temperatura, PM e ruído
TEMP_MINLIMITE: float = 18.0
TEMP_MAXLIMITE: float = 25.0
PM_LIMITE: float = 25.0
RUIDO_LIMITE: float = 40.0

# Dicionario para armazenar os dados de monitoramento
dados = {
    "Temperatura": [],
    "PM25": [],
    "Ruido": []
}
  
# Função para calcular a média, minimo e máximo
def calcular_estatisticas(valores):
    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)
    return media, menor, maior

# Programa principal
while True:
    # Quantidade de leituras (maior que zero)
    print("=========================================")
    quant_leituras = int(input("Digite a quantidade de leituras: "))
    while quant_leituras <= 0:
        print("\nQuantidade de leituras inválida. Digite um valor maior que zero.")
        quant_leituras = int(input("Digite a quantidade de leituras: "))

    leituras_criticas = 0
    # Leitura de valores
    for i in range(quant_leituras):
        print("\nLeitura", i + 1)
        temperatura = float(input("Digite a temperatura (°C): "))
        pm = float(input("Digite o valor de PM2.5 - média de 24 horas (µg/m³): "))
        ruido = float(input("Digite o nível de ruído (dB): "))
        print("\n")

        # Verificação dos limites
        alerta = False
        if temperatura < TEMP_MINLIMITE or temperatura > TEMP_MAXLIMITE:
            print("ALERTA: Temperatura fora do limite!")
            alerta = True
        if pm > PM_LIMITE:
            print("ALERTA: Valor de PM2,5 acima do limite!")
            alerta = True
        if ruido > RUIDO_LIMITE:
            print("ALERTA: Nível de ruído adcima do limite!")
            alerta = True

        if alerta:
            leituras_criticas += 1  # conta a leitura uma única vez
        else:
            print("Leitura dentro dos limites de referência estabelecidos")

        # Armazenamento dos dados
        dados["Temperatura"].append(temperatura)
        dados["PM25"].append(pm)
        dados["Ruido"].append(ruido)

    # Calculos Estátisticos
    print("=========================================")
    print("Calculos Estatísticos")
    
    # Média, Mínimo e Máximo dos valores de cada parâmetro
    print("\nMédia, Mínimo e Máximo")
    for parametro, valores in dados.items():
        media, menor, maior = calcular_estatisticas(valores)
        print(f"{parametro}:")
        print(f"  - Mínimo: {menor}")
        print(f"  - Máximo: {maior}")
        print(f"  - Média: {media}")

    print("\nQuantidade de ocorrências críticas de cada parâmetro:")
    for parametro, valores in dados.items():
        criticas = 0
        for v in valores:
            if parametro == "Temperatura":
                if v < TEMP_MINLIMITE or v > TEMP_MAXLIMITE:
                    criticas += 1
            elif parametro == "PM25":
                if v > PM_LIMITE:
                    criticas += 1
            elif parametro == "Ruido" and v > RUIDO_LIMITE:
                criticas += 1
        print(f"  - {parametro}: {criticas}")

    print("\nQuantidade de leituras com pelo menos um parâmetro crítico:")
    print(f"  - Total: {leituras_criticas}")

    #Percentual de leituras críticas
    print("\nPercentual de leituras críticas em relação ao total de leituras:")
    percentual = (leituras_criticas / quant_leituras) * 100 
    print(f"  - Percentual: {percentual:.2f}%")
    print("=========================================")

    # Classificação baseado nas percentagem
    print("Classificação das leituras")
    if(percentual > 30):
        print("Estado geral: condições ambientais de atenção, com frequência de ocorrências acima do critério estabelecido")
    else:
        print("Estado geral: frequência de ocorrências dentro do critério estabelecido para a simulação")

    # Ocorrências críticas por parâmetro (recalculadas para o relatório)
    criticas_temp = 0
    for v in dados["Temperatura"]:
        if v < TEMP_MINLIMITE or v > TEMP_MAXLIMITE:
            criticas_temp += 1

    criticas_pm = 0
    for v in dados["PM25"]:
        if v > PM_LIMITE:
            criticas_pm += 1

    criticas_ruido = 0
    for v in dados["Ruido"]:
        if v > RUIDO_LIMITE:
            criticas_ruido += 1

    # Classificação geral (mesmo critério usado na tela)
    if percentual > 30:
        classificacao = "Condições ambientais de atenção, com frequência de ocorrências acima do critério estabelecido"
    else:
        classificacao = "Frequência de ocorrências dentro do critério estabelecido para a simulação"

# Geração do relatório em Txt
    AMBIENTE = "Escola"
    nome_arquivo = "relatorio_escola.txt"

    linhas = []
    linhas.append("=========================================")
    linhas.append("RELATÓRIO DE MONITORAMENTO AMBIENTAL")
    linhas.append("=========================================")
    linhas.append(f"Ambiente monitorado: {AMBIENTE}")
    linhas.append(f"Quantidade de leituras: {quant_leituras}")

    linhas.append("\nLimites de referência e unidades:")
    linhas.append(f"  - Temperatura: {TEMP_MINLIMITE} a {TEMP_MAXLIMITE} °C")
    linhas.append(f"  - PM2.5: até {PM_LIMITE} µg/m³ (média de 24 h; cada leitura representa a média de 24 h)")
    linhas.append(f"  - Ruído: até {RUIDO_LIMITE} dB")

    linhas.append("\nMédia, mínimo e máximo:")
    unidades = {"Temperatura": "°C", "PM25": "µg/m³", "Ruido": "dB"}
    for parametro, valores in dados.items():
        media, menor, maior = calcular_estatisticas(valores)
        un = unidades[parametro]
        linhas.append(f"{parametro}:")
        linhas.append(f"  - Mínimo: {menor} {un}")
        linhas.append(f"  - Máximo: {maior} {un}")
        linhas.append(f"  - Média: {media:.2f} {un}")

    linhas.append("\nOcorrências críticas por parâmetro:")
    linhas.append(f"  - Temperatura: {criticas_temp}")
    linhas.append(f"  - PM25: {criticas_pm}")
    linhas.append(f"  - Ruido: {criticas_ruido}")

    linhas.append("\nLeituras com pelo menos um parâmetro crítico:")
    linhas.append(f"  - Quantidade: {leituras_criticas}")
    linhas.append(f"  - Percentual: {percentual:.2f}%")

    linhas.append("\nClassificação geral:")
    linhas.append(f"  {classificacao}")

    linhas.append("\nObservação: este resultado se refere a uma simulação baseada nos critérios adotados.")
    linhas.append("=========================================")

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("\n".join(linhas))

    print(f"\nRelatório salvo no arquivo: {nome_arquivo}")

    # Continuidade do programa
    resposta = input("\nDeseja realizar uma nova sequência de leituras? (S/N): ").strip().upper()
    while resposta !="S" and resposta != "N":
        print("\nResposta inválida. Digite 'S' para sim ou 'N' para não.")
        resposta = input("Deseja realizar uma nova sequência de leituras? (S/N): ").strip().upper()

    if resposta == "S":
        # Reinício dos dados
        for parametro in dados:
            dados[parametro] = []
        print("\nDados reiniciados. Iniciando nova sequência...\n")
    else:
        print("\nExecução encerrada. Obrigado por utilizar a Central de Monitoramento!")
        break
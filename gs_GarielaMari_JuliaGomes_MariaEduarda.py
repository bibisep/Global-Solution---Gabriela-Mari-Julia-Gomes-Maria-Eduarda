print("=" * 50)
print("SISTEMA DE MONITORAMENTO AMBIENTAL POR SATÉLITE")
print("=" * 50)

# Listas solicitadas no enunciado
tipos_eventos = []
paises = []
regioes = []
cidades = []
areas_afetadas = []
intensidades = []
ocorrencias = []

# Entrada da quantidade de eventos com validação
quantidade_eventos = 0

while quantidade_eventos <= 0:
    try:
        quantidade_eventos = int(input("Insira a quantidade de eventos registrados: "))

        if quantidade_eventos <= 0:
            print("Erro: a quantidade de eventos deve ser maior que zero.")

    except ValueError:
        print("Erro: digite um número inteiro válido.")
        quantidade_eventos = 0

# Coleta dos dados de cada evento
for i in range(quantidade_eventos):
    print("\n--- Evento", i + 1, "---")

    tipo = ""
    while tipo.strip() == "":
        tipo = input("Tipo de evento (ex: desmatamento, queimadas, variação climática): ")

        if tipo.strip() == "":
            print("Erro: o tipo de evento não pode ficar vazio.")

    pais = ""
    while pais.strip() == "":
        pais = input("País: ")

        if pais.strip() == "":
            print("Erro: o país não pode ficar vazio.")

    regiao = ""
    while regiao.strip() == "":
        regiao = input("Região: ")

        if regiao.strip() == "":
            print("Erro: a região não pode ficar vazia.")

    cidade = ""
    while cidade.strip() == "":
        cidade = input("Cidade: ")

        if cidade.strip() == "":
            print("Erro: a cidade não pode ficar vazia.")

    area = -1
    while area <= 0:
        try:
            area = float(input("Área afetada em km²: "))

            if area <= 0:
                print("Erro: a área afetada deve ser maior que zero.")

        except ValueError:
            print("Erro: digite um número válido para a área.")
            area = -1

    intensidade = 0
    while intensidade < 1 or intensidade > 10:
        try:
            intensidade = int(input("Intensidade do impacto (1 a 10): "))

            if intensidade < 1 or intensidade > 10:
                print("Erro: a intensidade deve estar entre 1 e 10.")

        except ValueError:
            print("Erro: digite um número inteiro entre 1 e 10.")
            intensidade = 0

    # CORRIGIDO: ocorrência deve ser maior que zero (não apenas >= 0)
    ocorrencia = -1
    while ocorrencia <= 0:
        try:
            ocorrencia = int(input("Número de ocorrências detectadas: "))

            if ocorrencia <= 0:
                print("Erro: o número de ocorrências deve ser maior que zero.")

        except ValueError:
            print("Erro: digite um número inteiro válido.")
            ocorrencia = -1

    # Armazenamento em listas
    tipos_eventos.append(tipo)
    paises.append(pais)
    regioes.append(regiao)
    cidades.append(cidade)
    areas_afetadas.append(area)
    intensidades.append(intensidade)
    ocorrencias.append(ocorrencia)

# Análise dos dados
total_eventos = quantidade_eventos
area_total = 0
soma_intensidades = 0
soma_densidades = 0

for i in range(total_eventos):
    area_total = area_total + areas_afetadas[i]
    soma_intensidades = soma_intensidades + intensidades[i]
    soma_densidades = soma_densidades + (ocorrencias[i] / areas_afetadas[i])

media_intensidade = soma_intensidades / total_eventos
densidade_media = soma_densidades / total_eventos

# Evento com maior área afetada
maior_area = max(areas_afetadas)
indice_maior_area = areas_afetadas.index(maior_area)

# Região com maior número de ocorrências
maior_ocorrencia = max(ocorrencias)
indice_maior_ocorrencia = ocorrencias.index(maior_ocorrencia)

# Quantidade de eventos acima da média de intensidade
eventos_acima_media = 0

for i in range(total_eventos):
    if intensidades[i] > media_intensidade:
        eventos_acima_media = eventos_acima_media + 1

# Evento mais crítico: 1º maior intensidade, 2º maior área em caso de empate
indice_critico = 0

for i in range(1, total_eventos):
    if intensidades[i] > intensidades[indice_critico]:
        indice_critico = i

    elif intensidades[i] == intensidades[indice_critico] and areas_afetadas[i] > areas_afetadas[indice_critico]:
        indice_critico = i

# Relatório final
print("\n" + "=" * 50)
print("RELATÓRIO DE ANÁLISE")
print("=" * 50)

print("Total de eventos registrados:", total_eventos)

print("-" * 50)
print("Resumo Geral")
print("-" * 50)
print("Área total afetada:", round(area_total, 2), "km²")
print("Média de intensidade:", round(media_intensidade, 2))

print("-" * 50)
print("Análises")
print("-" * 50)
print("Evento com maior área afetada:", tipos_eventos[indice_maior_area])
print("Local do evento com maior área:",
      cidades[indice_maior_area] + ", " + regioes[indice_maior_area] + ", " + paises[indice_maior_area])
print("Área do maior evento:", round(areas_afetadas[indice_maior_area], 2), "km²")
print("Região com maior número de ocorrências:", regioes[indice_maior_ocorrencia])
print("Número de ocorrências nessa região:", ocorrencias[indice_maior_ocorrencia])
print("Quantidade de eventos acima da média de intensidade:", eventos_acima_media)
print("Densidade média de ocorrências:", round(densidade_media, 2), "ocorrências/km²")

print("-" * 50)
print("Evento Mais Crítico")
print("-" * 50)
print("Tipo:", tipos_eventos[indice_critico])
print("Local:", cidades[indice_critico] + ", " + regioes[indice_critico] + ", " + paises[indice_critico])
print("Intensidade:", intensidades[indice_critico])
print("Área afetada:", round(areas_afetadas[indice_critico], 2), "km²")
print("Ocorrências:", ocorrencias[indice_critico])

print("=" * 50)
print("Total de desastres registrados:", total_eventos)
print("=" * 50)
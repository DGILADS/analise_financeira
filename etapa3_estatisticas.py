"""
=============================================================
SISTEMA DE ANÁLISE DE DADOS FINANCEIROS
Etapa 3 – Estatísticas com Bibliotecas + Remoção de Outliers
=============================================================
Objetivo:
  Ler o arquivo tratado (Etapa 2), calcular estatísticas
  usando bibliotecas prontas (statistics, math), exibir
  cada métrica com explicação didática e, em seguida,
  remover outliers MANUALMENTE e salvar o resultado final.

Conceitos utilizados:
  - Biblioteca statistics (média, mediana, variância, desvio)
  - Biblioteca math (raiz quadrada)
  - List e append()
  - Laços for e acumuladores (para remoção de outliers)
  - Condicionais if/elif/else
  - with open() para arquivos
  - Tratamento de exceções try/except
  - if __name__ == "__main__"
=============================================================
"""

import statistics  # Biblioteca padrão para cálculos estatísticos
import math        # Biblioteca matemática (usada para referência)

# Arquivos utilizados nesta etapa
ARQUIVO_ENTRADA  = "dados_corrigidos.txt"  # Gerado pela Etapa 2
ARQUIVO_SAIDA    = "dados_sem_outliers.txt"  # Gerado por esta etapa


# ─────────────────────────────────────────────────────────────
# FUNÇÕES DE LEITURA E ESCRITA
# ─────────────────────────────────────────────────────────────

def ler_arquivo(nome_arquivo: str) -> list:
    """
    Lê um arquivo texto e retorna uma lista de inteiros.
    Cada linha deve conter um único número inteiro.
    """
    lista = []

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    try:
                        numero = int(linha)
                        lista.append(numero)
                    except ValueError:
                        print(f"  ✘ Linha inválida ignorada: '{linha}'")

        print(f"✔ {len(lista)} registro(s) lido(s) de '{nome_arquivo}'.")
    except FileNotFoundError:
        print(f"✘ Arquivo '{nome_arquivo}' não encontrado.")
        print("  Execute primeiro a Etapa 2 (etapa2_processamento.py).")

    return lista


def salvar_arquivo(lista: list, nome_arquivo: str) -> None:
    """
    Salva uma lista de inteiros em arquivo texto (um por linha).
    """
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for numero in lista:
                arquivo.write(str(numero) + "\n")
        print(f"✔ Arquivo salvo: '{nome_arquivo}' ({len(lista)} registro(s)).")
    except IOError as erro:
        print(f"✘ Erro ao salvar arquivo: {erro}")


# ─────────────────────────────────────────────────────────────
# ETAPA 3 – CÁLCULO COM BIBLIOTECAS
# ─────────────────────────────────────────────────────────────

def calcular_e_exibir_estatisticas(lista: list) -> None:
    """
    Calcula e exibe estatísticas completas usando a biblioteca
    'statistics'. Cada métrica inclui comentário explicativo.

    Parâmetros:
        lista (list): lista de inteiros para análise.
    """
    if len(lista) == 0:
        print("Lista vazia. Impossível calcular estatísticas.")
        return

    # ── Média ──────────────────────────────────────────────────
    # Soma de todos os valores dividida pela quantidade de elementos.
    # Representa o valor "central" típico do conjunto de dados.
    media = statistics.mean(lista)

    # ── Mediana ────────────────────────────────────────────────
    # Valor que divide o conjunto ordenado ao meio (50% abaixo, 50% acima).
    # Menos sensível a valores extremos do que a média.
    mediana = statistics.median(lista)

    # ── Máximo ─────────────────────────────────────────────────
    # O maior valor presente no conjunto de dados.
    # Indica o limite superior dos dados observados.
    maximo = max(lista)

    # ── Mínimo ─────────────────────────────────────────────────
    # O menor valor presente no conjunto de dados.
    # Indica o limite inferior dos dados observados.
    minimo = min(lista)

    # ── Amplitude ──────────────────────────────────────────────
    # Diferença entre o maior e o menor valor (max - min).
    # Mede a dispersão total dos dados; quanto maior, mais espalhados.
    amplitude = maximo - minimo

    # ── Variância ──────────────────────────────────────────────
    # Média dos quadrados dos desvios em relação à média.
    # Mede o quanto os valores se afastam da média (em unidades²).
    variancia = statistics.variance(lista)

    # ── Desvio Padrão ──────────────────────────────────────────
    # Raiz quadrada da variância; mede a dispersão na mesma unidade dos dados.
    # Valores próximos de zero indicam dados concentrados em torno da média.
    desvio_padrao = statistics.stdev(lista)

    # ── Primeiros e Últimos 5 valores ──────────────────────────
    # Permitem inspecionar o início e o fim do vetor de dados.
    # Útil para verificar a ordem e a distribuição dos extremos.
    primeiros_5 = lista[:5]
    ultimos_5   = lista[-5:]

    # Exibe todos os resultados formatados
    print("\n" + "=" * 60)
    print("  ESTATÍSTICAS COMPLETAS (com bibliotecas)")
    print("=" * 60)
    print(f"  Média          : {media:.2f}")
    print(f"  Mediana        : {mediana:.2f}")
    print(f"  Máximo         : {maximo}")
    print(f"  Mínimo         : {minimo}")
    print(f"  Amplitude      : {amplitude}")
    print(f"  Variância      : {variancia:.2f}")
    print(f"  Desvio Padrão  : {desvio_padrao:.2f}")
    print(f"  Primeiros 5    : {primeiros_5}")
    print(f"  Últimos 5      : {ultimos_5}")
    print("=" * 60)


# ─────────────────────────────────────────────────────────────
# ETAPA 4 – REMOÇÃO DE OUTLIERS (SEM funções prontas)
# ─────────────────────────────────────────────────────────────

def calcular_media_manual(lista: list) -> float:
    """
    Calcula a média MANUALMENTE usando acumulador e laço for.
    Não utiliza sum(), statistics.mean() ou qualquer função pronta.
    """
    soma = 0
    contagem = 0

    for valor in lista:
        soma = soma + valor
        contagem = contagem + 1

    if contagem == 0:
        return 0.0

    return soma / contagem


def calcular_desvio_padrao_manual(lista: list, media: float) -> float:
    """
    Calcula o desvio padrão MANUALMENTE usando acumulador.
    Fórmula: sqrt( soma((xi - média)²) / (n - 1) )
    Não utiliza statistics.stdev() ou qualquer função pronta.
    """
    n = len(lista)

    if n < 2:
        return 0.0

    soma_quadrados = 0.0

    for valor in lista:
        diferenca = valor - media
        soma_quadrados = soma_quadrados + (diferenca * diferenca)

    variancia = soma_quadrados / (n - 1)

    # Calcula a raiz quadrada manualmente usando o método de Newton
    # (equivalente ao math.sqrt, mas implementado sem biblioteca)
    if variancia == 0:
        return 0.0

    # Método de Newton-Raphson para raiz quadrada
    estimativa = variancia
    for _ in range(50):  # 50 iterações garantem precisão suficiente
        estimativa = (estimativa + variancia / estimativa) / 2

    return estimativa


def remover_outliers(lista: list) -> list:
    """
    Remove outliers MANUALMENTE, sem usar funções prontas.

    Critério:
      - Outlier superior: valor > média + 2 * desvio_padrão
      - Outlier inferior: valor < média - 2 * desvio_padrão

    Parâmetros:
        lista (list): lista de inteiros.

    Retorna:
        lista_filtrada (list): lista sem os outliers.
    """
    if len(lista) == 0:
        return []

    # Calcula média e desvio padrão manualmente
    media        = calcular_media_manual(lista)
    desvio       = calcular_desvio_padrao_manual(lista, media)

    # Define os limites para identificar outliers
    limite_superior = media + 2 * desvio
    limite_inferior = media - 2 * desvio

    print(f"\n  Média          : {media:.2f}")
    print(f"  Desvio Padrão  : {desvio:.2f}")
    print(f"  Limite superior: {limite_superior:.2f}")
    print(f"  Limite inferior: {limite_inferior:.2f}")

    lista_filtrada = []
    removidos = 0

    # Percorre a lista e mantém apenas os valores dentro dos limites
    for valor in lista:
        if valor > limite_superior or valor < limite_inferior:
            # Valor é outlier – será descartado
            print(f"  ⚠ Outlier removido: {valor}")
            removidos = removidos + 1
        else:
            lista_filtrada.append(valor)

    print(f"\n  Total removido : {removidos} outlier(s)")
    print(f"  Registros finais: {len(lista_filtrada)}")

    return lista_filtrada


# ─────────────────────────────────────────────────────────────
# Ponto de entrada principal do programa
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 60)
    print("  ETAPA 3 – Estatísticas com Bibliotecas")
    print("=" * 60)

    # 1. Lê o arquivo tratado gerado na Etapa 2
    dados = ler_arquivo(ARQUIVO_ENTRADA)

    if len(dados) == 0:
        print("Nenhum dado disponível. Encerrando.")
    else:
        # 2. Calcula e exibe estatísticas completas com bibliotecas
        calcular_e_exibir_estatisticas(dados)

        # ─────────────────────────────────────────────────────
        print("\n" + "=" * 60)
        print("  ETAPA 4 – Remoção de Outliers (cálculo manual)")
        print("=" * 60)

        # 3. Remove outliers manualmente (sem funções prontas)
        dados_sem_outliers = remover_outliers(dados)

        # 4. Exibe o vetor final
        print(f"\n  Vetor final (sem outliers):")
        print(f"  {dados_sem_outliers}")

        # 5. Salva o resultado final em novo arquivo
        print()
        salvar_arquivo(dados_sem_outliers, ARQUIVO_SAIDA)

    print("\nSistema de análise financeira concluído com sucesso!\n")

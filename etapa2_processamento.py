"""
=============================================================
SISTEMA DE ANÁLISE DE DADOS FINANCEIROS
Etapa 2 – Processamento Manual (SEM funções prontas)
=============================================================
Objetivo:
  Ler o arquivo gerado na Etapa 1, calcular estatísticas
  MANUALMENTE (sem min(), max(), sum(), statistics etc.),
  substituir valores inválidos (≤ 0) pela média e salvar
  o vetor corrigido em novo arquivo.

Conceitos utilizados:
  - List e append()
  - Laços for e acumuladores manuais
  - Condicionais if/elif/else
  - Manipulação de arquivos com with open()
  - Tratamento de exceções try/except
  - if __name__ == "__main__"
=============================================================
"""

# Arquivos utilizados nesta etapa
ARQUIVO_ENTRADA = "dados_acoes.txt"       # Gerado pela Etapa 1
ARQUIVO_SAIDA   = "dados_corrigidos.txt"  # Gerado por esta etapa


# ─────────────────────────────────────────────────────────────
# FUNÇÕES DE LEITURA E ESCRITA
# ─────────────────────────────────────────────────────────────

def ler_arquivo(nome_arquivo: str) -> list:
    """
    Lê um arquivo texto e retorna uma lista de inteiros.
    Cada linha do arquivo deve conter um único número inteiro.

    Parâmetros:
        nome_arquivo (str): caminho do arquivo a ser lido.

    Retorna:
        lista (list): lista de inteiros lidos do arquivo.
    """
    lista = []  # Lista que receberá os valores lidos

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()  # Remove espaços e quebras de linha
                if linha:              # Ignora linhas vazias
                    try:
                        numero = int(linha)
                        lista.append(numero)  # Adiciona usando append()
                    except ValueError:
                        print(f"  ✘ Linha inválida ignorada: '{linha}'")

        print(f"✔ {len(lista)} registro(s) lido(s) de '{nome_arquivo}'.")
    except FileNotFoundError:
        print(f"✘ Arquivo '{nome_arquivo}' não encontrado.")
        print("  Execute primeiro a Etapa 1 (etapa1_coleta.py).")

    return lista


def salvar_arquivo(lista: list, nome_arquivo: str) -> None:
    """
    Salva uma lista de inteiros em arquivo texto (um por linha).

    Parâmetros:
        lista        (list): lista de inteiros a salvar.
        nome_arquivo (str) : caminho do arquivo de saída.
    """
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for numero in lista:
                arquivo.write(str(numero) + "\n")
        print(f"✔ Vetor corrigido salvo em '{nome_arquivo}'.")
    except IOError as erro:
        print(f"✘ Erro ao salvar arquivo: {erro}")


# ─────────────────────────────────────────────────────────────
# FUNÇÕES DE CÁLCULO MANUAL (SEM funções prontas)
# ─────────────────────────────────────────────────────────────

def calcular_media_manual(lista: list) -> float:
    """
    Calcula a média aritmética MANUALMENTE usando acumulador.
    Considera apenas valores válidos (> 0).

    Parâmetros:
        lista (list): lista de inteiros.

    Retorna:
        media (float): média dos valores válidos, ou 0.0 se vazia.
    """
    soma = 0       # Acumulador da soma
    contagem = 0   # Contador de valores válidos

    for valor in lista:
        if valor > 0:          # Apenas valores válidos
            soma = soma + valor
            contagem = contagem + 1

    if contagem == 0:
        return 0.0

    media = soma / contagem
    return media


def calcular_maximo_manual(lista: list) -> int:
    """
    Encontra o valor máximo MANUALMENTE, sem usar max().
    Considera apenas valores válidos (> 0).

    Parâmetros:
        lista (list): lista de inteiros.

    Retorna:
        maximo (int): maior valor encontrado.
    """
    maximo = None  # Inicializa sem valor

    for valor in lista:
        if valor > 0:  # Apenas valores válidos
            if maximo is None or valor > maximo:
                maximo = valor

    return maximo if maximo is not None else 0


def calcular_minimo_manual(lista: list) -> int:
    """
    Encontra o valor mínimo MANUALMENTE, sem usar min().
    Considera apenas valores válidos (> 0).

    Parâmetros:
        lista (list): lista de inteiros.

    Retorna:
        minimo (int): menor valor encontrado.
    """
    minimo = None  # Inicializa sem valor

    for valor in lista:
        if valor > 0:  # Apenas valores válidos
            if minimo is None or valor < minimo:
                minimo = valor

    return minimo if minimo is not None else 0


def obter_primeiros(lista: list, quantidade: int = 5) -> list:
    """
    Retorna os primeiros N valores da lista MANUALMENTE.
    Não usa slicing avançado — percorre com índice.

    Parâmetros:
        lista     (list): lista de inteiros.
        quantidade (int): quantos valores retornar (padrão: 5).

    Retorna:
        primeiros (list): lista com os primeiros N valores.
    """
    primeiros = []
    indice = 0

    for valor in lista:
        if indice >= quantidade:
            break
        primeiros.append(valor)
        indice = indice + 1

    return primeiros


def obter_ultimos(lista: list, quantidade: int = 5) -> list:
    """
    Retorna os últimos N valores da lista MANUALMENTE.
    Percorre a lista calculando o índice de início.

    Parâmetros:
        lista     (list): lista de inteiros.
        quantidade (int): quantos valores retornar (padrão: 5).

    Retorna:
        ultimos (list): lista com os últimos N valores.
    """
    ultimos = []
    total = len(lista)

    # Calcula o índice de início para os últimos N elementos
    inicio = total - quantidade
    if inicio < 0:
        inicio = 0

    indice = 0
    for valor in lista:
        if indice >= inicio:
            ultimos.append(valor)
        indice = indice + 1

    return ultimos


# ─────────────────────────────────────────────────────────────
# FUNÇÃO DE SUBSTITUIÇÃO DE VALORES INVÁLIDOS
# ─────────────────────────────────────────────────────────────

def substituir_invalidos(lista_original: list, media: float) -> list:
    """
    Substitui valores inválidos (≤ 0) pela média calculada.
    A média deve ter sido calculada APENAS com valores válidos.

    Parâmetros:
        lista_original (list) : lista com possíveis valores inválidos.
        media          (float): média dos valores válidos.

    Retorna:
        lista_corrigida (list): lista com inválidos substituídos.
    """
    lista_corrigida = []
    substituicoes = 0

    for valor in lista_original:
        if valor <= 0:
            # Substitui valor inválido pela média (convertida para int)
            lista_corrigida.append(int(media))
            substituicoes = substituicoes + 1
        else:
            lista_corrigida.append(valor)

    if substituicoes > 0:
        print(f"  ⚠ {substituicoes} valor(es) inválido(s) substituído(s) pela média ({int(media)}).")
    else:
        print("  ✔ Nenhum valor inválido encontrado.")

    return lista_corrigida


# ─────────────────────────────────────────────────────────────
# FUNÇÃO DE EXIBIÇÃO DOS RESULTADOS
# ─────────────────────────────────────────────────────────────

def exibir_resultados(lista: list, media: float, maximo: int, minimo: int) -> None:
    """
    Exibe os resultados estatísticos calculados manualmente.

    Parâmetros:
        lista   (list) : lista de inteiros (original, com inválidos).
        media   (float): média calculada.
        maximo  (int)  : valor máximo.
        minimo  (int)  : valor mínimo.
    """
    primeiros = obter_primeiros(lista, 5)
    ultimos   = obter_ultimos(lista, 5)

    print("\n" + "=" * 55)
    print("  RESULTADOS – CÁLCULO MANUAL")
    print("=" * 55)
    print(f"  Média   : {media:.2f}")
    print(f"  Máximo  : {maximo}")
    print(f"  Mínimo  : {minimo}")
    print(f"  Primeiros 5 valores : {primeiros}")
    print(f"  Últimos 5 valores   : {ultimos}")
    print("=" * 55)


# ─────────────────────────────────────────────────────────────
# Ponto de entrada principal do programa
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  ETAPA 2 – Processamento Manual")
    print("=" * 55)

    # 1. Lê os dados do arquivo gerado na Etapa 1
    dados = ler_arquivo(ARQUIVO_ENTRADA)

    if len(dados) == 0:
        print("Nenhum dado disponível. Encerrando.")
    else:
        # 2. Calcula estatísticas MANUALMENTE (apenas com valores válidos)
        media  = calcular_media_manual(dados)
        maximo = calcular_maximo_manual(dados)
        minimo = calcular_minimo_manual(dados)

        # 3. Exibe os resultados
        exibir_resultados(dados, media, maximo, minimo)

        # 4. Substitui valores inválidos (≤ 0) pela média
        print("\n  Verificando valores inválidos...")
        dados_corrigidos = substituir_invalidos(dados, media)

        # 5. Salva o vetor corrigido em novo arquivo
        print()
        salvar_arquivo(dados_corrigidos, ARQUIVO_SAIDA)

    print("\nEtapa 2 concluída. Execute 'etapa3_estatisticas.py' para continuar.\n")

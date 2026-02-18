"""
=============================================================
SISTEMA DE ANÁLISE DE DADOS FINANCEIROS
Etapa 1 – Coleta e Persistência
=============================================================
Objetivo:
  Ler números inteiros via input(), armazená-los em uma lista
  usando append() e salvar em arquivo texto (um número por linha).

Conceitos utilizados:
  - List e append()
  - Laço for / while
  - Condicionais if/elif/else
  - Manipulação de arquivos com open() / with open()
  - Tratamento de exceções try/except
  - if __name__ == "__main__"
=============================================================
"""

# Nome do arquivo de saída onde os dados serão persistidos
ARQUIVO_SAIDA = "dados_acoes.txt"


def coletar_dados() -> list:
    """
    Lê números inteiros fornecidos pelo usuário via teclado.

    O usuário pode digitar quantos valores quiser.
    Para encerrar, basta digitar 'fim'.
    Entradas inválidas (não numéricas) são ignoradas com aviso.

    Retorna:
        lista_numeros (list): lista de inteiros coletados.
    """
    lista_numeros = []  # Lista que armazenará os valores coletados

    print("=" * 55)
    print("  COLETA DE DADOS – Quantidade de Ações Compradas")
    print("=" * 55)
    print("Digite números inteiros, um por vez.")
    print("Para encerrar, digite: fim\n")

    while True:
        entrada = input("Informe um valor (ou 'fim' para encerrar): ").strip()

        # Verifica se o usuário quer encerrar a coleta
        if entrada.lower() == "fim":
            print("\nColeta encerrada pelo usuário.")
            break

        # Tenta converter a entrada para inteiro
        try:
            numero = int(entrada)
            lista_numeros.append(numero)  # Adiciona à lista usando append()
            print(f"  ✔ Valor {numero} adicionado. Total: {len(lista_numeros)} registro(s).")
        except ValueError:
            # Entrada não é um número inteiro válido
            print(f"  ✘ '{entrada}' não é um número inteiro válido. Tente novamente.")

    return lista_numeros


def salvar_dados(lista_numeros: list, nome_arquivo: str) -> None:
    """
    Salva a lista de inteiros em um arquivo texto.
    Cada número é gravado em uma linha separada.

    Parâmetros:
        lista_numeros (list): lista de inteiros a salvar.
        nome_arquivo  (str) : caminho/nome do arquivo de saída.
    """
    # Verifica se há dados para salvar
    if len(lista_numeros) == 0:
        print("\nNenhum dado para salvar. Encerrando.")
        return

    # Abre o arquivo em modo escrita ('w') usando with open()
    # O with garante que o arquivo será fechado corretamente
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for numero in lista_numeros:
                arquivo.write(str(numero) + "\n")  # Um número por linha

        print(f"\n✔ {len(lista_numeros)} valor(es) salvo(s) em '{nome_arquivo}'.")
    except IOError as erro:
        print(f"\n✘ Erro ao salvar o arquivo: {erro}")


def exibir_resumo(lista_numeros: list) -> None:
    """
    Exibe um resumo dos dados coletados antes de salvar.

    Parâmetros:
        lista_numeros (list): lista de inteiros coletados.
    """
    total = len(lista_numeros)

    if total == 0:
        print("\nNenhum dado coletado.")
        return

    print("\n" + "=" * 55)
    print("  RESUMO DA COLETA")
    print("=" * 55)
    print(f"  Total de registros : {total}")
    print(f"  Dados coletados    : {lista_numeros}")
    print("=" * 55)


# ─────────────────────────────────────────────────────────────
# Ponto de entrada principal do programa
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # 1. Coleta os dados via teclado
    dados = coletar_dados()

    # 2. Exibe um resumo do que foi coletado
    exibir_resumo(dados)

    # 3. Salva os dados no arquivo de saída
    salvar_dados(dados, ARQUIVO_SAIDA)

    print("\nEtapa 1 concluída. Execute 'etapa2_processamento.py' para continuar.\n")

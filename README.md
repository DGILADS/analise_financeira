# 📊 Sistema de Análise de Dados Financeiros em Python

> Sistema progressivo de análise estatística desenvolvido como exercício acadêmico de Python.  
> Trabalha com dados financeiros (ex: quantidade de ações compradas) em 4 etapas evolutivas.

---

## 📁 Estrutura do Projeto

```
exe7/
│
├── etapa1_coleta.py          # Etapa 1 – Coleta e persistência de dados
├── etapa2_processamento.py   # Etapa 2 – Processamento manual (sem funções prontas)
├── etapa3_estatisticas.py    # Etapas 3 e 4 – Estatísticas com bibliotecas + remoção de outliers
│
├── dados_acoes.txt           # Arquivo gerado pela Etapa 1 (entrada bruta)
├── dados_corrigidos.txt      # Arquivo gerado pela Etapa 2 (sem valores inválidos)
└── dados_sem_outliers.txt    # Arquivo gerado pela Etapa 3/4 (sem outliers)
```

---

## 🚀 Como Executar

Execute os programas **na ordem**, pois cada etapa depende do arquivo gerado pela anterior:

```bash
# Etapa 1 – coleta interativa de dados
python3 etapa1_coleta.py

# Etapa 2 – processamento e limpeza manual
python3 etapa2_processamento.py

# Etapas 3 e 4 – estatísticas completas + remoção de outliers
python3 etapa3_estatisticas.py
```

> **Atalho para testes:** O arquivo `dados_acoes.txt` já vem pré-preenchido com 25 valores de exemplo (incluindo 4 inválidos). Você pode pular a Etapa 1 e ir direto para a Etapa 2.

---

## 🔹 Etapa 1 – Coleta e Persistência

**Arquivo:** `etapa1_coleta.py`  
**Entrada:** teclado (`input()`)  
**Saída:** `dados_acoes.txt`

### O que faz

Lê números inteiros digitados pelo usuário um a um e os armazena em uma lista Python. Ao final, salva todos os valores em um arquivo texto, um número por linha.

### Fluxo de execução

```
Usuário digita número → validação → append() na lista → próximo número
                                                              ↓
                                                    usuário digita "fim"
                                                              ↓
                                              lista salva em dados_acoes.txt
```

### Conceitos aplicados

| Conceito                    | Onde é usado                                           |
| --------------------------- | ------------------------------------------------------ |
| `list` + `append()`         | Armazenamento dos valores coletados                    |
| `while True` + `break`      | Loop de coleta até o usuário digitar "fim"             |
| `try/except ValueError`     | Rejeita entradas não numéricas com aviso               |
| `with open(..., "w")`       | Escrita segura no arquivo (fecha automaticamente)      |
| Funções separadas           | `coletar_dados()`, `salvar_dados()`, `exibir_resumo()` |
| `if __name__ == "__main__"` | Ponto de entrada controlado                            |

### Exemplo de interação

```
Informe um valor (ou 'fim' para encerrar): 150
  ✔ Valor 150 adicionado. Total: 1 registro(s).
Informe um valor (ou 'fim' para encerrar): abc
  ✘ 'abc' não é um número inteiro válido. Tente novamente.
Informe um valor (ou 'fim' para encerrar): fim

Coleta encerrada pelo usuário.
✔ 1 valor(es) salvo(s) em 'dados_acoes.txt'.
```

### Formato do arquivo de saída

```
150
230
-5
410
0
...
```

---

## 🔹 Etapa 2 – Processamento Manual

**Arquivo:** `etapa2_processamento.py`  
**Entrada:** `dados_acoes.txt`  
**Saída:** `dados_corrigidos.txt`

### O que faz

Lê o arquivo da Etapa 1, calcula estatísticas básicas **sem usar nenhuma função pronta** (`min()`, `max()`, `sum()`, `statistics`, etc.), identifica e substitui valores inválidos (≤ 0) pela média calculada, e salva o vetor corrigido.

### Por que valores ≤ 0 são inválidos?

No contexto financeiro, a quantidade de ações compradas nunca pode ser zero ou negativa. Esses valores representam erros de entrada, dados corrompidos ou registros ausentes. A estratégia adotada é **substituí-los pela média dos valores válidos**, preservando o tamanho do vetor e evitando distorções nos cálculos futuros.

> ⚠️ **Importante:** os valores inválidos são **excluídos dos cálculos** de média, máximo e mínimo. Só depois de calcular a média com os valores válidos é que os inválidos são substituídos.

### Algoritmos implementados manualmente

#### Média (acumulador)

```python
soma = 0
contagem = 0
for valor in lista:
    if valor > 0:          # Ignora inválidos
        soma = soma + valor
        contagem = contagem + 1
media = soma / contagem
```

#### Máximo (comparação iterativa)

```python
maximo = None
for valor in lista:
    if valor > 0:
        if maximo is None or valor > maximo:
            maximo = valor
```

#### Mínimo (comparação iterativa)

```python
minimo = None
for valor in lista:
    if valor > 0:
        if minimo is None or valor < minimo:
            minimo = valor
```

#### Primeiros / Últimos 5 (percurso com índice)

```python
# Primeiros N: percorre até atingir N elementos
primeiros = []
indice = 0
for valor in lista:
    if indice >= 5: break
    primeiros.append(valor)
    indice = indice + 1

# Últimos N: calcula o índice de início
inicio = len(lista) - 5
```

### Conceitos aplicados

| Conceito               | Onde é usado                              |
| ---------------------- | ----------------------------------------- |
| Acumuladores manuais   | Cálculo de soma, contagem, máximo, mínimo |
| `for` + `if/elif/else` | Filtragem de valores válidos              |
| `append()`             | Construção da lista corrigida             |
| `with open(..., "r")`  | Leitura linha a linha do arquivo          |
| `with open(..., "w")`  | Escrita do vetor corrigido                |
| `try/except`           | Tratamento de arquivo não encontrado      |

### Exemplo de saída

```
RESULTADOS – CÁLCULO MANUAL
=======================================================
  Média   : 284.05
  Máximo  : 500
  Mínimo  : 75
  Primeiros 5 valores : [150, 230, -5, 410, 0]
  Últimos 5 valores   : [75, 0, 290, 360, 125]

  ⚠ 4 valor(es) inválido(s) substituído(s) pela média (284).
✔ Vetor corrigido salvo em 'dados_corrigidos.txt'.
```

---

## 🔹 Etapa 3 – Estatísticas com Bibliotecas

**Arquivo:** `etapa3_estatisticas.py` (primeira metade)  
**Entrada:** `dados_corrigidos.txt`  
**Saída:** exibição no terminal

### O que faz

Lê o arquivo tratado e calcula um conjunto completo de métricas estatísticas usando as bibliotecas padrão do Python (`statistics` e `math`). Cada métrica é acompanhada de um comentário explicativo didático.

### Métricas calculadas e suas explicações

| Métrica           | Função usada            | Explicação                                                                 |
| ----------------- | ----------------------- | -------------------------------------------------------------------------- |
| **Média**         | `statistics.mean()`     | Soma dividida pela quantidade. Representa o valor "central" típico.        |
| **Mediana**       | `statistics.median()`   | Valor do meio quando os dados estão ordenados. Menos afetada por extremos. |
| **Máximo**        | `max()`                 | Maior valor presente. Indica o limite superior observado.                  |
| **Mínimo**        | `min()`                 | Menor valor presente. Indica o limite inferior observado.                  |
| **Amplitude**     | `max - min`             | Diferença entre extremos. Mede a dispersão total dos dados.                |
| **Variância**     | `statistics.variance()` | Média dos quadrados dos desvios. Mede afastamento da média (em unidades²). |
| **Desvio Padrão** | `statistics.stdev()`    | Raiz da variância. Dispersão na mesma unidade dos dados.                   |
| **Primeiros 5**   | `lista[:5]`             | Inspeciona o início do vetor.                                              |
| **Últimos 5**     | `lista[-5:]`            | Inspeciona o fim do vetor.                                                 |

### Por que usar bibliotecas aqui?

Após dominar os algoritmos manuais na Etapa 2, esta etapa demonstra como o Python oferece implementações otimizadas e testadas para os mesmos cálculos. Em produção, sempre prefira as bibliotecas — elas são mais eficientes e menos propensas a erros.

### Exemplo de saída

```
ESTATÍSTICAS COMPLETAS (com bibliotecas)
============================================================
  Média          : 284.04
  Mediana        : 284.00
  Máximo         : 500
  Mínimo         : 75
  Amplitude      : 425
  Variância      : 14240.87
  Desvio Padrão  : 119.34
  Primeiros 5    : [150, 230, 284, 410, 284]
  Últimos 5      : [75, 284, 290, 360, 125]
```

---

## 🔹 Etapa 4 – Remoção de Outliers

**Arquivo:** `etapa3_estatisticas.py` (segunda metade)  
**Entrada:** `dados_corrigidos.txt`  
**Saída:** `dados_sem_outliers.txt`

### O que são outliers?

**Outliers** (ou "pontos fora da curva") são valores extremamente grandes ou pequenos que se afastam significativamente do padrão do conjunto de dados. Eles podem distorcer análises, enviesar médias e comprometer modelos preditivos.

**Exemplo prático:** se a maioria das compras de ações está entre 100 e 500 unidades, um registro de 50.000 unidades provavelmente é um erro de digitação — e deve ser removido antes da análise.

### Critério matemático adotado

```
Outlier superior: valor > média + 2 × desvio_padrão
Outlier inferior: valor < média - 2 × desvio_padrão
```

Este critério é baseado na **regra empírica da distribuição normal**: em dados normalmente distribuídos, ~95% dos valores estão dentro de 2 desvios padrão da média. Valores fora desse intervalo são estatisticamente improváveis e considerados outliers.

### Implementação manual (sem funções prontas)

#### Desvio padrão manual (método de Newton-Raphson para raiz quadrada)

```python
# 1. Calcula a variância manualmente
soma_quadrados = 0.0
for valor in lista:
    diferenca = valor - media
    soma_quadrados = soma_quadrados + (diferenca * diferenca)
variancia = soma_quadrados / (n - 1)

# 2. Raiz quadrada pelo método de Newton-Raphson (sem math.sqrt)
estimativa = variancia
for _ in range(50):
    estimativa = (estimativa + variancia / estimativa) / 2
desvio = estimativa
```

#### Filtragem dos outliers

```python
lista_filtrada = []
for valor in lista:
    if valor > limite_superior or valor < limite_inferior:
        print(f"Outlier removido: {valor}")
    else:
        lista_filtrada.append(valor)
```

### Exemplo de saída

```
ETAPA 4 – Remoção de Outliers (cálculo manual)
============================================================
  Média          : 284.04
  Desvio Padrão  : 119.34
  Limite superior: 522.71
  Limite inferior: 45.37

  Total removido : 0 outlier(s)
  Registros finais: 25

  Vetor final (sem outliers):
  [150, 230, 284, 410, ...]
```

> **Testando com outliers:** Para ver a remoção em ação, adicione valores extremos ao `dados_acoes.txt` antes de rodar a Etapa 2, por exemplo: `9999` (outlier superior) ou `2` (possível outlier inferior, dependendo da média).

---

## 🧠 Conceitos Fundamentais Aplicados

### Estruturas de dados

- **`list`**: estrutura principal de armazenamento em todas as etapas
- **`append()`**: único método de inserção utilizado (conforme diretriz pedagógica)

### Controle de fluxo

- **`for`**: iteração sobre listas e arquivos
- **`while True` + `break`**: loop de coleta com encerramento controlado
- **`if/elif/else`**: validação de entradas e filtragem de valores

### Arquivos

- **`with open(..., "r")`**: leitura segura (fecha automaticamente)
- **`with open(..., "w")`**: escrita segura (fecha automaticamente)
- **`.strip()`**: remoção de espaços e quebras de linha ao ler

### Boas práticas

- **Funções separadas**: cada responsabilidade em sua própria função
- **`if __name__ == "__main__"`**: separa definição de execução
- **`try/except`**: tratamento de erros de conversão e I/O
- **Nomes descritivos**: variáveis como `lista_numeros`, `soma_quadrados`, `limite_superior`
- **Comentários didáticos**: cada bloco lógico explicado

---

## 📐 Complexidade Computacional

| Operação                  | Complexidade |
| ------------------------- | ------------ |
| Leitura do arquivo        | O(n)         |
| Cálculo de média          | O(n)         |
| Cálculo de máximo/mínimo  | O(n)         |
| Substituição de inválidos | O(n)         |
| Cálculo de desvio padrão  | O(n)         |
| Remoção de outliers       | O(n)         |
| **Pipeline completo**     | **O(n)**     |

Todas as operações percorrem a lista uma única vez — complexidade linear O(n).

---

## 🔗 Dependências

- **Python 3.x** (sem instalação adicional necessária)
- **`statistics`** — biblioteca padrão do Python (já inclusa)
- **`math`** — biblioteca padrão do Python (já inclusa)

---

## 👨‍💻 Autor

Desenvolvido como exercício da disciplina de Python — Aula 2, Exercício 7.

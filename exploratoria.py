# Analise Exploratória dos dados

# Pacotes
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# arquivos 
import const
from utils import *


# função para conectar e extrair os dados direto no DB
df = fetch_data_from_db(const.consulta_sql)

#converter dados numericos
df['idade'] = df['idade'].astype(int)
df['valorsolicitado'] = df['valorsolicitado'].astype(float)
df['valortotalbem'] = df['valortotalbem'].astype(float)


#separando as variaveis categoricas e numericas
variaveis_categoricas = ['profissao', 'tiporesidencia', 
                         'escolaridade', 'score', 'estadocivil', 'produto']
variaveis_numericas = ['tempoprofissao', 'renda', 'idade',
                        'dependentes', 'valorsolicitado', 'valortotalbem']



#gerando gráficos categoricos
for coluna in variaveis_categoricas:
    df[coluna].value_counts().plot(kind='bar', figsize=(10, 6))
    plt.title(f'Distribuição de {coluna}')
    plt.ylabel('Contagem')
    plt.xlabel(coluna) 
    plt.xticks(rotation=45)
    plt.show()


#gerando gráficos numericos: 

#boxplot(outliers)
for coluna in variaveis_numericas:
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=coluna)
    plt.title(f'Boxplot de {coluna}')
    plt.show()

    #histograma(distribuição)
    df[coluna].hist(bins=20, figsize=(10, 6))
    plt.title(f'Histograma de ')
    plt.xlabel(coluna)
    plt.ylabel('frequencia')
    plt.show()


    #resumo estatistico
    print(f'Resumo estatístico de : \n', df[coluna].describe(), '\n')

#valores nulos
nulos_por_coluna = df.isnull().sum()
print(nulos_por_coluna)
    


### PROBLEMAS ENCONTRADOS:


# EDA:
    # Dados inválidos:

        # Profissao (categorica - dados inconsistente)
        # Tempo de Profissão 
        # Idade (valores acima do normal)
        # Tipo de Residencia (nulos)

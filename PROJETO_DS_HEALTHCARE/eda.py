# eda.py
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import warnings
warnings.filterwarnings("ignore") # Ignora warnings de divisão por zero ou plotagem

# 1. SETUP E CARREGAMENTO
os.makedirs("graficos", exist_ok=True)
try:
    df = pd.read_csv('dataset_healthcare_solutions.csv')
except FileNotFoundError:
    print("ERRO: 'dataset_healthcare_solutions.csv' não encontrado. Execute 'coleta_dados.py' primeiro.")
    exit()

# Converter a variável alvo para numérica para gráficos
df['readmitido_num'] = df['readmissao_30dias'].map({'Sim': 1, 'Não': 0})

def mostrar_e_salvar(figura, nome_arquivo): 
    # Sem plt.draw() e plt.pause() para evitar problemas de interface gráfica em alguns ambientes
    figura.savefig(f'graficos/{nome_arquivo}.png') 
    plt.close() 

# 2. Geração de Gráficos Essenciais

# Histograma da idade (hist_idade.png)
fig = plt.figure(figsize=(8,5))
plt.hist(df['idade'], bins=5, color='skyblue', edgecolor='black')
plt.title('Distribuição de Idade dos Pacientes')
mostrar_e_salvar(fig, 'hist_idade')

# Taxa de Readmissão (bar_taxa_readmissao.png)
fig = plt.figure(figsize=(6, 4))
contagem_readmissao = df['readmissao_30dias'].value_counts(normalize=True) * 100
contagem_readmissao.plot(kind='bar', color=['lightcoral', 'skyblue'])
plt.title('Taxa de Readmissão Hospitalar (Sim/Não)')
plt.xticks(rotation=0)
for i, v in enumerate(contagem_readmissao):
    plt.text(i, v + 1, f'{v:.1f}%', ha='center', fontweight='bold')
mostrar_e_salvar(fig, 'bar_taxa_readmissao')

# Boxplot: Tempo de Internação vs. Readmissão (box_tempo_readmissao.png)
fig = plt.figure(figsize=(8, 5))
df.boxplot(column='tempo_internacao_dias', by='readmissao_30dias', figsize=(8, 5), 
           patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Tempo de Internação por Status de Readmissão')
plt.suptitle('') 
mostrar_e_salvar(fig, 'box_tempo_readmissao')

# Scatter plot: tempo de internação x custo (scatter_tempo_custo.png)
fig = plt.figure(figsize=(8,5))
plt.scatter(df['tempo_internacao_dias'], df['custo_atendimento'], color='orange')
z = np.polyfit(df['tempo_internacao_dias'], df['custo_atendimento'], 1)
p = np.poly1d(z)
plt.plot(df['tempo_internacao_dias'], p(df['tempo_internacao_dias']), "r--", label='Tendência')
plt.title('Custo do Atendimento x Tempo de Internação')
mostrar_e_salvar(fig, 'scatter_tempo_custo')

print("--- SUCESSO: EDA finalizada. 4 gráficos salvos na pasta 'graficos'. ---")
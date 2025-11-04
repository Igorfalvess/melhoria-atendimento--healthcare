# modelo_readmissao.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings("ignore") # Ignora warnings de métricas devido ao N=20

# 1. CARREGAMENTO E LIMPEZA DE DADOS
os.makedirs("model_visuals", exist_ok=True)
try:
    df = pd.read_csv('dataset_healthcare_solutions.csv')
except FileNotFoundError:
    print("ERRO: 'dataset_healthcare_solutions.csv' não encontrado. Execute 'coleta_dados.py' primeiro.")
    exit()

# Conversão da variável alvo: 'Sim'/'Não' para 1/0
df['readmissao_30dias'] = df['readmissao_30dias'].map({'Sim': 1, 'Não': 0})
df = df.drop('id_paciente', axis=1)

# 2. PRÉ-PROCESSAMENTO 
X = df.drop('readmissao_30dias', axis=1)
Y = df['readmissao_30dias']

# One-Hot Encoding
X = pd.get_dummies(X, columns=['sexo', 'diagnostico', 'dispositivo_monitoramento'], drop_first=True)

# Separação Treino/Teste (test_size = 0.3)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42, stratify=Y)

# Escalonamento
numeric_cols = ['idade', 'tempo_espera_min', 'satisfacao_paciente', 'tempo_internacao_dias', 'custo_atendimento']
scaler = StandardScaler()
X_train[numeric_cols] = scaler.fit_transform(X_train[numeric_cols])
X_test[numeric_cols] = scaler.transform(X_test[numeric_cols])


# 3. MODELAGEM PREDITIVA (Random Forest)
modelo_rf = RandomForestClassifier(n_estimators=10, random_state=42)
modelo_rf.fit(X_train, Y_train)
Y_pred = modelo_rf.predict(X_test)


# 4. INTERPRETAÇÃO E VISUALIZAÇÃO
print("\n--- Resultados do Modelo Random Forest (N=20) ---")
print("Acurácia Geral:", accuracy_score(Y_test, Y_pred))
print("\nRelatório de Classificação:\n", classification_report(Y_test, Y_pred, zero_division=0))

# Geração do Gráfico de Importância das Variáveis
feature_imp = pd.Series(modelo_rf.feature_importances_, index=X_train.columns).sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=feature_imp.head(10), y=feature_imp.head(10).index)
plt.xlabel('Score de Importância (Feature Importance)')
plt.ylabel('Variáveis')
plt.title('Top 10 Variáveis na Previsão de Readmissão (Random Forest)')
plt.tight_layout()
plt.savefig('model_visuals/feature_importance.png')
plt.close()

print("--- SUCESSO: Modelo treinado. Gráfico de Feature Importance salvo em 'model_visuals/feature_importance.png'. ---")
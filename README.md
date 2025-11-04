# melhoria-atendimento--healthcare


**HealthCare Solutions: Análise de Dados para Melhoria do Atendimento Hospitalar**

**Descrição do Projeto**
Este projeto tem como objetivo aplicar conceitos de **Ciência de Dados** para aprimorar a **eficiência e a qualidade do atendimento hospitalar**, utilizando dados simulados de pacientes da HealthCare Solutions.
A iniciativa envolve **coleta, tratamento e análise exploratória de dados**, permitindo identificar padrões e gerar insights que apoiam decisões estratégicas baseadas em evidências.

O sistema simula uma base hospitalar realista, com informações sobre idade, sexo, tempo de espera, tempo de internação, custo do atendimento, diagnóstico, satisfação do paciente e uso de dispositivos de monitoramento.

---

### **Etapa 1 – Coleta e Geração de Dados**

O script `coleta_dados.py` foi desenvolvido para criar um **dataset fictício** com 100 registros de pacientes.
As variáveis contemplam:

* Idade e Sexo
* Tempo de Espera (minutos)
* Tempo de Internação (dias)
* Custo do Atendimento (R$)
* Satisfação do Paciente (escala de 1 a 5)
* Diagnóstico e uso de dispositivos de monitoramento
* Readmissão em até 30 dias

O resultado é o arquivo **`dataset_healthcare_solutions.csv`**, contendo dados simulados, anonimizados e prontos para análise.

**Parâmetros da Simulação**

| Parâmetro              | Valor              |
| ---------------------- | ------------------ |
| Total de Pacientes     | 100                |
| Idade                  | 18 a 90 anos       |
| Tempo de Espera        | 5 a 180 minutos    |
| Tempo de Internação    | 1 a 15 dias        |
| Custo do Atendimento   | R$ 500 a R$ 15.000 |
| Satisfação do Paciente | Escala de 1 a 5    |

---

### **Etapa 2 – Análise Exploratória de Dados (EDA)**

A segunda etapa, implementada no script `eda.py`, realiza uma **análise exploratória completa** para compreender o comportamento dos dados e identificar relações entre variáveis relevantes.

**Principais análises e gráficos gerados:**

* **Histograma de Idade:** mostra a distribuição etária dos pacientes e destaca média e mediana.
* **Boxplot do Custo de Atendimento:** identifica variações e possíveis outliers nos custos.
* **Dispersão entre Tempo de Internação e Custo:** evidencia a tendência de aumento de custos conforme o tempo de internação cresce.
* **Mapa de Correlação (Heatmap):** revela as correlações entre variáveis numéricas, auxiliando em futuras modelagens preditivas.

Todos os gráficos são gerados e salvos automaticamente nas versões **PNG e PDF** dentro da pasta `graficos/`.

**Saídas geradas:**

* `hist_idade.png`
* `box_custo.png`
* `scatter_tempo_custo.png`
* `correlacao.png`

---

### **Tecnologias Utilizadas**

* **Python 3**
* **NumPy** – geração e manipulação de dados numéricos
* **Pandas** – tratamento e análise de dados
* **Matplotlib** – visualização e criação de gráficos
* **Faker** – criação de dados fictícios realistas

---

### **Resultados e Conclusão**

O projeto demonstra como a aplicação da **Ciência de Dados na saúde** pode gerar valor real, permitindo:

* Identificar gargalos e padrões no atendimento;
* Compreender o perfil dos pacientes;
* Apoiar decisões estratégicas baseadas em dados;
* Promover uma gestão hospitalar mais eficiente e humanizada.

---

**Autor:** Igor Ferreira Alves
**Curso:** Engenharia da Computação — UNIFECAF (2025)

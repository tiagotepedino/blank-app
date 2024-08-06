import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

# Dados do cronograma com o nome atualizado
tasks = [
    {"Task": "Team Orientation with Kevin", "Start": "2025-07-01", "End": "2025-07-08"},
    {"Task": "Familiarization with CONTACT Software", "Start": "2025-07-09", "End": "2025-08-07"},
    {"Task": "Multi-body Model Assembly", "Start": "2025-07-20", "End": "2025-09-30"},
    {"Task": "Wheel/Rail Contact Simulation", "Start": "2025-10-01", "End": "2025-12-12"},
    {"Task": "Optimization of Rail Profiles", "Start": "2025-11-01", "End": "2025-12-30"},
    {"Task": "Interpretation, Evaluation, and Writing of Results", "Start": "2025-12-12", "End": "2025-12-30"},
]

# Converter para DataFrame
df = pd.DataFrame(tasks)

# Converter datas para datetime
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])

# Ordenar as tarefas pela data de início em ordem crescente
df = df.sort_values(by='Start', ascending=True)

# Configuração do Streamlit
st.title('Rail Profile Optimization Schedule')

# Configuração do gráfico
fig, ax = plt.subplots(figsize=(14, 8))

# Adicionar barras do Gantt
colors = ['#A61E51', '#BAD6CD', '#3066BE', '#923871']
for i, task in df.iterrows():
    ax.barh(task["Task"], (task["End"] - task["Start"]).days, left=task["Start"], color=colors[i % len(colors)], edgecolor='black')

# Ajustar o eixo x para mostrar as datas corretamente
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))

# Ajustar rótulos
plt.xticks(rotation=45, fontsize=12)
plt.title('Rail Profile Optimization', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)

# Ajustar os rótulos do eixo y com aumento do tamanho da fonte
ax.set_yticks(df.index)
ax.set_yticklabels(df["Task"], fontsize=12)

plt.tight_layout()

# Mostrar gráfico no Streamlit
st.pyplot(fig)

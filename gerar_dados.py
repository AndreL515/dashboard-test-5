import pandas as pd
import numpy as np

np.random.seed(42)
n = 500

df = pd.DataFrame({
    "aluno_id": range(1, n+1),
    "curso": np.random.choice(["Engenharia", "Direito", "Medicina", "TI", "Pedagogia"], n),
    "semestre": np.random.choice(["2022.1","2022.2","2023.1","2023.2","2024.1"], n),
    "situacao": np.random.choice(["Ativo", "Evadido", "Formado", "Trancado"], n, p=[0.6, 0.2, 0.15, 0.05]),
    "cr": np.round(np.random.uniform(4.0, 10.0, n), 2),
    "renda_familiar": np.random.choice(["Até 1 SM", "1-3 SM", "3-5 SM", "Acima 5 SM"], n),
    "modalidade": np.random.choice(["Presencial", "EAD"], n, p=[0.7, 0.3]),
})

df.to_csv("data/dados_brutos.csv", index=False)
print("Dados gerados com sucesso!")
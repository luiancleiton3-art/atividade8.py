import pandas as pd

# 1. Carrega os dados do arquivo CSV
dados = pd.read_csv("academia.csv")

# ==========================================
# ATIVIDADE 8 — Criando Novas Informações (Cálculo de IMC)
# ==========================================
print("--- ATIVIDADE 8 ---")

# Cria a nova coluna IMC aplicando a fórmula matemática
# Nota: usamos **2 para representar a Altura elevada ao quadrado
dados["IMC"] = dados["Peso"] / (dados["Altura"] ** 2)

# Exibe a tabela atualizada mostrando as colunas Nome, Peso, Altura e o novo IMC
print("Tabela atualizada com a coluna IMC (arredondado para 2 casas decimais):")
print(dados[["Nome", "Peso", "Altura", "IMC"]].round(2))
print("\n" + "=" * 50 + "\n")

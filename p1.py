import pandas as pd
df = pd.read_csv("MICRODADOS_ENEM_2023.csv", sep=";", encoding="latin-1")
print(df.shape)
print(df.columns)
colunas = ["SG_UF_PROVA","TP_ESCOLA","TP_SEXO","Q006","NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_LC","NU_NOTA_MT","NU_NOTA_REDACAO",]
print(f"Total de registros: {len(df)}")
print(df.info())
df = df.dropna(subset=["NU_NOTA_MT","NU_NOTA_REDACAO"])
print(f"Total de  após remoção de nulos: {len(df)}")
print(df.info())
df["MEDIA_GERAL"] = df[["NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_LC","NU_NOTA_MT"]].mean(axis=1)
#Analise 1 do Arquivo
media_por_estado = df.groupby("SG_UF_PROVA")["MEDIA_GERAL"].mean().sort_values(ascending=False)
print("\n=== Media por Estado ===")
print(media_por_estado)
#Analise 2 do Arquivo
media_por_escola = df.groupby("TP_ESCOLA")["MEDIA_GERAL"].mean()
print("\n=== Media por Tipo de Escola ===")
print(media_por_escola)
#Analise 3 do Arquivo
media_renda = df.groupby("Q006")["MEDIA_GERAL"].mean().sort_index()
print("\n=== Media por Renda Familiar ===")
print(media_renda)
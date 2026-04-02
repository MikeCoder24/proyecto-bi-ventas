import pandas as pd

df = pd.read_csv("ventas.csv")

df["ventas"] = df["precio"] * df["cantidad"]

ventas_producto = df.groupby("producto")["ventas"].sum()
ventas_pais = df.groupby("pais")["ventas"].sum()

df["fecha"] = pd.to_datetime(df["fecha"])
df["mes"] = df["fecha"].dt.month
ventas_mes = df.groupby("mes")["ventas"].sum()
print(ventas_mes)
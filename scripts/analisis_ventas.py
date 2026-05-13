# Script de análisis de ventas
# Autor: Facundo Pelizzari
# Este script procesa un dataset de ventas simuladas para obtener indicadores básicos

import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde la carpeta /datos
df = pd.read_csv("datos/ventas.csv")

# Calcular ventas totales
df["total"] = df["precio"] * df["cantidad"]
ventas_totales = df["total"].sum()

# Producto más vendido
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()

# Ventas por mes
df["fecha"] = pd.to_datetime(df["fecha"])
ventas_por_mes = df.groupby(df["fecha"].dt.to_period("M"))["total"].sum()

# Generar gráfico de evolución de ventas
plt.figure(figsize=(8,5))
ventas_por_mes.plot(kind="bar")
plt.title("Evolución de ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Ventas totales")
plt.tight_layout()
plt.savefig("resultados/ventas_por_mes.png")

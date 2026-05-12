import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos/ventas.csv")

ventas_totales = df["sales_amount"].sum()
print("Ventas totales:", ventas_totales)

if "product" in df.columns:
    producto_top = df.groupby("product")["sales_amount"].sum().idxmax()
    print("Producto más vendido:", producto_top)

df["sales_date"] = pd.to_datetime(df["sales_date"])
ventas_mes = df.groupby(df["sales_date"].dt.to_period("M"))["sales_amount"].sum()

print("Ventas por mes:")
print(ventas_mes)

plt.figure(figsize=(8,4))
ventas_mes.plot(kind="bar", color="skyblue")
plt.title("Evolución de ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Monto de ventas")
plt.tight_layout()
plt.savefig("resultados/ventas_por_mes.png")
plt.show()

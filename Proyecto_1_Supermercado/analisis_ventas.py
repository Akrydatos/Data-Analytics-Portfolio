import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Configuración estilo general
# -----------------------------
sns.set(style="whitegrid")  # Fondo blanco con grid suave
palette_prod = "viridis"
palette_cat = "coolwarm"
palette_fecha = "magma"

# -----------------------------
# Cargar datos
# -----------------------------
df = pd.read_csv("ventas.csv", decimal=',', encoding='utf-8-sig')

# Convertir columnas numéricas
df["Precio_unitario"] = pd.to_numeric(df["Precio_unitario"], errors='coerce')
df["Total"] = pd.to_numeric(df["Total"], errors='coerce')

# Convertir Fecha a datetime
df["Fecha"] = pd.to_datetime(df["Fecha"])

# -----------------------------
# Exploración de datos
# -----------------------------
print("Primeras filas:")
print(df.head())

print("\nInformación del DataFrame:")
print(df.info())

print("\nDescripción estadística:")
print(df.describe())

print("\nValores nulos por columna:")
print(df.isnull().sum())

# -----------------------------
# Crear agregados
# -----------------------------
ventas_producto = df.groupby("Producto")["Total"].sum().reset_index()
ventas_categoria = df.groupby("Categoria")["Total"].sum().reset_index()
ventas_fecha = df.groupby("Fecha")["Total"].sum().reset_index()
ventas_producto_promedio = df.groupby("Producto")["Total"].mean().reset_index()

# -----------------------------
# Gráficos
# -----------------------------

# Ventas por producto
plt.figure(figsize=(8,5))
ax = sns.barplot(data=ventas_producto, x="Producto", y="Total", palette=palette_prod)
plt.title("Ventas totales por producto", fontsize=14, weight='bold')
plt.ylabel("Total vendido (€)")
plt.xlabel("Producto")
for i, v in enumerate(ventas_producto["Total"]):
    ax.text(i, v + 0.5, f"{v:.2f}", ha='center')
plt.tight_layout()
plt.savefig("ventas_por_producto.png")
plt.show()

# Ventas por categoría
plt.figure(figsize=(6,4))
ax = sns.barplot(data=ventas_categoria, x="Categoria", y="Total", palette=palette_cat)
plt.title("Ventas totales por categoría", fontsize=14, weight='bold')
plt.ylabel("Total vendido (€)")
plt.xlabel("Categoría")
for i, v in enumerate(ventas_categoria["Total"]):
    ax.text(i, v + 0.5, f"{v:.2f}", ha='center')
plt.tight_layout()
plt.savefig("ventas_por_categoria.png")
plt.show()

# Evolución por fecha
plt.figure(figsize=(8,5))
sns.lineplot(data=ventas_fecha, x="Fecha", y="Total", marker="o", color="purple")
plt.title("Evolución de ventas por fecha", fontsize=14, weight='bold')
plt.ylabel("Total vendido (€)")
plt.xlabel("Fecha")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("ventas_por_fecha.png")
plt.show()

# -----------------------------
# Resultados tabulares
# -----------------------------
print("\nVentas totales por producto:")
print(ventas_producto.sort_values(by="Total", ascending=False))

print("\nVentas totales por categoría:")
print(ventas_categoria.sort_values(by="Total", ascending=False))

print("\nVentas totales por fecha:")
print(ventas_fecha.sort_values(by="Fecha"))

print("\nVentas promedio por producto:")
print(ventas_producto_promedio.sort_values(by="Total", ascending=False))





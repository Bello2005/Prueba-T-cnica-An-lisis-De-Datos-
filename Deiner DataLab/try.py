import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV y establecer la primera fila como encabezados
df_csv = pd.read_csv('output.csv', header=1)

# Seleccionar la fila "Tasa de Desocupación (TD)"
td_row = df_csv[df_csv['Concepto'] == 'Tasa de Desocupación (TD)']

# Transponer la fila seleccionada
Dg = td_row.T

# Resetear el índice
Dg.reset_index(inplace=True)

# Renombrar las columnas
Dg.columns = ['Año', 'Tasa de Desocupación']

# Eliminar las filas que no contienen datos relevantes
Dg = Dg.iloc[2:]

# Quitar la palabra 'Unnamed: ' de los años y convertirlos a numérico
Dg['Año'] = Dg['Año'].str.replace('Unnamed: ', '').astype(int)

# Convertir la columna de "Tasa de Desocupación" a numérico
Dg['Tasa de Desocupación'] = pd.to_numeric(Dg['Tasa de Desocupación'])

# Validación del DataFrame final
print("DataFrame Final para Graficar:")
print(Dg)

# Verificar si hay datos faltantes
if Dg.isnull().values.any():
    print("Hay valores nulos en el DataFrame. Revisa los datos.")
    exit()

# Graficar la fila de "Tasa de Desocupación"
ax = Dg.plot.bar(x='Año', y='Tasa de Desocupación', color='blue', width=0.8, legend=False)
plt.xlabel('Año')
plt.ylabel('Tasa de Desocupación')
plt.title('Tasa de Desocupación por Año')
plt.xticks(rotation=0)
plt.tight_layout()

# Añadir etiquetas de valores en las barras
for p in ax.patches:
    ax.annotate(f'{p.get_height():.2f}', (p.get_x() * 1.005, p.get_height() * 1.005))

# Guardar la gráfica en un archivo
plt.savefig('tasa_desocupacion_por_año.png')

# Mostrar la gráfica
plt.show()

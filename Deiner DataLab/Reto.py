import pandas as pd
import matplotlib.pyplot as plt


try:
    df_excel = pd.read_excel('Libro3.xlsx')
except FileNotFoundError:
    print("El archivo 'Libro3.xlsx' no se encontró.")
    exit()


try:
    df_excel.to_csv('output.csv', index=False)
    print("El archivo CSV 'output.csv' se ha creado exitosamente.")
except Exception as e:
    print(f"Error al convertir el archivo Excel a CSV: {e}")
    exit()


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


try:
    df_csv = pd.read_csv('output.csv', header=2)
except FileNotFoundError:
    print("El archivo 'output.csv' no se encontró.")
    exit()


print("DataFrame Completo:")
print(df_csv)



try:
    Dg = df_csv[df_csv[df_csv.columns[0]] == 'Tasa de Desocupación (TD)'].transpose()
except KeyError as e:
    print(f"Error al encontrar la columna: {e}")
    exit()


Dg.reset_index(inplace=True)


Dg.columns = Dg.iloc[0]
Dg = Dg[1:]


Dg.rename(columns={Dg.columns[0]: 'Año', Dg.columns[1]: 'Tasa de Desocupación'}, inplace=True)


Dg['Año'] = Dg['Año'].str.replace('Unnamed: ', '').astype(float)


Dg['Tasa de Desocupación'] = pd.to_numeric(Dg['Tasa de Desocupación'])

print("DataFrame Final para Graficar:")
print(Dg)



ax = Dg.plot.bar(x='Año', y='Tasa de Desocupación', color='blue', width=0.9, legend=False)
plt.xlabel('Año')
plt.ylabel('Tasa de Desocupación')
plt.title('Tasa de Desocupación por Año')
plt.xticks(rotation=0)
plt.tight_layout()


for p in ax.patches:
    ax.annotate(f'{p.get_height():.2f}', (p.get_x() * 1.005, p.get_height() * 1.005))


plt.savefig('tasa_desocupacion_por_año.png')


plt.show()

# El análisis de la tasa de desocupación en Chocó, basado en datos de 2015 a 2023, reveló fluctuaciones
# anuales que indican cambios en la economía regional. La transformación de los datos de Excel a CSV,
# seguida de la limpieza y visualización, permitió identificar patrones de desempleo cruciales.
# Estos hallazgos no solo proporcionan una base sólida para la toma de decisiones estratégicas,
# sino que también subrayan la importancia de la analítica de datos en la gestión de políticas laborales.


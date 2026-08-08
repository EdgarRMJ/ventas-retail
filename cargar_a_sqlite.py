import pandas as pd
import sqlite3

df = pd.read_csv('data/SampleSuperstore.csv', encoding='latin-1')

# Renombrar columnas para que coincidan con la tabla SQL
df = df.rename(columns={
    'Ship Mode': 'ship_mode',
    'Segment': 'segment',
    'Country': 'country',
    'City': 'city',
    'State': 'state',
    'Postal Code': 'postal_code',
    'Region': 'region',
    'Category': 'category',
    'Sub-Category': 'sub_category',
    'Sales': 'sales',
    'Quantity': 'quantity',
    'Discount': 'discount',
    'Profit': 'profit'
})

conexion = sqlite3.connect('ventas.db')
df.to_sql('ventas', conexion, if_exists='append', index=False)
conexion.close()

print("Carga completada.")
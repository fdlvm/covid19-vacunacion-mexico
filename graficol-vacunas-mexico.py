## Tutorial generando mi primer gráfico lineal con phyton.

## PASO 1: Importar librerias
import pandas as pd
import plotly.express as px

## PASO 2: Importar datos de origen de vacunacion 
df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/Mexico.csv')
print(df.head())

## PASO 3: Generando el grafico lineal con plotly
fig = px.line(df, x = 'date', y = 'total_vaccinations', title='Histórico de aplicación de vacunas COVID19 en México')
##fig.show()
fig.write_html('grafico-vacunacion-mexico.html', auto_open=True)
# Dashboard de anúncios de venda de carros

Aplicativo web interativo para explorar um conjunto de dados de anúncios de veículos usados nos Estados Unidos.

## Funcionalidades

- Histograma da quilometragem (`odometer`) dos veículos anunciados
- Gráfico de dispersão relacionando quilometragem e preço, colorido por condição do veículo
- Caixas de seleção que permitem exibir ou ocultar cada gráfico

## Dados

`vehicles_us.csv` — 51.525 anúncios com 13 colunas (preço, ano do modelo, modelo, condição, cilindros, combustível, quilometragem, transmissão, tipo, cor, tração 4x4, data do anúncio e dias listado).

## Tecnologias

pandas, plotly-express, streamlit

## Aplicativo online

https://SEU-APP.onrender.com/

## Executar localmente

​```bash
python -m venv vehicles_env
vehicles_env\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
​```
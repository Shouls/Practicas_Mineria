import requests
import io
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
from kaggle.api.kaggle_api_extended import KaggleApi


def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def get_csv_from_url(url:str) -> pd.DataFrame:
    s=requests.get(url).content
    return pd.read_csv(io.StringIO(s.decode('utf-8')))

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

api = KaggleApi() #entra a la API
api.authenticate() #se autentica con el .json que esta en: C:\Users<Windows-username>.kaggle\kaggle.json on Windows. If the token is not there, an error will be raised
api.dataset_download_file('mrmorj/nintendo-games-dataset', file_name= 'data.csv')

#Lee el archivo que se descarga de la API, hay que tener cuidado con la ruta del archivo, debe ser la misma?
df = pd.read_csv(".././Practica_1/data.csv")
print_tabulate(df)




# File: get.py
# pip install -e /Users/merilin/Documents/GitHub/geihdanepy 


import pandas as pd 
import urllib
import requests
import collections
import os
from .utils import __referenciador_modulo, __referenciador_modulo_2020, __referenciador_zona, __referenciador_zona_2020, meses, __referenciador_modulo_macro2018, __referenciador_modulo_macro2018_alt, remove_unnamed_cols, detect_delimiter
import datetime

cwd = '/Users/merilin/Documents/GitHub/geihdanepy'

def __link(año:int, mes:str, modulo:str, zona:str) -> str:
    mes = mes.capitalize()
    current_year = 2024
    if año not in range(2007, current_year + 1):
        print(f'ValueError: {año} no es un año valido.')
        return None
    elif mes not in meses():
        print(f'ValueError: {mes} no es un mes valido.')
        return None
    if modulo=='Migracion':
        modulo, zona = __referenciador_modulo()[modulo],  __referenciador_zona()[zona.capitalize()]
        mes_num = f'0{meses().index(mes) + 1}'[-2:]
        link = f'{cwd}/src/geihdanepy/sets/{año}/{mes}.csv/{modulo}_{año}_{mes_num}.csv'
        print(f"Constructed link: {link}")
        return link
    else:
        if (año != 2020) | ((año == 2020) & (mes == 'Abril')):
            modulo, zona = __referenciador_modulo()[modulo],  __referenciador_zona()[zona]
            link = f'{cwd}/src/geihdanepy/sets/{año}/{mes}.csv/{zona}{modulo}.csv'
            print(f"Constructed link: {link}")
            return link
        elif ((año == 2020) & (mes != 'Abril')):
            modulo, zona = __referenciador_modulo_2020()[modulo.capitalize()],  __referenciador_zona_2020()[zona.capitalize()]
            link = f'{cwd}/src/geihdanepy/sets/{año}/{mes}.csv/{zona} - {modulo}.csv'
            print(f"Constructed link: {link}")
            return link

def datos(año: int, mes: str, modulo: str, zona: str) -> pd.DataFrame:
    link = __link(año, mes, modulo, zona)
    delimiter, encoding = detect_delimiter(link)
    if zona == 'all':
        a = remove_unnamed_cols(pd.read_csv(__link(año, mes, modulo, 'area'), sep=delimiter, encoding=encoding, low_memory=False))
        c = remove_unnamed_cols(pd.read_csv(__link(año, mes, modulo, 'cabecera'), sep=delimiter, encoding=encoding, low_memory=False))
        r = remove_unnamed_cols(pd.read_csv(__link(año, mes, modulo, 'resto'), sep=delimiter, encoding=encoding, low_memory=False))
        valores = [x for x, y in collections.Counter(list(a.columns) + list(c.columns)).items() if y > 1]
        valores = [x for x, y in collections.Counter(valores + list(r.columns)).items() if y > 1]
        a, c, r = a[valores], c[valores], r[valores]
        return pd.concat([a, c, r])
    else:
        try:
            df = remove_unnamed_cols(pd.read_csv(link, sep=delimiter, encoding=encoding, low_memory=False))
            #print(df.head())
            print(f"Data read successfully from {link} with encoding {encoding}")
            return df
        except FileNotFoundError:
            print(f"[Errno 2] No such file or directory: '{link}'")
            return pd.DataFrame()  # Return an empty DataFrame if file not found
        except UnicodeDecodeError:
            print(f"UnicodeDecodeError: Failed to read data from {link} with default encoding, trying 'latin1'")
            try:
                df = remove_unnamed_cols(pd.read_csv(link, sep=delimiter, encoding='latin1', low_memory=False))
                #print(df.head())
                print(f"Data read successfully from {link} with 'latin1' encoding")
                return df
            except Exception as e:
                print(f"Failed to read data from {link} with 'latin1' encoding: {e}")
        except FileNotFoundError as e:
            print(f'FileNotFoundError: {e}')
        except KeyError as e:
            print(f'KeyError: {e} no se reconoce como un argumento valido')
        except ValueError as e: 
            print(f'ValueError: {e}')
        except Exception as e:
            print(f'An error occurred: {e}')
        return None


def datos_marco_2018(año:int, mes:str, modulo:str) -> pd.DataFrame:
    mes = mes.capitalize()
    if año < 2023:
        modulo = __referenciador_modulo_macro2018()[modulo].lower()
        link = f'{cwd}/src/geihdanepy/sets/{año}/{mes}/{modulo}.csv'
    else:
        modulo = __referenciador_modulo_macro2018_alt()[modulo]
        link = f'{cwd}/src/geihdanepy/sets/{año}/{mes}/{modulo}.CSV'
    delimiter, encoding = detect_delimiter(link)

    try:
        print(f"Attempting to read data from {link} with encoding {encoding}")
        df = pd.read_csv(link, sep=delimiter, encoding=encoding, low_memory=False)
        df = remove_unnamed_cols(df)
        #print(df.head())
        return df
    except FileNotFoundError:
        print(f"[Errno 2] No such file or directory: '{link}'")
        return pd.DataFrame()  # Return an empty DataFrame if file not found
    except UnicodeDecodeError:
        print(f"UnicodeDecodeError: Failed to read data from {link} with encoding {encoding}, trying 'latin1'")
        try:
            df = pd.read_csv(link, sep=delimiter, encoding='latin1', low_memory=False)
            df = remove_unnamed_cols(df)
            #print(df.head())
            return df
        except Exception as e:
            print(f"Failed to read data from {link} with 'latin1' encoding: {e}")
    except Exception as e:
        print(f"An error occurred while reading {link}: {e}")
    return None


def info_modulos_marco2018() -> str:
    '''
    Funcion para conocer los codigo de los modulos de la GEIH dentro de las funciones
    de geihdanepy.
    ''' 

    url = f'https://raw.githubusercontent.com/BautistaDavid/geihdanepy/main/src/geihdanepy/txt_files/modulos_marco2018.txt'
    file = urllib.request.urlopen(url)
    for line in file:
        decoded_line = line.decode('utf-8')
        print(decoded_line)


def info_zonas() -> str:
    '''
    Funcion para conocer los codigos de las zonas de la GEIH dentro de las 
    funciones de geihdanepy
    '''
    url = f'https://raw.githubusercontent.com/BautistaDavid/geihdanepy/main/src/geihdanepy/txt_files/zonas.txt'
    file = urllib.request.urlopen(url)
    for line in file:
        decoded_line = line.decode("utf-8")
        print(decoded_line)


def info_modulos() ->str:
    '''
    Funcion para conocer los codigos de los modulos de la GEIH dentro de las 
    funciones de geihdanepy
    '''
    url = f'https://raw.githubusercontent.com/BautistaDavid/geihdanepy/main/src/geihdanepy/txt_files/modulos.txt'
    file = urllib.request.urlopen(url)
    for line in file:
        decoded_line = line.decode("utf-8")
        print(decoded_line)
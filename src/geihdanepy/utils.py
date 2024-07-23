def __referenciador_modulo():
    ref_modulo = {'Vivienda':'v',
                   'Caracteristicas':'c',
                   'Fuerza':'f',
                   'Ocupados':'o',
                   'Desocupados':'d',
                   'Inactivos':'i',
                   'Migracion':'migracion',
                   'Otras actividades':'o_a',
                   'Otros ingresos':'o_i'}
    return ref_modulo 

def __referenciador_modulo_2020():
    ref_modulo = {'Vivienda':'Vivienda y Hogares',
                   'Caracteristicas':r'Características generales (Personas)',
                   'Fuerza':'Fuerza de trabajo',
                   'Ocupados':'Ocupados',
                   'Desocupados':'Desocupados',
                   'Inactivos':'Inactivos',
                   'Migracion':'migracion',
                   'Otras actividades':'Otras actividades y ayudas en la semana',
                   'Otros ingresos':'Otros ingresos'}
    return ref_modulo 

def __referenciador_modulo_macro2018():
    ref_modulo = {'Caracteristicas':'caracteristicas',
        'Vivienda':'hogar_vivienda',
        'Fuerza':'fuerza_trabajo',
        'Migracion':'migracion',
        'Desocupados':'no_ocupados',
        'Ocupados':'ocupados',
        'Otras actividades':'otras_formas_trabajo',
        'Otros ingresos':'otros_ingresos_impuestos',
        'Tipo investigacion':'tipo_investigacion'}
    return ref_modulo

def __referenciador_modulo_macro2018_alt():
    ref_modulo = {'Caracteristicas':'Caracterกsticas generales, seguridad social en salud y educaciขn',
        'Vivienda':'Datos del hogar y la vivienda',
        'Fuerza':'Fuerza de trabajo',
        'Migracion':'Migraciขn',
        'Desocupados':'No ocupados',
        'Ocupados':'Ocupados',
        'Otras actividades':'Otras formas de trabajo',
        'Otros ingresos':'Otros ingresos e impuestos'}
    return ref_modulo
    
def __referenciador_zona():
    ref_zona = {'Cabecera':'C',
                "Area":"A",
                "Resto":"R"}
    return ref_zona

def __referenciador_zona_2020():
    ref_zona = {'Cabecera':'Cabecera',
                "Area":"╡rea",
                "Resto":"Resto"}
    return ref_zona

def meses():
    return ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']


# Some cleaning functions for reading the CSV-s
def remove_unnamed_cols(df):
    for c in df.columns:
        if "Unnamed" in c:
            df = df.drop(columns = [c])
    return df

def detect_delimiter(filepath):
    with open(filepath, 'rb') as f:
        # Read a small part of the file to determine encoding
        rawdata = f.read(10000)
    
    encodings = ['utf-8', 'latin1']
    encoding = None
    
    for enc in encodings:
        try:
            rawdata.decode(enc)
            encoding = enc
            break
        except UnicodeDecodeError:
            continue
    
    if not encoding:
        encoding = 'utf-8'  # Default to utf-8 if none found
    
    with open(filepath, 'r', encoding=encoding) as f:
        first_line = f.readline()
    
    delimiters = [',', ';', '\t', '|']
    detected_delimiter = max(delimiters, key=first_line.count)
    
    return detected_delimiter, encoding
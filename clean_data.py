"""Taller evaluable presencial"""

import pandas as pd


def load_data(input_file):
    """Lea el archivo usando pandas y devuelva un DataFrame"""

    #
    # Esta parte es igual al taller anterior
    #
    df = pd.read_csv(input_file)
    return df


def create_key(df, n):
    """Cree una nueva columna en el DataFrame que contenga el key de la columna 'text'"""

    df = df.copy()

    # Copie la columna 'text' a la columna 'key'
    # Remueva los espacios en blanco al principio y al final de la cadena
    # Convierta el texto a minúsculas
    # Transforme palabras que pueden (o no) contener guiones por su version sin guion.
    # Remueva puntuación y caracteres de control
    # Convierta el texto a una lista de tokens
    # Una el texto sin espacios en blanco
    # Convierta el texto a una lista de n-gramas
    # Ordene la lista de n-gramas y remueve duplicados
    # Convierta la lista de ngramas a una cadena
    
    return df


def generate_cleaned_column(df):
    """Crea la columna 'cleaned' en el DataFrame"""

    df = df.copy()

    # Ordene el dataframe por 'key' y 'text'
    # Seleccione la primera fila de cada grupo de 'key'
    # Cree un diccionario con 'key' como clave y 'text' como valor
    # Cree la columna 'cleaned' usando el diccionario

    return df


def save_data(df, output_file):
    """Guarda el DataFrame en un archivo"""
    #
    # Este código es identico al anteior
    #
    df = df.copy()
    df = df[["cleaned"]]
    df = df.rename(columns={"cleaned": "text"})
    df.to_csv(output_file, index=False)


def main(input_file, output_file, n=2):
    """Ejecuta la limpieza de datos"""
    #
    # Este código es identico al anteior
    #
    df = load_data(input_file)
    df = create_key(df, n)
    df = generate_cleaned_column(df)
    df.to_csv("test.csv", index=False)
    save_data(df, output_file)


if __name__ == "__main__":
    main(
        input_file="input.txt",
        output_file="output.txt",
    )
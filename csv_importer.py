import pandas as pd

class CSVImporter:
    def __init__(self, engine):
        self.engine = engine

    def import_csv_to_mysql(self, csv_file, table_name):
        # Especificar las columnas que se van a leer
        columns = [ 'CODIGOS','REPORTES','REPORTES','DEPARTAMENTO','PROVINCIA','DISTRITO','DISTRITO','DIRECCION','REFERENCIA', 'ADMINISTRADOR', 'ASOCIADO', 'DNI', 'NUMERO', 'RAZON_SOCIAL', 'RUC', 'BASE_EMPRESA', 'CORREO', ' TELEFONO']
  
        # Leer el archivo CSV y seleccionar solo las columnas necesarias
        df = pd.read_csv(csv_file, sep=';', usecols=columns)

        # Convertir todos los valores del DataFrame a cadenas (strings)
        df = df.applymap(str)    
         
        # Eliminar el espacio extra en el nombre de la columna 'Correo'
        df.rename(columns=lambda x: x.strip(), inplace=True)
        
        print("Datos a insertar en la tabla MySQL:")
        print(df)
                
        # Insertar los datos en la tabla MySQL
        df.to_sql(table_name, con=self.engine, if_exists='append', index=False)
        
        print("Datos insertados correctamente en la tabla MySQL.")

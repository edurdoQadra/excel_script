
from sqlalchemy import create_engine

class DatabaseConnector:
    def __init__(self, hostname="localhost", username="root", password="", database="bd_mailing"):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        self.engine = self.connect_to_database()

    def connect_to_database(self):
        # Construye la cadena de conexión utilizando los parámetros proporcionados
        connection_string = f"mysql+pymysql://{self.username}:{self.password}@{self.hostname}/{self.database}"
        # Crea el motor de SQLAlchemy con la cadena de conexión
        engine = create_engine(connection_string)
        # Devuelve el motor para que pueda ser utilizado por otras partes del código
        return engine

    def close_connection(self):
        # Cierra la conexión al finalizar el proceso
        self.engine.dispose()

    def execute_query(self, query):
        # Ejecuta una consulta en la base de datos y devuelve el resultado
        return self.engine.execute(query)

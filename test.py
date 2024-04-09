from db_conection import DatabaseConnector

def test_database_connection():
    try:
        # Crear una instancia del conector de base de datos
        connector = DatabaseConnector()

        # Intentar establecer la conexión
        engine = connector.connect_to_database()

        # Si la conexión se establece correctamente, imprimir un mensaje de éxito
        print("Conexión exitosa a la base de datos.")

        # Cerrar la conexión
        connector.close_connection()
    except Exception as e:
        # Si ocurre algún error, imprimir un mensaje de error
        print(f"Error al conectar a la base de datos: {str(e)}")

if __name__ == "__main__":
    # Ejecutar la función de prueba
    test_database_connection()
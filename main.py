from db_conection import DatabaseConnector
from csv_importer import CSVImporter

def main():
    csv_file = './file/bet.csv'
    table_name = 'matriz'

    connector = DatabaseConnector()

    engine = connector.connect_to_database()

    importer = CSVImporter(engine)

    importer.import_csv_to_mysql(csv_file, table_name)

    connector.close_connection()

if __name__ == "__main__":
    main()
 
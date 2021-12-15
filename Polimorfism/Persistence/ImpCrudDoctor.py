import mysql.connector
from Persistence import ICrud


class ImportCrudDoctor(ICrud.ICrud):
    def get_connection(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='hospital_db',
                                                 user='root',
                                                 password='1mTh3B0ss4ndY0ur343sl4v3')
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)

        return connection

    def close_connection(self, connection):
        if connection:
            connection.close()

    def to_get_by(self, doctor_id):
        try:
            connection = self.get_connection()
            cursor = connection.cursor()
            select_query = 'select * from Doctor where Doctor_Id = %s'
            cursor.execute(select_query, (doctor_id,))
            records = cursor.fetchall()
            self.close_connection(connection)
        except (Exception, mysql.connector.Error) as error:
            print("Error while getting data", error)

        return records

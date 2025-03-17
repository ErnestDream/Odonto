import psycopg2
from psycopg2 import errors

class Telefono:
    
    """
    Una clase que realiza las operaciones de CRUD para la tabla de telefono

    Attributes:
        idTelefono: El id del telefono
        telefono: El número de teléfono
        idPaciente: El id del paciente al que pertenece el teléfono
        
    """
    def __init__(self, idTelefono, telefono, idPaciente):
        """	
        Inicializa los atributos de la clase
        """

        self.idTelefono = idTelefono
        self.telefono = telefono
        self.idPaciente = idPaciente

    def create(self, conn, cursor):
        """
        Método que inserta en la tabla de create los datos de un objeto introducido por el usuario
        Args:
            conn: La conexión a la base de datos
            cursor: El cursor de la base de datos
        Returns:
        """
            
        query = """
        INSERT INTO telefono (idTelefono, telefono, idPaciente)
        VALUES (%s, %s, %s)
        """

        try:
            cursor.execute(query, (
                self.idTelefono, self.telefono, self.idPaciente
            ))
            conn.commit()
            print("Telefono insertado correctamente.")
        except psycopg2.Error as e:
            print(f"Error al insertar el telefono: {e}")
        
    @staticmethod
    def read(cursor, idTelefono):
        """
        Método selección de la tabla, o lectura de los datos si lo prefieres
        Args:
            cursor: El cursor de la conexión a la base de datos
            idTelefono: El id del telefono a buscar
        Returns:
            cursor.fetchone() : La tupla con los datos del telefono
        """
        query='SELECT * FROM telefono WHERE idTelefono = %s ;'
        cursor.execute(query, (idTelefono, ))
        return cursor.fetchone()
        
    def update(self, conn, cursor, telefono):
        """
        Método actualización de la tupla, o actualizacion de los datos
        Args:
            conn: La conexión a la base de datos
            cursor: El cursor de la base de datos
        Returns:
            cursor.fetchone() : La tupla con los datos del
        """
        resultado = Telefono.read(cursor, self.idTelefono)
        print("Datos actuales del telefono:")
        print(f"Telefono: {resultado[1]}")
        
        query = """
        UPDATE telefono
        SET telefono = %s
        WHERE idTelefono = %s
        """
        cursor.execute(query, (self.telefono, self.idTelefono))
        
        print("Cambios guardados correctamente.")
        resultado = Telefono.read(cursor, self.idTelefono)
        print("Nuevos datos del telefono:")
        print(f"Telefono: {resultado[1]}")
        
        conn.commit()
        return cursor.fetchone()
        
    @staticmethod
    def delete(conn, cursor, idTelefono):
        """"
        Método que borra un objeto de la tabla telefono
        Args:
            conn: La conexión a la base de datos
            cursor: El cursor de la base de datos
            idTelefono: El id del telefono a borrar
        Returns:
            bool: True si se borra el telefono, False si no se borra    
        """
        try:
            if cursor.rowcount > 0:
                query = "DELETE FROM telefono WHERE idTelefono = %s"
                cursor.execute(query, (idTelefono,))
                conn.commit()
                cursor.rowcount
                return True
            else:
                print("No se encontró el telefono con el id proporcionado.")
                return False
        except errors.ForeignKeyViolation as e:
            print(f"Error al borrar el telefono: {e}")
            return False



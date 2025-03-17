import psycopg2
from psycopg2 import errors

class Profesional:

    
    """
    Una clase que realiza las operaciones de CRUD para la tabla de profesional

    Attributes:
        IdOdontologo: El id del odontólogo que es profesional
        Cedula: La cedula del odontólogo que es profesional
        
    """

    def __init__(self, idOdontologo, cedula):
        """
        Inicializa los atributos de la clase
        """
        self.idOdontologo = idOdontologo
        self.cedula = cedula

    def create(self, conn, cursor):
        """
        Método que inserta en la tabla de profesional los datos de un objeto
        Args:
            conn: La conexión a la base de datos
            cursor: El cursor de la base de datos
        Returns:
        """

        query = """
        INSERT INTO profesional (idOdontologo, cedula)
        VALUES (%s, %s)
        """

        try:
            cursor.execute(query, (
                self.idOdontologo, self.cedula
            ))
            conn.commit()
            print("Profesional insertado correctamente.")
        except psycopg2.Error as e:
            print(f"Error al insertar el profesional: {e}")
    
    @staticmethod
    def read(cursor, idOdontologo):
        """	
        Método selección de la tabla, o lectura de los datos si lo prefieres
        Args:
            cursor: El cursor de la conexión a la base de datos
            idOdontologo: El id del odontologo a buscar
        Returns:
            cursor.fetchone() : La tupla con los datos del profesional
        """
        query='SELECT * FROM profesional WHERE idOdontologo = %s ;'
        cursor.execute(query, (idOdontologo, ))
        return cursor.fetchone()
    
    def update(self, conn, cursor, profesional):
        """	
        Método actualización de la tupla, o actualizacion de los datos
        Args:
            conn: La conexión a la base de datos
            cursor: El cursor de la base de datos
            profesional: El objeto con los datos actualizados
        Returns:
            cursor.fetchone() : La tupla con los datos del profesional
        """
        resultado = Profesional.read(cursor, self.idOdontologo)
        print("Datos actuales del profesional:")
        print(f"Cedula: {resultado[1]}")
        
        query = """
        UPDATE profesional
        SET cedula = %s
        WHERE idOdontologo = %s
        """
        cursor.execute(query, (self.cedula, self.idOdontologo))
        
        print("Cambios guardados correctamente.")
        resultado = Profesional.read(cursor, self.idOdontologo)
        print("Nuevos datos del profesional:")
        print(f"Cedula: {resultado[1]}")
        
        conn.commit()
        return cursor.fetchone()
    
    @staticmethod
    def delete(conn, cursor, idOdontologo):
        """"
        Método que borra un objeto de la tabla profesional
        Args:
            conn: La conexión a la base de datos
            cursor: El cursor de la base de datos
            idOdontologo: El id del odontólogo que es profesional
        Returns:
            bool: True si se borra el profesional, False si no
        """
        try:
            if cursor.rowcount > 0:
                query = "DELETE FROM profesional WHERE idOdontologo = %s"
                cursor.execute(query, (idOdontologo,))
                conn.commit()
                cursor.rowcount
                return True
            else:
                print("No se encontró el profesional con el id proporcionado.")
                return False
        except errors.ForeignKeyViolation as e:
            print(f"Error al borrar el profesional: {e}")
            return False    

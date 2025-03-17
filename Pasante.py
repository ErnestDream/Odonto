import psycopg2
from psycopg2 import errors

class Pasante:

    """
    Una clase que realiza las operaciones de CRUD para la tabla de pasante

    Attributes:
        IdOdontologo: El id del odontologo que es pasante
        Institucion: La institucion donde el odontologo realiza su pasantia
    """

    def __init__(self, idOdontologo, institucion):
        """
        Inicializa los atributos de la clase
        """
        self.idOdontologo = idOdontologo
        self.institucion = institucion

    def create(self, conn, cursor):
        """
        Metodo que inserta en la tabla de pasante los datos de un objeto
        Args:
            conn: La conexión a la base de datos
            cursor: El cursor de la base de datos
        Returns:
        """
            
        query = """
        INSERT INTO pasante (idOdontologo, institucion)
        VALUES (%s, %s)
        """

        try:
            cursor.execute(query, (
                self.idOdontologo, self.institucion
            ))
            conn.commit()
            print("Pasante insertado correctamente.")
        except psycopg2.Error as e:
            print(f"Error al insertar el pasante: {e}")
    
    @staticmethod
    def read(cursor, idOdontologo):
        """	
        Método selección de la tabla, o lectura de los datos si lo prefieres
        Args:
            cursor: El cursor de la conexión a la base de datos
            idOdontologo: El id del odontologo a buscar
        Returns:
            cursor.fetchone() : La tupla con los datos del pasante
        """
        query='SELECT * FROM pasante WHERE idOdontologo = %s ;'
        cursor.execute(query, (idOdontologo, ))
        return cursor.fetchone()
    
    def update(self, conn, cursor, pasante):
        """	
        Método actualización de la tupla, o actualizacion de los datos
        Args:
            conn: La conexión a la base de datos
            cursor: El cursor de la base de datos
        Returns:
            cursor.fetchone() : La tupla con los datos del pasante
        """
        resultado = Pasante.read(cursor, self.idOdontologo)
        print("Datos actuales del pasante:")
        print(f"Institucion: {resultado[1]}")
        
        query = """
        UPDATE pasante
        SET institucion = %s
        WHERE idOdontologo = %s
        """
        cursor.execute(query, (self.institucion, self.idOdontologo))
        
        print("Cambios guardados correctamente.")
        resultado = Pasante.read(cursor, self.idOdontologo)
        print("Nuevos datos del pasante:")
        print(f"Institucion: {resultado[1]}")
        
        conn.commit()
        return cursor.fetchone()
    
    @staticmethod
    def delete(conn, cursor, idOdontologo):
        """
        Método que borra una tupla de la tabla pasante
        Args:
            conn: La conexión a la base de datos
            cursor: El cursor de la base de datos
            idOdontologo: El id del odontologo a borrar
        Returns:
            bool: True si se borra la tupla, False en caso contrario
        """
        try:
            if cursor.rowcount > 0:
                query = "DELETE FROM pasante WHERE idOdontologo = %s"
                cursor.execute(query, (idOdontologo,))
                conn.commit()
                cursor.rowcount
                return True
            else:
                print("No se encontró el pasante.")
                return False
        except errors.ForeignKeyViolation as e:
            print(f"Error al borrar el pasante: {e}")
            return False

import psycopg2

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
        """
        query='SELECT * FROM pasante WHERE idOdontologo = %s ;'
        cursor.execute(query, (idOdontologo, ))
        return cursor.fetchone()
    
    def update(self, conn, cursor, pasante):
        """	
        Método actualización de la tupla, o actualizacion de los datos
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
        """
        print("Datos borrados:")
        resultado = Pasante.read(cursor, idOdontologo)
        print("Datos del pasante:")
        print(f"Institucion: {resultado[1]}")
        
        query = "DELETE FROM pasante WHERE idOdontologo = %s"
        cursor.execute(query, (idOdontologo,))
        conn.commit()
        return cursor.rowcount

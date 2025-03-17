
import psycopg2


class Pasante:

    """
    Una clase que realiza las operaciones de CRUD para la tabla de pasante

    Attributes:
        
    """

    def __init__(self, idOdontologo, institucion):
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
        query='SELECT * FROM pasante WHERE idOdontologo = %s ;'
        cursor.execute(query, (idOdontologo, ))
        return cursor.fetchone()
    
    def update(self, conn, cursor, pasante):
        resultado = Pasante.read(cursor, self.idOdontologo)
        print("Datos del pasante:")
        print(f"Institucion: {resultado[1]}")
        
        query = """
        UPDATE pasante
        SET institucion = %s
        WHERE idOdontologo = %s
        """
        cursor.execute(query, (self.institucion, self.idOdontologo))
        
        print("Cambios guardados correctamente.")
        resultado = Pasante.read(cursor, self.idOdontologo)
        print("Datos del pasante:")
        print(f"Institucion: {resultado[1]}")
        
        conn.commit()
        return cursor.fetchone()
    
    def delete(conn, cursor, idOdontologo):
        print("Datos borrados:")
        resultado = Pasante.read(cursor, idOdontologo)
        print("Datos del pasante:")
        print(f"Institucion: {resultado[1]}")
        
        query = "DELETE FROM pasante WHERE idOdontologo = %s"
        cursor.execute(query, (idOdontologo,))
        conn.commit()
        return cursor.rowcount

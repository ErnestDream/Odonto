import psycopg2

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
        """
        query='SELECT * FROM profesional WHERE idOdontologo = %s ;'
        cursor.execute(query, (idOdontologo, ))
        return cursor.fetchone()
    
    def update(self, conn, cursor, profesional):
        """	
        Método actualización de la tupla, o actualizacion de los datos
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
        """
        print("Datos borrados:")
        resultado = Profesional.read(cursor, idOdontologo)
        print("Datos del profesional:")
        print(f"Institucion: {resultado[1]}")
        
        query = "DELETE FROM profesional WHERE idOdontologo = %s"
        cursor.execute(query, (idOdontologo,))
        conn.commit()
        return cursor.rowcount

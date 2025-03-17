import psycopg2


class Profesional:

    
    """
    Una clase que realiza las operaciones de CRUD para la tabla de profesional

    Attributes:
        
    """

    def __init__(self, idOdontologo, cedula):
        self.idOdontologo = idOdontologo
        self.cedula = cedula

    def create(self, conn, cursor):
        """
        Metodo que inserta en la tabla de profesional los datos de un objeto
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
        query='SELECT * FROM profesional WHERE idOdontologo = %s ;'
        cursor.execute(query, (idOdontologo, ))
        return cursor.fetchone()
    
    def update(self, conn, cursor, profesional):
        resultado = Profesional.read(cursor, self.idOdontologo)
        print("Datos del profesional:")
        print(f"Cedula: {resultado[1]}")
        
        query = """
        UPDATE profesional
        SET cedula = %s
        WHERE idOdontologo = %s
        """
        cursor.execute(query, (self.cedula, self.idOdontologo))
        
        print("Cambios guardados correctamente.")
        resultado = Profesional.read(cursor, self.idOdontologo)
        print("Datos del profesional:")
        print(f"Cedula: {resultado[1]}")
        
        conn.commit()
        return cursor.fetchone()
    
    def delete(conn, cursor, idOdontologo):
        print("Datos borrados:")
        resultado = Profesional.read(cursor, idOdontologo)
        print("Datos del profesional:")
        print(f"Institucion: {resultado[1]}")
        
        query = "DELETE FROM profesional WHERE idOdontologo = %s"
        cursor.execute(query, (idOdontologo,))
        conn.commit()
        return cursor.rowcount

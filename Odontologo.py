
import psycopg2


class Odontologo:

    """
    Una clase que realiza las operaciones de CRUD para la tabla de odontologo

    Attributes:
        
    """


    def __init__(self, idOdontologo, nombre, primerApellido, segundoApellido, telefono, fechaNacimiento):
        self.idOdontologo = idOdontologo
        self.nombre = nombre
        self.primerApellido = primerApellido
        self.segundoApellido = segundoApellido
        self.telefono = telefono
        self.fechaNacimiento = fechaNacimiento

    def create(self, conn, cursor):

        """
        Metodo que inserta en la tabla de odontologo los datos de un objeto
        """

        query = """
        INSERT INTO odontologo (idOdontologo, nombre, primerApellido, segundoApellido, telefono, fechaNacimiento)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (
                self.idOdontologo, self.nombre, self.primerApellido,
                self.segundoApellido, self.telefono, self.fechaNacimiento
            ))
            conn.commit()
            print("Odontólogo insertado correctamente.")
        except psycopg2.Error as e:
            print(f"Error al insertar el odontólogo: {e}")

    #--->   Metodo seleccion de la tabla, o lectura de los datos si lo prefieres <---#

    @staticmethod
    def read(cursor, idOdontologo):
        query='SELECT * FROM odontologo WHERE idOdontologo = %s ;'
        cursor.execute(query, (idOdontologo, ))
        return cursor.fetchone()

    #--->   Metodo actualizacion de la tupla, o actualizacion de los datos  <---#

    def update(self, conn, cursor, odontologo):
        
        resultado = Odontologo.read(cursor, self.idOdontologo)
        print("Datos del odontólogo:")
        print(f"Nombre: {resultado[1]} {resultado[2]} {resultado[3]}")
        print(f"Teléfono: {resultado[4]}")
        print(f"Fecha de nacimiento: {resultado[5]}")

        query = """
        UPDATE odontologo
        SET nombre = %s, primerApellido = %s, segundoApellido = %s, telefono = %s, fechaNacimiento = %s
        WHERE idOdontologo = %s
        """
        cursor.execute(query, (self.nombre, self.primerApellido, self.segundoApellido, 
                               self.telefono, self.fechaNacimiento, self.idOdontologo))
        
        print("Cambios guardados correctamente.")
        resultado = Odontologo.read(cursor, self.idOdontologo)
        print("Datos del odontólogo:")
        print(f"Nombre: {resultado[1]} {resultado[2]} {resultado[3]}")
        print(f"Teléfono: {resultado[4]}")
        print(f"Fecha de nacimiento: {resultado[5]}")

        conn.commit()
        return cursor.fetchone()

    #--->   Metodo eliminacion de la tupla, o lectura de los datos si lo prefieres <---#

    @staticmethod
    def delete(conn, cursor, idOdontologo):

        print("Datos borrados:")
        resultado = Odontologo.read(cursor, idOdontologo)
        print("Datos del odontólogo:")
        print(f"Nombre: {resultado[1]} {resultado[2]} {resultado[3]}")
        print(f"Teléfono: {resultado[4]}")
        print(f"Fecha de nacimiento: {resultado[5]}")

        query = "DELETE FROM odontologo WHERE idOdontologo = %s"
        cursor.execute(query, (idOdontologo,))
        conn.commit()
        return cursor.rowcount
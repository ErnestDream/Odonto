
import psycopg2


class Paciente:
    
    """
    Una clase que realiza las operaciones de CRUD para la tabla de paciente

    Attributes:
        
    """

    def __init__(self, idPaciente, nombre, primerApellido, segundoApellido, fechaNacimiento, idOdontologo):
        self.idPaciente = idPaciente
        self.nombre = nombre
        self.primerApellido = primerApellido
        self.segundoApellido = segundoApellido
        self.fechaNacimiento = fechaNacimiento
        self.idOdontologo = idOdontologo

    def create(self, conn, cursor):

        """
        Metodo que inserta en la tabla de paciente los datos de un objeto
        """

        query = """
        INSERT INTO paciente (idPaciente, nombre, primerApellido, segundoApellido, fechaNacimiento, idOdontologo)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (
                self.idPaciente, self.nombre, self.primerApellido,
                self.segundoApellido, self.fechaNacimiento,
                self.idOdontologo
            ))
            conn.commit()
            print("Paciente insertado correctamente.")
        except psycopg2.Error as e:
            print(f"Error al insertar el paciente: {e}")

    #--->   Metodo seleccion de la tabla, o lectura de los datos si lo prefieres <---#

    @staticmethod
    def read(cursor, idPaciente):
        query='SELECT * FROM paciente WHERE idPaciente = %s ;'
        cursor.execute(query, (idPaciente, ))
        return cursor.fetchone()

    #--->   Metodo actualizacion de la tupla, o actualizacion de los datos  <---#

    def update(self, conn, cursor, paciente):
        
        resultado = Paciente.read(cursor, self.idPaciente)
        print("Datos del paciente:")
        print(f"Nombre: {resultado[1]} {resultado[2]} {resultado[3]}")
        print(f"Teléfono: {resultado[4]}")
        print(f"Fecha de nacimiento: {resultado[5]}")

        query = """
        UPDATE paciente
        SET nombre = %s, primerApellido = %s, segundoApellido = %s, fechaNacimiento = %s
        WHERE idPaciente = %s
        """
        cursor.execute(query, (self.nombre, self.primerApellido, self.segundoApellido,
                                self.fechaNacimiento, self.idPaciente))
        
        resultado = Paciente.read(cursor, self.idPaciente)
        print("Datos del paciente:")
        print(f"Nombre: {resultado[1]} {resultado[2]} {resultado[3]}")
        print(f"Teléfono: {resultado[4]}")
        print(f"Fecha de nacimiento: {resultado[5]}")

        conn.commit()
        return cursor.fetchone()
    
    def delete(conn, cursor, idPaciente):

        print("Datos borrados:")
        resultado = Paciente.read(cursor, idPaciente)
        print("Datos del paciente:")
        print(f"Nombre: {resultado[1]} {resultado[2]} {resultado[3]}")
        print(f"Teléfono: {resultado[4]}")
        print(f"Fecha de nacimiento: {resultado[5]}")

        query = "DELETE FROM paciente WHERE idPaciente = %s"
        cursor.execute(query, (idPaciente,))
        conn.commit()
        return cursor.rowcount

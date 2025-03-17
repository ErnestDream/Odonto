import psycopg2

class Paciente:
    
    """
    Una clase que realiza las operaciones de CRUD para la tabla de paciente

    Attributes:
        IdPaciente: El id del paciente
        Nombre: El nombre del paciente
        PrimerApellido: El primer apellido del paciente
        SegundoApellido: El segundo apellido del paciente
        FechaNacimiento: La fecha de nacimiento del paciente
        IdOdontologo: El id del odontólogo que atiende al paciente
        
    """

    def __init__(self, idPaciente, nombre, primerApellido, segundoApellido, fechaNacimiento, idOdontologo):
        """
        Inicializa los atributos de la clase
        """
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

    @staticmethod
    def read(cursor, idPaciente):
        """
        Método selección de la tabla, o lectura de los datos si lo prefieres
        """
        query='SELECT * FROM paciente WHERE idPaciente = %s ;'
        cursor.execute(query, (idPaciente, ))
        return cursor.fetchone()

    def update(self, conn, cursor, paciente):
        """	
        Método que actualiza en la tabla de paciente los datos de un objeto
        """


        resultado = Paciente.read(cursor, self.idPaciente)
        print("Datos del paciente actuales:")
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
        print("Cambios en los datos del paciente:")
        print(f"Nombre: {resultado[1]} {resultado[2]} {resultado[3]}")
        print(f"Teléfono: {resultado[4]}")
        print(f"Fecha de nacimiento: {resultado[5]}")

        conn.commit()
        return cursor.fetchone()
    
    @staticmethod
    def delete(conn, cursor, idPaciente):
        """"
        Método que borra en la tabla de paciente los datos de un objeto
        """
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

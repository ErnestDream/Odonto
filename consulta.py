import psycopg2

class Consulta:

    
    """
    Una clase que realiza las operaciones de CRUD para la tabla de consulta

    Attributes:
        
    """

    def __init__(self, idConsulta, fecha, horaInicio, horaFin, motivo, idPaciente):
        self.idConsulta = idConsulta
        self.fecha = fecha
        self.horaInicio = horaInicio
        self.horaFin = horaFin
        self.motivo = motivo
        self.idPaciente = idPaciente
    
    def create(self, conn, cursor):

        """
        Metodo que inserta en la tabla de consulta los datos de un objeto
        """

        query = """
        INSERT INTO consulta (idConsulta, fecha, horaInicio, horaFin, motivo, idPaciente)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (
                self.idConsulta, self.fecha, self.horaInicio,
                self.horaFin, self.motivo, self.idPaciente
            ))
            conn.commit()
            print("Consulta insertada correctamente.")
        except psycopg2.Error as e:
            print(f"Error al insertar la consulta: {e}")	

    @staticmethod
    def read(cursor, idConsulta):
        query='SELECT * FROM consulta WHERE idConsulta = %s ;'
        cursor.execute(query, (idConsulta, ))
        return cursor.fetchone()
    
    def update(self, conn, cursor, consulta):
        resultado = Consulta.read(cursor, self.idConsulta)
        print("Datos de la consulta:")
        print(f"Fecha: {resultado[1]}")
        print(f"Hora de inicio: {resultado[2]}")
        print(f"Hora de fin: {resultado[3]}")
        print(f"Motivo: {resultado[4]}")
        print(f"ID Paciente: {resultado[5]}")
        
        query = """
        UPDATE consulta
        SET fecha = %s, horaInicio = %s, horaFin = %s, motivo = %s, idPaciente = %s
        WHERE idConsulta = %s
        """
        cursor.execute(query, (self.fecha, self.horaInicio, self.horaFin, 
                               self.motivo, self.idPaciente, self.idConsulta))
        
        print("Cambios guardados correctamente.")
        resultado = Consulta.read(cursor, self.idConsulta)
        print("Datos de la consulta:")
        print(f"Fecha: {resultado[1]}")
        print(f"Hora de inicio: {resultado[2]}")
        print(f"Hora de fin: {resultado[3]}")
        print(f"Motivo: {resultado[4]}")
        print(f"ID Paciente: {resultado[5]}")
        
        conn.commit()
        return cursor.fetchone()
    
    @staticmethod
    def delete(conn, cursor, idConsulta):
        print("Datos borrados:")
        resultado = Consulta.read(cursor, idConsulta)
        print("Datos de la consulta:")
        print(f"Fecha: {resultado[1]}")
        print(f"Hora de inicio: {resultado[2]}")
        print(f"Hora de fin: {resultado[3]}")
        print(f"Motivo: {resultado[4]}")
        print(f"ID Paciente: {resultado[5]}")
        
        query = "DELETE FROM consulta WHERE idConsulta = %s"
        cursor.execute(query, (idConsulta,))
        conn.commit()
        return cursor.rowcount

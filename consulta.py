import psycopg2
from psycopg2 import Error

class Consulta:

    
    """
    Una clase que realiza las operaciones de CRUD para la tabla de consulta

    Attributes:
        idConsulta: El id de la consulta
        fecha: La fecha de la consulta
        horaInicio: La hora de inicio de la consulta
        horaFin: La hora de fin de la consulta
        motivo: El motivo de la consulta
        idPaciente: El id del paciente que asistió a la consulta
        
    """

    def __init__(self, idConsulta, fecha, horaInicio, horaFin, motivo, idPaciente):
        """
        Inicializa los atributos de la clase
        """
        self.idConsulta = idConsulta
        self.fecha = fecha
        self.horaInicio = horaInicio
        self.horaFin = horaFin
        self.motivo = motivo
        self.idPaciente = idPaciente
    
    def create(self, conn, cursor):

        """
        Método que inserta en la tabla de consulta los datos de un objeto
    
        Args:
            conn: La conexión a la base de datos
            cursor: El cursor de la base de datos
        Returns:
        
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
        """	
        Método selección de la tabla, o lectura de los datos si lo prefieres

        args:
            cursor: El cursor de la base de datos
            idConsulta: El id de la consulta a leer
        Returns:
            cursor.fetchone(): La fila
        """
        query='SELECT * FROM consulta WHERE idConsulta = %s ;'
        cursor.execute(query, (idConsulta, ))
        return cursor.fetchone()
    
    def update(self, conn, cursor, consulta):
        """
        Método que actualiza en la tabla de consulta los datos de un objeto

        Args:
            conn: La conexión a la base de datos
            cursor: El cursor de la base de datos
            consulta: El objeto con los datos actualizados  
        Returns:
            cursor.fetchone(): La fila actualizada
        """
        resultado = Consulta.read(cursor, self.idConsulta)
        print("Datos actuales de la consulta:")
        print(f"Fecha: {resultado[1]}")
        print(f"Hora de inicio: {resultado[2]}")
        print(f"Hora de fin: {resultado[3]}")
        print(f"Motivo: {resultado[4]}")
        print(f"ID del paciente: {resultado[5]}")
        
        query = """
        UPDATE consulta
        SET fecha = %s, horaInicio = %s, horaFin = %s, motivo = %s, idPaciente = %s
        WHERE idConsulta = %s
        """
        cursor.execute(query, (self.fecha, self.horaInicio, self.horaFin, 
                               self.motivo, self.idPaciente, self.idConsulta))
        
        print("Cambios guardados correctamente.")
        resultado = Consulta.read(cursor, self.idConsulta)
        print("Nuevos datos de la consulta:")
        print(f"Fecha: {resultado[1]}")
        print(f"Hora de inicio: {resultado[2]}")
        print(f"Hora de fin: {resultado[3]}")
        print(f"Motivo: {resultado[4]}")
        print(f"ID del paciente: {resultado[5]}")
        
        conn.commit()
        return cursor.fetchone()
    
    @staticmethod
    def delete(conn, cursor, idConsulta):
        """
        Método que borra de la tabla de consulta los datos de un objeto

        Args:
            conn: La conexión a la base de datos
            cursor: El cursor de la base de datos
            idConsulta: El id de la consulta a borrar
        Returns:
            cursor.rowcount: El número de filas afectadas
        """
        try:
            if cursor.rowcount > 0:
                query = "DELETE FROM consulta WHERE idConsulta = %s"
                cursor.execute(query, (idConsulta,))
                conn.commit()
                cursor.rowcount
                return True
            else:
                print("No se encontró la consulta.")
                return False
        except psycopg2.Error as e:
            print("Error al borrar la consulta: ", e)
            return False
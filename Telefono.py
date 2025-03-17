import psycopg2


class Telefono:
    
    """
    Una clase que realiza las operaciones de CRUD para la tabla de telefono

    Attributes:
        idTelefono: El id del telefono
        telefono: El número de teléfono
        idPaciente: El id del paciente al que pertenece el teléfono
        
    """
    def __init__(self, idTelefono, telefono, idPaciente):
        """	
        Inicializa los atributos de la clase
        """

        self.idTelefono = idTelefono
        self.telefono = telefono
        self.idPaciente = idPaciente

    def create(self, conn, cursor):
        """
        Método que inserta en la tabla de create los datos de un objeto introducido por el usuario
        """
            
        query = """
        INSERT INTO telefono (idTelefono, telefono, idPaciente)
        VALUES (%s, %s, %s)
        """

        try:
            cursor.execute(query, (
                self.idTelefono, self.telefono, self.idPaciente
            ))
            conn.commit()
            print("Telefono insertado correctamente.")
        except psycopg2.Error as e:
            print(f"Error al insertar el telefono: {e}")
        
    @staticmethod
    def read(cursor, idTelefono):
        """
        Método selección de la tabla, o lectura de los datos si lo prefieres
        """
        query='SELECT * FROM telefono WHERE idTelefono = %s ;'
        cursor.execute(query, (idTelefono, ))
        return cursor.fetchone()
        
    def update(self, conn, cursor, telefono):
        """
        Método actualización de la tupla, o actualizacion de los datos
        """
        resultado = Telefono.read(cursor, self.idTelefono)
        print("Datos actuales del telefono:")
        print(f"Telefono: {resultado[1]}")
        
        query = """
        UPDATE telefono
        SET telefono = %s
        WHERE idTelefono = %s
        """
        cursor.execute(query, (self.telefono, self.idTelefono))
        
        print("Cambios guardados correctamente.")
        resultado = Telefono.read(cursor, self.idTelefono)
        print("Nuevos datos del telefono:")
        print(f"Telefono: {resultado[1]}")
        
        conn.commit()
        return cursor.fetchone()
        
    @staticmethod
    def delete(conn, cursor, idTelefono):
        """"
        Método que borra un objeto de la tabla telefono
        """
        resultado = Telefono.read(cursor, idTelefono)
        if resultado:
            print("Datos borrados del teléfono del paciente:")
            print(f"ID: {resultado[0]}")
            print(f"Número de telélefono: {resultado[1]}")
            print(f"Paciente al que pertenece: {resultado[2]}")
        
        query = "DELETE FROM telefono WHERE idTelefono = %s"
        cursor.execute(query, (idTelefono,))
        conn.commit()
        return cursor.rowcount



import psycopg2

def conexionBD(dbname, user, password, host, port):
    """
    Conexta a la base de datos por medio de la biblioteca psycopg2

    Args:
        dbname  (string):   nombre del BD
        user    (string):   usuario de la bd
        password    (string):   contrasenia de la bd
        host    (string):   host de la bd
        port    (string):   puerto de la bd

    Returns:
        TO DO conn, cursor

    Examples:
        conexionBD(myBD, ernestd, p4ssw0rd, localhost, 5432)
    """

    try:
        #se declara una variable conn que... TO DO 
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        #TO DO 
        cursor = conn.cursor()
        return conn, cursor
    except psycopg2.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None, None


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

############################################# Clase de los pacientes  ########################################################

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
    
class Consulta:
    def __init__(self, idConsulta, fecha, horaInicio, horaFin, motivo, idPaciente):
        self.idConsulta = idConsulta
        self.fecha = fecha
        self.horaInicio = horaInicio
        self.horaFin = horaFin
        self.motivo = motivo
        self.idPaciente = idPaciente
    
    def create(self, conn, cursor):
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
    
class Pasante:
    def __init__(self, idOdontologo, institucion):
        self.idOdontologo = idOdontologo
        self.institucion = institucion

    def create(self, conn, cursor):
            
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
            
class Profesional:
    def __init__(self, idOdontologo, cedula):
        self.idOdontologo = idOdontologo
        self.cedula = cedula

    def create(self, conn, cursor):
            
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
    
class Telefono:
    def __init__(self, idTelefono, telefono, idPaciente):
        self.idTelefono = idTelefono
        self.telefono = telefono
        self.idPaciente = idPaciente

    def create(self, conn, cursor):
            
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
    def read(cursor, idOdontologo):
        query='SELECT * FROM telefono WHERE idOdontologo = %s ;'
        cursor.execute(query, (idOdontologo, ))
        return cursor.fetchone()
        
    
    def update(self, conn, cursor, telefono):
        resultado = Telefono.read(cursor, self.idTelefono)
        print("Datos del telefono:")
        print(f"Telefono: {resultado[1]}")
        
        query = """
        UPDATE telefono
        SET telefono = %s
        WHERE idTelefono = %s
        """
        cursor.execute(query, (self.telefono, self.idTelefono))
        
        print("Cambios guardados correctamente.")
        resultado = Telefono.read(cursor, self.idTelefono)
        print("Datos del telefono:")
        print(f"Telefono: {resultado[1]}")
        
        conn.commit()
        return cursor.fetchone()
        
    
    def delete(conn, cursor, idOdontologo):
        print("Datos borrados:")
        resultado = Telefono.read(cursor, idOdontologo)
        print("Datos del telefono:")
        print(f"Telefono: {resultado[1]}")
        
        query = "DELETE FROM telefono WHERE idTelefono = %s"
        cursor.execute(query, (idOdontologo,))
        conn.commit()
        return cursor.rowcount

conn, cursor = conexionBD(
    dbname = 'odontodos',
    user = 'postgres',
    password = 'posgresito',
    host = 'localhost',
    port = '5432'
)

############################################# Insertar datos  ########################################################

# Verificar que la conexión y el cursor sean válidos
#if conn and cursor:
#    # Crear un objeto Odontologo con los datos de prueba
#    odontologo = Odontologo(
#    idOdontologo=input("ID: "),
#    nombre=input("Nombre: "),             
#    primerApellido=input("Primer apellido: "),
#    segundoApellido=input("Segundo apellido: "),
#    telefono=input("Telefono: "),
#    fechaNacimiento=input("Fecha de nacimiento (YYYY-MM-DD): "),
#    )

#odontologo.create(conn, cursor)

############################################# Seleccionar datos  ########################################################

#resultado = Odontologo.read(cursor, idOdontologo=1)
#if resultado:
#    print("Datos del odontólogo:")
#    print(f"ID: {resultado[0]}")
#    print(f"Nombre: {resultado[1]} {resultado[2]} {resultado[3]}")
#    print(f"Teléfono: {resultado[4]}")
#    print(f"Fecha de nacimiento: {resultado[5]}")
#else:
#    print("No se encontró ningún odontólogo con ese ID.")

############################################# Actualizar datos  ########################################################
    
#odontologo = Odontologo(
#    idOdontologo=1,                      # ID del odontólogo a actualizar
#    nombre="Juan",                       # Nuevo nombre
#    primerApellido="Perez",              # Nuevo primer apellido
#    segundoApellido="Gomez",             # Nuevo segundo apellido
#    telefono="1234567890",               # Nuevo teléfono
#    fechaNacimiento="1980-01-01"         # Nueva fecha de nacimiento
#)

#odontologo.update(conn, cursor, odontologo)

############################################# Eliminar datos  ########################################################


#Odontologo.delete(conn, cursor, idOdontologo=9)

#Cerrar la conexión y el cursor


############################################# Insertar datos paciente ########################################################

# Verificar que la conexión y el cursor sean válidos

#if conn and cursor:
#    # Crear un objeto Odontologo con los datos de prueba
#    paciente = Paciente(
#    idPaciente=input("ID: "),
#    nombre=input("Nombre: "),             
#    primerApellido=input("Primer apellido: "),
#    segundoApellido=input("Segundo apellido: "),
#    fechaNacimiento=input("Fecha de nacimiento (YYYY-MM-DD): "),
#    idOdontologo=input("ID Odontologo: ")
#    )
#
#paciente.create(conn, cursor)

############################################# Seleccionar datos paciente ########################################################

#resultado = Paciente.read(cursor, idPaciente=5)
#if resultado:
#    print("Datos del paciente:")
#    print(f"ID: {resultado[0]}")
#    print(f"Nombre: {resultado[1]} {resultado[2]} {resultado[3]}")
#    print(f"Fecha de nacimiento: {resultado[4]}")
#    print(f"Odontólogo: {resultado[5]}")
#else:
#    print("No se encontró ningún paciente con ese ID.")

############################################# Actualizar datos paciente ########################################################

#paciente = Paciente(
#    idPaciente=5,                           # ID del odontólogo a actualizar
#    nombre="adios",                         # Nuevo nombre
#    primerApellido="z",                     # Nuevo primer apellido
#    segundoApellido="z",                    # Nuevo segundo apellido
#    fechaNacimiento="2000-01-01",            # Nueva fecha de nacimiento
#    idOdontologo=3
#)
#
#paciente.update(conn, cursor, paciente)

############################################# Eliminar datos paciente ########################################################

#Paciente.delete(conn, cursor, idPaciente=5)

############################################# Insertar datos consulta ########################################################

# Verificar que la conexión y el cursor sean válidos
#if conn and cursor:
#    # Crear un objeto Odontologo con los datos de prueba
#    consulta = Consulta(
#    idConsulta=input("ID: "),
#    fecha=input("Fecha: "),
#    horaInicio=input("Hora de inicio: "),
#    horaFin=input("Hora de fin: "),
#    motivo=input("Motivo: "),
#    idPaciente=input("ID Paciente: ")
#    )

#consulta.create(conn, cursor)

############################################# Seleccionar datos consulta ########################################################

#resultado = Consulta.read(cursor, idConsulta=4)
#if resultado:
#    print("Datos del consulta:")
#    print(f"ID: {resultado[0]}")
#    print(f"Fecha: {resultado[1]}")
#    print(f"Hora de inicio: {resultado[2]}")
#    print(f"Hora de fin: {resultado[3]}")
#    print(f"Motivo: {resultado[4]}")
#    print(f"ID Paciente: {resultado[5]}")
#else:
#    print("No se encontró ninguna consulta con ese ID.")

############################################# Actualizar datos consulta ########################################################

#consulta = Consulta(
#    idConsulta=4,                           # ID del odontólogo a actualizar
#    fecha="2021-01-01",                     # Nueva fecha
#    horaInicio="10:00",                     # Nueva hora de inicio 
#    horaFin="11:00",                        # Nueva hora de fin
#    motivo="Caries",                        # Nuevo motivo
#    idPaciente=100001                            # Nuevo ID Paciente
#)
#
#consulta.update(conn, cursor, consulta)

############################################# Eliminar datos consulta ########################################################

# Consulta.delete(conn, cursor, idConsulta=4)

############################################# Insertar datos pasante ########################################################

# Verificar que la conexión y el cursor sean válidos
#if conn and cursor:
#    # Crear un objeto Odontologo con los datos de prueba
#    pasante = Pasante(
#    idOdontologo=input("ID: "),
#    institucion=input("Institucion: ")
#    )

#pasante.create(conn, cursor)

############################################# Seleccionar datos pasante ########################################################	

#resultado = Pasante.read(cursor, idOdontologo=4)
#if resultado:
#    print("Datos del pasante:")
#    print(f"ID: {resultado[0]}")
#    print(f"Institucion: {resultado[1]}")
#else:
#    print("No se encontró ninguna consulta con ese ID.")

############################################# Actualizar datos pasante ########################################################

#pasante = Pasante(
#    idOdontologo=4,                           # ID del odontólogo a actualizar
#    institucion="Universidad de la vida"      # Nueva institucion
#)

#pasante.update(conn, cursor, pasante)

############################################# Eliminar datos pasante ########################################################

#Pasante.delete(conn, cursor, idOdontologo=4)

############################################# Insertar datos profesional ########################################################

# Verificar que la conexión y el cursor sean válidos
#if conn and cursor:
#    # Crear un objeto Odontologo con los datos de prueba
#    profesional = Profesional(
#    idOdontologo=input("ID: "),
#    cedula=input("Cedula: ")
#    )

#profesional.create(conn, cursor)

############################################# Seleccionar datos profesional ########################################################	

#resultado = Profesional.read(cursor, idOdontologo=4)
#if resultado:
#    print("Datos del profesional:")
#    print(f"ID: {resultado[0]}")
#    print(f"Cedula: {resultado[1]}")
#else:
#    print("No se encontró ninguna consulta con ese ID.")

############################################# Actualizar datos profesional ########################################################

#profesional = Profesional(
#    idOdontologo=4,                           # ID del odontólogo a actualizar
#    Cedula="Universidad de la vida"      # Nueva institucion
#)

#profesional.update(conn, cursor, profesional)

############################################# Eliminar datos profesional ########################################################

#Profesional.delete(conn, cursor, idOdontologo=4)

############################################# Insertar datos telefono ########################################################

# Verificar que la conexión y el cursor sean válidos
#if conn and cursor:
#    # Crear un objeto Odontologo con los datos de prueba
#    profesional = Profesional(
#    idOdontologo=input("ID: "),
#    cedula=input("Cedula: ")
#)
#
#profesional.create(conn, cursor)
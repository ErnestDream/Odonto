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

############################################# Clase de objeto  ########################################################

"""
    Objeto que funcion para la conexion de a la base de datos

    ------------------------> MODIFICAR AQUI <------------------------
"""
conn, cursor = conexionBD(
    dbname = 'odontodos',
    user = 'postgres',
    password = 'posgresito',
    host = 'localhost',
    port = '5432'
)



############################################# Insertar datos odontologo  ########################################################

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

############################################# Seleccionar datos odontologo ########################################################

#resultado = Odontologo.read(cursor, idOdontologo=1)
#if resultado:
#    print("Datos del odontólogo:")
#    print(f"ID: {resultado[0]}")
#    print(f"Nombre: {resultado[1]} {resultado[2]} {resultado[3]}")
#    print(f"Teléfono: {resultado[4]}")
#    print(f"Fecha de nacimiento: {resultado[5]}")
#else:
#    print("No se encontró ningún odontólogo con ese ID.")

############################################# Actualizar datos odontologo ########################################################
    
#odontologo = Odontologo(
#    idOdontologo=1,                      # ID del odontólogo a actualizar
#    nombre="Juan",                       # Nuevo nombre
#    primerApellido="Perez",              # Nuevo primer apellido
#    segundoApellido="Gomez",             # Nuevo segundo apellido
#    telefono="1234567890",               # Nuevo teléfono
#    fechaNacimiento="1980-01-01"         # Nueva fecha de nacimiento
#)

#odontologo.update(conn, cursor, odontologo)

############################################# Eliminar datos odontologo ########################################################


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
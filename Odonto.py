import psycopg2

from Odontologo import Odontologo
from Paciente import Paciente
from Consulta import Consulta
from Pasante import Pasante
from Profesional import Profesional
from Telefono import Telefono

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
    dbname = 'odonto',
    user = 'postgres',
    password = 'posgresito',
    host = 'localhost',
    port = '5432'
)

class Menu:
    @staticmethod
    def mostrar_menu_principal():
        print("\n--- Menú Principal ---")
        print("1. Operaciones CRUD para Odontólogo")
        print("2. Operaciones CRUD para Paciente")
        print("3. Operaciones CRUD para Consulta")
        print("4. Operaciones CRUD para Pasante")
        print("5. Operaciones CRUD para Profesional")
        print("6. Operaciones CRUD para Teléfono")
        print("7. Salir")

    @staticmethod
    def mostrar_menu_crud(nombre_clase):
        print(f"\n--- Menú CRUD para {nombre_clase} ---")
        print("1. Crear")
        print("2. Leer")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver al Menú Principal")

    @staticmethod
    def ejecutar_menu_principal():
        while True:
            Menu.mostrar_menu_principal()
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                Menu.ejecutar_menu_crud("Odontólogo")
            elif opcion == "2":
                Menu.ejecutar_menu_crud("Paciente")
            elif opcion == "3":
                Menu.ejecutar_menu_crud("Consulta")
            elif opcion == "4":
                Menu.ejecutar_menu_crud("Pasante")
            elif opcion == "5":
                Menu.ejecutar_menu_crud("Profesional")
            elif opcion == "6":
                Menu.ejecutar_menu_crud("Teléfono")
            elif opcion == "7":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

    @staticmethod
    def ejecutar_menu_crud(nombre_clase):
        while True:
            Menu.mostrar_menu_crud(nombre_clase)
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                Menu.crear_registro(nombre_clase)
            elif opcion == "2":
                Menu.leer_registro(nombre_clase)
            elif opcion == "3":
                Menu.actualizar_registro(nombre_clase)
            elif opcion == "4":
                Menu.eliminar_registro(nombre_clase)
            elif opcion == "5":
                print("Volviendo al Menú Principal...")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

    @staticmethod
    def crear_registro(nombre_clase):
        """
        Crea un registro en la tabla correspondiente.
        """
        if nombre_clase == "Odontólogo":
            odontologo = Odontologo(
                idOdontologo=input("ID: "),
                nombre=input("Nombre: "),
                primerApellido=input("Primer apellido: "),
                segundoApellido=input("Segundo apellido: "),
                telefono=input("Teléfono: "),
                fechaNacimiento=input("Fecha de nacimiento (YYYY-MM-DD): "),
            )
            odontologo.create(conn, cursor)
        
        elif nombre_clase == "Paciente":
            # Verificar que la conexión y el cursor sean válidos

            if conn and cursor:
            # Crear un objeto paciente con los datos
                paciente = Paciente(
                idPaciente=input("ID: "),
                nombre=input("Nombre: "),             
                primerApellido=input("Primer apellido: "),
                segundoApellido=input("Segundo apellido: "),
                fechaNacimiento=input("Fecha de nacimiento (YYYY-MM-DD): "),
                idOdontologo=input("ID Odontologo: ")
            )

            paciente.create(conn, cursor)

        elif nombre_clase == "Consulta":
            # Verificar que la conexión y el cursor sean válidos
            if conn and cursor:
                # Crear un objeto Consulta con los datos de prueba
                consulta = Consulta(
                idConsulta=input("ID: "),
                fecha=input("Fecha: "),
                horaInicio=input("Hora de inicio: "),
                horaFin=input("Hora de fin: "),
                motivo=input("Motivo: "),
                idPaciente=input("ID Paciente: ")
            )

            consulta.create(conn, cursor)

        elif nombre_clase == "Pasante":
            # Verificar que la conexión y el cursor sean válidos
            if conn and cursor:
                # Crear un objeto Pasante con los datos de prueba
                pasante = Pasante(
                idOdontologo=input("ID: "),
                institucion=input("Institucion: ")
            )

            pasante.create(conn, cursor)
        
        elif nombre_clase == "Profesional":
            # Verificar que la conexión y el cursor sean válidos
            if conn and cursor:
                # Crear un objeto Profesional con los datos de prueba
                profesional = Profesional(
                idOdontologo=input("ID: "),
                cedula=input("Cedula: ")
            )

            profesional.create(conn, cursor)

        elif nombre_clase == "Teléfono":
            # Verificar que la conexión y el cursor sean válidos
            if conn and cursor:
                # Crear un objeto Odontologo con los datos de prueba
                telefono = Telefono(
                idTelefono=input("ID: "),
                telefono=input("Número de télefono: "),
                idPaciente=input("ID del paciente al que pertenece: ")
            )

            telefono.create(conn, cursor)
        
        else:
            print(f"Operación no implementada para {nombre_clase}.")

    @staticmethod
    def leer_registro(nombre_clase):
        """
        Lee un registro de la tabla correspondiente.
        """
        id_registro = input(f"Ingresa el ID del {nombre_clase}: ")
        if nombre_clase == "Odontólogo":
            resultado = Odontologo.read(cursor, id_registro)
            if resultado:
                print("Datos del odontólogo:")
                print(f"ID: {resultado[0]}")
                print(f"Nombre: {resultado[1]} {resultado[2]} {resultado[3]}")
                print(f"Teléfono: {resultado[4]}")
                print(f"Fecha de nacimiento: {resultado[5]}")
            else:
                print("No se encontró ningún odontólogo con ese ID.")

        elif nombre_clase == "Paciente":
            resultado = Paciente.read(cursor, id_registro)
            if resultado:
                print("Datos del paciente:")
                print(f"ID: {resultado[0]}")
                print(f"Nombre: {resultado[1]} {resultado[2]} {resultado[3]}")
                print(f"Fecha de nacimiento: {resultado[4]}")
                print(f"Odontólogo: {resultado[5]}")
            else:
                print("No se encontró ningún paciente con ese ID.")
            
        elif nombre_clase == "Consulta":
            resultado = Consulta.read(cursor, id_registro)
            if resultado:
                print("Datos del consulta:")
                print(f"ID: {resultado[0]}")
                print(f"Fecha: {resultado[1]}")
                print(f"Hora de inicio: {resultado[2]}")
                print(f"Hora de fin: {resultado[3]}")
                print(f"Motivo: {resultado[4]}")
                print(f"ID Paciente: {resultado[5]}")
            else:
                print("No se encontró ninguna consulta con ese ID.")

        elif nombre_clase == "Pasante":
            resultado = Pasante.read(cursor, id_registro)
            if resultado:
                print("Datos del pasante:")
                print(f"ID: {resultado[0]}")
                print(f"Institucion: {resultado[1]}")
            else:
                print("No se encontró ningun pasante con ese ID.")

        elif nombre_clase == "Profesional":
            resultado = Profesional.read(cursor, id_registro)
            if resultado:
                print("Datos del profesional:")
                print(f"ID: {resultado[0]}")
                print(f"Cedula: {resultado[1]}")
            else:
                print("No se encontró ningun profesional con ese ID.")

        elif nombre_clase == "Teléfono":
            resultado = Telefono.read(cursor, id_registro)
            if resultado:
                print("Datos del teléfono del paciente:")
                print(f"ID: {resultado[0]}")
                print(f"Número de telélefono: {resultado[1]}")
                print(f"Paciente al que pertenece: {resultado[2]}")
            else:
                print("No se encontró ningun teléfono con ese ID.")

        else:
            print(f"Operación no implementada para {nombre_clase}.")
            return

    @staticmethod
    def actualizar_registro(nombre_clase):
        """
        Actualiza un registro en la tabla correspondiente.
        """
        id_registro = input(f"Ingresa el ID del {nombre_clase} a actualizar: ")
        
        if nombre_clase == "Odontólogo":
            odontologo = Odontologo(
                idOdontologo=id_registro,                      # ID del odontólogo a actualizar
                nombre=input("Nombre del odontólogo: "),                       # Nuevo nombre
                primerApellido=input("Primer apellido del odontólogo: "),              # Nuevo primer apellido
                segundoApellido=input("Segundo apellido del odontólogo: "),             # Nuevo segundo apellido
                telefono=input("Número de teléfono del odontólogo: "),               # Nuevo teléfono
                fechaNacimiento=input("Fecha de nacimiento (AAAA-MM-DD) del odontólogo: ")         # Nueva fecha de nacimiento
            )
            
            odontologo.update(conn, cursor, odontologo)

        elif nombre_clase == "Paciente":
            paciente = Paciente(
                idPaciente=id_registro,                 # ID del paciente a actualizar
                nombre=input("Nombre del paciente: "),                         # Nuevo nombre
                primerApellido=input("Primer apellido del paciente: "),                     # Nuevo primer apellido
                segundoApellido=input("Segundo apellido del paciente: "),                    # Nuevo segundo apellido
                fechaNacimiento=input("Fecha de nacimiento del paciente (AAAA-MM-DD): "),            # Nueva fecha de nacimiento
                idOdontologo=input("Nuevo ID Odontologo: ")  # Nuevo ID Odontologo
            )
            paciente.update(conn, cursor, paciente)

        elif nombre_clase == "Consulta":
            consulta = Consulta(
                idConsulta=id_registro,
                fecha=input("Fecha (YYYY-MM-DD): "),
                horaInicio=input("Hora de inicio (HH:MM:SS): "),
                horaFin=input("Hora de fin (HH:MM:SS): "),
                motivo=input("Motivo: "),
                idPaciente=input("ID del paciente: "),
            )
            consulta.update(conn, cursor)
        
        elif nombre_clase == "Pasante":
            pasante = Pasante(
                idOdontologo=id_registro,                           # ID del odontólogo a actualizar
                institucion=input("Institución: ")      # Nueva institucion
            )
            pasante.update(conn, cursor, pasante)

        elif nombre_clase == "Profesional":
            profesional = Profesional(
                idOdontologo=id_registro,                           # ID del odontólogo a actualizar
                cedula=input("Cedula: ")      # Nueva institucion
            )
            profesional.update(conn, cursor, profesional)

        elif nombre_clase == "Teléfono":
            telefono = Telefono(
                idTelefono=id_registro,                           # ID del odontólogo a actualizar
                telefono=input("Número de teléfono: "),      # Nueva institucion
                idPaciente=input("ID del paciente al que pertenece: ")
            )
            telefono.update(conn, cursor, telefono)
            
        else:
            print(f"Operación no implementada para {nombre_clase}.")

    @staticmethod
    def eliminar_registro(nombre_clase):
        """
        Elimina un registro de la tabla correspondiente.
        """

        id_registro = input(f"Ingresa el ID del {nombre_clase} a eliminar: ")
        
        if nombre_clase == "Odontólogo":
            Odontologo.delete(conn, cursor, id_registro)

        elif nombre_clase == "Paciente":
            Paciente.delete(conn, cursor, id_registro)

        elif nombre_clase == "Consulta":
            Consulta.delete(conn, cursor, id_registro)

        elif nombre_clase == "Pasante":
            Pasante.delete(conn, cursor, id_registro)
            
        elif nombre_clase == "Profesional":
            Profesional.delete(conn, cursor, id_registro)
            
        elif nombre_clase == "Teléfono":
            Telefono.delete(conn, cursor, id_registro)
        
        else:
            print(f"Operación no implementada para {nombre_clase}.")


Menu.ejecutar_menu_principal()



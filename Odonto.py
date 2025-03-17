import psycopg2
import re
from datetime import datetime

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

def validar_nombre(nombre):
    """
    Valida que el nombre solo contenga letras y guiones medios.
    """
    if not re.match(r"^[A-Za-zÁ-Úá-úñÑ\- ]+$", nombre):
        return False
    return True

def validar_telefono(telefono):
    """
    Valida que el teléfono tenga exactamente 10 dígitos.
    """
    if not telefono.isdigit() or len(telefono) != 10:
        return False
    return True

def validar_id(id_registro):
    """
    Valida que el ID solo contenga dígitos.
    """
    if not id_registro.isdigit():
        return False
    return True

def valida_hora(hora):
    if not re.match(r"^(?:[01]\d|2[0-3]):[0-5]\d", hora):
        return False
    return True

def validar_longitud(texto, longitud):
    """
    Valida que el texto tenga la longitud especificada.
    """
    if len(texto) != longitud:
        return False
    return True

def validar_fecha(fecha):
    if not re.match(r"^(?:19|20)\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$", fecha):
        return False
    return True

class Menu:
    @staticmethod
    def mostrar_menu_principal():
        """	
        Muestra el menú principal de la aplicación.
        """

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
        """
        Muestra el menú CRUD para la clase especificada.
        """

        print(f"\n--- Menú CRUD para {nombre_clase} ---")
        print("1. Crear")
        print("2. Leer")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver al Menú Principal")

    @staticmethod
    def ejecutar_menu_principal():

        """
        Ejecuta el menú principal de la aplicación dependiendo de las opciones dadas por el usuario.
        """

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
        """
        Ejecuta alguna de las operaciones CRUD para la clase especificada con la opción dada por el usuario.
        """

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
            
            #Validaciones de tipos de datos
            if not validar_nombre(odontologo.nombre) and not validar_nombre(odontologo.primerApellido) and not validar_nombre(odontologo.segundoApellido):
                print("Nombre o apellidos inválidos, los nombres o apellidos no deben de llevar números o carácteres especiales. Intenta de nuevo.")
                return
            if not validar_telefono(odontologo.telefono):
                print("Número de teléfono inválido. Debe contener 10 dígitos. Intenta de nuevo.")
                return
            if not validar_id(odontologo.idOdontologo):
                print("ID inválido. Debe contener solo dígitos. Intenta de nuevo.")
                return
            if not validar_longitud(odontologo.nombre, 120) and not validar_longitud(odontologo.primerApellido, 50) and not validar_longitud(odontologo.segundoApellido, 50):
                print("Nombre o apellidos inválidos, los nombres o apellidos no son tan largos, creo. Intenta de nuevo.")
                return
            if not validar_fecha(odontologo.fechaNacimiento):
                print("Fecha inválida. Debe contener solo dígitos en el formato (YYYY-MM-DD). Intenta de nuevo.")
                return
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
            
            #Validaciones de tipos de datos
            if not validar_nombre(paciente.nombre) and not validar_nombre(paciente.primerApellido) and not validar_nombre(paciente.segundoApellido):
                print("Nombre o apellidos inválidos, los nombres o apellidos no deben de llevar números o carácteres especiales. Intenta de nuevo.")
                return
            if not validar_id(paciente.idPaciente) and not validar_id(paciente.idOdontologo):
                print("ID inválido. Debe contener solo dígitos. Intenta de nuevo.")
            if not validar_longitud(paciente.nombre, 120) and not validar_longitud(paciente.primerApellido, 50) and not validar_longitud(paciente.segundoApellido, 50):
                print("Nombre o apellidos inválidos, los nombres o apellidos no son tan largos, creo. Intenta de nuevo.")
                return
            if not validar_fecha(paciente.fechaNacimiento):
                print("Fecha inválida. Debe contener solo dígitos en el formato (YYYY-MM-DD). Intenta de nuevo.")
                return

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
            
            #Validaciones de tipos de datos
            if not validar_id(consulta.idConsulta) and not validar_id(consulta.idPaciente):
                print("ID inválido. Debe contener solo dígitos. Intenta de nuevo.")
                return
            if not valida_hora(consulta.horaInicio) and not valida_hora(consulta.horaFin):
                print("Hora inválida. Debe contener solo dígitos en el formato (HH:MM). Intenta de nuevo.")
                return
            
            consulta.create(conn, cursor)

        elif nombre_clase == "Pasante":
            # Verificar que la conexión y el cursor sean válidos
            if conn and cursor:
                # Crear un objeto Pasante con los datos de prueba
                pasante = Pasante(
                idOdontologo=input("ID: "),
                institucion=input("Institucion: ")
            )
            
            #Validaciones de tipos de datos
            if not validar_id(pasante.idOdontologo):
                print("ID inválido. Debe contener solo dígitos. Intenta de nuevo.")
                return

            pasante.create(conn, cursor)
        
        elif nombre_clase == "Profesional":
            # Verificar que la conexión y el cursor sean válidos
            if conn and cursor:
                # Crear un objeto Profesional con los datos de prueba
                profesional = Profesional(
                idOdontologo=input("ID: "),
                cedula=input("Cedula: ")
            )

            #Validaciones de tipos de datos
            if not validar_id(profesional.idOdontologo):
                print("ID inválido. Debe contener solo dígitos. Intenta de nuevo.")
                return
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

            #Validaciones de tipos de datos
            if not validar_id(telefono.idTelefono) and not validar_id(telefono.idPaciente):
                print("ID inválido. Debe contener solo dígitos. Intenta de nuevo.")
                return
            if not validar_telefono(telefono.telefono):
                print("Número de teléfono inválido. Debe contener 10 dígitos. Intenta de nuevo.")
                return
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
        
            #Validaciones de tipos de datos
            if not validar_nombre(odontologo.nombre) and not validar_nombre(odontologo.primerApellido) and not validar_nombre(odontologo.segundoApellido):
                print("Nombre o apellidos inválidos, los nombres o apellidos no deben de llevar números o carácteres especiales. Intenta de nuevo.")
                return
            if not validar_telefono(odontologo.telefono):
                print("Número de teléfono inválido. Debe contener 10 dígitos. Intenta de nuevo.")
                return
            if not validar_id(odontologo.idOdontologo):
                print("ID inválido. Debe contener solo dígitos. Intenta de nuevo.")
                return
            if not validar_longitud(odontologo.nombre, 120) and not validar_longitud(odontologo.primerApellido, 50) and not validar_longitud(odontologo.segundoApellido, 50):
                print("Nombre o apellidos inválidos, los nombres o apellidos no son tan largos, creo. Intenta de nuevo.")
                return
            if not validar_fecha(odontologo.fechaNacimiento):
                print("Fecha inválida. Debe contener solo dígitos en el formato (YYYY-MM-DD). Intenta de nuevo.")
                return

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

            #Validaciones de tipos de datos
            if not validar_nombre(paciente.nombre) and not validar_nombre(paciente.primerApellido) and not validar_nombre(paciente.segundoApellido):
                print("Nombre o apellidos inválidos, los nombres o apellidos no deben de llevar números o carácteres especiales. Intenta de nuevo.")
                return
            if not validar_id(paciente.idPaciente) and not validar_id(paciente.idOdontologo):
                print("ID inválido. Debe contener solo dígitos. Intenta de nuevo.")
            if not validar_longitud(paciente.nombre, 120) and not validar_longitud(paciente.primerApellido, 50) and not validar_longitud(paciente.segundoApellido, 50):
                print("Nombre o apellidos inválidos, los nombres o apellidos no son tan largos, creo. Intenta de nuevo.")
                return
            if not validar_fecha(paciente.fechaNacimiento):
                print("Fecha inválida. Debe contener solo dígitos en el formato (YYYY-MM-DD). Intenta de nuevo.")
                return

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

            #Validaciones de tipos de datos
            if not validar_id(consulta.idConsulta) and not validar_id(consulta.idPaciente):
                print("ID inválido. Debe contener solo dígitos. Intenta de nuevo.")
                return
            if not valida_hora(consulta.horaInicio) and not valida_hora(consulta.horaFin):
                print("Hora inválida. Debe contener solo dígitos en el formato (HH:MM). Intenta de nuevo.")
                return

            consulta.update(conn, cursor)
        
        elif nombre_clase == "Pasante":
            pasante = Pasante(
                idOdontologo=id_registro,                           # ID del odontólogo a actualizar
                institucion=input("Institución: ")      # Nueva institucion
            )
            
            #Validaciones de tipos de datos
            if not validar_id(pasante.idOdontologo):
                print("ID inválido. Debe contener solo dígitos. Intenta de nuevo.")
                return

            pasante.update(conn, cursor, pasante)

        elif nombre_clase == "Profesional":
            profesional = Profesional(
                idOdontologo=id_registro,                           # ID del odontólogo a actualizar
                cedula=input("Cedula: ")      # Nueva institucion
            )
            profesional.update(conn, cursor, profesional)

            #Validaciones de tipos de datos
            if not validar_id(profesional.idOdontologo):
                print("ID inválido. Debe contener solo dígitos. Intenta de nuevo.")
                return

        elif nombre_clase == "Teléfono":
            telefono = Telefono(
                idTelefono=id_registro,                           # ID del odontólogo a actualizar
                telefono=input("Número de teléfono: "),      # Nueva institucion
                idPaciente=input("ID del paciente al que pertenece: ")
            )
            
            #Validaciones de tipos de datos
            if not validar_id(telefono.idTelefono) and not validar_id(telefono.idPaciente):
                print("ID inválido. Debe contener solo dígitos. Intenta de nuevo.")
                return
            if not validar_telefono(telefono.telefono):
                print("Número de teléfono inválido. Debe contener 10 dígitos. Intenta de nuevo.")
                return
            
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

#Ejecucion del menu
Menu.ejecutar_menu_principal()



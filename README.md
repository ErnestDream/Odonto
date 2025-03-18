# Odonto: Sistema de gestion de un consultorio dental.

Descripción: El propósito del proyecto es poner en práctica las cuestiones aprendidas en el curso de Python 2, se busca hacer un programa bien hecho que realice un CRUD, con la principal característica de que contará con una conexión a una base de datos en Postgresql

Pre requisitos:
* Tener instalado y configurado un cliente de Postgresql, así como un usuario con los permisos para crear bases de datos(CREATEDB), tablas (public) y para insertar en las tablas

Instalación:
* Descargar el archivo de sql de la documentación, llamado "bdodonto.sql"
* Instalar psycopg2 con el comado "pip install psycopg2" en donde sea que se vaya a usar el programa
* Ejecuta el primer comando de bdodonto.sql

`CREATE DATABASE odonto;

* Copia y pega lo restante del archivo sql en psql (CLI de Postgres)
* Descargar "Odonto.py" y los demas archivos: Odontologo, Paciente, Consulta, Pasante, Profesional y Telefono .py
    
# Importante:
* Si tienes configuraciones distintas a las por default, cambialas por tus datos en el archivo Odonto.py

* Obvio, hay que hacerlo para la contraseña


Uso:
* Usar opciones descritas en el menú
* Salir del programa con la opción del menú o con Ctrl+C

Autor: Jorge Ernesto Ceballos Guzman aka. ErnestDream (github)

Notas Adicionales: Instalar las extensiones de Python en VS necesarias (Python, Python Debugger, Pylance), si es que se ejecuta desde la terminal de VS

Estado del Proyecto: Versión del proyecto: 1.3

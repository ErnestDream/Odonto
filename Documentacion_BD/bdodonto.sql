
CREATE DATABASE odonto;

CREATE TABLE odontologo(
	idOdontologo NUMERIC(2,0) NOT NULL,
	nombre VARCHAR(120) NOT NULL,
	primerApellido VARCHAR(50) NOT NULL,
	segundoApellido VARCHAR(50) NOT NULL,
	telefono CHAR(10) NULL,
	fechaNacimiento DATE NOT NULL,
	
	CONSTRAINT pkOdontologo
	PRIMARY KEY (idOdontologo),
	
	CONSTRAINT uqOdontologoTelefono
	UNIQUE (telefono)
	);
	
CREATE TABLE paciente(
	idPaciente NUMERIC(6,0) NOT NULL,
	nombre VARCHAR(120) NOT NULL,
	primerApellido VARCHAR(50) NOT NULL,
	segundoApellido VARCHAR(50) NOT NULL,
	fechaNacimiento DATE NOT NULL,
	idOdontologo NUMERIC(2,0) NOT NULL,
	
	CONSTRAINT pkPaciente
	PRIMARY KEY (idPaciente),
	
	CONSTRAINT fkPacienteOdontologo
	FOREIGN KEY (idOdontologo)
	REFERENCES odontologo(idOdontologo)
	ON DELETE RESTRICT 
	ON UPDATE CASCADE
	);
	
CREATE TABLE consulta(
	idConsulta NUMERIC(12,0) NOT NULL,
	fecha DATE NOT NULL,
	horaInicio TIME NOT NULL,
	horaFin TIME NOT NULL,
	motivo VARCHAR(255) NOT NULL,
	idPaciente NUMERIC(6,0) NOT NULL,
	
	CONSTRAINT pkConsulta
	PRIMARY KEY (idConsulta),
	
	CONSTRAINT fkConsultaPaciente
	FOREIGN KEY (idPaciente)
	REFERENCES paciente(idPaciente)
	ON DELETE RESTRICT 
	ON UPDATE CASCADE
	);
	
CREATE TABLE pasante (
	idOdontologo NUMERIC(2,0) NOT NULL,
	institucion VARCHAR(255) NOt NULL,
	
	CONSTRAINT pkPasante
	PRIMARY KEY (idOdontologo),
	
	CONSTRAINT fkPasanteOdontologo
	FOREIGN KEY (idOdontologo)
	REFERENCES odontologo(idOdontologo)
	ON DELETE RESTRICT 
	ON UPDATE CASCADE
	);
	
CREATE TABLE profesional (
	idOdontologo NUMERIC(2,0) NOT NULL,
	cedula VARCHAR(255) NOt NULL,
	
	CONSTRAINT pkProfesional
	PRIMARY KEY (idOdontologo),
	
	CONSTRAINT fkProfesionalOdontologo
	FOREIGN KEY (idOdontologo)
	REFERENCES odontologo(idOdontologo)
	ON DELETE RESTRICT 
	ON UPDATE CASCADE
	);

CREATE TABLE telefono (
	idTelefono NUMERIC(6,0) NOT NULL,
	telefono CHAR(10) NOT NULL,
	idPaciente NUMERIC(6,0) NOT NULL,
	
	CONSTRAINT fkTelefonoPaciente
	FOREIGN KEY (idPaciente)
	REFERENCES paciente(idPaciente)
	ON DELETE RESTRICT 
	ON UPDATE CASCADE
	);


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
	institucion VARCHAR(255) NOt NULL,
	
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
	
INSERT INTO odontologo (idOdontologo, nombre, primerApellido, segundoApellido, telefono, fechaNacimiento)
VALUES (1, 'Mariana', 'González', 'Ramírez', '5551234567', '1985-06-15');

INSERT INTO profesional (idOdontologo, institucion)
VALUES (1, 'Universidad Nacional Autónoma de México');

INSERT INTO paciente (idPaciente, nombre, primerApellido, segundoApellido, fechaNacimiento, idOdontologo)
VALUES (100001, 'Carlos', 'Hernández', 'López', '1990-04-20', 1);

INSERT INTO telefono (idTelefono, telefono, idPaciente)
VALUES (1, '5567894321', 100001);

INSERT INTO consulta (idConsulta, fecha, horaInicio, horaFin, motivo, idPaciente)
VALUES (100000000001, '2025-03-12', '10:00:00', '11:00:00', 'Revisión dental', 100001);

INSERT INTO odontologo (idOdontologo, nombre, primerApellido, segundoApellido, telefono, fechaNacimiento)
VALUES (2, 'Luis', 'Martínez', 'Díaz', '5559876543', '1998-08-25');

INSERT INTO pasante (idOdontologo, institucion)
VALUES (2, 'Instituto Politécnico Nacional');

INSERT INTO paciente (idPaciente, nombre, primerApellido, segundoApellido, fechaNacimiento, idOdontologo)
VALUES (100002, 'Andrea', 'Pérez', 'Torres', '2001-11-30', 2);

INSERT INTO telefono (idTelefono, telefono, idPaciente)
VALUES (2, '5556667778', 100002);

INSERT INTO consulta (idConsulta, fecha, horaInicio, horaFin, motivo, idPaciente)
VALUES (100000000002, '2025-03-13', '12:30:00', '13:30:00', 'Limpieza dental', 100002);



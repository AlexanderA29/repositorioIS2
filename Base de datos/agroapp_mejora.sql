use SistemaDeRiego
go

SELECT * FROM dbo.Campos_Informacion;
SELECT * FROM dbo.Compatibilidad_Cultivo;
SELECT * FROM dbo.Configuracion_Sistema;
SELECT * FROM dbo.Cuidado_Papa;
SELECT * FROM dbo.Enfermedades;
SELECT * FROM dbo.Plagas;
SELECT * FROM dbo.Recomendaciones;
SELECT * FROM dbo.Registro_Lecturas_Sensores;
SELECT * FROM dbo.Registro_Notificaciones;
SELECT * FROM dbo.Registro_Riego;
SELECT * FROM dbo.Registro_Siembra;
SELECT * FROM dbo.Sensores_Humedad;
SELECT * FROM dbo.Sensores_Temperatura;
SELECT * FROM dbo.Sugerencias;
SELECT * FROM dbo.Tipo_Cultivo_Etapas;
SELECT * FROM dbo.Tipo_Cultivo_Informacion;
SELECT * FROM dbo.Tips_Sembrar_Papas;


INSERT INTO dbo.Campos_Informacion (ID_Campo, Nombre_Campo, Tipo_Cultivo, ID_Tipo_Cultivo)
VALUES 
(2, 'Campo 2', 'Maíz', 1), -- Maíz compatible con la papa
(3, 'Campo 3', 'Habas', 1), -- Habas compatible con la papa
(4, 'Campo 4', 'Zanahorias', 1); -- Zanahorias compatible con la papa

CREATE TABLE Usuarios (
    ID_Usuario INT IDENTITY(1,1) PRIMARY KEY, -- Identificador único con incremento automático
    Nombre NVARCHAR(100) NOT NULL,           -- Nombre del usuario
    Correo NVARCHAR(255) UNIQUE NOT NULL,    -- Correo único del usuario
    Contraseña NVARCHAR(255) NOT NULL,       -- Contraseña del usuario
    Fecha_Creacion DATETIME DEFAULT GETDATE() -- Fecha de creación del usuario
);


INSERT INTO Usuarios (Nombre, Correo, Contraseña)
VALUES 
('Jason', 'jason@example.com', 'password123'),
('Zairy', 'zairy@example.com', 'securepass456'),
('Alexander', 'alexander@example.com', 'alex789');

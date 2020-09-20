from connection.conn import Conexion

class Database:
    def __init__ (self, conn):
        self.conn = conn

    def crear_alumno(self):

        create_table_query = '''

            CREATE TABLE IF NOT EXISTS alumno(
                alumno_id SERIAL PRIMARY KEY NOT NULL,
                nombres varchar(150) NOT NULL,
                edad int NOT NULL,
                correo varchar(150) NOT NULL
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
        conn.commit()

    def crear_profesor(self):
    
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  profesor(
                profesor_id  SERIAL PRIMARY KEY NOT NULL,
                nombres varchar(150) NOT NULL,
                edad int NOT NULL,
                correo varchar(150) NOT NULL
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
        conn.commit()
        
    def crear_salon(self):

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  salones(
                id_salon  SERIAL  PRIMARY KEY NOT NULL,
                nombre_salon varchar(150) NOT NULL
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
        conn.commit()
        
    def crear_curso(self):

        create_table_query = '''

            CREATE TABLE IF NOT EXISTS cursos(
                curso_id SERIAL PRIMARY KEY NOT NULL,
                nombre varchar(150) NOT NULL
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
        conn.commit()
    
    def crear_periodo_escolar(self):

        create_table_query = '''

            CREATE TABLE IF NOT EXISTS periodo_escolar(
                id_periodo SERIAL PRIMARY KEY NOT NULL,
                nombre_periodo VARCHAR(150) NOT NULL,
                fecha_desde date NOT NULL,
                fecha_hasta date NOT NULL
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
        conn.commit()
    
    def crear_profesor_curso(self):

        create_table_query = '''

            CREATE TABLE IF NOT EXISTS profesor_curso(
                id_profesor_curso SERIAL PRIMARY KEY NOT NULL,
                id_profesor INTEGER NOT NULL,
                id_curso INTEGER NOT NULL,
                CONSTRAINT fk_profesor FOREIGN KEY (id_profesor) REFERENCES profesor(profesor_id),
                CONSTRAINT fk_curso FOREIGN KEY (id_curso) REFERENCES cursos(curso_id)
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
        conn.commit()
  
    def crear_malla_curricular(self):

        create_table_query = '''

            CREATE TABLE IF NOT EXISTS malla_curricular(
                id_malla SERIAL PRIMARY KEY NOT NULL,
                id_periodo INT NOT NULL,
                id_salon INT NOT NULL,
                id_profesor_curso INT NOT NULL,
                CONSTRAINT fk_periodo_escolar FOREIGN KEY (id_periodo) REFERENCES periodo_escolar(id_periodo),
                CONSTRAINT fk_salones FOREIGN KEY (id_salon) REFERENCES salones(id_salon),
                CONSTRAINT fk_profesor_curso FOREIGN KEY (id_profesor_curso) REFERENCES profesor_curso(id_profesor_curso)
            );

        '''
        conn.ejecutar_sentencia(create_table_query)
        conn.commit()

    def crear_notas(self):

        create_table_query = '''

            CREATE TABLE IF NOT EXISTS notas(
                id_nota SERIAL PRIMARY KEY NOT NULL,
                id_alumno INT NOT NULL,
                id_malla INT NOT NULL,
                nota INT NOT NULL,
                CONSTRAINT fk_alumno FOREIGN KEY (id_alumno) REFERENCES alumno(alumno_id),
                CONSTRAINT fk_malla FOREIGN KEY (id_malla) REFERENCES malla_curricular(id_malla)
            );

        '''
        conn.ejecutar_sentencia(create_table_query)
        conn.commit()

conn = Conexion('sistema_colegio')
database= Database(conn)
database.crear_profesor()
database.crear_alumno()
database.crear_salon()
database.crear_periodo_escolar()
database.crear_curso()
database.crear_profesor_curso()
database.crear_malla_curricular()
database.crear_notas()
conn.close_connection()
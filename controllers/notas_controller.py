from classes.nota import Nota
from classes.alumno import Alumno
from classes.malla import Malla
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Registro_notas:
    def __init__(self):
        self.nota = Nota()
        self.alumno = Alumno()
        self.malla = Malla()
        self.salir = False
    
    def menu(self):
        while True:
            try:
                print('''
                ======================
                    Registro Notas
                ======================
                ''')
                menu = ['Listar notas', 'Buscar notas', "Registrar notas", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_registro_notas()
                elif respuesta == 2:
                    self.buscar_registro_notas()
                elif respuesta == 3:
                    self.insertar_registro_notas()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')
    
    def listar_registro_notas(self):
        print('''
        =========================
            Lista de Periodo
        =========================
        ''')
        notas = self.nota.obtener_notas('id_nota')
        print(print_table(notas, ['id_nota', 'id_alumno', 'id_malla','nota']))
        input("\nPresione una tecla para continuar...")

    def buscar_registro_notas(self):
        print('''
        =======================
            Buscar Periodo
        =======================
        ''')
        try:
            id_nota = input_data("Ingrese el ID del periodo >> ", "int")
            notas = self.nota.obtener_nota({'id_periodo': id_nota})
            print(print_table(notas, ['id_periodo', 'nombre_periodo', 'Fecha_desde', 'Fecha_hasta']))

            if notas:
                if pregunta("¿Deseas dar mantenimiento al periodo?"):
                    opciones = ['Editar periodo', 'Eliminar periodo', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        pass
                        #self.editar_registrar_notas(id_nota)
                    elif respuesta == 2:
                        pass
                        #self.eliminar_registrar_notas(id_nota)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_registro_notas(self):
        print('''
        =========================
            Lista de Alumno
        =========================
        ''')

        alumno = self.alumno.obtener_alumnos('alumno_id')
        print(print_table(alumno, ['alumno_id', 'nombres', 'edad', 'correo']))

        alumno_id = input_data("Ingrese el ID del alumno >> ", 'int')
        
        print('''
        ===================================
            Lista de Malla Curriculares
        ===================================
        ''')
        malla = self.malla.obtener_mallas('id_malla')
        print(print_table(malla, ['id_malla', 'id_periodo','id_salon','id_profesor_curso']))

        id_malla = input_data("Ingrese la ID de la malla curricular >> ", 'int')

        while True:

            nota = input_data("Ingrese la nota >> ", 'int')

            if nota >= 0 and nota <= 20:
                break
            else:
                print('Ingresar una nota entre 00 al 20')

        self.nota.guardar_nota({
            'id_alumno': alumno_id,
            'id_malla': id_malla,
            'nota': nota
                })
        print('''
        ================================
            Nuevo Periodo agregado !
        ================================
        ''')
        self.listar_registro_notas()
    
    def editar_periodo(self, id_nota):
        print('''
        =========================
            Lista de Alumno
        =========================
        ''')

        alumno = self.alumno.obtener_alumnos('alumno_id')
        print(print_table(alumno, ['alumno_id', 'nombres', 'edad', 'correo']))

        alumno_id = input_data("Ingrese el ID del alumno >> ", 'int')
        
        print('''
        ===================================
            Lista de Malla Curriculares
        ===================================
        ''')
        malla = self.malla.obtener_mallas('id_malla')

        print(print_table(malla, ['id_malla', 'id_periodo','id_salon','id_profesor_curso']))

        id_malla = input_data("Ingrese la ID de la malla curricular >> ", 'int')
        
        while True:
            
            nota = input_data("Ingrese la nota >> ", 'int')

            if nota >= 0 and nota <= 20:
                break
            else:
                print('Ingresar una nota entre 00 al 20')
        
        self.nota.modificar_nota({
            'id_nota': id_nota
        }, {
            'id_alumno': alumno_id,
            'id_malla': id_malla,
            'nota': nota
        })
        print('''
        ===================================
            Registro de Nota Editada !
        ===================================
        ''')
    
    def eliminar_periodo(self, id_nota):
        self.nota.eliminar_nota({
            'id_nota': id_nota
        })
        print('''
        ====================================
            Registro de Nota Eliminado !
        ====================================
        ''')
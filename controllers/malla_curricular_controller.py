from classes.malla import Malla
from classes.nota import Nota
from classes.salon import Salon
from classes.periodo import Periodo
from classes.curso import Curso
from classes.profesor_curso import Profesor_curso
from controllers.periodo_controller import Periodo_controller
from helpers.menu import Menu
from helpers.helper import print_table, input_data, pregunta


class Malla_curricular_controller:
    def __init__(self):
        self.malla = Malla()
        self.nota = Nota()
        self.salon = Salon()
        self.periodo = Periodo()
        self.profesor_curso = Profesor_curso()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ========================
                    Malla Curricular
                ========================
                ''')
                menu = ['Listar malla curricular', 'Buscar malla curricular', 'Nueva malla curricular', "Salir"]
                respuesta = Menu(menu).show()

                if respuesta == 1:
                    self.listar_malla()
                elif respuesta == 2:
                    self.buscar_malla()
                elif respuesta == 3:
                    self.insertar_malla()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    
    def listar_malla(self):
        print('''
        ==================================
            Lista de Malla Curricular
        ==================================
        ''')
        malla = self.malla.obtener_mallas('id_malla')
        print(print_table(malla, ['id_malla', 'id_periodo', 'id_salon', 'id_profesor_curso']))
        input("\nPresione una tecla para continuar...")

    def buscar_malla(self):
        print('''
        ==================================
            Buscar de Malla Curricular
        ==================================
        ''')
        try:
            id_malla = input_data("Ingrese el ID de la malla curricular >> ", "int")
            malla = self.malla.obtener_malla({'id_malla': id_malla})
            print(print_table(malla, ['id_malla', 'id_periodo', 'id_salon', 'id_profesor_curso']))

            if malla:
                if pregunta("¿Deseas dar mantenimiento a la malla curricular?"):
                    opciones = ['Editar malla', 'Eliminar malla', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_malla(id_malla)
                    elif respuesta == 2:
                        self.eliminar_malla(id_malla)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_malla(self):
        print('''
        =========================
            Lista de Periodo
        =========================
        ''')
        periodo = self.periodo.obtener_periodos('id_periodo')
        print(print_table(periodo, ['id_periodo', 'nombre_periodo', 'Fecha_desde', 'Fecha_hasta']))

        id_periodo = input_data("Ingrese el ID del periodo >> ", 'int')
        
        print('''
        ==========================
            Lista de Salones
        ==========================
        ''')
        salones = self.salon.obtener_salones('id_salon')
        print(print_table(salones, ['id_salon', 'nombre_salon']))

        
        id_salon = input_data("Ingrese la ID del salon >> ", 'int')
        
        print('''
        =================================
            Lista de Profesor Curso
        =================================
        ''')

        profesor_curso = self.profesor_curso.obtener_profesor_cursos('id_profesor_curso')
        print(print_table(profesor_curso, ['id_profesor_curso', 'id_profesor', 'id_curso']))
        
        id_profesor_curso = input_data("Ingrese el ID Curso Profesor >> ", 'int')
        self.malla.guardar_malla({
            'id_periodo': id_periodo,
            'id_salon': id_salon,
            'id_profesor_curso': id_profesor_curso
        })
        print('''
        =================================
            Nueva Malla agregado !
        =================================
        ''')
        self.listar_malla()

    def editar_malla(self, id_malla):

        print('''
        =========================
            Lista de Periodo
        =========================
        ''')
        periodo = self.periodo.obtener_periodos('id_periodo')
        print(print_table(periodo, ['id_periodo', 'nombre_periodo', 'Fecha_desde', 'Fecha_hasta']))

        id_periodo = input_data("Ingrese el ID del periodo >> ", 'int')
        
        print('''
        ==========================
            Lista de Salones
        ==========================
        ''')
        salones = self.salon.obtener_salones('id_salon')
        print(print_table(salones, ['id_salon', 'nombre_salon']))

        
        id_salon = input_data("Ingrese la ID del salon >> ", 'int')
        
        print('''
        =================================
            Lista de Profesor Curso
        =================================
        ''')

        profesor_curso = self.profesor_curso.obtener_profesor_cursos('id_profesor_curso')
        print(print_table(profesor_curso, ['id_profesor_curso', 'id_profesor', 'id_curso']))
        
        id_profesor_curso = input_data("Ingrese el ID Curso Profesor >> ", 'int')
        self.malla.modificar_malla({
            'id_malla': id_malla
        }, {
            'id_periodo': id_periodo,
            'id_salon': id_salon,
            'id_profesor_curso': id_profesor_curso
        })
        print('''
        ==========================
            Malla Editada !
        ==========================
        ''')

    def eliminar_malla(self, id_malla):
        self.malla.eliminar_malla({
            'id_malla': id_malla
        })
        print('''
        ===========================
            Malla Eliminado !
        ===========================
        ''')
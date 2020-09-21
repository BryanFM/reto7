from classes.periodo import Periodo
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Periodo_controller:
    def __init__(self):
        self.periodo = Periodo()
        self.salir = False
    
    def menu(self):
        while True:
            try:
                print('''
                ===============
                    Periodo
                ===============
                ''')
                menu = ['Listar periodo', 'Buscar periodo', "Nuevo periodo", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_periodo()
                elif respuesta == 2:
                    self.buscar_periodo()
                elif respuesta == 3:
                    self.insertar_periodo()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')
    
    def listar_periodo(self):
        print('''
        =========================
            Lista de Periodo
        =========================
        ''')
        periodo = self.periodo.obtener_periodos('id_periodo')
        print(print_table(periodo, ['id_periodo', 'Nombre', 'Fecha_desde', 'Fecha_hasta']))
        input("\nPresione una tecla para continuar...")
    
    def buscar_periodo(self):
        print('''
        =======================
            Buscar Periodo
        =======================
        ''')
        try:
            id_periodo = input_data("Ingrese el ID del periodo >> ", "int")
            periodo = self.periodo.obtener_periodo({'id_periodo': id_periodo})
            print(print_table(periodo, ['id_periodo', 'nombre_periodo', 'Fecha_desde', 'Fecha_hasta']))

            if periodo:
                if pregunta("¿Deseas dar mantenimiento al periodo?"):
                    opciones = ['Editar periodo', 'Eliminar periodo', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_periodo(id_periodo)
                    elif respuesta == 2:
                        self.eliminar_periodo(id_periodo)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")
    
    def insertar_periodo(self):
        nombre = input_data("Ingrese el nombre del periodo >> ")
        Fecha_desde = input_data("Ingrese la fecha de Inicio >> ")
        Fecha_hasta = input_data("Ingrese la fecha final >> ")
        self.periodo.guardar_periodo({
            'nombre_periodo': nombre,
            'Fecha_desde': Fecha_desde,
            'Fecha_hasta': Fecha_hasta
                })
        print('''
        ================================
            Nuevo Periodo agregado !
        ================================
        ''')
        self.listar_periodo()
    
    def editar_periodo(self, id_periodo):
        nombre = input_data("Ingrese el nuevo nombre del periodo >> ")
        Fecha_desde = input_data("Ingrese la fecha de Inicio >> ")
        Fecha_hasta = input_data("Ingrese la fecha final >> ")
        self.periodo.modificar_periodo({
            'periodo_id': id_periodo
        }, {
            'nombre': nombre,
            'Fecha_desde': Fecha_desde,
            'Fecha_hasta': Fecha_hasta
        })
        print('''
        =========================
            Periodo Editado !
        =========================
        ''')
    
    def eliminar_periodo(self, id_periodo):
        self.periodo.eliminar_periodo({
            'periodo_id': id_periodo
        })
        print('''
        ==========================
            Periodo Eliminado !
        ==========================
        ''')
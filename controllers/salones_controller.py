from classes.salon import Salon
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Salon_controller:
    def __init__(self):
        self.salon = Salon()
        self.salir = False
    
    def menu(self):
        while True:
            try:
                print('''
                ===============
                    Salones
                ===============
                ''')
                menu = ['Listar salones', 'Buscar salones', "Nuevo salones", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_salones()
                elif respuesta == 2:
                    self.buscar_salones()
                elif respuesta == 3:
                    self.insertar_salones()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')
    
    def listar_salones(self):
        print('''
        =========================
            Lista de Salones
        =========================
        ''')
        salones = self.salon.obtener_salones('id_salon')
        print(print_table(salones, ['id_salon', 'nombre_salon']))
        input("\nPresione una tecla para continuar...")
    
    def buscar_salones(self):
        print('''
        =======================
            Buscar Salones
        =======================
        ''')
        try:
            id_salon = input_data("Ingrese el ID del salon >> ", "int")
            salones = self.salon.obtener_salon({'id_salon': id_salon})
            print(print_table(salones, ['id_salon', 'nombre_salon']))

            if salones:
                if pregunta("¿Deseas dar mantenimiento al periodo?"):
                    opciones = ['Editar salones', 'Eliminar salones', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_salones(id_salon)
                    elif respuesta == 2:
                        self.eliminar_salones(id_salon)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")
    
    def insertar_salones(self):
        nombre_salon = input_data("Ingrese el nombre del salón >> ")
        self.salon.guardar_salon({
            'nombre_salon': nombre_salon
                })
        print('''
        ==============================
            Nuevo Salon agregado !
        ==============================
        ''')
        self.listar_salones()
    
    def editar_salones(self, id_salon):
        print('''
        =========================
            Lista de Salones
        =========================
        ''')
        salones = self.salon.obtener_salones('id_salon')
        print(print_table(salones, ['id_salon', 'nombre_salon']))

        nombre_salon = input_data("Ingrese el nombre del salón >> ")
        self.salon.modificar_salon({
            'id_salon': id_salon
        }, {
            'nombre_periodo': nombre_salon
        })
        print('''
        ======================
            Salon Editado !
        ======================
        ''')
    
    def eliminar_salones(self, id_salon):
        self.salon.eliminar_salon({
            'id_salon': id_salon
        })
        print('''
        ==========================
            Salon Eliminado !
        ==========================
        ''')
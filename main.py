from helpers.menu import Menu
from controllers.profesores_controller import Profesores_controller
from controllers.cursos_controller import Cursos_controller
from controllers.salones_controller import Salon_controller
from controllers.malla_curricular_controller import Malla_curricular_controller
from controllers.periodo_controller import Periodo_controller
from controllers.alumnos_controller import Alumnos_controller
from controllers.notas_controller import Registro_notas
import pprint

def iniciar_app():
    try:
        print('''
        ==========================
            Sistema de Colegio
        ==========================
        ''')
        menu_principal = ["Profesores", "Alumnos", "Cursos", "Periodo Escolar", "Salones", "Habilitar salones y cursos", "Registro de notas", "Salir"]
        respuesta = Menu(menu_principal).show()
        if respuesta == 1:
            profesor = Profesores_controller()
            profesor.menu()
            if profesor.salir:
                iniciar_app()
        elif respuesta == 2:
            alumno = Alumnos_controller()
            alumno.menu()
            if alumno.salir:
                iniciar_app()
        elif respuesta == 3:
            curso = Cursos_controller()
            curso.menu()
            if curso.salir:
                iniciar_app()
        elif respuesta == 4:
            periodo = Periodo_controller()
            periodo.menu()
            if periodo.salir:
                iniciar_app()
        elif respuesta == 5:
            salones = Salon_controller()
            salones.menu()
            if salones.salir:
                iniciar_app()
        elif respuesta == 6:
            malla = Malla_curricular_controller()
            malla.menu()
            if malla.salir:
                iniciar_app()
        elif respuesta == 7:
            notas = Registro_notas()
            notas.menu()
            if notas.salir:
                iniciar_app()

        print("\nGracias por utilizar el sistema\n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')

iniciar_app()
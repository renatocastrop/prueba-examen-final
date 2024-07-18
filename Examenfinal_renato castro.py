import os
import csv
import random
lista_trabajadores=["Juan Perez", "Maria Garcia", "Ana Martinez", "Carlos Lopez", "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]
sueldos={}

def sueldos_random(lista_trabajadores):
    sueldos={trabajador:random.randint(300000, 2500000)
for trabajador in lista_trabajadores}
    return sueldos

def mostrar_sueldos(sueldos):
     print('Sueldos asignados: ')
     for trabajador, sueldo in sueldos.items():
        print(f"{trabajador} : {sueldo}")      

def ver_estadisticas(sueldos):
    sueldo_mas_alto=max(sueldos.values()) 
    sueldo_mas_bajo=min(sueldos.values())
    promedio_sueldos=round(sum(sueldos.values())/len(sueldos), 2)
    
    print(f"Sueldo mas alto :{sueldo_mas_alto}")
    print(f"Sueldo mas bajo :{sueldo_mas_bajo}")
    print(f"Promedio sueldos :{promedio_sueldos}")
     
def generar_reporte_csv(sueldos):
    with open('Sueldos.csv', 'w', newline='') as archivo_csv:
              escritor_csv=csv.writer(archivo_csv,delimiter=';')
              escritor_csv.writerow(['Nombre empleado', 'Sueldo base', 'Descuento Salud', 'Descuento AFP', 'Sueldo base'])
            
def mostrar_menu():
     print('MENU')
     print("1.- Asignar sueldos aleatorios")  
     print("2.- Clasificar sueldos")  
     print("3.- Ver estadisticas")  
     print("4.- Reporte de sueldos")  
     print("5.- Salir del programa")

def ejecutar_opcion(opcion, sueldos):
    if opcion=='1':
          sueldos=sueldos_random(lista_trabajadores)
          mostrar_sueldos(sueldos)
    elif opcion=='3':
        if sueldos:
            ver_estadisticas(sueldos)
        else:
            print('Debe asignar sueldos primero.') 
    elif opcion=='4':
        if sueldos:
            generar_reporte_csv(sueldos)
            print('Reporte listo!')
    elif opcion=='5':
         print('Saliendo del programa...')
         print('Desarrollado por Carlos Vergara')
         print('Rut 12.345.678-9')
         return False
    else:
         print('Opcion invalida')
         return True

def menu():
    continuar=True
    while continuar:
        mostrar_menu()
        opcion=input('Ingrese una opcion: ')
        continuar=ejecutar_opcion(opcion,sueldos)

menu()
    

              
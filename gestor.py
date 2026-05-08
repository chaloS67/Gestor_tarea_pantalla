import os,json

def limpiar_pantalla():
       os.system("clear")

def mostrar_menu():
       
        print("\n === GESTOR DE TAREAS === \n")
        print (" \n === ELIGA UNA OPCION === \n ")
        print ("1- AGREGAR TAREA")
        print ("2- VER TAREA")
        print ("3- COMPLETAR TAREA")
        print ("4- ELIMINAR TAREA")
        print ("5- SALIR")
       

def pedir_opcion():
       while True:
            opcion = input("elegir una opcion")

            if opcion in ["1","2","3","4","5"]:
                return int (opcion)
                  
            print("Opcion incorrecta volver a ingresar")

def agregar_tarea(tareas):
        nueva_tarea = definir_tarea(tareas)
        tareas.append(nueva_tarea)
        guardar_tareas(tareas)
        print("\n TAREA AGREGADA CON EXITO \n")
   
def guardar_tareas(tareas):
       with open ("tareas.json", "w") as archivo:
              json.dump(tareas,archivo , indent=4)

def cargar_tareas():
       try:
                with open ("tareas.json","r") as archivo:        
                        
                        tareas = json.load(archivo)   
                        return tareas
       except:
              
              return[]

def definir_tarea(tarea):
      titulo = input ("ingresar titulo de la tarea ")

      tarea = {
           "id" : len(tarea) + 1,
           "titulo" : titulo,
           "estado" : "pendiente"
          
      }
      return(tarea)

def ver_tareas(tareas):
        
        print ("\n === LISTA DE TAREAS === \n")
        print("-" * 50)
        if not tareas:
                print ("No hay tareas registradas")
                return
        
        for tarea in tareas:
                 print(
                    f"{tarea['id']} |"
                    f" {tarea['titulo']} |"
                    f" {tarea['estado']} |"
                )
        print("-" * 50)

def buscar_tarea(tareas , id_tarea):
       for tarea in tareas:
              if tarea["id"] == id_tarea:
                return tarea
       
                      

def elegir_tarea(tareas):
        print("\n  === Elegir el numero de tarea a seleccionar === \n")
        ver_tareas()
        numero = int (input ())
        tarea = buscar_tarea(tareas,numero)
        return tarea
        

def eliminar_tarea(tareas):
       ver_tareas (tareas)
       numero = int (input("eliga el numero de tarea a eliminar"))
       tarea = buscar_tarea(tareas,numero)
       
       
       if tarea is None:
                
                print("Tarea no encontrada")
                return

       
       
       print ("\n === TAREA SELECCIONADA === \n")
       print(f"Numero : {tarea['id']}")
       print(f"Titulo : {tarea['titulo']}")
       print(f"Estado : {tarea['estado']}")
       confirmacion = input ("\n Estas seguro que quieres eliminar tarea 1-si 2-no \n")

       if confirmacion == "1":
              tareas.remove(tarea)
              print ("TAREA ELIMINADA")
              guardar_tareas(tareas)
       else:
              print ("ELIMINACION CANCELADA")


def completar_tarea(tareas):
       ver_tareas (tareas)
       numero = int (input("eliga el numero de tarea a completar"))
       tarea = buscar_tarea(tareas,numero)
       
       if tarea is None:
                
                print("Tarea no encontrada")
                return
       
       print ("\n === TAREA SELECCIONADA === \n")
       print(f"Numero : {tarea['id']}")
       print(f"Titulo : {tarea['titulo']}")
       print(f"Estado : {tarea['estado']}")
       confirmacion = input ("\n Estas seguro que quieres marcar como completada tarea 1-si 2-no \n")

       if confirmacion == "1":
              tarea["estado"] = "completado"
              print ("TAREA COMPLETADA")
              guardar_tareas(tareas)
       else:
              print ("ACCION CANCELADA")
       
       
       
def main ():

        tareas = cargar_tareas()
        
        while True:
                limpiar_pantalla()
                mostrar_menu()
                opcion = pedir_opcion()
                if opcion == 1:
                        agregar_tarea(tareas)
                        input("Ingrese enter para continuar")
                elif opcion == 2:
                        ver_tareas(tareas)
                        input("Ingrese enter para continuar")
                elif opcion == 3:
                        completar_tarea(tareas) 
                        input("Ingrese enter para continuar")
                elif opcion == 4:
                       eliminar_tarea(tareas)
                       input("Ingrese enter para continuar")
                elif opcion == 5:
                        print("Saliendo del programa...")
                        break     

if __name__ == "__main__":
    main()
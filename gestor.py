def mostrar_menu():
   
        print("\n === GESTOR DE TAREAS === \n")
        print (" \n === ELIGA UNA OPCION === \n ")
        print ("1- AGREGAR TAREA")
        print ("2- VER TAREA")
        print ("3- SALIR")
        

def pedir_opcion():
       while True:
            opcion = input("elegir una opcion")

            if opcion in ["1","2","3"]:
                return int (opcion)
                  
            print("Opcion incorrecta volver a ingresar")

def agregar_tarea(tareas):
        nueva_tarea = definir_tarea(tareas)
        tareas.append(nueva_tarea)
        return(tareas)

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
     
        for tarea in tareas:
                print(f"Numero : {tarea['id']}")
                print(f"Titulo : {tarea['titulo']}")
                print(f"Estado : {tarea['estado']}")
                print()
                
def main ():
    
        tareas = []
        while True:
                mostrar_menu()
                opcion = pedir_opcion()
                if opcion == 1:
                        agregar_tarea(tareas)
                if opcion == 2:
                        ver_tareas(tareas) 
                if opcion == 3:
                        print("Saliendo del programa...")
                        break     
       

if __name__ == "__main__":
    main()
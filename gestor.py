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
                return opcion
                  
            print("Opcion incorrecta volver a ingresar")


def main ():
    
       
        mostrar_menu()
        opcion = pedir_opcion()
       

if __name__ == "__main__":
    main()
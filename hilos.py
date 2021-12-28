import threading
  
def print_num():
    """
    funcion que imprime numeros del 1 al 10
    """
    for i in range(11):
        print(i)

def print_square(num):
    """
    funcion que imprime el cuadrado de un numero
    """
    print("Square: {}".format(num * num))
  
if __name__ == "__main__":
    #creando los hilos y arrancando hilos
    t1 = threading.Thread(target=print_square, args=(10,)).start()
    t2 = threading.Thread(target=print_num).start()

    print("Hilos ejecutados correctamente!")
#Rock,papel and scissors game

#traer el texto del archivo imagenes
#encapsular para que queden ambas opciones en un recuadro

import datetime
import os
import random

def decorators(fun1):
    def wrapper(*args):
        length = len(fun1(*args))*"_"
        length_space = len(fun1(*args))*" "
        
        print(f"    __{length}_")
        print(f"   | {length_space} ||      ")
        print(f"   | {fun1(*args)} ||      ")  #Dos string necesit
        print(f"   |__{length}|/      ")
        print(f"                               ")
    return wrapper    


def read_data():
    with open("./imagenes.txt", "r", encoding="UTF-8") as f:
        opcion = [line.strip('\n') for line in f]
        opcion = {key:opcion for key,opcion in enumerate(opcion,1)}
    return opcion    

@decorators
def together(usuario,oponente):
    return f' {usuario} vs {oponente} '


def Ganador(usuario,oponente): #comparar para saber quien es el ganador con if!!

    if usuario == "ROCK" and oponente == "PAPER":
       print("¡¡¡The computer has won!!!") 
    elif usuario == "ROCK" and oponente == "SCISSORS":
       print("¡¡¡The winner is you!!!")
    elif usuario == "PAPER" and oponente == "ROCK":
       print("¡¡¡The winner is you!!!")
    elif usuario == "PAPER" and oponente == "SCISSORS":
       print("¡¡¡The computer has won!!!")  
    elif usuario == "SCISSORS" and oponente == "PAPER":
       print("¡¡¡The winner is you!!!")
    elif usuario == "SCISSORS" and oponente == "ROCK":
       print("¡¡¡The computer has won!!!")
    else:
        print("¡¡¡Nobody wins!!!")     


dict_computer = read_data() 
turn_computer = dict_computer.get(random.randint(1,3))
print(turn_computer)
 

def run():

    os.system("cls")
    print(" Welcome to rock,papel and scissors game")
    print(" 1 - ROCK ")
    print(" 2 - PAPER ")
    print(" 3 - SCISSORS")

    while True:
        try:
            opcion_usuario = int(input("  Choose an option: "))
            if opcion_usuario == 1:
               opcion_usuario = "ROCK"    
            elif opcion_usuario == 2:
                opcion_usuario = "PAPER" 
            elif opcion_usuario == 3: 
                opcion_usuario = "SCISSORS" 
            else:
                print("  Value does not correspond, choose other opcion please")
                continue          
        except ValueError:
            print("No se puede ingresar String")
        break    
    

    together(opcion_usuario,turn_computer)
    Ganador(opcion_usuario,turn_computer)


if __name__ == "__main__":
    run()
#Validador de numero positivos
'''
def validadorpositivo(a):
    def numeros(b):           #Se puede poner arriba en la funcion superior
        if a>0 and b>0:
            return True
        else:
            return False  
    return numeros

def run():
    validador=validadorpositivo(10)
    print(validador(+8))

if __name__=="__main__":
    run()     
'''

# Dado un string y un numero, multiplique e imprima 
# el string la cant de veces solicitado

'''
def cadena(string):
    def numero(n):
        assert type(string) == str, "Ingreso un formato incorrecto"
        return n*string  
    return numero    

def run():
    texto_5 = cadena("Nicolas")
    print(texto_5(5))

if __name__=="__main__":
    run()  
'''

# This closure returns a function that return the division of an x number by n
#

def make_division_by(x: int):
    def division_by(n: int) -> int:
            assert n==0, "You cannot division by zero"
            return int(n/x) 
    return division_by


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))   #the expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))   #the expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))   #the expected output is 3


if __name__=="__main__":
    run()
import time

'''

def fibo_gen():
    n1:int = 0 
    n2:int = 1 
    counter:int = 0
    while True:
        if counter==0:
            counter+=1
            yield n1

        elif counter==1:
            counter+=1
            yield n2

        else:
            aux = n1 + n2
            n1,n2=n2,aux
            counter+=1
            yield aux


if __name__=='__main__':
    get_fibo_gen = fibo_gen()
    for element in get_fibo_gen:
        print(element)
        time.sleep(0.2)


'''        

#Generador fibonacci con un limite

def fibo_gen(limite: int):
    n1:int =0
    n2:int =1
    counter:int =0
    while True:
        if limite == 0:
            counter += 1
            yield n1
        elif limite == 1:
            counter += 1
            yield n2
        elif counter <= limite:
            aux: int = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux
        else:
            break


if __name__=='__main__':
    limites = int(input("Introduce your limit value for the fibonacci function: "))
    fibo_limite = fibo_gen(limites)
    for i,y in enumerate(fibo_limite,1):
        print(i-1,":",y-1)
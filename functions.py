
from dispensa import dispensa, tam , linha , coluna

def mostrarDispensa():
     for l in range(len(dispensa)):
        print(dispensa[l])

def verifyDispensaIsNotEmpty():
  if not dispensa or all(not linha for linha in dispensa): 
              print("Dispensa esta vazia")
              return
  for l in range(len(dispensa)):
    for c in range(len(dispensa[l])):
            cont = 0
            if dispensa[l][c] is None or dispensa[l][c] == " ":
                  cont += 1
                  if cont > 0:
                    if cont > 0:
                       print(f"Há espaço(s) vazio(s) na dispensa\nNas posições ({l},{c}) da dispensa ") 
                       print(f"Há {cont} espaço(s) vazio(s)")
                    else:
                       print("\n Não ha espaços vazios na dispensa")      

                  
        



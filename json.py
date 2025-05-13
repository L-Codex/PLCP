import json
agenda={}
agenda["Nome"]=input("Nome: ")
agenda["Celular"]=input("Celular: ")
agenda["Email"]=input("E-mail: ")

lista=[]
lista.append(agenda)
with open("dados.json","w")as arquivo:
    json.dump(lista,arquivo,indent=4)

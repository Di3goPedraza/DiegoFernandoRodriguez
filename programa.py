import json
import os

with open('Manuales.json') as infManual:
    data=json.load(infManual)

def validarMenu(msj):
    while True:
        try:
            op=int(input(msj))
            if op=='': 
                print('Inegrese alguna opcion')
                input('enter...\n')
                continue
            return op
        except Exception:
            print('solo se aceptan datos numericos')

def validarPag(msj):
    while True:
        try:
            id=int(input(msj))
            while True:
                if id=='' or id<=0: #Exige al ususario que ingrese un dato numerico mayor a 1
                    print('intentelo de nuevo no se admite datos iguales o menores a 0\n')
                    id=int(input(msj))
                    continue #evita el return u hace que se repita la condicion hasta que sea falsa
                return id
        except ValueError:
            print('Ingrese solo datos Numericos')
            input('enter.....')

def addType(msj):
        os.system('clear')
        data=input(msj)
        while data.split()=='' or data.isdigit():
            os.system('cls')
            print('No deje el espacio BASIO y evite utilizar numeros\n')
            data=input(msj)
        while data.isdigit():
          os.system('cls')
          data=input(msj)
        return data     

def addTemas():
    lista=[]
    nexx=True
    while nexx:
        os.system('clear')
        title=addType('ingrese el titulo del tema\n')
        calsificaicon=validarPag('ingrese el rango en el que se clasifica el tema\n')
        lista.append({
            "Titulo":title.capitalize(),
            "Clasificacion":calsificaicon
        })
        op=validarMenu('ingrese 1 para agg mas temas o cualquier caracter para salir\n')
        if op!=1:
            return lista

def read():
    print(' '*16,' MANUEALES')
    for  llave, contenido in data['manuales'].items():
        print(f'\nManual: {llave}')
        for subLlave,subcontenido in contenido.items():
            if subLlave== 'temas':
                print('temas')
                for llave in subcontenido:
                    for ky, value in llave.items():
                        print(f'\t{ky}:{value}')
                    print('\n')
            else:
                print(f'{subLlave} {subcontenido}') 
            
    input('Enter....')

def create():
    os.system('clear')
    nomManual=addType('Ingrese el nombre del MANUAL\n')
    autor=addType('Ingrese el nombre del autor\n')
    pag=validarPag('ingrese la cantidad de paginas del manual\n')
    temas=addTemas()
    data['manuales'][nomManual]={
        "author":autor,
        "paginas":pag,
        "temas":temas
    }
    with open("Manuales.json",'w') as destino:
        json.dump(data,destino,indent=4)
    
def delete():
    for  llave, contenido in data['manuales'].items():
        print(f'Manual:{llave}')
    op=input('Ingrese el nombre del manual que desea eliminar\n')
    for llave, contenido in data['manuales'].items():
        cont=0
        if llave == op or llave ==op.capitalize():
            valor=data["manuales"].pop(op.capitalize())
            print(f'El manual {op.capitalize()} fue eliminado con exito\npresione enter para continuar...')
            cont+=1
            input()
            with open("Manuales.json",'w') as destino:
                json.dump(data,destino,indent=4)
            return
    if cont==0:
        return print('El manual no fue encontrado sorry!!!')
    
def updateTema():
    while True:
        op=validarMenu('Ingrese 1 para Actualizar TEMA o 0 para agregar nuevo TEMA')
        if op== 0:
            addTemas()
        elif op==1:
            print('XD')
        else:
            return

def update():
    read()
    op=input('ingrese el manual que desea actualizar\n')
    op=op.lower()
    for llave, contenido in data['manuales'].items():
        if llave == op or llave ==op.capitalize():
            llave=addType('Ingrese el NUEVO nombre del Manual\n')
            contenido["author"]=addType('Ingrese el NUEVO nombre del autor\n')
            contenido["paginas"]=validarPag('ingrese la NUEVA cantidad de paginas del manual\n')
            contenido['temas']=updateTema()
            input('Vema')
            
def generarTxt():
    texto=''
    for manual in data['manuales'].keys():
        c1=0
        c2=0
        c3=0
        texto+=f'Manual{manual}\n'
        if 'temas' in data['manuales'][manual]:
            for tema in data["manuales"][manual]["temas"]:
                if tema["Clasificacion"] ==1:
                    c1+=1
                elif tema["Clasificacion"] ==2:
                    c2+=1
                elif tema["Clasificacion"] ==3:
                    c3+=1
        texto+=f'contiene:\n temas basicos:{c1}\ntemas intermedios:{c2}\ntemas avanzados:{c3}\n'
        with open('datos.txt','w',encoding='utf-8') as destino:
            destino.write(texto)

def menu():
    nexx=True
    while nexx:
        conf=True
        os.system('clear')
        print(' '*16,'MENU PRINCIPAL \n')
        print(' '*13,"1.CREAR\n\
              2.MODIFICAR\n\
              3.ELIMINAR\n\
              4.LISTAR\n\
              5.GENERAR INFORME DE DATOS\n\
              6. salir")
        op=validarMenu('Ingrese una opcion del anterior menu\n')
        if op==6:
            nexx=False
            return print('THE END')
        elif op<1 or op>6:
            print('Ingrese una opcion correcta (1 a 6)')
            conf=False
            input('Enter...')
        if conf == True:
            switch={1:create,4:read,3:delete,5:generarTxt,2:update}
            switch[op]()

menu()
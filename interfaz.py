from singleLinkedList import SingleLinkedList

from doubleLinkedList import DoubleLinkedList
#from colorama import *
#init()


class interfaz:
    def __init__(self):
        self.new_SLL = SingleLinkedList()
        self.new_DLL = DoubleLinkedList()

    def mostrar_opciones(self):
        bandera = True
        while bandera == True:
            print('1: trabajar con listas simples')
            print('2: trabajar con listas dobles')
            print('3: salir')
            try:
                opcion = int(input('ingrese opcion: '))
                if opcion == 1:
                    self.listas_simples()
                elif opcion == 2:
                    self.listas_dobles()
                elif opcion == 3:
                    bandera = False
                else:
                    print('opcion inexistente')
            except:
                print('ingrese un numero por favor')

############################################################################

    def listas_simples(self):
        bandera = True
        while bandera == True:
            print('1: añadir nodo')
            print('2: elimianar nodo')
            print('3: consultar valor contenido en el nodo')
            print('4: modificar valor de nodo')
            print('5: invertir lista')
            print('6: validacion especial')
            print('7: salir')
            try:
                opcion = int(input('ingrese opcion: '))
                if opcion == 1:
                    self.añadir_nodo_SLL()
                elif opcion == 2:
                    self.eliminar_nodo_SLL()
                elif opcion == 3:
                    self.new_SLL.show_info_sll()
                    try:
                        posicion = int(input('en que posicion: '))
                        if posicion <= self.new_SLL.length:
                            self.consultar_valor_SLL(posicion)
                        else:
                            print('posicion erronea')
                    except:
                        print('ingrese un numero por favor')
                elif opcion == 4:
                    self.new_SLL.show_info_sll() #####
                    try:
                        posicion = int(input('en que posicion: '))
                        if posicion <= self.new_SLL.length:
                            valor = int(input('que valor: '))
                            self.modificar_valor_SLL(posicion, valor)
                        else:
                            print('posicion inexistente')
                    except:
                        print('ingrese un numero por favor')
                elif opcion == 5:
                    self.invertir_lista_SLL()
                elif opcion == 6:
                    self.validacion_especial_SLL()
                elif opcion == 7:
                    bandera = False
                else:
                    print('opcion inexistente')
            except:
                print('ingrese un numero por favor')

    def añadir_nodo_SLL(self):
        bandera = True
        while bandera == True:
            print('1: añadir al inicio')
            print('2: añadir al final')
            print('3: añadir en una posicion especifica')
            print('4: salir')
            try:
                opcion = int(input('ingrese opcion: '))
                if opcion >= 1 and opcion <= 3:
                    try:
                        valor = int(input('ingrese valor: '))
                        if self.buscarNodoSLL(valor) == False:
                            print('ya existe el valor')
                        else:
                            if opcion == 1:
                                self.new_SLL.unshift_node(valor)
                            elif opcion == 2:
                                self.new_SLL.push_node(valor)
                            elif opcion == 3:
                                self.new_SLL.show_info_sll() ######
                                try:
                                    posicion = int(input('en que posicion: '))
                                    if posicion <= self.new_SLL.length:
                                        self.new_SLL.insert_node(posicion, valor)
                                    else:
                                        print('posicion erronea')
                                except: 
                                    print('ingrese un numero por favor')
                    except:
                        print('ingrese un numero por favor')
                elif opcion==4:
                    bandera = False
                else:
                    print('opcion inexistente')
            except:
                print('ingrese un numero por favor')

    def eliminar_nodo_SLL(self):
        bandera = True
        while bandera == True:
            print('1: eliminar al inicio')
            print('2: eliminar al final')
            print('3: eliminar en posicion especifica')
            print('4: salir')
            try:
                opcion = int(input('ingrese opcion: '))
                if opcion == 1:
                    self.new_SLL.shift_node()
                elif opcion == 2:
                    self.new_SLL.pop_node()
                elif opcion == 3:
                    self.new_SLL.show_info_sll() #####
                    try:
                        posicion = int(input('en que posicion: '))
                        if posicion <= self.new_SLL.length:
                            self.new_SLL.remove_node(posicion)
                        else:
                            print('posicion erronea')
                    except:
                        print('ingrese un numero por favor')
                elif opcion == 4:
                    bandera = False
                else:
                    print('opcion inexistente')
            except:
                print('ingrese un numero por favor')

    def consultar_valor_SLL(self, indice):
        valor = self.new_SLL.get_node_value(indice)
        print(valor)  ######

    def modificar_valor_SLL(self, indice, valor):
        self.new_SLL.update_node_value(indice, valor)

    def invertir_lista_SLL(self):
        self.new_SLL.reverse_node()
        
    def invertir_lista_SLL_especial(self):
        contador = 1
        while contador <= self.new_SLL.length:
            new_value = pow(int(self.new_SLL.get_node_value(contador)), 0.5)
            self.new_SLL.update_node_value(contador, new_value)
            contador+=1 ######
        self.new_SLL.reverse_node()

    def validacion_especial_SLL(self):
        bandera = True
        while bandera == True:
            print('1: invertir lista (especial)')
            print('2: salir')
            try:
                opcion = int(input('opcion: '))
                if opcion == 1:
                    self.invertir_lista_SLL_especial()
                elif opcion == 2:
                    bandera = False
                else:
                    print('opcion inexistente')    
            except:
                print('ingrese un numero por favor')

            

    ############################################################DOBLEMENTE ENLAZADAS

    def listas_dobles(self):
        bandera = True
        while bandera == True:
            print('1: añadir nodo')
            print('2: elimianar nodo')
            print('3: consultar valor contenido en el nodo')
            print('4: modificar valor de nodo')
            print('5: invertir lista')
            print('6: validacion especial')
            print('7: salir')
            try:
                opcion = int(input('ingrese opcion: '))
                if opcion == 1:
                    self.añadir_nodo_DLL()
                elif opcion == 2:
                    self.eliminar_nodo_DLL()
                elif opcion == 3:
                    print(self.new_DLL.print_list())
                    try:
                        posicion = int(input('en que posicion: '))
                        if posicion <= self.new_DLL.length:
                            self.consultar_valor_DLL(posicion)
                        else:
                            print('posicion inexistente')
                    except:
                        print('ingrese un numero por favor')
                elif opcion == 4:
                    print(self.new_DLL.print_list()) #####
                    try:
                        posicion = int(input('en que posicion: '))
                        if posicion <= self.new_DLL.length:
                            try:
                                valor = int(input('que valor: ')) ###
                                self.modificar_valor_DLL(posicion, valor)
                            except:
                                print('ingrese un numero por favor')
                        else:
                            print('posicion inexistente')
                    except:
                        print('ingrese un numero por favor')
                elif opcion == 5:
                    self.invertir_lista_DLL()
                elif opcion == 6:
                    self.validacion_especial_DLL()
                elif opcion == 7:
                    bandera = False
                else:
                    print('opcion inexistente')
            except:
                print('ingrese un numero por favor')

    def añadir_nodo_DLL(self):
        bandera = True
        while bandera == True:
            print('1: añadir al inicio')
            print('2: añadir al final')
            print('3: añadir en una posicion especifica')
            print('4: salir')
            try:
                opcion = int(input('ingrese opcion: '))
                if opcion >= 1 and opcion <=3:
                    valor = int(input('ingrese valor: '))
                    if self.buscarNodoDLL(valor) == False:
                        print('ya existe el valor')
                    else:
                        if opcion == 1:
                            self.new_DLL.unshift_node(valor)
                        elif opcion == 2:
                            self.new_DLL.push_node(valor)
                        elif opcion == 3:
                            print(self.new_DLL.print_list()) #####
                            try:
                                posicion = int(input('en que posicion: '))
                                if posicion <= self.new_DLL.length:
                                    self.new_DLL.insert_node(posicion, valor)
                                else:
                                    print('posicion erronea')
                            except:
                                print('ingrese un numero por favor')
                elif opcion == 4:
                    bandera = False
                else:
                    print('opcion inexistente')
            except:
                print('ingrese un numero por favor')

    def eliminar_nodo_DLL(self):
        bandera = True
        while bandera == True:
            print('1: eliminar al inicio')
            print('2: eliminar al final')
            print('3: eliminar en posicion especifica')
            print('4: salir')
            try:
                opcion = int(input('ingrese opcion: '))
                if opcion == 1:
                    self.new_DLL.shift_node()
                elif opcion == 2:
                    self.new_DLL.pop_node()
                elif opcion == 3:
                    print(self.new_DLL.print_list()) ####
                    try:
                        posicion = int(input('en que posicion: '))
                        if posicion <= self.new_DLL.length:
                            self.new_DLL.remove_node(posicion)
                        else: 
                            print('posicion erronea')
                    except:
                        print('ingrese un numero por favor')
                elif opcion == 4:
                    bandera = False
                else:
                    print('opcion inexistente')
            except:
                print('ingrese un numero por favor')

    def consultar_valor_DLL(self, indice):
        valor = self.new_DLL.get_node_value(indice)
        print(valor) ######

    def modificar_valor_DLL(self, indice, valor):
        self.new_DLL.update_node_value(indice, valor)

    def invertir_lista_DLL_especial(self):
        contador = 1
        tamaño = self.new_DLL.length
        while contador <= tamaño:
            new_value = pow(int(self.new_DLL.get_node_value(contador)), 0.5)
            ##print(new_value)
            self.new_DLL.update_node_value(contador, new_value)
            print(self.new_DLL.print_list())
            contador+=1 #####
            ##print(contador)
        self.new_DLL.reverse_node()
        
    def invertir_lista_DLL(self):
        self.new_DLL.reverse_node()
        
    def validacion_especial_DLL(self):
        bandera = True
        while bandera == True:
            print('1: invertir lista (especial)')
            print('2: actualizar valor nodo (especial)')
            print('3: salir')
            try:
                opcion = int(input('opcion: '))
                if opcion == 1:
                    self.invertir_lista_DLL_especial()
                elif opcion == 2:
                    print(self.new_DLL.print_list()) #####
                    try:
                        posicion = int(input('en que posicion: '))
                        if posicion <= self.new_DLL.length:
                            valor = int(input('que valor: '))
                            if self.validacionModificarNodo(posicion, valor)==True:
                                self.modificar_valor_DLL(posicion, valor)
                            else:
                                print('valor a erroreno')
                        else:
                            print('posicion erronea')
                    except:
                        print('ingrese un numero por favor')
                elif opcion == 3:
                    bandera = False
                else:
                    print('opcion inexistente')
            except:
                print('ingrese un numero por favor')
        
##################################################################PUNTOS 4, 5, 6

    def buscarNodoSLL(self, valor):
        contador = 1
        while contador <= self.new_SLL.length:
            if self.new_SLL.get_node_value(contador) == valor:
                return False
            contador+=1
        return True
    
    def buscarNodoDLL(self, valor):
        contador = 1
        while contador <= self.new_DLL.length:
            if self.new_DLL.get_node_value(contador) == valor:
                return False
            contador+=1
        return True
    
    def validacionModificarNodo(self, indice, valor):
        v1 = int(self.new_DLL.get_node_value(indice-1))
        if valor == v1 * v1:
            return True
        else:
            return False
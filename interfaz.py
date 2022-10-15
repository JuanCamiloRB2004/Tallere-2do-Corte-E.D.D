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
            opcion = int(input('ingrese opcion: '))
            if opcion == 1:
                self.listas_simples()
            elif opcion == 2:
                print('ya')
            elif opcion == 3:
                bandera = False

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
            opcion = int(input('ingrese opcion: '))
            if opcion == 1:
                self.añadir_nodo_SLL()
            elif opcion == 2:
                self.eliminar_nodo_SLL()
            elif opcion == 3:
                self.new_SLL.show_info_sll()
                posicion = int(input('en que posicion: '))
                self.consultar_valor_SLL(posicion)
            elif opcion == 4:
                posicion = int(input('en que posicion: '))
                valor = input('que valor')
                self.modificar_valor_SLL(posicion, valor)
            elif opcion == 5:
                self.invertir_lista_SLL()
            elif opcion == 6:
                self.validacion_especial_SLL()
            elif opcion == 7:
                bandera = False

    def añadir_nodo_SLL(self):
        bandera = True
        while bandera == True:
            print('1: añadir al inicio')
            print('2: añadir al final')
            print('3: añadir en una posicion especifica')
            print('4: salir')
            opcion = int(input('ingrese opcion: '))
            valor = input('ingrese valor: ')
            if self.buscarNodoSLL(valor) == False:
                print('ya existe el valor')
            else:
                if opcion == 1:
                    self.new_SLL.unshift_node(valor)
                elif opcion == 2:
                    self.new_SLL.push_node(valor)
                elif opcion == 3:
                    posicion = int(input('en que posicion: '))
                    self.new_SLL.insert_node(posicion, valor)
                elif opcion == 4:
                    bandera = False

    def eliminar_nodo_SLL(self):
        bandera = True
        while bandera == True:
            print('1: eliminar al inicio')
            print('2: eliminar al final')
            print('3: eliminar en posicion especifica')
            print('4: salir')
            opcion = int(input('ingrese opcion: '))
            if opcion == 1:
                self.new_SLL.shift_node()
            elif opcion == 2:
                self.new_SLL.pop_node()
            elif opcion == 3:
                posicion = int(input('en que posicion: '))
                self.new_SLL.remove_node(posicion)
            elif opcion == 4:
                bandera = False

    def consultar_valor_SLL(self, indice):
        valor = self.new_SLL.get_node_value(indice)
        return valor

    def modificar_valor_SLL(self, indice, valor):
        self.new_SLL.update_node_value(indice, valor)

    def invertir_lista_SLL(self):
        self.new_SLL.reverse_node()
        
    def invertir_lista_SLL_especial(self):
        contador = 1
        while contador < self.new_SLL.length:
            new_value = pow(self.new_SLL.get_node_value(contador), 1/2)
            self.new_SLL.update_node_value(contador, new_value)
        self.new_SLL.reverse_node()

    def validacion_especial_SLL(self):
        print('1: invertir lista (especial)')
        print('2: salir')
        opcion = int(input('opcion: '))
        bandera = True
        while bandera == True:
            if opcion == 1:
                self.invertir_lista_SLL_especial()
            elif opcion == 2:
                bandera = False
            

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
            opcion = int(input('ingrese opcion: '))
            if opcion == 1:
                self.añadir_nodo_DLL()
            elif opcion == 2:
                self.eliminar_nodo_DLL()
            elif opcion == 3:
                print(self.new_DLL.print_list())
                posicion = int(input('en que posicion: '))
                self.consultar_valor_DLL(posicion)
            elif opcion == 4:
                posicion = int(input('en que posicion: '))
                valor = input('que valor')
                if self.validacionModificarNodo(posicion, valor)==True:
                    self.modificar_valor_DLL(posicion, valor)
                else:
                    print('valor a erroreno')
            elif opcion == 5:
                self.invertir_lista_DLL()
            elif opcion == 6:
                print('para despues')
            elif opcion == 7:
                bandera = False

    def añadir_nodo_DLL(self):
        bandera = True
        while bandera == True:
            print('1: añadir al inicio')
            print('2: añadir al final')
            print('3: añadir en una posicion especifica')
            print('4: salir')
            opcion = int(input('ingrese opcion: '))
            valor = input('ingrese valor: ')
            if self.buscarNodoDLL(valor) == False:
                print('ya existe el valor')
            else:
                if opcion == 1:
                    self.new_DLL.unshift_node(valor)
                elif opcion == 2:
                    self.new_DLL.push_node(valor)
                elif opcion == 3:
                    posicion = int(input('en que posicion: '))
                    self.new_DLL.insert_node(posicion, valor)
                elif opcion == 4:
                    bandera = False

    def eliminar_nodo_DLL(self):
        bandera = True
        while bandera == True:
            print('1: eliminar al inicio')
            print('2: eliminar al final')
            print('3: eliminar en posicion especifica')
            print('4: salir')
            opcion = int(input('ingrese opcion: '))
            if opcion == 1:
                self.new_DLL.shift_node()
            elif opcion == 2:
                self.new_DLL.pop_node()
            elif opcion == 3:
                posicion = int(input('en que posicion: '))
                self.new_DLL.remove_node(posicion)
            elif opcion == 4:
                bandera = False

    def consultar_valor_DLL(self, indice):
        valor = self.new_DLL.get_node_value(indice)
        return valor

    def modificar_valor_DLL(self, indice, valor):
        self.new_DLL.update_node_value(indice, valor)

    def invertir_lista_DLL_especial(self):
        contador = 1
        while contador < self.new_DLL.length:
            new_value = pow(self.new_DLL.get_node_value(contador), 1/2)
            self.new_DLL.update_node_value(contador, new_value)
        self.new_DLL.reverse_node()
        
    def invertir_lista_DLL(self):
        self.new_DLL.reverse_node()
        
    def validacion_especial_DLL(self):
        print('1: invertir lista (especial)')
        print('2: salir')
        opcion = int(input('opcion: '))
        bandera = True
        while bandera == True:
            if opcion == 1:
                self.invertir_lista_DLL_especial()
            elif opcion == 2:
                bandera = False
        
##################################################################PUNTOS 4, 5, 6

    def buscarNodoSLL(self, valor):
        contador = 1
        while contador < self.new_SLL.length:
            if self.new_SLL.get_node_value(contador) == valor:
                return False
        return True
    
    def buscarNodoDLL(self, valor):
        contador = 1
        while contador < self.new_DLL.length:
            if self.new_DLL.get_node_value(contador) == valor:
                return False
        return True
    
    def validacionModificarNodo(self, indice, valor):
        if valor == self.new_DLL.get_node_value(indice-1)*self.new_DLL.get_node_value(indice-1):
            return True
        else:
            return False
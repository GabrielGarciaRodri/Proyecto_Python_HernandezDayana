import os
import sys
import modules as modulo

if __name__=='__main__':
    print(modulo.menu)
    isActive=True
    while isActive:
        try:
            opcion=input('Escriba aqui la opcion')
            match opcion:
                case 1:
                    modulo.registrarJ()
                    modulo.jugarPc()
                
                
                
                
                
        except:
            input('Elija una opcion correcta ')
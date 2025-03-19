print("bienvenido al banco CETIS 50")
print("***********")

# saldo inicial
saldo = 1000 # saldo inicial

#bucle de cajero automatico
while True:
    print("\nseleccione una opcion:")
    print("1. consultar saldo")
    print("2. realizar deposito")
    print("3.realizar retiro")
    print("4. salir")
    opcion = input("ingrese el numero de la opcion deseada: ")
    
    # consultar saldo
    if opcion == "1":
        print(f"su saldo actual es: ${saldo}")
        
    # realizar deposito
    elif opcion == "2":
        deposito = float(input("ingrese el monto a depositar: "))
        saldo += deposito
        print(f"deposito realizado. su nuevo saldo es: ${saldo}")
        
    # realizar retiro
    elif opcion == "3":
        retiro = float (input("ingrese el monto a retirar: "))
        if retiro > saldo:
            print("saldo insuficiente.")
        else:
            saldo -= retiro
            print(f"retiro realizado su nuevo saldo es: ${saldo}")
    # salir
    elif opcion == "4":
        print("gracias por usar banco CETIS 50. ¡hasta luego!")
        break
    
    #opcion invalida
    else:
        print("opcion invalida. intente nuevamente.")
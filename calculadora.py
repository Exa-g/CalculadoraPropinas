def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Ingresa un numero valido.")
            
def obtener_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= 0:
                return valor
            else:
                print("Error: Ingresa un numero entero positivo.")
        except ValueError:
            print("Error: Ingresar un numero entero valido.")
         
def calculadora_propina(monto, porcentaje):
    propina = monto * (porcentaje / 100)
    return propina

def dividir_cuenta(total, personas):
    return total / personas

def redondear_total(total):
    return round(total,2)

def main():
    print("Bien benido a la Calculadora de Propinas")
    
    #Ingresa el monto de la cuenta
    monto_cuenta = obtener_numero("Ingresa el monto de la cuenta: $")
    
    #Ingresar el porcentaje de propina deseada
    porcentanje_propina = obtener_numero("Ingresa el porcentaje de propina (porcentaje deseado): ")
    
    #Calcula la propina
    propina = calculadora_propina(monto_cuenta, porcentanje_propina)
    
    #Preguntar si se desea redondear el total
    redondear = input("Desea redondear el total? (Si/No): ").lower() == "si"
    
    #Calcula el total con o sin redondeo
    total = monto_cuenta + propina
    
    if redondear:
        total = redondear_total(total)
        
    #Preguntar si desea dividir la cuenta
    dividir = input("Desea dividir la cuenta? (Si/No): ").lower() == "si"
    
    #Calcular y mostrar el total final
    if dividir:
        personas = obtener_entero_positivo("Ingresa el numero de personas: ")
        total_por_persona = dividir_cuenta(total, personas)
        print("\n=== Resultado ===")
        print(f"Total a pagar (incluyendo propina): ${total: .2f}")
        print(f"Total por persona (dividido entre {personas} personas): ${total_por_persona: .2f}")
    else:
        print("\n=== Resultado ===")
        print(f"Total a pagar (incluyendo propina): ${total:.2f}")
        
if __name__ == "__main__":
    main()
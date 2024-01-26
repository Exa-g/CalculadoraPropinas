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
    monto_cuenta = float(input("Ingresa el monto de la cuenta: $"))
    
    #Ingresar el porcentaje de propina deseada
    porcentanje_propina = float(input("Ingresa el porcentaje de propina (porcentaje deseado): " + "%"))
    
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
        personas = int(input("Ingresa el numero de personas: "))
        total_por_persona = dividir_cuenta(total, personas)
        print(f"\nCada persona debe pagar: ${total_por_persona: 2f}")
    else:
        print(f"\nEl total a pagar es: ${total:.2f}")
        
        if __name__ == "__main__":
            main()
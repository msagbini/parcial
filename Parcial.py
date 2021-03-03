# Punto 1
c_llantas = int(input('Digite cuántas llantas va a adquirir: '))
if c_llantas >= 1 and c_llantas < 5:
    p_unit = 300
    v_pagar = p_unit * c_llantas
    print(f'El valor por llanta es: {p_unit} y el valor total es: {v_pagar}')
elif c_llantas >= 5 and c_llantas <= 10:
    p_unit = 250
    v_pagar = p_unit * c_llantas
    print(f'El valor por llanta es: {p_unit} y el valor total es: {v_pagar}')
elif c_llantas > 10:
    p_unit = 200
    v_pagar = p_unit * c_llantas
    print(f'El valor por llanta es: {p_unit} y el valor total es: {v_pagar}')
else:
    print("Digita otro valor.")
            
# Punto 2

valor_pagar = int(input("Digite el valor de su compra: "))
n_cedula = str(input('Escriba los 2 últimos dígitos de su cédula: '))

if n_cedula == '01':
    valor_pagar = valor_pagar * 0.9
    print(f'El valor total de su compra es: {valor_pagar}')
elif n_cedula == '25':
    valor_pagar = valor_pagar * 0.75
    print(f'El valor total de su compra es: {valor_pagar}')
elif n_cedula == '44':
    valor_pagar = valor_pagar * 0.65
    print(f'El valor total de su compra es: {valor_pagar}')
elif n_cedula == '57':
    valor_pagar = valor_pagar * 0.5
    print(f'El valor total de su compra es: {valor_pagar}')
else:
    print(f'El valor total de su compra es: {valor_pagar}')
    
# Punto 3

valor_colchones = int(input('Digite el precio de los colchones: '))
cantidad_colchones = int(input('Cuántos colchones desea adquirir: '))
if cantidad_colchones > 0 and cantidad_colchones < 3:
    valor_pagar = (valor_colchones * cantidad_colchones)
    print(f'El valor total de su compra es: {valor_pagar}')
elif cantidad_colchones >= 3 and cantidad_colchones < 6:
    valor_pagar = (valor_colchones * cantidad_colchones) * 0.8
    print(f'El valor total de su compra es: {valor_pagar}')
elif cantidad_colchones >= 6 and cantidad_colchones < 8:
    valor_pagar = (valor_colchones * cantidad_colchones) * 0.75
    print(f'El valor total de su compra es: {valor_pagar}')
elif cantidad_colchones >= 8:
    valor_pagar = (valor_colchones * cantidad_colchones) * 0.7
    print(f'El valor total de su compra es: {valor_pagar}')
else:
    print("No aplicó descuento")
 
# Punto 4

n_estudiantes = int(input('Digite el número de estudiantes: '))
if n_estudiantes < 20:
    elegidos = n_estudiantes * 0.5
    print(f'El número de estudiantes seleccionados es de: {elegidos}')
elif n_estudiantes >= 20 and n_estudiantes <= 30:
    elegidos = n_estudiantes * 0.6
    print(f'El número de estudiantes seleccionados es de: {elegidos}')
elif n_estudiantes > 30:
    elegidos = n_estudiantes * 0.7
    print(f'El número de estudiantes seleccionados es de: {elegidos}')
else:
    print("La cantidad no aplica para la muestra")
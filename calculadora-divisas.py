# -+- coding: utf-8 -*-

def euro_dolar_calculator(ammount):
    # A día de hoy: 1 € son 1.13 $
    euro_to_dollar_rate = 1.13
    return ammount * euro_to_dollar_rate

def run():
    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('-----------------------------------------')
    print('Convierte de euros a dolares.')
    print('Cambio: 1 euro = 1.13 dolares')
    print('-----------------------------------------')

    ammount = float(input('Ingresa la cantidad de euros a convertir: '))

    result = euro_dolar_calculator(ammount)

    print("${} euros son ${} dolares.".format(ammount, result))
    print('')
    print('-----------------------------------------')



if __name__ == '__main__':
    run()
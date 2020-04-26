def run():
    print('')
    print('------------- SERIES DE TIEMPO -------------')
    print('')
    number_values = int(input('Digite la cantidad de valores a registrar: '))
    values = []

    for i in range(number_values):
        item = float(input('Digite el valor de la serie de tiempo: '))
        values.append(item)

    print('')
    print('')
    print('------------- DIFERENCIAS FINITAS -------------')
    print('Las diferencias de finitas de la serie de timepo registrada son:')
    print('')

    for i in range ( len(values) ):
        if i < len(values) -1:
            a = values[i]
            b = values[i + 1]
            result = b - a
            print(result)

if __name__ == '__main__':
    run()
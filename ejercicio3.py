def run():

    print('')
    print('************* Instituto Técnico de Contaduría *************')
    print('')

    number_students = int(input('Digite la cantidad de estudiantes de la carrera Técnico en Contaduría: '))
    students_list = []

    if number_students < 1:
        print('No hay estudiantes en la carrera Técnico en Contaduría')

    for i in range(number_students):
        student_name = str(input('Digite el nombre completo del estudiante: '))
        student_grade = float(input('Digite la nota del estudiante: '))
            
        if student_grade < 0.0 :
            print('La nota del estudiante debe ser mayor a 0.0')
            student_grade = float(input('Digite la nota del estudiante: '))
            
        if student_grade > 5.0 :
            print('La nota del estudiante debe ser menor a 5.0')
            student_grade = float(input('Digite la nota del estudiante: '))

        student = [student_name, student_grade]
        students_list.append(student)
    
    print('')
    print('')
    print('****************************************************')
    print('')
    print('Informes del Instituto Técnico de contaduría')
    print('')
    print('****************************************************')
    print('')

    average = 0
    under_average = 0
    for student in students_list:
        print('La nota del estudiante {} es {}'.format(student[0], student[1]))
        average = average + student[1]

    average = average / len(students_list)

    for student in students_list:
        if student[1] < average:
            under_average = under_average + 1
    
    students_list.sort(key=lambda student: student[1])
    student_low_grade = students_list[0]
    student_high_grade = students_list[len(students_list)-1]

    print('')
    print('El estudiante que obtuvo la mayor nota fue: {}'.format(student_high_grade[0]))
    print('La nota obtenida por {} fue: {} '.format( student_high_grade[0], student_high_grade[1] ))

    print('')
    print('El estudiante que obtuvo la menor fue: {}'.format(student_low_grade[0]))
    print('La nota obtenida por {} fue: {} '.format( student_low_grade[0], student_low_grade[1] ))
    
    print('')
    print('El promedio de notas de los {} estudiantes fue: {}'.format(len(students_list), average))

    if under_average > 1:
        print('La cantidad de estudiantes con una nota inferior a {} son: {} estudiantes.'.format( average, under_average ) )
    else:
        print('La cantidad de estudiantes con una nota inferior a {} son: {} estudiante.'.format( average, under_average ) )

if __name__ == '__main__':
    run()
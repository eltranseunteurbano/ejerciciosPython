import numpy as np
import random

def fill (matriz, grades):
    rows = np.size(matriz[0:,0]) - 1
    columns = np.size(matriz[0,0:]) - 1

    position = 0

    for i in range (0, rows):
        for j in range(0, columns):
            position = position + 1
            matriz[i,j] = grades[position-1]

    return matriz

def drawData(matriz, students, courses):
    rows=np.size(matriz[0:,0])
    columns=np.size(matriz[0,0:])
    text=""

    for i in range(-1, rows):
        for j in range(-1,columns):
            if(i==-1 and j==-1):
                text = "\t"
            elif(i==-1 and j>=0 and j <columns-1):
                text = text + "\t" + str(courses[j])

            elif(i>=0 and i < rows-1 and j==-1):
                text = text + "\n" + str(students[i])

            elif(i>=0 and i<rows-1 and j< columns-1 and j>=0):
                text = text + "\t" + str(matriz[i,j])

            elif(i == rows and j == -1):
                text = "promedio"
    return text

def average(type_average, search, vector, matriz,):
    position = 0
    prom = 0
    for i in range(0, np.size(vector)):
        if search == vector[i]:
            position = i

    if type_average == 'courses':
        prom = np.mean(matriz[0:,position])
    
    if type_average == 'students':
        prom = np.mean(matriz[position,0:])
    
    return prom

def standar_deviation(search, vector, matriz):
    position = 0
    standar = 0

    for i in range (0, np.size(vector)):
        if search == vector[i]:
            position = i
    
    standar = np.std(matriz[position,0:])
    return standar


def run():

    print('')
    print('************* Instituto Técnico de Contaduría *************')
    print('')

    number_students = int(input('Digite la cantidad de estudiantes de la carrera Técnico en Contaduría: '))
    number_courses = int(input('Digite la cantidad de asignaturas: '))

    students_list = []
    courses_list = []

    student_high_grades = ''
    student_low_grades = ''

    group_average = 0
    under_average = 0

    averages_course = []
    courses_grades = []

    if number_students > 0:
        for i in range(number_students):
            name = str(input('Digite el nombre completo del estudiante: '))
            students_list.append(name)
    
    if number_courses > 0:
        for i in range(number_courses):
            name = str(input('Digite el nombre completo de la asignatura: '))
            courses_list.append(name)
    
    for student in students_list:
        print('******* Digite las notas del estudiante {} *******'.format(student))
        for course in courses_list:
            grade_value = float(input('Dige la nota de la asignatura {} : '.format(course)))
            if(grade_value < 0.0):
                print('Por favor ingrese un número mayor a 0.0')
                grade_value = float(input('Dige la nota de la asignatura {} : '.format(course)))
            elif(grade_value > 5.0):
                print('Por favor ingrese un número menor a 5.0')
                grade_value = float(input('Dige la nota de la asignatura {} : '.format(course)))

            courses_grades.append(grade_value)
    
    grades_courses = np.empty( ( (number_students + 1) , (number_courses + 1) ) )
    grades_matriz = fill(grades_courses, courses_grades)    
    print('')
    print('')
    print('****************************************************')
    print('')
    print('Informes del Instituto Técnico de contaduría')
    print('')
    print('****************************************************')

    print('')
    print('******* Promedio de notas por estudiante *******')
    print('')
    student_grade = []
    for i in range (len(students_list)):
        average_value = average('students', students_list[i], students_list, grades_matriz)
        print('La nota promedio del estudiante {} es {}'.format( students_list[i], average_value ))
        student_grade.append([students_list[i], average_value])
        group_average = group_average + average_value
    
    group_average = group_average / len(students_list)
    student_grade.sort(key=lambda average: average[1])

    student_high_grades = student_grade[len(student_grade)-1]
    student_low_grades = student_grade[0]

    for student in student_grade:
        if student[1] < group_average:
            under_average = under_average + 1

    print('')
    print('')
    print('******* Promedio de notas por asignatura *******')
    print('')
    for i in range (len(courses_list)):
        average_value = average('courses', courses_list[i], courses_list, grades_matriz)
        print('La nota promedio de la asignatura {} es {}'.format( courses_list[i], average_value ))
        averages_course.append(average_value)

    print('')
    print('El estudiante que obtuvo la mayor nota fue {}'.format(student_high_grades[0]))
    print('La nota obtenido por {} fue: {}'.format(student_high_grades[0], student_high_grades[1]))

    print('')
    print('El estudiante que obtuvo la menor nota fue {}'.format(student_low_grades[0]))
    print('La nota obtenido por {} fue: {}'.format(student_low_grades[0],student_low_grades[1]))

    print('')
    print('La nota promedio del grupo fue: {}'.format(group_average))

    print('')
    if under_average > 1:
        print('La cantidad de estudiantes con una nota inferior a {} son : {} estudiantes'.format(group_average, under_average))
    else:
        print('La cantidad de estudiantes con una nota inferior a {} son : {} estudiante'.format(group_average, under_average))

    print('')
    standar_value = standar_deviation(student_high_grades, students_list, grades_matriz)
    print('La desviación estándar de las notas obtenidas por el estudiante {} es {}'.format(student_high_grades[0],standar_value))

    print('')

    draw = drawData(grades_matriz, students_list, courses_list)
    print(draw)

if __name__ == '__main__':
    run()
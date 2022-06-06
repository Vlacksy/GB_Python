def students_gen(tutors, klasses):
    for i in range(len(tutors)):
        if i+1 > len(klasses):
            yield tutors[i], None
        else:
            yield tutors[i], klasses[i]


tutors_1 = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses_1 = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

tutors_2 = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses_2 = ['9А', '7В', '9Б', '9В', '8Б']  # check when number of klasses less than tutors

students_gen_1 = students_gen(tutors_1, klasses_1)
students_gen_2 = students_gen(tutors_2, klasses_2)

print(*students_gen_1)
print(*students_gen_2)


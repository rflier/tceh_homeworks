right_answers = 0

def validate_answer(user_answer, valid_answer):
    global right_answers

    if answer1 == valid_answer:
        print('Right')
        right_answers += 1
    else:
        print('Wrong!')

# databas = {
#     'Wat is 1': 'int'.
# }

# for question, answe in database.items(0:
#     print(question, answe))

answer1 = input('What is 1? ')
validate_answer(answer1, 'int')

answer2 = input('2+2 = ?' )
validate_answer(int(answer2, 'int'))

answer3 = input('Capital of Russia? ')
validate_answer(answer3, 'Moscow')


print('You gave {} right answers' .format(right_answers))


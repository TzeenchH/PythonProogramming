step_counter = 0


def switcher():
    print('Выберите решение(да или нет):')
    choose = input().lower()
    step_builder(choose)


def step_builder(ch: str):
    correct_answers = ('да', 'нет')
    if ch not in correct_answers:
        print('введите один из указанных вариантов')
        switcher()
    global step_counter
    positive_chose = ('Не уверен что уткам нужны зонтики, но кто я чтобы спорить.',
                      'Честно говоря я не знаю',
                      'Такой темы диалога я не ожидал',
                      'Тут должна быть не менее хтоническая вставка для да, но я её не предумал',)
    negative_chose = ('Логично, зачем ей зонт. она же утка.',
                      'Вот и хорошо, я всё равно не знаю',
                      'Нет, мы определённо обсуждаем утку',
                      'Ещё одна ветка диалога, придумаю после релиза',)
    answers = ('Хотите знать куда она пошла?',
               'Мы обсуждаем утку, вы же это понимаете?',
               'Это странно, не так ли?',
               'Продам гараж оптом, берёте?',
               'Вам не продам. Спасибо за внимание',)
    if step_counter == 4:
        print(answers[step_counter])
        exit(0)
    if ch == 'да':
        print(positive_chose[step_counter])
        print(answers[step_counter])
        step_counter += 1
        return switcher()

    print(negative_chose[step_counter])
    print(answers[step_counter])
    step_counter += 1
    return switcher()


if __name__ == "__main__":
    print('утка маляр вышла погулять, ей взять зонт?')
    switcher()

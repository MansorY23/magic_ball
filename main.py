import random
def greeting():
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    name = input('Как тебя зовут?')
    print(f"Привет, {name}")

def choice(answer):
    random_answer = random.randint(0,20)
    return answer[random_answer]

ball_answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

greeting()
while True:
    question = input('Задай вопрос')
    print(choice(ball_answers))
    another_question = input('Хочешь задать ещё вопрос?')
    if another_question == 'да':
        continue
    elif another_question == 'нет':
        print('Возвращайся если возникнут вопросы!')
        break


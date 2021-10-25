
def open_qustions(
        number: int
                  ):
    with open('modules/ru.txt', 'r', encoding='utf-8') as file:
        question = file.read().split('#\n')[number]
    return question
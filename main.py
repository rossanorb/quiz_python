from utils import clear, header
from questions import Questions
from data import series, questions


def main():
    clear()
    header()

    q = Questions(series, questions)
    question = ''

    while question != 'END':
        question = q.get_next_question()

        if question != 'END':
            print(question)

            op = input('Escolha uma das opções acima: ')
            Questions.set_answer(op)

        clear()

    Questions.show_answers()
    Questions.reset()


if __name__ == '__main__':
    while True:
        main()

        input('Pressione <ENTER> para continuar...')

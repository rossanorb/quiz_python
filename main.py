from utils import clear, header
from questions import Questions
from data import series, questions


def main():
    clear()
    q = Questions(series, questions)

    while q.next_question():
        op = input("\nEscolha uma das opções acima:\n\n")
        Questions.set_answer(op)
        clear()

    Questions.show_answers()
    Questions.reset()


while True:
    header()
    input('Pressione <ENTER> para continuar...')

    main()

    input('Pressione <ENTER> para refazer o teste...')
    clear()

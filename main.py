from utils import clear, header
from questions import Questions
from data import series, questions


def main():
    clear()
    question = Questions(series, questions)

    while question.next_question():
        op = input("\nEscolha uma das opções acima:\n\n")
        while not question.option_validation(op):
            print('Opção inválida!')
            op = input("\nEscolha entre a, b, c, d ou e:\n\n")

        question.set_answer(op)
        clear()

    question.show_result()
    question.reset()


while True:
    header()
    input('Pressione <ENTER> para continuar...\n')

    main()

    input('Pressione <ENTER> para refazer o teste...\n')
    clear()



class Questions:

    answers = {
        1: '',
        2: '',
        3: '',
        4: '',
        5: ''
    }

    def __init__(self, series, questions):
        self.__series = series()
        self.__questions = questions()

    def series(self):
        print(self.__series['a']['serie'])
        print(self.__series['a']['msg'])

    def get_next_question(self):
        for aw in Questions.answers:
            if Questions.answers[aw] == '':
                return self.__questions[aw]['title']

        return 'END'

    @staticmethod
    def set_answer(value):
        for aw in Questions.answers:
            if Questions.answers[aw] == '':
                Questions.answers[aw] = value
                return True

        return False

    @staticmethod
    def show_answers():
        for aw in Questions.answers:
            if Questions.answers[aw] != '':
                print("index {index} é {valor} ".format(index=aw, valor=Questions.answers[aw]))
            else:
                print("index {index} é vazio".format(index=aw))

    @staticmethod
    def reset():
        for aw in Questions.answers:
            Questions.answers[aw] = ''

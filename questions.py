import random


class Questions:

    answers = {
        1: '',
        2: '',
        3: '',
        4: '',
        5: ''
    }

    options = {}

    def __init__(self, series, questions):
        self.__series = series()
        self.__questions = questions()

    def series(self):
        print(self.__series['a']['serie'])
        print(self.__series['a']['msg'])

    @staticmethod
    def option_validation(value):
        for option in Questions.options:
            if option == value:
                return True
        return False

    @staticmethod
    def scramble(data):
        index = ['a', 'b', 'c', 'd', 'e']
        i = 0

        ls = list(data.items())
        random.shuffle(ls)
        ls_scrambled = dict(ls)

        for item in ls_scrambled:
            Questions.options[index[i]] = {
                'letter': item,
                'text': ls_scrambled[item]
            }
            i = i + 1

        return Questions.options

    @staticmethod
    def show_question(data):
        data['questions'] = Questions.scramble(data['questions'])

        print(data['title'])
        for q in data['questions']:
            print("\n%s) %s" % (q, data['questions'][q]['text']))

    def next_question(self):
        for aw in Questions.answers:
            if Questions.answers[aw] == '':
                self.show_question(self.__questions[aw])
                return True

        return False

    @staticmethod
    def set_answer(option):
        value = Questions.options[option]['letter']
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
                print("index %d é vazio " % aw)

    @staticmethod
    def reset():
        for aw in Questions.answers:
            Questions.answers[aw] = ''

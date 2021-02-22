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

    def option_validation(self, value):
        for option in Questions.options:
            if option == value:
                return True
        return False

    @staticmethod
    def __scramble(data):
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
    def __show_question(data):
        data['questions'] = Questions.__scramble(data['questions'])

        print(data['title'])
        for q in data['questions']:
            print("\n%s) %s" % (q, data['questions'][q]['text']))

    def next_question(self):
        for aw in Questions.answers:
            if Questions.answers[aw] == '':
                self.__show_question(self.__questions[aw])
                return True

        return False

    def set_answer(self, option):
        value = Questions.options[option]['letter']
        for aw in Questions.answers:
            if Questions.answers[aw] == '':
                Questions.answers[aw] = value
                return True

        return False

    def reset(self):
        for aw in Questions.answers:
            Questions.answers[aw] = ''

    def show_result(self):
        answers = []
        result = {}

        for answer in Questions.answers:
            answers.append(Questions.answers[answer])

        answers.sort()
        for letter in answers:
            result[letter] = answers.count(letter)

        max_key = max(result, key=result.get)
        print("\n:::::: %s ::::::\n%s\n" % (self.__series[max_key]['serie'], self.__series[max_key]['msg']))

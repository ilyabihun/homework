from datetime import date, datetime


class Human:
    def __init__(self, name, surname, dob):
        self._name = name
        self._surname = surname
        self.__dob = dob
        self._age = 0

    def hello(self):
        print(f'Hello {self._name}')

    def age_in(self):
        today = date.today()
        self._age = today.year - self.__dob.year - ((today.month, today.day) < (self.__dob.month, self.__dob.day))
        return self._age


class Parents:
    def __init__(self, mother, father, brother_sister):
        self.mother = mother
        self.father = father
        self.brother_sister = brother_sister

    def check_br_or_sis(self):
        if self.brother_sister == '':
            print('Lucky, you are the main favorite in the family')
        else:
            return

    def acquaintance(self):
        print(f'Now i know your family {self._name}')

class Work:

    def __init__(self, company):
        if age >= 18:
            self.company = company
        else:
            print('You are still small')


class Passport:

    def __init__(self, ident_number, p_of_i, reg):
        if self._age >= 14:
            self.ident_number = ident_number
            self.p_of_i = p_of_i
            self.reg = reg
        else:
            print('You are still small')


class Work:
    def __init__(self, company):
            self.company = company


class Auto_story:
    def __init__(self, license):
        if self._age >= 18:
            self.__license = license
            self.__car = None
        else:
            print('You are still small')

    @property
    def have_car(self, ):
        return self.__car

    @have_car.setter
    def have_car(self, car):
        self.__car = car
        if self.__car.lower == 'no':
            self.__car = input('What car would you like')


def print_register():
    person = Human(input('Hi, enter your name'), input('surname'),
                   datetime.strptime(input('date of birth yyyy,mm,dd'), '%Y,%M,%d'))
    person.age_in()
    person.hello()
    return person

def print_parents():
    parents = Parents(input('Enter your mother name'), input('enter your father name'),
                      input('You are have brother or sister'))
    parents.check_br_or_sis()
    parents.acquaintance(Human) #тут я уже запутался


def print_passport():
    passport = Passport()
    passport.age_in #ну и тут тоже


def print_auto_story():
    pass


def print_work():
    pass


def print_exit():
    y = input('Are you sure? You data will not be saved! (y/n) ')
    if y in ('y', 'Y'):
        print('Have a nice day! Bye!')
        exit()


if __name__ == "__main__":
    choices = {
        "1": print_register,
        "2": print_parents,
        "3": print_passport,
        "4": print_auto_story,
        "5": print_work,
        "0": print_exit,
    }

    menu = """
Choose menu option:\n
1. Registration
2. Parens
3. Passport
4. Auto story
5. Work
0. Exit
    """
    while True:
        menu_number = input(f'{menu}\nEnter menu number - ')
        choice = choices.get(menu_number)
        if not choice:
            print('Non valid menu option')
            continue
        choice()
person = None# не уверен что нужно создавать пустые, но мне кажется их нужно выводить после функций
parents = None
passport = None
work = None
auto_story = None
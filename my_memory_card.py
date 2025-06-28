from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QPushButton, QGroupBox, QButtonGroup
from random import shuffle,randint


app = QApplication([])
main = QWidget()
main.total = 0
main.score = 0
#main.current_question = -1

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

main.setWindowTitle('Memory Card')
mainquestion = QLabel('Какая смертельная доза бананов?')

questions = list = []
q1 = Question('Количество хромосом у человека','46','52','42 БРАТУУУХА','Да')
questions.append(q1)
q2 = Question('Кто создал таблицу Менделева', 'Менделеев', 'Максим сладкий', 'Гоголь', 'Я')
questions.append(q2)
q3 = Question('Сколько у меня детей в подвале?(чёрних)', '52', '25', '5', '225')
questions.append(q3)

buttonAnswer = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответа')
rbtn1 = QRadioButton('400')
rbtn2 = QRadioButton('350')
rbtn3 = QRadioButton('300')
rbtn4 = QRadioButton('555')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

line1 = QHBoxLayout()
line2 = QVBoxLayout()
line3 = QVBoxLayout()

line2.addWidget(rbtn1)
line2.addWidget(rbtn2)
line3.addWidget(rbtn3)
line3.addWidget(rbtn4)

line1.addLayout(line2)
line1.addLayout(line3)

RadioGroupBox.setLayout(line1)

AnsGroupBox = QGroupBox('Результаты теста')
lbResult = QLabel('Неправильно')
lbCorrect = QLabel('Правильный ответ: 400')

lineRes = QVBoxLayout()
lineRes.addWidget(lbResult, alignment=(Qt.AlignLeft | Qt.AlignTop))
lineRes.addWidget(lbCorrect, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(lineRes)

def showQuestion():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    buttonAnswer.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

answer = [rbtn1, rbtn2, rbtn3, rbtn4]

def showResult():
    AnsGroupBox.show()
    RadioGroupBox.hide()
    buttonAnswer.setText('Следущий Вопрос')
    
def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    mainquestion.setText(q.question)
    lbCorrect.setText(q.right_answer)
    showQuestion()

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно')
        main.score += 1
        print('Рейтинг:', main.score / main.total * 100 ,'%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неправильно')
            print('Рейтинг:', main.score / main.total * 100 ,'%')        




def show_correct(res):
    lbResult.setText(res)
    showResult()

def next_question():
    '''main.current_question += 1
    if main.current_question >= len(questions):
        main.current_question = 0
    num_questions = questions[main.current_question]
    ask(num_questions)'''
    main.total += 1
    cur_question = randint(0, len(questions) - 1)
    q = questions[cur_question]
    ask(q)
    print('Статистика')
    print('-Всего вопросов:', main.total)
    print('-Правильных ответов:', main.score)

def click_ok():
    if buttonAnswer.text() == 'Ответить':
        check_answer()
    else:
        next_question()

layoutLine1 = QHBoxLayout()
layoutLine2 = QHBoxLayout()
layoutLine3 = QHBoxLayout()

layoutLine1.addWidget(mainquestion, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layoutLine2.addWidget(RadioGroupBox)
layoutLine2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layoutLine3.addStretch(1)
layoutLine3.addWidget(buttonAnswer, stretch=3)
layoutLine3.addStretch(1)

lineCard = QVBoxLayout()


lineCard.addLayout(layoutLine1, stretch=3)
lineCard.addLayout(layoutLine2, stretch=8)
lineCard.addStretch(1)
lineCard.addLayout(layoutLine3, stretch=1)
lineCard.addStretch(1)
lineCard.addSpacing(5)

buttonAnswer.clicked.connect(click_ok)

main.resize(600, 300)
main.setLayout(lineCard)
next_question()
main.show()
app.exec_()



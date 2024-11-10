import pgzrun
TITLE = 'QuizMaster'
WIDTH = 870
HEIGHT = 650
question = []
questionfilename = 'questions.txt'
questioncount = 0
questionindex = 0

mbox = Rect(0, 0, 880, 80)
qbox = Rect(0, 0, 650, 150)
tbox = Rect(0, 0, 150, 150)
abox1 = Rect(0, 0, 300, 150)
abox2 = Rect(0, 0, 300, 150)
abox3 = Rect(0, 0, 300, 150)
abox4 = Rect(0, 0, 300, 150)
sbox = Rect(0, 0, 150, 330)

mbox.move_ip(0, 0)
qbox.move_ip(20,100)
tbox.move_ip(700, 100)
abox1.move_ip(20, 270)
abox2.move_ip(370,270)
abox3.move_ip(20, 450)
abox4.move_ip(370, 450)
sbox.move_ip(700, 270)

answerboxes = [abox1, abox2, abox3, abox4]

def draw():
   screen.fill('black')
   screen.draw.filled_rect(mbox, 'blue')
   screen.draw.filled_rect(qbox, 'green')
   screen.draw.filled_rect(tbox, 'purple')
   screen.draw.filled_rect(sbox, 'orange')

   for box in answerboxes:
      screen.draw.filled_rect(box, 'red')

   screen.draw.textbox('skip', sbox, color = 'white', angle = -90)
   screen.draw.textbox('Welcome to Quiz Master!', mbox, color = 'white')
   screen.draw.textbox(qu[0], qbox, color = 'white')
   index = 1
   for box in answerboxes:
      screen.draw.textbox(qu[index], box, color = 'white')
      index +=1

def update():
   movemessage()

def movemessage():
   mbox.x = mbox.x-2
   if mbox.right <0:
      mbox.left = WIDTH

def readquestion():
   global questioncount, question
   qfile = open(questionfilename, 'r')
   for questions in qfile:
      question.append(questions)
      questioncount +=1
   qfile.close()

def readnextquestion():
   global questionindex
   questionindex += 1
   return question.pop(0).split(',')
readquestion()
qu = readnextquestion()

pgzrun.go()
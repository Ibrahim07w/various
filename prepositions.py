import numpy as np
import random as r
import time

text = 'Erinnern an- suchen nach- interesieren fur- Ärgern uber- fragen nach- Einflussen Auf- warten Auf- freuen Auf- freuen uber- denken an- träumen von- beschäftigen mit- bitten um- telefonieren mit- teilnehmen an- achten Auf- fliehen vor- hören von- verabschieden von- Leiden an- geraten in- verfugen uber- retten uber- erkundigen nach- greifen zu- Engagieren fur- abstimmen uber- stimmen fur- sorgen fur- Beißen in- ändern Auf- beziehen Auf- beschränken Auf- spezialisieren auf- verlassen Auf- vertragen mit- in einziehen- einladen zu- Um mitternacht- zu hause- An telefon- In stock- an computer- an tisch- an kasse- ins gebirge- in internet- in moment- Auf facebook- Auf website- Aus grunde- nach vorschrift- zufolge fur- Bei wetter- Auf weise- nach umfrage- In allgemeinen- begeistert von- wichtig fur- Tipps zu- Auf spuren- Auf fahrstuhl- zeichen fur- Stolz auf- fur bestellung- recht auf- uberrascht uber- an eingang- meinung zu- bachelor in- auf ewigkeit- lieferung an- armut an- bekannt fur- zu fruhstuck- zu termin- in moment- an Haltstelle- an gleis'

splitted = text.split('- ')
verben = []
for word in splitted:
    verben.append(word.strip())
# print(verben)
questions = []
answers = []
for verb in verben:
    separated = verb.split(' ')
    for syllabul in separated:
        if len(syllabul) > 4:
            questions.append(syllabul.lower())
        else:
            answers.append(syllabul.lower())
# print(question)
# print(answer)
'''random_verb = r.choice(questions)
index = questions.index(random_verb)
answer = answers[index]
print(random_verb,index)
input = input('enter the appropriate preposition :  ')
if str(input) == str(answer):
    print('correct')
else:
    print(f'wrong, the right one is {answer}')'''

no_verben = 0
start_time = time.time
wrong_verben = []
correct = 0
wrong = 0
no_verben = 0
x = len(questions)

print(x)
print(verben)
print(questions)
print(answers)

def verben_game(no__woerter = x):
    global no_verben, start_time, wrong_verben, wrong, correct, no_verben, x
    if not questions :
        print('the woerter has finished')
#        end_time = time.time()
#        time_taken = end_time - start_time
        percentage = (correct / x)* 100
#        print(time_taken)
        print(percentage)
        print(wrong)
        print(wrong_verben)
    else:
        random_verb = r.choice(questions)
        Index = questions.index(random_verb)
        answer = answers[Index]
        questions.remove(random_verb)
        answers.pop(Index)
        no_verben += 1
        print(no_verben)
        antwort = input(f'enter the appropriate preposition to {random_verb}:  ')
        if str(antwort.strip()) == answer:
            print('correct')
            correct += 1
            verben_game()
        else:
            print(f'wrong, the right one is {answer}')
            print('')
            time.sleep(1.0)
            wrong_verben.append(random_verb)
            wrong += 1
            verben_game()
verben_game()
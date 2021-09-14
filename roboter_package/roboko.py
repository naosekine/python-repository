import csv
import os
import textwrap
from termcolor import colored
from operate import set_csv
from talk import talk

first_talk = 'こんにちは！私はRobokoです。あなたの名前はなんですか？'
while True:
    talk.talk(first_talk)
    name = input()
    if name:
        break

if os.path.exists('ranking.csv'):
    reader = set_csv.read_csv('ranking.csv')
    sorted = set_csv.sort_csv(reader)
    for row in sorted:
        restrant = row['NAME']
        recommend = textwrap.dedent(f'''\
        私のおすすめのレストランは{restrant}です。
        このレストランは好きですか？[Yes/No]''')
        while True:
            talk.talk(recommend)
            answer = input().title()
            if answer:
                break
        if answer == 'Yes':
            break

question = f'{name}さん。どこのレストランが好きですか？'
while True:
    talk.talk(question)
    restrant = input().title()
    if restrant:
        break

if not os.path.exists('ranking.csv'):
    set_csv.create_csv('ranking.csv', restrant)
else:
    update_list = set_csv.update_csv(reader, restrant)
    set_csv.write_csv('ranking.csv', update_list)

last_talk = f'''\
{name}さん。ありがとうございました。
良い一日を！さようなら。'''
talk.talk(last_talk)

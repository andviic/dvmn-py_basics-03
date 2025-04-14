import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

email_from = 'andviic@yandex.ru'
email_to = 'andviic@gmail.com'
subject = 'Приглашаю на онлайн-курс по программированию на языке Python'
website = 'https://dvmn.org/profession-ref-program/fav/mXSvs/'
friend_name = 'Вероника'
my_name = 'Андрей'

letter = f'''\
From: {email_from}
To: {email_to}
Subject: {subject}
Content-Type: text/plain; charset="UTF-8";

Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''

letter = letter.encode('UTF-8')

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(LOGIN, PASSWORD)
server.sendmail(email_from, email_to, letter)
server.quit()
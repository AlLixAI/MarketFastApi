import smtplib
from email.message import EmailMessage

from celery import Celery

from src.config import SMTP_USER, SMTP_PASSWORD

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery('tasks', broker='redis://localhost:6379')


def get_email_template_dashboard(username: str, useremail: str):
    email = EmailMessage()
    email['Subject'] = 'Регистрация на фастапи сайте'
    email['From'] = SMTP_USER
    email['To'] = useremail

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, {username} добро пожаловать на наш сайт</h1>'
        '</div>',
        subtype='html'
    )
    return email

@celery.task
def send_email_congrats_to_join(username: str, useremail: str):
    email = get_email_template_dashboard(username, useremail)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)
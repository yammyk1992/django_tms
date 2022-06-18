# import os
#
# from django.core.mail import send_mail
#
#
# def send(user_email):
#     send_mail(
#         'Спасибо за регистрацию',
#         'Мы будем присылать вам много спама',
#         os.getenv('EMAIL_HOST_USER'),
#         ['user_email'],
#         fail_silently=False,
#     )

from django.core.mail import send_mail


def send_alert_email():

    send_mail(

        'Alerte StructurePulse',

        'Danger détecté sur le bâtiment',

        'example@gmail.com',

        ['admin@gmail.com'],

        fail_silently=False,
    )
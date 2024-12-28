def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if '@' not in recipient or 'ru' not in recipient:
        print(f'"Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('раз два три как слышно', 'nevskaya@mail.ru')
send_email('sugar and spies and all things nice', 'the_searchers')
send_email('over and over i keep going over the world', 'university.help@gmail.com')
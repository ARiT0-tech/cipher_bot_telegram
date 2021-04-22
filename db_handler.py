from user_chat import User, History
import db_session


def db_create():
    db_session.global_init("db_cipher.db")


def check(update):
    db_sess = db_session.create_session()
    users = list()
    for user in db_sess.query(User).filter(User.chat_id == update.message.chat_id):
        users.append(user.id)
    if len(users) != 0:
        return users[0]
    else:
        user = User()
        user.chat_id = update.message.chat_id
        db_sess.add(user)
        db_sess.commit()
        return user.id


def print_history(id):
    db_sess = db_session.create_session()
    histories = list()
    for history in db_sess.query(History).filter(History.id == id):
        histories.append(history.message_one)
        histories.append(history.message_two)
        histories.append(history.message_three)
        histories.append(history.message_four)
        histories.append(history.message_five)
    for history in range(len(histories)):
        if histories[history] is None:
            histories[history] = '<None>'
    if len(histories) == 0:
        return 'История пуста'
    else:
        return ';\n'.join(histories)


def create_history(id, text, cipher_text):
    db_sess = db_session.create_session()
    histories = list()
    for history in db_sess.query(History).filter(History.id == id):
        histories.append(history)
    if len(histories) != 0:
        for history in db_sess.query(History).filter(History.id == id):
            history.message_one, history.message_two, \
            history.message_three, history.message_four, \
            history.message_five = f'{text}|{cipher_text}', \
                                   history.message_one, history.message_two, \
                                   history.message_three, history.message_four
        db_sess.commit()
    else:
        history = History()
        history.id = id
        history.message_one = f'{text}|{cipher_text}'
        db_sess.add(history)
        db_sess.commit()

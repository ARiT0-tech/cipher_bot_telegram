import sqlalchemy
from db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    chat_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)


class History(SqlAlchemyBase):
    __tablename__ = 'history'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    message_one = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    message_two = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    message_three = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    message_four = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    message_five = sqlalchemy.Column(sqlalchemy.String, nullable=True)

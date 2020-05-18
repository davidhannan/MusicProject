from flask_login import UserMixin

from db import get_db


class User(UserMixin):
    def __init__(self, id_, name, email, profile_pic, saved_item):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic
        self.saved_item = saved_item

    @staticmethod
    def get(user_id):
        db = get_db()
        user = db.execute(
            "SELECT * FROM user WHERE id = ?", (user_id,)
        ).fetchone()
        if not user:
            return None

        user = User(
            id_=user[0], name=user[1], email=user[2], profile_pic=user[3], saved_item=user[4]
        )
        return user

    @staticmethod
    def create(id_, name, email, profile_pic, saved_item):
        db = get_db()
        db.execute(
            "INSERT INTO user (id, name, email, profile_pic, saved_item)"
            " VALUES (?, ?, ?, ?, ?)",
            (id_, name, email, profile_pic, saved_item),
        )
        db.commit()

    @staticmethod
    def saveItem(item, id):
        db =get_db()
        print(id)
        print(item)
        db.execute(
            "UPDATE user SET saved_item = saved_item || ? WHERE id = ?", (item, id)
        )
        db.commit()

    @staticmethod
    def getItems(id):
        db = get_db()
        items = db.execute(
            "SELECT saved_item FROM user WHERE id = ?", (id,)
        ).fetchone()
        print(items[0])
        return items

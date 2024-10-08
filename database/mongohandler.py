from pymongo import MongoClient
from database.entities import User, Message


class Operations:
    def __init__(self,
                 connect_string="mongodb+srv://Elzio:senha1234@samples.t58pc.mongodb.net/?retryWrites=true&w=majority&appName=Samples"):
        self.client = MongoClient(connect_string)
        self.db = self.client["mongo_chat"]
        self.users_collection = self.db["user"]
        self.messages_collection = self.db["messages"]

    def validate_login(self, nickname: str, password: str):
        user = self.users_collection.find_one({"nickname": nickname, "password": password})
        return user is not None

    def add_new_message(self, m: Message):
        return self.messages_collection.insert_one(m.__dict__).inserted_id

    def get_messages_from(self, sender_nickname: str, receiver_nickname: str):
        query = {
            "nickname_from": sender_nickname,
            "nickname_to": receiver_nickname
        }
        return list(self.messages_collection.find(query))

    def add_new_user(self, user: User):
        if self.users_collection.find_one({"nickname": user.nickname}):
            return False
        else:
            self.users_collection.insert_one(user.__dict__)
            return True

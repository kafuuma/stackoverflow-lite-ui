from flask import abort
from werkzeug.security import generate_password_hash, check_password_hash
from api.core.models import Model
from api.core import JWT


class Auth:
    _current_subject = None

    _User = None

    def __init__(self, UserModel):
        self.UserModel = UserModel
        self.jwt = JWT()

    def issue_token(self, credentials):
        user = self.get_user(credentials["email"])
        if not user._password_matches(credentials["password"]):
            return abort(401, "Invalid login credentials")
        return self.jwt.generate_token(user.attributes["email"])

    def authenticate(self):
        subject = self.jwt.get_subject_from_headers()
        current_subject = Auth._current_subject
        # user could be cached, there is no reason to make another db query
        if current_subject and subject == current_subject and Auth._User:
            return True
        Auth._current_subject = subject
        Auth._User = self.get_user(subject)
        return True

    def is_authenticated(self):
        self.authenticate()
        return True

    def get_user(self, email):
        data = self.UserModel.where(email=email).first()
        if not data:
            return abort(
                401,
                "Authentication Failed (Invalid Login Credentials)"
            )
        return self.UserModel(data)

    def id(self):
        try:
            self.authenticate()
        except Exception:
            abort(401, "User is not signed in")  # pragma: no cover
        return Auth._User.attributes["id"]


class User(Model):
    hidden = ["password"]

    @classmethod
    def table_name(cls):
        return "users"

    def _creating(self):
        password = self.attributes["password"]
        self.attributes["password"] = generate_password_hash(password)

    def _password_matches(self, password):
        return check_password_hash(self.attributes["password"], password)

    @classmethod
    def owns_question(cls, question):
        return cls.entity_belongs_to_user(question)

    @classmethod
    def owns_answer(cls, answer):
        return cls.entity_belongs_to_user(answer)

    @classmethod
    def entity_belongs_to_user(cls, entity, attribute="user_id"):
        return User.auth().id() == entity.get_attribute(attribute)

    @classmethod
    def auth(cls):
        return Auth(cls)

import random

from .base_model import BaseModel, db
import string


class BookmarkModel(BaseModel):
    __tablename__ = "bookmarks"

    body = db.Column(db.Text, nullable=True)
    url = db.Column(db.Text, nullable=False)
    short_url = db.Column(db.String(5), nullable=True)
    visits = db.Column(db.Integer, default=0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.short_url = self.generate_short_characters()

    def __repr__(self):
        return f'Bookmark>>> {self.url}'

    def generate_short_characters(self):
        characters = string.digits + string.ascii_letters
        print(characters)
        picked_characters = ''.join(random.choices(characters, k=3))

        link = self.query.filter_by(short_url=picked_characters).first()

        if link:
            self.generate_short_charecters()
        else:
            return picked_characters
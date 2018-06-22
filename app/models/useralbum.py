""""""

from sqlalchemy import ForeignKey, UniqueConstraint
from app import db
from .user import User
from .albumjet import AlbumJet

class UserAlbum(db.Model):

    __tablename__ = 'useralbum'

    __table_args__ = (
        UniqueConstraint("iduser", "idalbum"),
    )

    # atributes
    # ------------------------------------------------------
    id = db.Column(db.Integer, primary_key=True)
    iduser = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    idalbum = db.Column(db.Integer, db.ForeignKey('albumjet.id'), nullable=False)
    laminas = db.Column(db.Integer)
    
    # agregates
    # ------------------------------------------------------
    user = db.relationship("User", viewonly=True)
    album = db.relationship("AlbumJet", viewonly=True)
    lamina_list = db.relationship("UserLamina", back_populates="useralbum", viewonly=True)

    def __rpr__(self):
        return __str__(self)

    def __str__(self):
        return "<UserAlbum user=%s, album=%s>" % (self.user.nickname, self.album.nombre)

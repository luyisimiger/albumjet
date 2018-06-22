""""""

from sqlalchemy import UniqueConstraint
from app import db

class UserLamina(db.Model):

    __tablename__ = 'userlaminas'

    __table_args__ = (
        UniqueConstraint("iduseralbum", "idlamina"),
    )

    id = db.Column('id', db.Integer, primary_key=True)
    iduseralbum = db.Column(db.Integer, db.ForeignKey('useralbum.id'), nullable=False)
    idlamina = db.Column(db.Integer, db.ForeignKey('laminas.id'), nullable=False)
    mark = db.Column(db.Boolean, nullable=False)

    useralbum = db.relationship("UserAlbum", back_populates="lamina_list")
    lamina = db.relationship("Lamina")

    def __repr__(self):

        return {
            "id": id,
            "iduseralbum": iduseralbum,
            "idlamina": idlamina,
            "mark": mark,
        }

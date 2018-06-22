""""""

from app import db

class Lamina(db.Model):

    __tablename__ = 'laminas'

    # atributes
    # ------------------------------------------------------
    id = db.Column('id', db.Integer, primary_key=True)
    idalbum = db.Column(db.Integer, db.ForeignKey('albumjet.id'), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(256), nullable=False)
    descripcion = db.Column(db.String(256), nullable=False)

    album = db.relationship("AlbumJet", back_populates="lamina_list", viewonly=True)

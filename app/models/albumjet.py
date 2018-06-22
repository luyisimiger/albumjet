""""""

from app import db

class AlbumJet(db.Model):

    __tablename__ = 'albumjet'
    
    # atributes
    # ------------------------------------------------------
    id = db.Column('id', db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    descripcion = db.Column(db.String(256), nullable=False)
    laminas = db.Column(db.Integer)

    lamina_list = db.relationship("Lamina", back_populates="album", viewonly=True)
